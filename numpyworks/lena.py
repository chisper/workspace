#!/usr/bin/env python

import numpy.testing
import scipy.misc
import sys
import matplotlib.pyplot

lena = scipy.misc.lena()
LENA_X = 512
LENA_Y = 512
numpy.testing.assert_equal((LENA_X,LENA_Y),lena.shape)

yfactor = float(sys.argv[1])
xfactor = float(sys.argv[2])

resized =lena.repeat(yfactor,axis =0).repeat(xfactor,axis=1)

matplotlib.pyplot.subplot(211)
matplotlib.pyplot.imshow(lena)

