"""A set of classes that can be used to represent an electric car."""

from car import Car

class Battery:                                                         # Here, We define a seperate class for our battery unlike earlier.
    """A simple attempt to model a battery for an electric car"""      # This just make the code more simple and readable.
 
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        "Print a statement describing the battery size."
        print(f"This car has a {self.battery_size}-KWh battery.")

    def get_range(self):                                               # Add range according to our battery capacity.
        """Print a statement abt. the range this battery provides"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go abt. {range} miles on a full-charge.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
 
    def __init__(self, make, model, year):

        """Initialize attributes of the parent class.
        Then initialize attributes specific to a electric car"""

        super().__init__(make, model, year)    
        self.battery = Battery()     
    
    def read_gas_tank(self):                     # As, electric car don't require a gas tank so we define a method in ElectricCar with same name as in Car.
        """Electric cars don't require a gas talk."""   # And so, it will overrid the value in parent class, 
        print(f"This car doesn't require a gas tank, you dumbo!")  # And pass this message.
