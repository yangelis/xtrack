import xtrack as xt

import xtrack._temp.lhc_match as lm


default_tol = {
    None: 1e-8,
    "betx": 1e-6,
    "bety": 1e-6,
}  # to have no rematching w.r.t. madx

scale = 23348.89927
grad = 132.6  # hl15 is 132.6, hl16 is 132.2
scl = 0.06
sch = 0.99
sc79 = 0.999
bmaxds = 500
imb = 1.50

qtlim1 = grad / scale
qtlim2 = 160.0 / scale
qtlimq5 = 160.0 / scale
qtlim3 = 200.0 / scale
qtlim4 = 125.0 / scale
qtlim5 = 120.0 / scale
qtlimq4 = 160.0 / scale

quads_ir15_defaults = {
    "kqx1.l5": {"step": 1e-6, "limits": (-qtlim1, -0.90 * qtlim1)},
    "kqx2a.l5": {"step": 1e-6, "limits": (-qtlim1, -0.90 * qtlim1)},
    "kqx3.l5": {"step": 1e-6, "limits": (-qtlim1, -0.90 * qtlim1)},
    # kq4
    "kq4.l5b1": {"step": 1e-6, "limits": (scl * qtlimq4, sch * qtlimq4)},
    "kq4.r5b1": {"step": 1e-6, "limits": (-sch * qtlimq4, -scl * qtlimq4)},
    "kq4.l5b2": {"step": 1e-6, "limits": (-sch * qtlimq4, -scl * qtlimq4)},
    "kq4.r5b2": {"step": 1e-6, "limits": (scl * qtlimq4, sch * qtlimq4)},
    # kq5
    "kq5.l5b1": {"step": 1e-6, "limits": (-sch * qtlimq5, -scl * qtlimq5)},
    "kq5.r5b1": {"step": 1e-6, "limits": (scl * qtlimq5, sch * qtlimq5)},
    "kq5.l5b2": {"step": 1e-6, "limits": (scl * qtlimq5, sch * qtlimq5)},
    "kq5.r5b2": {"step": 1e-6, "limits": (-sch * qtlimq5, -scl * qtlimq5)},
    # kq6
    "kq6.l5b1": {"step": 1e-6, "limits": (scl * qtlim2, sch * qtlim2)},
    "kq6.r5b1": {"step": 1e-6, "limits": (-sch * qtlim2, -scl * qtlim2)},
    "kq6.l5b2": {"step": 1e-6, "limits": (-sch * qtlim2, -scl * qtlim2)},
    "kq6.r5b2": {"step": 1e-6, "limits": (scl * qtlim2, sch * qtlim2)},
    # kq7
    "kq7.l5b1": {"step": 1e-6, "limits": (-sc79 * qtlim3, -scl * qtlim3)},
    "kq7.r5b1": {"step": 1e-6, "limits": (scl * qtlim3, sc79 * qtlim3)},
    "kq7.l5b2": {"step": 1e-6, "limits": (scl * qtlim3, sc79 * qtlim3)},
    "kq7.r5b2": {"step": 1e-6, "limits": (-sc79 * qtlim3, -scl * qtlim3)},
    # kq8
    "kq8.l5b1": {"step": 1e-6, "limits": (scl * qtlim3, sc79 * qtlim3)},
    "kq8.r5b1": {"step": 1e-6, "limits": (-sc79 * qtlim3, -scl * qtlim3)},
    "kq8.l5b2": {"step": 1e-6, "limits": (-sc79 * qtlim3, -scl * qtlim3)},
    "kq8.r5b2": {"step": 1e-6, "limits": (scl * qtlim3, sc79 * qtlim3)},
    # kq9
    "kq9.l5b1": {"step": 1e-6, "limits": (-sc79 * qtlim3, -scl * qtlim3)},
    "kq9.r5b1": {"step": 1e-6, "limits": (scl * qtlim3, sc79 * qtlim3)},
    "kq9.l5b2": {"step": 1e-6, "limits": (scl * qtlim3, sc79 * qtlim3)},
    "kq9.r5b2": {"step": 1e-6, "limits": (-sc79 * qtlim3, -scl * qtlim3)},
    # kq10
    "kq10.l5b1": {"step": 1e-6, "limits": (scl * qtlim3, sch * qtlim3)},
    "kq10.r5b1": {"step": 1e-6, "limits": (-sch * qtlim3, -scl * qtlim3)},
    "kq10.l5b2": {"step": 1e-6, "limits": (-sch * qtlim3, -scl * qtlim3)},
    "kq10.r5b2": {"step": 1e-6, "limits": (scl * qtlim3, sch * qtlim3)},
    # kqtl11
    "kqtl11.l5b1": {"step": 1e-6, "limits": (-sch * qtlim4, sch * qtlim4)},
    "kqtl11.r5b1": {"step": 1e-6, "limits": (-sch * qtlim4, sch * qtlim4)},
    "kqtl11.l5b2": {"step": 1e-6, "limits": (-sch * qtlim4, sch * qtlim4)},
    "kqtl11.r5b2": {
        "step": 1e-6,
        "limits": (-sch * qtlim4 * 500 / 550, sch * qtlim4 * 500 / 550),
    },
    # kqt12
    "kqt12.l5b1": {"step": 1e-6, "limits": (-sch * qtlim5, sch * qtlim5)},
    "kqt12.r5b1": {"step": 1e-6, "limits": (-sch * qtlim5, sch * qtlim5)},
    "kqt12.l5b2": {"step": 1e-6, "limits": (-sch * qtlim5, sch * qtlim5)},
    "kqt12.r5b2": {"step": 1e-6, "limits": (-sch * qtlim5, sch * qtlim5)},
    # kqt13
    "kqt13.l5b1": {"step": 1e-6, "limits": (-sch * qtlim5, sch * qtlim5)},
    "kqt13.r5b1": {"step": 1e-6, "limits": (-sch * qtlim5, sch * qtlim5)},
    "kqt13.l5b2": {"step": 1e-6, "limits": (-sch * qtlim5, sch * qtlim5)},
    "kqt13.r5b2": {"step": 1e-6, "limits": (-sch * qtlim5, sch * qtlim5)},
}


