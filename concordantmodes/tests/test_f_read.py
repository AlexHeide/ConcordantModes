import numpy as np
import os
import re
from numpy.linalg import inv
from numpy import linalg as LA

from concordantmodes.f_read import FcRead


def test_f_read():
    errors = []

    os.chdir("./ref_data/f_read_test/")

    FCr = FcRead("fc.dat")
    FCr.run()
    fc_ref = [
        [
            0.4979448204,
            -0.0165621609,
            -5.29e-08,
            -0.257132153,
            0.0156954116,
            1.7959e-06,
            -0.0713232083,
            0.0845403615,
            -1.12865e-05,
            -0.0734882268,
            -0.0363389844,
            0.064473976,
            -0.0734878728,
            -0.0363548847,
            -0.0644635342,
            -0.0225133594,
            -0.0109797432,
            -8.984e-07,
        ],
        [
            -0.0165621507,
            0.6078583599,
            -3.7755e-06,
            -0.0348154431,
            -0.0951352547,
            -6.707e-07,
            0.0697599634,
            -0.297041958,
            3.29932e-05,
            -0.0326783854,
            -0.1075719729,
            0.0962461739,
            -0.0326923287,
            -0.1076191286,
            -0.0962755696,
            0.0469883445,
            -0.0004900456,
            8.488e-07,
        ],
        [
            -5.36e-08,
            -3.7758e-06,
            0.55828213,
            -5.054e-07,
            8.4e-08,
            -0.0618671813,
            -9.5628e-06,
            3.26668e-05,
            -0.0502917618,
            0.0611230618,
            0.0952257474,
            -0.2227533763,
            -0.0611126634,
            -0.0952548866,
            -0.2227074273,
            -2.765e-07,
            1.642e-07,
            -0.0006623833,
        ],
        [
            -0.2571321737,
            -0.0348154804,
            -5.056e-07,
            0.4285031321,
            -0.1281996348,
            -3.0417e-06,
            -0.0226770953,
            -6.99692e-05,
            3.364e-07,
            -0.0300077946,
            -0.0028422725,
            0.0033203586,
            -0.030007115,
            -0.0028418823,
            -0.0033193107,
            -0.0886789534,
            0.1687692392,
            2.1631e-06,
        ],
        [
            0.0156954014,
            -0.0951352491,
            8.4e-08,
            -0.128199649,
            0.5553356667,
            4.1627e-06,
            0.0382310787,
            0.0055106906,
            -9.038e-07,
            -0.0172866169,
            0.0044973077,
            -0.0027548449,
            -0.0172939829,
            0.0044970489,
            0.0027556565,
            0.1088537686,
            -0.4747054648,
            -4.1546e-06,
        ],
        [
            1.7958e-06,
            -6.705e-07,
            -0.0618672721,
            -3.0416e-06,
            4.1627e-06,
            0.046589097,
            -2.9571e-06,
            -1.0799e-06,
            0.0016569475,
            0.0288037157,
            -0.0002620796,
            0.0087007536,
            -0.0288004191,
            0.0002627444,
            0.0086986485,
            9.063e-07,
            -3.0771e-06,
            -0.0037781745,
        ],
        [
            -0.0713232685,
            0.0697600372,
            -9.5629e-06,
            -0.0226770575,
            0.0382310767,
            -2.9572e-06,
            0.0929951477,
            -0.0904878833,
            1.13908e-05,
            0.0046925653,
            -0.0090443221,
            -0.0006355818,
            0.0046923494,
            -0.0090441724,
            0.0006379649,
            -0.0083797364,
            0.0005852639,
            -1.2537e-06,
        ],
        [
            0.0845404505,
            -0.2970420108,
            3.26669e-05,
            -7.00323e-05,
            0.005510689,
            -1.0799e-06,
            -0.0904878474,
            0.3131395389,
            -3.52199e-05,
            0.0037034166,
            -0.0121687308,
            -0.0013087421,
            0.0037055715,
            -0.0121748779,
            0.001312076,
            -0.0013915589,
            0.0027353917,
            2.989e-07,
        ],
        [
            -1.12864e-05,
            3.2993e-05,
            -0.0502917911,
            3.363e-07,
            -9.038e-07,
            0.0016569622,
            1.13907e-05,
            -3.52197e-05,
            0.0463424661,
            -0.0082228449,
            0.0259915742,
            0.0008257863,
            0.00822215,
            -0.0259882714,
            0.0008322029,
            2.544e-07,
            -1.724e-07,
            0.0006343735,
        ],
        [
            -0.0734882103,
            -0.0326784072,
            0.0611230373,
            -0.030007802,
            -0.017286611,
            0.028803708,
            0.0046925529,
            0.0037034412,
            -0.0082228366,
            0.0913391208,
            0.0437114691,
            -0.0748607016,
            0.005644911,
            0.0043794386,
            -0.0069302383,
            0.0018194276,
            -0.0018293307,
            8.70313e-05,
        ],
        [
            -0.0363390042,
            -0.1075719514,
            0.0952257571,
            -0.0028422699,
            0.0044973082,
            -0.0002620689,
            -0.0090443039,
            -0.0121687483,
            0.0259915762,
            0.0437114697,
            0.1068957623,
            -0.1057893994,
            0.0043813907,
            0.0077678315,
            -0.0136770487,
            0.0001327177,
            0.0005797978,
            -0.0014888162,
        ],
        [
            0.0644739817,
            0.0962461701,
            -0.2227533703,
            0.0033203576,
            -0.0027548441,
            0.008700742,
            -0.0006355885,
            -0.0013087394,
            0.0008257631,
            -0.0748607035,
            -0.1057894012,
            0.2343245939,
            0.0069293873,
            0.0136696542,
            -0.0212987832,
            0.0007725655,
            -6.28396e-05,
            0.0002010545,
        ],
        [
            -0.0734878565,
            -0.0326923508,
            -0.0611126395,
            -0.0300071225,
            -0.0172939769,
            -0.0288004113,
            0.004692337,
            0.0037055963,
            0.0082221417,
            0.0056449111,
            0.004381392,
            0.0069293849,
            0.0913371459,
            0.0437290276,
            0.0748479441,
            0.0018205851,
            -0.0018296882,
            -8.64198e-05,
        ],
        [
            -0.0363549045,
            -0.1076191068,
            -0.0952548966,
            -0.0028418797,
            0.0044970495,
            0.0002627338,
            -0.0090441542,
            -0.0121748958,
            -0.0259882734,
            0.0043794373,
            0.0077678315,
            0.0136696531,
            0.0437290282,
            0.1069483958,
            0.1058218977,
            0.0001324729,
            0.0005807258,
            0.0014888854,
        ],
        [
            -0.0644635395,
            -0.0962755655,
            -0.2227074214,
            -0.0033193098,
            0.0027556557,
            0.008698637,
            0.0006379716,
            0.0013120731,
            0.0008321797,
            -0.0069302409,
            -0.0136770498,
            -0.0212987832,
            0.0748479459,
            0.1058218994,
            0.234273975,
            -0.0007728273,
            6.29872e-05,
            0.0002014129,
        ],
        [
            -0.0225133113,
            0.0469883621,
            -2.763e-07,
            -0.088678997,
            0.1088537343,
            9.063e-07,
            -0.008379734,
            -0.0013915465,
            2.543e-07,
            0.0018194242,
            0.000132718,
            0.000772564,
            0.0018205816,
            0.0001324732,
            -0.0007728258,
            0.1159320365,
            -0.154715741,
            -6.225e-07,
        ],
        [
            -0.0109797926,
            -0.0004900417,
            1.641e-07,
            0.168769274,
            -0.4747054587,
            -3.077e-06,
            0.0005852634,
            0.0027353727,
            -1.724e-07,
            -0.0018293213,
            0.0005798023,
            -6.28406e-05,
            -0.0018296788,
            0.0005807303,
            6.29882e-05,
            -0.1547157447,
            0.4712995951,
            2.9378e-06,
        ],
        [
            -8.981e-07,
            8.488e-07,
            -0.0006622751,
            2.163e-06,
            -4.1546e-06,
            -0.0037782569,
            -1.2538e-06,
            2.99e-07,
            0.0006344053,
            8.70119e-05,
            -0.0014887909,
            0.0002010257,
            -8.64006e-05,
            0.00148886,
            0.0002013841,
            -6.224e-07,
            2.9378e-06,
            0.0034037169,
        ],
    ]

    if np.setdiff1d(np.array(fc_ref), np.array(FCr.fc_mat.tolist())).size:
        errors.append("Read in force constants do not match the reference.")

    os.chdir("../../")

    assert not errors, "errors occured:\n{}".format("\n".join(errors))

