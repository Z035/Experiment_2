from Integrator import Integrator


class Euler(Integrator):

    def step(self, t, y):
        # compute dy/dt based on current pos
        dydt = self._model.rhs(t,y)

        # return state at t+dt
        return y + dydt * self._dt