def connect_lr_qx(collider, nqx=0, ir=5):
    """Connect specified right kqx in IP5 of IP1 with the left kqx"""
    collider.vars[f"kqx{nqx}.r{ir}"] = -collider.vars[f"kqx{nqx}.l{ir}"]


def connect_lr_qs(collider, nq=0, ir=5, bim=1):
    """Connect specified kq in ir for either beam with the left kq"""
    collider.vars[f"kq{nq}.r{ir}b{bim}"] = -collider.vars[f"kq{nq}.l{ir}b{bim}"]


def connect_q2s(collider, ir=5):
    """Connect Q2 in IP5, or IP1 to be used as one for matching"""
    collider.vars[f"kqx2b.l{ir}"] = collider.vars[f"kqx2a.l{ir}"]
    collider.vars[f"kqx2a.r{ir}"] = -collider.vars[f"kqx2a.l{ir}"]
    collider.vars[f"kqx2b.r{ir}"] = -collider.vars[f"kqx2a.l{ir}"]


def rematch_ir15(
    collider,
    betxip5,
    betyip5,
    tw_sq_a45_ip5_a56=None,
    match_on_triplet=0,
    match_inj_tunes=0,
    no_match_beta=False,
    ir5q4sym=0,
    ir5q5sym=0,
    ir5q6sym=0,
    restore=True,
    solve=False,
):
    """Match IP5 for the beta_x, beta_y, and copy strenghts to IP1

    Parameters
    ----------
    collider : xtrack.Multiline
        HL-LHC collider with b1 and b2
    betxip5 : float
        betax for ip1 and ip5
    betyip5 : float
        betay for ip1 and ip5
    tw_sq_a45_ip5_a56 : dict
        Dictionary for beam1, beam2 with twiss tables for arcs 45, 56
    match_on_triplet: int
        Flag to select how to match the triplet.
        0 : Don't touch the triplet
        1 : Q1, Q2, Q3 free
        2 : Q2 free
        3 :
        4 : Link Q1 with Q3
    match_inj_tunes: bool
    no_match_beta: bool
        If False, match beta at the ip
    ir5q4sym: int
        Flag to connect Q4
        0 : Connect Q4 left for both beams and Q4 right for both beams
        1 : Connect Q4 left and right
    ir5q5sym: int
        Flag to connect Q5
        0 : Connect Q5 left for both beams and Q5 right for both beams
        1 : Connect Q5 left and right
    ir5q6sym: int
        Flag to connect Q6
        0 : Connect Q6 left for both beams and Q6 right for both beams
        1 : Connect Q6 left and right
    restore: bool
        Flag to restore the variables if the match fails
    solve: bool
        Flag to solve or not

    """

    if tw_sq_a45_ip5_a56 is None:
        tw_sq_a45_ip5_a56 = lm.get_arc_periodic_solution(
            collider, arc_name=["45", "56"]
        )

    targets = []

    if no_match_beta == False:
        targets.append(
            xt.TargetSet(
                line="lhcb1",
                at="ip5",
                betx=betxip5,
                bety=betyip5,
                alfx=0,
                alfy=0,
                dx=0,
                dpx=0,
            )
        )
        targets.append(
            xt.TargetSet(
                line="lhcb2",
                at="ip5",
                betx=betxip5,
                bety=betyip5,
                alfx=0,
                alfy=0,
                dx=0,
                dpx=0,
            )
        )
    else:
        targets.append(
            xt.TargetSet(line="lhcb1", at="ip5", alfx=0, alfy=0, dx=0, dpx=0)
        )
        targets.append(
            xt.TargetSet(line="lhcb2", at="ip5", alfx=0, alfy=0, dx=0, dpx=0)
        )

    targets.append(
        xt.TargetSet(
            line="lhcb1",
            at="e.ds.r5.b1",
            betx=tw_sq_a45_ip5_a56["lhcb1"]["56"]["betx", "e.ds.r5.b1"],
            bety=tw_sq_a45_ip5_a56["lhcb1"]["56"]["bety", "e.ds.r5.b1"],
            alfx=tw_sq_a45_ip5_a56["lhcb1"]["56"]["alfx", "e.ds.r5.b1"],
            alfy=tw_sq_a45_ip5_a56["lhcb1"]["56"]["alfy", "e.ds.r5.b1"],
            dx=tw_sq_a45_ip5_a56["lhcb1"]["56"]["dx", "e.ds.r5.b1"],
            dpx=tw_sq_a45_ip5_a56["lhcb1"]["56"]["dpx", "e.ds.r5.b1"],
        )
    )
    targets.append(
        xt.TargetSet(
            line="lhcb2",
            at="e.ds.r5.b2",
            betx=tw_sq_a45_ip5_a56["lhcb2"]["56"]["betx", "e.ds.r5.b2"],
            bety=tw_sq_a45_ip5_a56["lhcb2"]["56"]["bety", "e.ds.r5.b2"],
            alfx=tw_sq_a45_ip5_a56["lhcb2"]["56"]["alfx", "e.ds.r5.b2"],
            alfy=tw_sq_a45_ip5_a56["lhcb2"]["56"]["alfy", "e.ds.r5.b2"],
            dx=tw_sq_a45_ip5_a56["lhcb2"]["56"]["dx", "e.ds.r5.b2"],
            dpx=tw_sq_a45_ip5_a56["lhcb2"]["56"]["dpx", "e.ds.r5.b2"],
        )
    )

    muxIP5b1_l = collider["lhcb1"].varval["muxip5b1_l"]
    muxIP5b1_r = collider["lhcb1"].varval["muxip5b1_r"]
    muyIP5b1_l = collider["lhcb1"].varval["muyip5b1_l"]
    muyIP5b1_r = collider["lhcb1"].varval["muyip5b1_r"]
    muxIP5b1 = muxIP5b1_l + muxIP5b1_r
    muyIP5b1 = muyIP5b1_l + muyIP5b1_r

    muxIP5b2_l = collider["lhcb2"].varval["muxip5b2_l"]
    muxIP5b2_r = collider["lhcb2"].varval["muxip5b2_r"]
    muyIP5b2_l = collider["lhcb2"].varval["muyip5b2_l"]
    muyIP5b2_r = collider["lhcb2"].varval["muyip5b2_r"]
    muxIP5b2 = muxIP5b2_l + muxIP5b2_r
    muyIP5b2 = muyIP5b2_l + muyIP5b2_r

    if match_inj_tunes == 0:
        targets.append(
            xt.TargetSet(line="lhcb1", at="ip5", mux=muxIP5b1_l, muy=muyIP5b1_l)
        )
        targets.append(
            xt.TargetSet(line="lhcb1", at="e.ds.r5.b1", mux=muxIP5b1, muy=muyIP5b1)
        )
        targets.append(
            xt.TargetSet(line="lhcb2", at="ip5", mux=muxIP5b2_l, muy=muyIP5b2_l)
        )
        targets.append(
            xt.TargetSet(line="lhcb2", at="e.ds.r5.b2", mux=muxIP5b2, muy=muyIP5b2)
        )

    else:
        targets.append(
            xt.TargetSet(
                line="lhcb1",
                at="e.ds.r5.b1",
                mux=muxIP5b1,
                muy=muyIP5b1,
            )
        )
        targets.append(
            xt.TargetSet(
                line="lhcb2",
                at="e.ds.r5.b2",
                mux=muxIP5b2,
                muy=muyIP5b2,
            )
        )

    vary_list = []

    if ir5q4sym == 0:
        collider.vars["imq4l"] = (
            -collider.vars["kq4.l5b2"] / collider.vars["kq4.l5b1"] / 100
        )
        collider.vars["imq4r"] = (
            -collider.vars["kq4.r5b2"] / collider.vars["kq4.r5b1"] / 100
        )

        collider.vars["kq4.l5b2"] = -(
            collider.vars["kq4.l5b1"] * collider.vars["imq4l"] * 100
        )
        collider.vars["kq4.r5b2"] = -(
            collider.vars["kq4.r5b1"] * collider.vars["imq4r"] * 100
        )

        if (
            collider.varval["imq4l"] < 1 / imb / 100
            or collider.varval["imq4l"] > imb / 100
        ):
            collider.vars["imq4l"]._set_value(1 / imb / 100)
        if (
            collider.varval["imq4r"] < 1 / imb / 100
            or collider.varval["imq4r"] > imb / 100
        ):
            collider.vars["imq4r"]._set_value(1 / imb / 100)

        vary_list.append(xt.Vary("imq4l", limits=(1 / imb / 100, imb / 100)))
        vary_list.append(xt.Vary("imq4r", limits=(1 / imb / 100, imb / 100)))
        vary_list.append(xt.Vary("kq4.l5b1"))
        vary_list.append(xt.Vary("kq4.r5b1"))
    elif ir5q4sym == 1:
        connect_lr_qs(collider, nq=4, ir=5, bim=1)
        connect_lr_qs(collider, nq=4, ir=5, bim=2)
        vary_list.append(xt.Vary("kq4.l5b1"))
        vary_list.append(xt.Vary("kq4.l5b2"))

    if ir5q5sym == 0:
        collider.vars["imq5l"] = (
            -collider.vars["kq5.l5b2"] / collider.vars["kq5.l5b1"] / 100
        )
        collider.vars["imq5r"] = (
            -collider.vars["kq5.r5b2"] / collider.vars["kq5.r5b1"] / 100
        )

        collider.vars["kq5.l5b2"] = -(
            collider.vars["kq5.l5b1"] * collider.vars["imq5l"] * 100
        )
        collider.vars["kq5.r5b2"] = -(
            collider.vars["kq5.r5b1"] * collider.vars["imq5r"] * 100
        )

        if (
            collider.varval["imq5l"] < 1 / imb / 100
            or collider.varval["imq5l"] > imb / 100
        ):
            collider.vars["imq5l"]._set_value(1 / imb / 100)
        if (
            collider.varval["imq5r"] < 1 / imb / 100
            or collider.varval["imq5r"] > imb / 100
        ):
            collider.vars["imq5r"]._set_value(1 / imb / 100)

        vary_list.append(xt.Vary("imq5l", limits=(1 / imb / 100, imb / 100)))
        vary_list.append(xt.Vary("imq5r", limits=(1 / imb / 100, imb / 100)))
        vary_list.append(xt.Vary("kq5.l5b1"))
        vary_list.append(xt.Vary("kq5.r5b1"))
    elif ir5q5sym == 1:
        connect_lr_qs(collider, nq=5, ir=5, bim=1)
        connect_lr_qs(collider, nq=5, ir=5, bim=2)
        vary_list.append(xt.Vary("kq5.l5b1"))
        vary_list.append(xt.Vary("kq5.l5b2"))

    if ir5q6sym == 0:
        collider.vars["imq6l"] = (
            -collider.vars["kq6.l5b2"] / collider.vars["kq6.l5b1"] / 100
        )
        collider.vars["imq6r"] = (
            -collider.vars["kq6.r5b2"] / collider.vars["kq6.r5b1"] / 100
        )

        collider.vars["kq6.l5b2"] = -(
            collider.vars["kq6.l5b1"] * collider.vars["imq6l"] * 100
        )
        collider.vars["kq6.r5b2"] = -(
            collider.vars["kq6.r5b1"] * collider.vars["imq6r"] * 100
        )

        if (
            collider.varval["imq6l"] < 1 / imb / 100
            or collider.varval["imq6l"] > imb / 100
        ):
            collider.vars["imq6l"]._set_value(1 / imb / 100)
        if (
            collider.varval["imq6r"] < 1 / imb / 100
            or collider.varval["imq6r"] > imb / 100
        ):
            collider.vars["imq6r"]._set_value(1 / imb / 100)

        vary_list.append(xt.Vary("imq6l", limits=(1 / imb / 100, imb / 100)))
        vary_list.append(xt.Vary("imq6r", limits=(1 / imb / 100, imb / 100)))
        vary_list.append(xt.Vary("kq6.l5b1"))
        vary_list.append(xt.Vary("kq6.r5b1"))
    elif ir5q6sym == 1:
        connect_lr_qs(collider, nq=6, ir=5, bim=1)
        connect_lr_qs(collider, nq=6, ir=5, bim=2)
        vary_list.append(xt.Vary("kq6.l5b1"))
        vary_list.append(xt.Vary("kq6.l5b2"))

    quads_ir5_b1 = (
        "kq4.l5b1 kq4.r5b1 kq5.l5b1 kq5.r5b1 kq6.l5b1 kq6.r5b1 "
        "kq7.l5b1 kq7.r5b1 kq8.l5b1 kq8.r5b1 kq9.l5b1 kq9.r5b1 "
        "kq10.l5b1 kq10.r5b1 kqtl11.l5b1 kqtl11.r5b1 "
        "kqt12.l5b1 kqt12.r5b1 kqt13.l5b1 kqt13.r5b1"
    )

    quads_ir5_b2 = (
        "kq4.l5b2 kq4.r5b2 kq5.l5b2 kq5.r5b2 kq6.l5b2 kq6.r5b2 "
        "kq7.l5b2 kq7.r5b2 kq8.l5b2 kq8.r5b2 kq9.l5b2 kq9.r5b2 "
        "kq10.l5b2 kq10.r5b2 kqtl11.l5b2 kqtl11.r5b2 kqt12.l5b2 "
        "kqt12.r5b2 kqt13.l5b2 kqt13.r5b2"
    )
    # Beam 1
    for quad in quads_ir5_b1.split()[6:]:
        vary_list.append(xt.Vary(quad))

    # Beam 2
    for quad in quads_ir5_b2.split()[6:]:
        vary_list.append(xt.Vary(quad))

    if match_on_triplet == 0:  # q1 q2 q3 untouched
        pass
    elif match_on_triplet == 1:  # Q1 Q2 Q3 free
        connect_q2s(collider)
        connect_lr_qx(collider, 1)
        connect_lr_qx(collider, 3)
        vary_list.append(xt.Vary("kqx1.l5"))
        vary_list.append(xt.Vary("kqx2a.l5"))
        vary_list.append(xt.Vary("kqx3.l5"))
    elif match_on_triplet == 2:
        # connect kqx2a and kqx2b left and right
        connect_q2s(collider)
        vary_list.append(xt.Vary("kqx2a.l5"))
    elif match_on_triplet == 4:
        # link q3 and q1
        # First set everything to zero

        collider.vars["kqx1.r5"] = -collider.vars["kqx1.l5"]
        collider.vars["kqx3.l5"] = collider.vars["kqx1.l5"]
        collider.vars["kqx3.r5"] = -collider.vars["kqx1.l5"]

        connect_q2s(collider)
        vary_list.append(xt.Vary("kqx1.l5"))
        vary_list.append(xt.Vary("kqx2a.l5"))
    elif match_on_triplet == 5:
        connect_q2s(collider)
        connect_lr_qx(collider, 1)
        connect_lr_qx(collider, 3)
        vary_list.append(xt.Vary("kqx1.l5"))
        vary_list.append(xt.Vary("kqx2a.l5"))
        targets.append(
            xt.Target(
                lambda tt: tt.lhcb1["bety", "mqxfb.b2r5_entry"]
                - tt.lhcb1["betx", "mqxfa.b3r5_exit"],
                value=xt.GreaterThan(0),
                tol=1e-2,
            )
        )

    twiss_init_b1 = tw_sq_a45_ip5_a56["lhcb1"]["45"].get_twiss_init("s.ds.l5.b1")
    twiss_init_b1.mux = 0
    twiss_init_b1.muy = 0

    twiss_init_b2 = tw_sq_a45_ip5_a56["lhcb2"]["45"].get_twiss_init("s.ds.l5.b2")
    twiss_init_b2.mux = 0
    twiss_init_b2.muy = 0

    opt = collider.match(
        solve=False,
        only_markers=False,
        method="4d",
        solver_options={"n_bisections": 3, "min_step": 1e-6, "n_steps_max": 25},
        default_tol=default_tol,
        ele_start=["s.ds.l5.b1", "s.ds.l5.b2"],
        ele_stop=["e.ds.r5.b1", "e.ds.r5.b2"],
        restore_if_fail=restore,
        assert_within_tol=False,
        twiss_init=[twiss_init_b1, twiss_init_b2],
        targets=targets,
        vary=vary_list,
        verbose=False,
        n_steps_max=25,
    )

    if solve:
        opt.solve()

    collider.varval["kqx1.r5"] = -collider.varval["kqx1.l5"]
    collider.varval["kqx2.l5"] = collider.varval["kqx2a.l5"]
    collider.varval["kqx2a.l5"] = collider.varval["kqx2.l5"]
    collider.varval["kqx2b.l5"] = collider.varval["kqx2.l5"]
    collider.varval["kqx2a.r5"] = -collider.varval["kqx2.l5"]
    collider.varval["kqx2b.r5"] = -collider.varval["kqx2.l5"]
    collider.varval["kqx3.r5"] = -collider.varval["kqx3.l5"]

    collider.varval["kqx1.l1"] = collider.varval["kqx1.l5"]
    collider.varval["kqx2a.l1"] = collider.varval["kqx2a.l5"]
    collider.varval["kqx2b.l1"] = collider.varval["kqx2b.l5"]
    collider.varval["kqx3.l1"] = collider.varval["kqx3.l5"]
    collider.varval["kqx1.r1"] = collider.varval["kqx1.r5"]
    collider.varval["kqx2a.r1"] = collider.varval["kqx2a.r5"]
    collider.varval["kqx2b.r1"] = collider.varval["kqx2b.r5"]
    collider.varval["kqx3.r1"] = collider.varval["kqx3.r5"]

    # remove the imqXlr knobs if any
    quads_imqlr = "kq4.l5b2 kq4.r5b2 kq5.l5b2 kq5.r5b2 kq6.l5b2 kq6.r5b2"
    for quad in quads_imqlr.split():
        collider.vars[quad] = collider.varval[quad]

    for quad in quads_ir5_b1.split():
        collider.varval[quad.replace("5b", "1b")] = collider.varval[quad]

    for quad in quads_ir5_b2.split():
        collider.varval[quad.replace("5b", "1b")] = collider.varval[quad]

    return opt


