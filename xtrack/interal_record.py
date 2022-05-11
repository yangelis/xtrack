import numpy as np
import xobjects as xo

class RecordIdentifier(xo.Struct):
    '''
    To be inserted in the beam element.
    '''
    buffer_id = xo.Int64
    offset = xo.Int64
RecordIdentifier.extra_sources = []
RecordIdentifier.extra_sources.append(r'''
/*gpufun*/
/*gpuglmem*/ int8_t* RecordIdentifier_getp_record(RecordIdentifier record_id, LocalParticle* part){
    /*gpuglmem*/ int8_t* io_buffer = LocalParticle_get_io_buffer(part);
    if (io_buffer == NULL){
        return NULL;
    }

    int64_t buffer_id = RecordIdentifier_get_buffer_id(record_id);
    /*gpuglmem*/ int64_t* found_id = (/*gpuglmem*/ int64_t*)io_buffer;
    if (buffer_id != (*found_id)){
        printf("Error: buffer_id mismatch!\n");
        return NULL;
    }

    int64_t offset = RecordIdentifier_get_offset(record_id);

    return io_buffer + offset;
    }

''')

class RecordIndex(xo.Struct):
    '''
    To be inserted in the record class.
    '''
    capacity = xo.Int64
    num_recorded = xo.UInt32
    _dummy = xo.UInt32 # to make sure the size is a multiple of 64 bits (not really needed)
    buffer_id = xo.Int64
RecordIndex.extra_sources = []
RecordIndex.extra_sources.append('''

/*gpufun*/
int64_t RecordIndex_get_slot(RecordIndex record_index){

    if (record_index == NULL){
        return -2;
    }
    int64_t capacity = RecordIndex_get_capacity(record_index);
    /*gpuglmem*/ uint32_t* num_recorded = RecordIndex_getp_num_recorded(record_index);

    if(*num_recorded >= capacity){
        return -1;}

    uint32_t slot = atomic_add(num_recorded, 1);   //only_for_context opencl
    uint32_t slot = atomicAdd(num_recorded, 1);    //only_for_context cuda
    uint32_t slot = *num_recorded;                 //only_for_context cpu_serial
    *num_recorded = slot + 1;                      //only_for_context cpu_serial

    return (int64_t) slot;
    }

''')

def init_internal_record(internal_record_class, capacity, io_buffer):

    init_dict = {}
    if np.isscalar(capacity):
        # One-level record
        capacity = int(capacity)
        for ff in internal_record_class.XoStruct._fields:
            if hasattr(ff.ftype, 'to_nplike'): #is array
                init_dict[ff.name] = capacity
    else:
        # Record with multiple subrecords
        init_dict = {}
        for ff in internal_record_class.XoStruct._fields:
            if ff.name in capacity.keys():
                subtable_class = ff.ftype
                init_dict[ff.name] = {}
                for sff in subtable_class._fields:
                    if hasattr(sff.ftype, 'to_nplike'): #is array
                        init_dict[ff.name][sff.name] = capacity[ff.name]

    record = internal_record_class(_buffer=io_buffer, **init_dict)

    if np.isscalar(capacity):
        # One-level record
        record._index.capacity = capacity
    else:
        # Record with multiple subrecords
        for kk in capacity.keys():
            getattr(record, kk)._index.capacity = capacity[kk]

    return record

def start_internal_logging(element, record, io_buffer):

    assert record._buffer is io_buffer, (
        "The record should be stored in the specified io_buffer")

    element._internal_record_id.offset = record._offset
    element._internal_record_id.buffer_id = xo.Int64._from_buffer(
                                                    record._buffer, 0)
    element.io_buffer = io_buffer
    element.record = record

def stop_internal_logging(element):
    element._internal_record_id.offset = 0
    element._internal_record_id.buffer_id = 0
    element.io_buffer = None

def start_internal_logging_for_elements_of_type(tracker, element_type, capacity):

    record = init_internal_record(element_type._internal_record_class, capacity,
                                  tracker.io_buffer)

    for nn in tracker.line.element_names:
        ee = tracker.line.element_dict[nn]

        if (hasattr(ee, 'io_buffer') and ee.io_buffer is not None
            and ee.io_buffer is not tracker.io_buffer):
            raise RuntimeError(f'The element `{nn}` has an io_buffer that is '
                'incompatible with the io_buffer of the tracker. Please clear '
                'the internal logging for the element using '
                '`stop_internal_record(element=...)`.')

        if isinstance(ee, element_type):
            start_internal_logging(ee, record, tracker.io_buffer)
    return record

def stop_internal_logging_for_elements_of_type(tracker, element_type):

    for ee in tracker.line.elements:
        if isinstance(ee, element_type):
            stop_internal_logging(ee)

def generate_get_record(ele_classname, record_classname):
    content = '''
RECORDCLASSNAME ELECLASSNAME_getp_internal_record(ELECLASSNAME el, LocalParticle* part){
    RecordIdentifier record_id = ELECLASSNAME_getp__internal_record_id(el);
    if (RecordIdentifier_get_buffer_id(record_id) <= 0){
        return NULL;
    }
    else{
        return (RECORDCLASSNAME) RecordIdentifier_getp_record(record_id, part);
    }
    }
    '''.replace(
        'RECORDCLASSNAME', record_classname).replace('ELECLASSNAME', ele_classname)
    return content