import numpy as np

import xobjects as xo
import xtrack as xt

context = xo.ContextCpu()

line = xt.Line(elements=dict(
            qf1=xt.Multipole(knl=[0, 0.1]),
            qf2=xt.Multipole(knl=[0, 0.2]),
            qf3=xt.Multipole(knl=[0, 0.3]),
            dr=xt.Drift(length=1.)),
        element_names=['qf1', 'qf2', 'qf3', 'dr'])

tracker = line.build_tracker(_context=context)

elements_to_trim = [nn for nn in line.element_names if nn.startswith('qf')]

qf_setter = xt.CustomSetter(tracker, elements_to_trim,
                            field='knl', index=1 # we want to change knl[1]
                            )

values = qf_setter.get_values()
assert np.all(values == np.array([0.1, 0.2, 0.3]))

qf_setter.set_values(np.array([10., 100., 1000.]))
assert np.all(qf_setter.get_values() == np.array([10., 100., 1000.]))
assert line['qf1'].knl[1] == 10.
assert line['qf2'].knl[1] == 100.
assert line['qf3'].knl[1] == 1000.