collider = xt.Multiline.from_json("collider_00_from_madx.json")
collider.build_trackers()

collider.vars.load_madx_optics_file(
    "../../test_data/hllhc15_thick/opt_round_300_1500.madx"
)

collider.lhcb1.twiss_default["only_markers"] = True
collider.lhcb2.twiss_default["only_markers"] = True
collider.lhcb1.twiss_default["method"] = "4d"
collider.lhcb2.twiss_default["method"] = "4d"
collider.lhcb2.twiss_default["reverse"] = True

lm.set_var_limits_and_steps(collider)
collider.vars.vary_default.update(quads_ir15_defaults)

tw45_xt_0 = lm.get_arc_periodic_solution(collider, arc_name=["45"])

twiss_init_b1 = tw45_xt_0["lhcb1"]["45"].get_twiss_init("s.ds.l5.b1")
twiss_init_b1.mux = 0
twiss_init_b1.muy = 0

tw_pre_b1_0 = collider.lhcb1.twiss(
    ele_start="s.ds.l5.b1", ele_stop="e.ds.r5.b1", twiss_init=twiss_init_b1
)

print(tw_pre_b1_0[["betx", "bety"], ["ip5"]])

tw45_56_xt = lm.get_arc_periodic_solution(collider, arc_name=["45", "56"])

