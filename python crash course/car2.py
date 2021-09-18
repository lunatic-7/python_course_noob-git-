"""A set of classes represent all types od Cars"""

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