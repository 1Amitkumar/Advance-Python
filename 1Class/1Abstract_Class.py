
from abc import ABCMeta, abstractmethod, abstractproperty


class AbstractVehicle(metaclass=ABCMeta):

    @abstractmethod
    def make_noise(self):                 # abstract method
        pass

    @property
    def brand(self):                      # abstract read-only-property
        pass

    def getname(self):                    # abstract read/write property
        pass

    def setname(self, value):
        pass

    def is_active(self):                   # non-abstract method
        return True


class Car(AbstractVehicle):
    def make_noise(self):
        print("droom")
    pass


rex = Car()
print(rex.is_active())
rex.make_noise()