betx0_ip1 = 0.600
bety0_ip1 = 0.600
betx0_ip5 = 0.600
bety0_ip5 = 0.600

match_on_triplet = 1
collider.varval["kqx1.l5"] *= 0.99  # else kqx1.l5 hits the lower limit
optimizers = {}

optimizers["ir15"] = rematch_ir15(
    collider,
    betx0_ip5,
    bety0_ip5,
    tw_sq_a45_ip5_a56=tw45_56_xt,
    restore=False,
    solve=True,
    match_on_triplet=5,
)
print(optimizers["ir15"].target_status())
print(optimizers["ir15"].log())

# Match a second time and keep triplet untouched
optimizers["ir15_run2"] = rematch_ir15(
    collider,
    betx0_ip5,
    bety0_ip5,
    tw_sq_a45_ip5_a56=tw45_56_xt,
    restore=False,
    solve=True,
    match_on_triplet=0,
)
print(optimizers["ir15_run2"].target_status())
print(optimizers["ir15_run2"].log())


# Match again with constant triplet just in case
optimizers["ir15_run3"] = rematch_ir15(
    collider,
    betx0_ip5,
    bety0_ip5,
    tw_sq_a45_ip5_a56=tw45_56_xt,
    restore=False,
    solve=True,
    match_on_triplet=0,
)
print(optimizers["ir15_run3"].target_status())
print(optimizers["ir15_run3"].log())


