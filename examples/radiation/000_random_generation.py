import numpy as np

import xobjects as xo
import xtrack as xt
import xline as xl
import xpart as xp
from pathlib import Path

ctx = xo.ContextCpu()
ctx = xo.ContextCupy()
#ctx = xo.ContextPyopencl()

part = xp.Particles(_context=ctx, p0c=6.5e12, x=[1,2,3])
part._init_random_number_generator()

class TestElement(xt.BeamElement):
     _xofields={
        'dummy': xo.Float64,
        }
TestElement.XoStruct.extra_sources = [
    xp._pkg_root.joinpath('random_number_generator/rng_src/base_rng.h'),
    xp._pkg_root.joinpath('random_number_generator/rng_src/local_particle_rng.h'),
    ]
TestElement.XoStruct.extra_sources.append('''
/*gpufun*/
void TestElement_track_local_particle(TestElementData el, LocalParticle* part0){
    //start_per_particle_block (part0->part)
        double rr = LocalParticle_generate_random_double(part);
        LocalParticle_set_x(part, rr);
    //end_per_particle_block
}
''')

telem = TestElement(_context=ctx)

telem.track(part)

# Use turn-by-turn monitor to acquire some statistics

tracker = xt.Tracker(_buffer=telem._buffer,
        sequence=xl.Line(elements=[telem]),
            save_source_as='source.c')

tracker.track(part, num_turns=1e6, turn_by_turn_monitor=True)

import matplotlib.pyplot as plt
plt.close('all')
plt.figure()
for i_part in range(part._capacity):
    x = tracker.record_last_track.x[i_part, :]
    assert np.all(x>0)
    assert np.all(x<1)
    hstgm, bin_edges = np.histogram(x,  bins=50, range=(0, 1), density=True)

    bin_centers = 0.5*(bin_edges[:-1] + bin_edges[1:])
    plt.plot(bin_centers, hstgm)
    plt.ylim(bottom=0, top=1.1)
    plt.grid(True)
    assert np.allclose(hstgm, 1, rtol=1e-10, atol=0.03)
plt.show()

