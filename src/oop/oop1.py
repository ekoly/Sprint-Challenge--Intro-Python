# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    """
        This is the base class.
    """
    pass

class FlightVehicle(Vehicle):
    """
        This is a flying vehicle.
    """
    pass

class Starship(FlightVehicle):
    """
        This is a space flying vehicle.
    """
    pass

class Airplane(FlightVehicle):
    """
        This is an atmosphere flying vehicle.
    """
    pass

class GroundVehicle(Vehicle):
    """
        This is a ground vehicle.
    """
    pass

class Car(GroundVehicle):
    """
        This is a 4-wheeled ground vehicle.
    """
    pass

class Motorcycle(GroundVehicle):
    """
        This is a 2-wheeled ground vehicle.
    """
    pass