tw45_xt = lm.get_arc_periodic_solution(collider, arc_name=["45"])
twiss_init_b1 = tw45_xt["lhcb1"]["45"].get_twiss_init("s.ds.l5.b1")
twiss_init_b1.mux = 0
twiss_init_b1.muy = 0

tw_pre_b1 = collider.lhcb1.twiss(
    ele_start="s.ds.l5.b1", ele_stop="e.ds.r5.b1", twiss_init=twiss_init_b1
)

print(tw_pre_b1[["betx", "bety"], ["ip5"]])

import matplotlib.pyplot as plt


fig, axs = plt.subplots(figsize=(21, 11))
axs.set_title("IP5")
axs.plot(
    tw_pre_b1["s", "s.ds.l5.b1":"e.ds.r5.b1"],
    tw_pre_b1["betx", "s.ds.l5.b1":"e.ds.r5.b1"],
    label=r"$\beta_x$, $\beta_0 = 0.6 m$",
)
axs.plot(
    tw_pre_b1["s", "s.ds.l5.b1":"e.ds.r5.b1"],
    tw_pre_b1["bety", "s.ds.l5.b1":"e.ds.r5.b1"],
    label=r"$\beta_y$, $\beta_0 = 0.6 m$",
)
axs.plot(
    tw_pre_b1_0["s", "s.ds.l5.b1":"e.ds.r5.b1"],
    tw_pre_b1_0["betx", "s.ds.l5.b1":"e.ds.r5.b1"],
    label=r"$\beta_x$, $\beta_0 = 0.5 m$",
    ls="--",
)
axs.plot(
    tw_pre_b1_0["s", "s.ds.l5.b1":"e.ds.r5.b1"],
    tw_pre_b1_0["bety", "s.ds.l5.b1":"e.ds.r5.b1"],
    label=r"$\beta_y$, $\beta_0 = 0.5 m$",
    ls="--",
)
axs.set_xlabel("s [m]")
axs.set_ylabel(r"$\beta_{x,y}$ [m]")
axs.legend()
plt.show()
