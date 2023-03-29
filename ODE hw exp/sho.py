import numpy as np

from Model import Model


class SHOscillator(Model):
    def __init__(self, omega):
        self._omega = omega

    def rhs(self, t, y):

        assert(len(y) == 2)

        dydt = np.zeros_like(y)

        # legibility purposes
        x, v = y[0], y[1]

        dydt[0] = v
        dydt[1] = - (self._omega**2) * x

        return dydt
