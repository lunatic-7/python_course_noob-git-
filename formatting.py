name = "wasif" 
age = 17
print("hello " + name + " your age is " + str(age))   # ugly syntax
print("hello {} your age is {} ".format(name, age)) # python 3
print(f"hello {name} your age is {age}")  # python 3.6 [best syntax]
print(f"hello {name} your age is {age + 3}") # we can also do addition in age like this.