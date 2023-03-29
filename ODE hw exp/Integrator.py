import abc


class Integrator(abc.ABC):
    @abc.abstractmethod
    def __init__(self, model, dt):
        """
        :param model: model obj with a rhs() method that takes t,y and returns dy/dt
        :param dt:
        """
        self._model = model
        self._dt = dt

    @abc.abstractmethod
    def step(self, t, y):
        """
        Take a step
        :param t: current time
        :param y: vector of state
        :return: y at time t+dt
        """
        pass
