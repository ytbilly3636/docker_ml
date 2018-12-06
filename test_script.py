# -*- coding: utf-8 -*-

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import chainer
import chainer.links as L
import chainer.function as F
from chainer import Chain, Variable, optimizers

print(chainer.__version__)
print(matplotlib.__version__)

a = np.random.rand(10).flatten()
plt.plot(a)
plt.show()
