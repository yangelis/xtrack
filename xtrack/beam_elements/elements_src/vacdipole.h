// copyright ############################### //
// This file is part of the Xtrack Package.  //
// Copyright (c) CERN, 2021.                 //
// ######################################### //

#ifndef XTRACK_VACDIPOLE_H
#define XTRACK_VACDIPOLE_H

// VACDIPOLE

/*gpufun*/
void VACDipole_track_local_particle(VACDipoleData el, LocalParticle* part0) {

    double const volt   = VACDipoleData_get_voltage(el); // rfv
    double const qd     = VACDipoleData_get_frequency(el); // rff
    double const lag    = VACDipoleData_get_lag(el); // rfl
    int64_t const ramp1 = VACDipoleData_get_ramp(el, 0); 
    int64_t const ramp2 = VACDipoleData_get_ramp(el, 1);
    int64_t const ramp3 = VACDipoleData_get_ramp(el, 2);
    int64_t const ramp4 = VACDipoleData_get_ramp(el, 3);

    double const omega  = qd * 2 * PI;
    double const phirf  = lag * 2 * PI;
    
    int64_t const rampup   = ramp2 - ramp1;
    int64_t const rampdown = ramp4 - ramp3;

    //start_per_particle_block (part0->part)

        double const  p0c            = LocalParticle_get_p0c(part);
        double const  one_plus_delta = 1. + LocalParticle_get_delta(part);
        int64_t const at_turn        = LocalParticle_get_at_turn(part);

        double vrf    = 0.3 * volt / p0c * 1.e9; 
        double nprime = 0.0;
       
        if (at_turn < ramp1) { // votage stable at zero
            nprime = 0.0;
        } else if (at_turn < ramp2) {  // ramping up the voltage
            nprime = 1.0 * (at_turn - ramp1) / rampup;
        } else if (at_turn < ramp3) { // voltage stable at maximum
            nprime = 1.0;
        } else if (at_turn < ramp4) { // ramping down the voltage
            nprime = 1.0 * (ramp4 - at_turn) / rampdown;
        } else { // stable again at zero
            nprime = 0.0;
        }

        double const py_kick = nprime * vrf * one_plus_delta * sin(omega * at_turn + phirf);
        LocalParticle_add_to_py(part, py_kick);

    //end_per_particle_block
}

#endif
