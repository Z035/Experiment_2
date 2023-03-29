import abc


class Model(abc.ABC):
    @abc.abstractmethod
    def rhs(self, t, y):
        """

        :param t:
        :param y:
        :return: dy/dt (array like) at time t
        """

    # model registry

    _registry = {}

    # key = 'ymal friendly name' of each Model subclass
    # value = subclasses

    def __init_subclass__(cls, exposed_name, **kwargs):
        """

        :param exposed_name: sth like 'sho' for SHOscillator
        :param kwargs:
        :return:
        """
        super().__init_subclass__(**kwargs)
        cls._registry[exposed_name] = cls
