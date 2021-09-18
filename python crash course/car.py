"""A class that can be used to represent a car"""

class Car:
    """A simple attemp to model a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.fill_gas_tank = 0 

    def get_discriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"\n{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def read_gas_tank(self):              # Let's add this new method read_gas_tank to Car class.
        """Read if gas tank is there"""
        print(f"This car has a {self.fill_gas_tank} value.")

    def update_odometer(self, mileage):                   # here we define a funct. to update a car's mileage each time.
        """Set the odometer value to current reading.
        Reject the change if it tries to roll back the odometer"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add this incremented value to odometer reading"""
        self.odometer_reading += miles
