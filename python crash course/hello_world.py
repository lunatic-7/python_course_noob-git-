                                                  ### CHAPTER - 1 (GETTING STARTED) ###

# In this we just learn how to install python and etc...
                                          
                                           ### CHAPTER - 2 (VARIABLES AND SIMPLE DATA TYPES) ###

print("Hello python world!")

# Variables

message = "Hello python world!" # Here 'message' is a variable. In which we can assign any of our values.
print(message)

message = "Hello python crash course world!" # We can use a varible many time with diff. values.
print(message)

# String method

name = "ada lovelace"
print(name.title())  # This method capitalises 1st lttr of each word just like a title.
print(name.lower())  # This method makes every lttr small.
print(name.upper())  # This method capitalises all the lttrs.

# Using variables in strings

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" # f (formatting) method is used to add up variables.
line = f"Hello, {full_name.title()}!"
print(line)

# Adding whitespaces

print("\tpython") # \t to leave some space before a value.
print("Languages: \npython\nC\njava script") # \n to move to a new line.
print("Languages: \n\tpython\n\tC\n\tjava script") # \n\t we can use both together also.

# Removing spaces

favourite_language = "python  "
print(favourite_language.rstrip())  # to remove right side's xtra space, this might create difficulty for python.

favourite_language = "  python"
print(favourite_language.lstrip()) # to remove left side's xtra space, = = = = = = .

favourite_language = "   python   "
print(favourite_language.strip()) # to remove both side's xtra space.

# Numbers

print(3 + 5) # addition
print(7 - 3) # subtraction
print(7 * 3) # multiplication
print(16 / 4) # division
print(4 ** 3) # exponential (4 ki shakti 3)
print(6 % 3) # it gives reminder in output.
print(4 + (3*7) / 3 ** 1 - 6) # python calculation follows P E M D M A S
# P - PARENTHESIS ()
# E - EXPONENT **
# M - MULTIPLICATION *
# D - DIVISION /
# M - MODULO %
# A - ADDITION +
# S - SUBTRACTION -

# Multiple assignments

x, y, z = 1, 2, 3 # like this we can assign diff. values in one line.
print(x)
print(y)
print(z)

# Constants

MAX_CONNECTIONS = 5000 # this kind of variable (all capitals) behaves like a constant it's value can never be changed.
print(MAX_CONNECTIONS)

# The Zen Of Python by Tim Peters.

import this # this is just a imp. philosophy of python.

                                            ### CHAPTER - 3 (INTRODUCING LISTS) ###

players = ['John cena', 'Dean ambrose', 'Seth rollins', 'Roman reings'] # a way to store collection of informations.
print(players)

# Accessing elements in a list

players = ['John cena', 'Dean ambrose', 'Seth rollins', 'Roman reings']
print(players[0]) # to access 1st element in the list.
print(players[0].upper()) # to access and capitalize 1st element in the list.
print(players[-1]) # to access last element in the list.
message = f"My favourite player is {players[0].title()}." # we can also use individual values from a list.
print(message)

# Changing, adding and removing elements from the list

bicycles = ['honda', 'suzuki', 'bajaj']
print(bicycles)
bicycles[-1] = 'hayabuza' # changing an element.
print(bicycles)
bicycles.append('duccati') # to add new element in previous list at the end.
print(bicycles) 

cric = [] # we can also add elements in an empty list.
cric.append('Ms Dhoni')
cric.append('raina')
cric.append('kohli')
print(cric)
bicycles.insert(1, 'apache') # to insert element in b\w a list.
print(bicycles)

bicycles = ['honda', 'suzuki', 'bajaj']
del bicycles[1] # to remove an element from the list permanently.
print(bicycles)

bicycles = ['honda', 'suzuki', 'bajaj']
popped_bicycle = bicycles.pop() # to remove last element from the list temporarily.
print(bicycles)
print(popped_bicycle) # we can print the removced element.
print(f"The last motorcycle I owned was a {popped_bicycle.title()}.")

bicycles = ['honda', 'suzuki', 'bajaj']
second_owned = bicycles.pop(1) # removing element temorarily while knowing it's position.
print(f"The 2nd motorcycle I owned was a {second_owned.title()}.")

bicycles = ['honda', 'suzuki', 'bajaj', 'hayabuza']
bicycles.remove('hayabuza') # removing by name
print(bicycles)
bicycles = ['honda', 'suzuki', 'bajaj', 'hayabuza']
too_expensive = 'hayabuza'
bicycles.remove(too_expensive) # removing by a reason.
print(f"{too_expensive.title()} is too expensive for me, but believe me that's not for so long.")

# Organising a list

# ----> sorting a list permanently by sort() method

cars = ['bmw', 'audi', 'lamborghini', 'ferrari']
print(cars)
cars.sort() # changes list in alphabetical order permanantly
print(cars)
cars.sort(reverse=True) # to print in reverse alphabetical order.
print(cars)

# ----> sorting a list temporarily by sorted() function

cars = ['bmw', 'audi', 'lamborghini', 'ferrari']
print(cars)
print(sorted(cars)) # changes list in alphabetical order teporarily.
print(cars)

# Printing a list in reverse order by reverse() method

cars = ['bmw', 'audi', 'lamborghini', 'ferrari']
cars.reverse() # it simply reverses the original order.
print(cars)

# Finding the length of a list by len() function

cars = ['bmw', 'audi', 'lamborghini', 'ferrari']
print(len(cars)) # to count no. of elements in the list.

                                                ### CHAPTER - 4 (WORKING WITH LISTS) ###

# Looping through an entire list using for loop

magicians = ['alice', 'carolina', 'hudini', 'dynamo']
for magician in magicians: # for loop, this is used to print each name in a list once, it just assign a variable magician to each name in the list and python interpreter reads it line by line.
    print(magician) # this space is necessary otherwise it will give indentation error.

magicians = ['alice', 'carolina', 'hudini', 'dynamo']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!") # like this we can print message to them.
    print(f"I can't wait to see ur next trick, {magician.title()}.\n") # \n to leave space after 2 lines.
    
print("Thank you, everyone that was great magic show.") # no need of indentation in this line, otherwise it will run like a loop means 1 time for each magician.

# Making numerical list using range() function

for value in range(1,6): # it never prints the last value here 6.
    print(value)

numbers = list(range(1,6)) # like this we can use range func. inside list func. to make a list.
print(numbers)
even_numbers = list(range(2,11,2)) # in this range the last 2 indicates how much no. we have to add up in 1st no. contantly till we reach last no.
print(even_numbers)

squares = []
for value in range(1,11):
    squares.append(value ** 2) # here we create a list to squares of 1 to 10 through while loop and append it to empty varible of squares.
print(squares)

# Simple statics with a list of no.

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(digits)) # to print lowest no. in list use min func.
print(max(digits)) # to print highest no. in list use max func.
print(sum(digits)) # to print sum of no. in list use sum func.

# List comprehensions (usually not for beginners but I will do)

squares = [value ** 2 for value in range(1,11)] # just a short method to write 181 no. of code.
print(squares)

# Slicing a list

players = ['john cena', 'seth rollins', 'dean ambrose', 'brock lesner']
print(players[0:3]) # to print some part of list. we use this method.
print(players[ :3 ]) # if we omit 1st place python itself start from 0.
print(players[2: ]) # if we omit 2nd place python itself end on last value in list.
print(players[ : ]) # if we don't put any no. it prints the whole list.
print(players[-3: ]) # it prints last three values.

# Looping through a slice

players = ['john cena', 'seth rollins', 'dean ambrose', 'brock lesner']
print("Here are the first three players of my team:")
for player in players[ :3]: # like this we can loop in a slice.
    print(player.title())

# Copying a loop

my_foods = ['ice cream', 'biryani', 'tikka', 'kebab']
friend_foods = my_foods[:] # like this we can copy our list
my_foods.append('carrot') # this will only be added in my list only
friend_foods.append('tomato') # this will only be added in my friend's list only
print("My foods are:")
print(my_foods)
print("My friend's foods are:")
print(friend_foods)

# Tuple (a kind of list that can never be changed)

dimensions = (200,50) # in this list we use parenthesis () instead od sq. brackets [] , these are permanent list and if we try to alter it's value it will give type error.
print(dimensions[0])
print(dimensions[1])
for dimension in dimensions: # like this we can loop a tuple
    print(dimension)

# Writing over a tuple 
                 # Although you can’t modify a tuple, you can assign a new value to a variable that represents a tuple.

dimensions = (200,50)
print("original dimension:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100) # like this we can assign new value to our dimensions using loop.
print("\nmodified dimension:")
for dimension in dimensions:
    print(dimension)

                                                    ### CHAPTER - 5 (IF STATEMENTS) ###

cars = ['audi', 'bmw', 'ferrari', 'lamborghini']
for car in cars:
    if car == 'bmw': # just an example of if statement.
        print(car.upper()) # if car is bmw it will print in upper.
    else:
        print(car.lower()) # else it will print in lower.

# Conditional test

car = 'audi' # ckecking for equality.
print(car == 'audi') # this simply asks python is the value of variable is audi? if yes it gives True in output.
print(car == 'bmw') # as it is wrong it simply gives False.
print(car.upper() == 'AUDI') # this will give True, case insensitive.

requested_topping = 'mushroom' 
if requested_topping != 'capsicum': # checking for inequality. this can be read as: is the requested topping not capsicum. 
    print("Hold the capsicum...")

# Numerical comparisons

age = 17 
print(age ==17) # check for equality.

answer = 17
if answer != 47: # check for inequality.
    print("Wrong answer. Try again!")

ans = 7
print(ans < 10) # as correct so gives True in output.
print(ans <= 11) # as correct gives True in output.
print(ans > 10) # as wrong gives False in output.

# Using and to check multiple conditions

age_0 = 7
age_1 = 17
print((age_0 < 10) and (age_1 < 16)) # as one of them is wrong it gives False.
print((age_0 < 10) and (age_1 <= 17)) # as both conditions correct so we get True.

# Using or to check multiple conditions

age_0 = 7
age_1 = 17
print((age_0 < 10) or (age_1 < 16)) # as one of them is correct it gives True. 
print((age_0 > 10) or (age_1 < 17)) # as both are wrong it gives False.

# Check whether a value is in list

req_top = ['onion', 'chicken', 'capsicum']
print('chicken' in req_top) # as correct gives True.
print('mushroom' in req_top) # as wrong gives False.

# Check whether a value is not in list

req_top = ['onion', 'chicken', 'capsicum']
topin = 'mushroom'
if topin not in req_top: # as correct give given output.
    print(f"{topin.title()}, No I don't want this toppin")

# Boolean expression 

# ---> A boolean expression is just another name for a conditional test.
# ---> A boolean expression is either true or false.
# eg: game_active = True
#      can_edit = False

# If-else statement

age = 17
if age >= 18:
    print("you are eligible for voting.") # as condition is false.
    print("have to got your voter id?") # these lines will not be printed.
else:
    print("sorry you are too young to vote.") # as false
    print("try as soon as you become eligible.") # else part will be printed, means these lines.

# If-elif-else chain

age = 17
if age < 4: # if ---> agar
    print("Your admission is free.") 
elif age < 18: # elif ---> ya to agar
    print("Your admission fees is $25")
else: # else ---> ya to
    print("Your admission fees is $70")

age = 17 # just a better approach of previous example in 326.
if age < 4: # if ---> agar
    price = 0
elif age < 18: # elif ---> ya to agar
    price = 25
else: # else ---> ya to
    price = 70
print(f"Your admission fees is ${price}.")

# Using multiple elif blocks

age = 67
if age < 4: # if ---> agar
    price = 0
elif age < 18: # elif ---> ya to agar
    price = 25
elif age < 65: # elif ---> ya to agar
    price = 40
else:
    price = 20 # else ---> ya to
print(f"Your admission fees is ${price}.")

# Note : The else block is a catchall statement. It matches any condition that
# wasn’t matched by a specific if or elif test, and that can sometimes include
# invalid or even malicious data. If you have a specific final condition you are
# testing for, consider using a final elif block and omit the else block. As a
# result, you’ll gain extra confidence that your code will run only under the
# correct conditions.

# Testing multiple conditions

toppin = ['chicken', 'extra cheese'] # through this method we can check multiple conditions.
if 'chicken' in toppin:
    print("Adding chicken.")
if 'pepperoni' in toppin: # we can't use else here otherwise python wont check multiple conditions.
    print("Adding pepperoni.")
if 'extra cheese' in toppin:
    print("Adding extra cheese.")
print("\nEnjoy ur pizza!")

# Note : In summary, if you want only one block of code to run, use an if-elifelse
# chain. If more than one block of code needs to run, use a series of
# independent if statements.

# Using if statement with list

requested_toppings = ['cheese', 'chicken', 'capsicum', 'onion']
for requested_topping in requested_toppings:
    if requested_topping == 'chicken': # as we are out of pizza.
        print("Sorry, We are out of chicken right now.") # so we want to print this code in the loop.
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making ur pizza.")

# Checking that a list is not empty

requested_toppings = []
if requested_toppings: # when we write variable's name with if, it checks if the list is empty or not.
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.") # if not empty then print these lines.
    print("\nFinished making ur pizza.")
else:
    print("Are u sure u want a plain pizza!") # if empty then print this line.

# Using multiple list

available_toppings = ['cheese', 'chicken', 'capsicum', 'onion']
requested_toppings = ['cheese', 'french fries', 'onion'] # arbitrary order of a person of french fries.
for requested_topping in requested_toppings: 
    if requested_topping in available_toppings: # checking for requested_topping in available_toppins. 
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry! We don't have {requested_topping}.") # if any one of them is not available the we get this printed in place of that requested_topping.
print("\nFinished making ur pizza")

                                                    ### CHAPTER - 6 (DICTIONARIES) ###

alien_0 = {'color' : 'green', 'points' : 5} # In dictionaries we can store many informations.
new_points = alien_0['points']
print(alien_0['color']) # The string 'color' is a key in this dictionary, and it's associated value is green.
print(alien_0['points'])
print(f"You just earned {new_points} points.")

# Adding new key value pairs

# Dictionaries are dynamic structures, and you can add new key-value pairs
# to a dictionary at any time.

alien_0 = {'color' : 'green', 'points' : 5}
print(alien_0)
alien_0['x_position'] = 0 # like this we can add new values to the dictionary.
alien_0['y_position'] = 25 # we use [] brackets to add new values.
print(alien_0)

# Starting with an empty dictionary

alien_0 = {}
alien_0['color'] = 'green' # like this we can add values in an empty dictionary.
alien_0['points'] = 5
print(alien_0)

# Modifying value in a dictionary

alien_0 = {'color' : 'green', 'points' : 5}
print(f"The alien is {alien_0['color']} and it gives {alien_0['points']} points.")
alien_0['color'] = 'yellow' # like this we can modify a value of dictionary.
alien_0['points'] = 7
print(f"The alien is {alien_0['color']} and it gives {alien_0['points']} points.")

alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}
# Now we move alien to the right.
# We will determine it's dist. according to it's given speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
alien_0['x_position']  = alien_0['x_position']  + x_increment # like this we add increment in previous value.
print(f"The distance it covered is {alien_0['x_position']}, according to {alien_0['speed']} speed.")

# Removing key-value pairs

alien_0 = {'color' : 'green', 'points' : 5}
print(alien_0)
del alien_0['color'] # we use del func. to remove a key-value pairs permanently.
print(alien_0)

# A dictionary of similar objects

fav_language = {
    'sarah' : 'python',
    'ali' : 'c++', # like this we can store a poll of diff. people.
    'john' : 'java',
    'randy' : 'python',
}
language = fav_language['ali'].title()
print(f"Ali's fav. language is {language}.")

# Using get() to access values

# If there’s a chance the key you’re asking for might not exist, consider
# using the get() method instead of the square bracket notation. If we use regular
# method then it will give an error.

alien_0 = {'color' : 'green', 'score' : 5}
point_value = alien_0.get('points', 'No point value assigned') # Use this method when u hve doubt abt. ur value presence.
print(point_value)

# Looping through all key value pairs by items() method

fav_language = {
    'sarah' : 'python',
    'ali' : 'c++', # like this we can store a poll of diff. people.
    'john' : 'java',
    'randy' : 'python',
}
for k, v in fav_language.items(): # like this we can print all key with their values.
    print(f"\nKey: {k}") # shrtcut k = key 
    print(f"Value : {v}") # shrtcut v = value

# Looping through all the keys in dictionary by keys() method

fav_language = {
    'sarah' : 'python',
    'ali' : 'c++', # like this we can store a poll of diff. people.
    'john' : 'java',
    'randy' : 'python',
}
for name in fav_language.keys(): # to print all the keys in the dictionary.
    print(name.title()) #  Here, python itself assign all the keys in a variable name.

fav_language = {
    'sarah' : 'python',
    'ali' : 'c++', # like this we can store a poll of diff. people.
    'john' : 'java',
    'randy' : 'python',
}
friends = ['sarah', 'john'] # here we assign a varible name.
for name in fav_language.keys():
    print(f"Hi {name.title()}")
    if name in friends:
        language = fav_language[name].title()
        print(f"\t{name.title()}, I see you love {language}!") # we print special message for friend.

# Looping through a dictionary's keys in a particular method by sorted() func.

fav_language = {
    'sarah' : 'python',
    'ali' : 'c++', # like this we can store a poll of diff. people.
    'john' : 'java',
    'randy' : 'python',
}
for name in sorted(fav_language.keys()): # this sorted fun. arranges loop in alphabetical order.
    print(f"{name.title()}, Thank you for taking the poll.")

# Looping through all values in dictionary by values() method.

fav_language = {
    'sarah' : 'python',
    'ali' : 'c++', # like this we can store a poll of diff. people.
    'john' : 'java',
    'randy' : 'python',
}
for language in fav_language.values(): # here value() method print all the values.
    print(language.title())

# To see each language chosen without repetition, we can use a set.
# A set is a collection in which each item must be unique:
fav_language = {
    'sarah' : 'python',
    'ali' : 'c++', # like this we can store a poll of diff. people.
    'john' : 'java',
    'randy' : 'python',
}
for language in set(fav_language.values()): # it doesn't repeat the value 'python'.
    print(language.title())

# Nesting
# A list of dictionaries
# Sometimes you’ll want to store multiple dictionaries in a list, or a list of
# items as a value in a dictionary. This is called nesting.

alien_0 = {'color' : 'green', 'points' : 5}
alien_1 = {'color' : 'yellow', 'points' : 7}
alien_2 = {'color' : 'red', 'points' : 10}
aliens = [alien_0, alien_1, alien_2] # here dictionaries are stored in a list.
for alien in aliens:
    print(alien)

# Make an empty list for storing aliens
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens
for alien in aliens[ :5]:
    print(alien)
print("...")

# Show how many aliens have been created
print(f"Total no. of aliens {len(aliens)}.")

# A list in a dictionary

# Note ---> When you need to break up a long line
# in a print() call, choose an appropriate point at which to break the line
# being printed, and end the line with a quotation mark. Indent the next
# line, add an opening quotation mark, and continue the string. Python
# will automatically combine all of the strings it finds inside the parentheses.

# Store inf. abt. a pizza being ordered.
pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms', 'extra cheese'],
}
# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
"with the following toppings:")
for topping in pizza['toppings']:
    print('\t' + topping)

# A dictionary in a dictionary

users = {
    'aeinstein' : {
        'first' : 'albert',
        'last' : 'einstein',
        'location' : 'princeton',
        },                              # Like this we can store dictionary in a dictionary.
    'mcurie' : {          # But we usually don't prefer it as codes get complicated.
        'first' : 'marie',
        'last' : 'curie',
        'location' : 'paris',
    },

}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

                                                ### CHAPTER - 7 (USER INPUT AND WHILE LOOP) ###

# input() funct.

message = input("Tell me something & I will repeat it back to you: ") # Here we ask user to input something & print that back.
print(message)

# For writing prompt that is longer than 1 line
prompt = "If, you tell me who you are! We can personalize ur details " 
prompt += "So, What is ur name? " # Like this we can add 2 prompts.
name = input(prompt)
print(f"Hello : {name.title()}")

# Using int() to accept numerical input

# When we give a numerical input python interprets it in strings.
# ex:
# age = (input("Enter your age : "))
# print(age >= 17) # this will give an error as python can't compare an string with integer value.
# So, now we have to use int funct.

age = int(input("What is your age : ")) # as we use int() funct. here so python gives no error.
if age >= 18:
    print("You are eligible for voting.")
else:
    print("Wait! A little longer.")

# When you use numerical input to do calculations and comparisons,
# be sure to convert the input value to a numerical representation first. By using int() func.

# The Modulo operator

number = int(input("Enter a no. & I will tell you if it is even or odd : "))
if number % 2 == 0:
    print(f"Your no. {number} is even.")
else:
    print(f"Your no. {number} is odd.")

# While loop
# The while loop runs as long as, or while, a certain condition is True.

current_no = 1
while current_no <= 7: # this loop will run until we get 7.
    print(current_no)
    current_no += 1 # It will constantly add 1 in current_no until we get 7.

# Letting the user choose when to quit

prompt = "\nTell me something & I will repeat it back to you: "
prompt += "\nEnter quit to exit the programm. "
message = ""
while message != 'quit': # this will check if we have entered quit
    message = input(prompt) # this programm will run until we enter quit.
    if message != 'quit': # We have to use this if statement if we don't want any message after quit.
        print(message)

# Using a flag
# Through this method we can add many events in which programm can be closed.
prompt = "\nTell me something & I will repeat it back to you: "
prompt += "\nEnter quit or end to exit the programm. "
active = True # Jb tk active true rhega message input hoga.
while active:
    message = input(prompt)

    if message == 'quit': # If we enter quit active will turn to false & message will not be printed.
        active = False
    elif message == 'end': # same like quit.
        active = False
    else:
        print(message)

# Using break to exit a loop

prompt = "\nTell me a country you want to visit: "
prompt += "\n(Enter 'quit' to exit the programm) "
while True:
    country = input(prompt)
    
    if country == 'quit':
        break # Through break statement the terminal ownself stops.
    else:
        print(f"I would also like to visit {country.title()}.")
# Note ---> You can use the break statement in any of Python’s loops. For example, you could use
# break to quit a for loop that’s working through a list or a dictionary.

# Using continue in a loop

# eg: We want to print odd no's only b/w 0 to 10.
current_no = 0
while current_no < 10:
    current_no += 1
    if current_no % 2 == 0: # It will not print even no's.
        continue
    print(current_no)

# Using a while loop with lists and dictionaries
# Moving items from one list to another.

unconfirmed_users = ['alice', 'brian', 'candace'] # A list of unconfirmed users.
confirmed_users = [] # An empty list to hold confirmed users
# Verifying each user until there are no more unconfirmed user.
# Move each verified user into the list of confirmed user.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
# The pop() func. removes unverified user one by one from the end of unconfirmed_users list.
    print(f"Verifying User : {current_user.title()}.")
    confirmed_users.append(current_user)
# Display all confirmed user.
print(f"\nThe following users have been confirmed :")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Removing all instances of a specific value from a list

# with for loop we have learnt to remove a specific value once from a list using remove()
# func. but with a while loop we can remove all the instances of that particular word 
# until we remove all that kind of word from the list.
pets = ['dog', 'cat', 'elephant', 'cat', 'rat', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat') # Here we apply remove() func. in a while loop so it keeps running until it remove all the words naming 'cat'.
print(pets)

# Filling a dictionary with users input

responses = {} # an empty dictionary
# Set a flag to indicate the polling is active
polling_active = True

while polling_active:
    # prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    # Store the response in the dictionary
    responses[name] = response
    # Find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person response? (yes/no) ")
    if repeat == 'no':
        polling_active = False
# Polling is complete, Show the results
print("\n.......Poll Results.......")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")

                                                    ### CHAPTER - 8 (FUNCTIONS) ###

# Defining a function

def greet_user(): # Here, def func. is used which means we define a function.
    """Display a simple greeting.""" # The text is a comment called a docstring, which describes what the function does.
    print("Hello!") # Finally this will be printed.
greet_user() # Here, we call the func.

# Passing information to a function

def greet_user(username): # Here we write a variable username in bracket 
    """Display a simple greeting."""
    print(f"Hello! {username.title()}.")
greet_user("wasif") # Here, we pass argument Wasif to it.

# Positional Arguments

def describe_pet(animal_type, pet_name): # Here animal_type and pet_name are parameters.
    """Display information about a pet."""
    print(f"\nI have a {animal_type.title()}.")
    print(f"My {animal_type.title()}'s name is {pet_name.title()}.")
describe_pet("hamster", "harry") # Here we pass arguments hamster and harry to it acc. to position.

# Multiple Arguments

describe_pet("dog", "willie") # Now we don't need to write whole code again. We just need to call that function with describe_pet().
# And like this we can pass diff. arguments to it. REMEMBER- Order matters in positional arguments...

# Keyword Arguments

describe_pet(pet_name ="harry", animal_type ="hamster") # If we write keywords like this, then we don't need to worry abt. their positions.

# Default values

def describe_pet(pet_name, animal_type ="hamster"): # Here we have set default animal_type to hamster
    """Display information about a pet."""
    print(f"\nI have a {animal_type.title()}.")
    print(f"My {animal_type.title()}'s name is {pet_name.title()}.")
describe_pet(pet_name ="harry") # We changed the definition of describe_pet() to include a default value, 
# 'hamster', for animal_type. Now when the function is called with no animal_type
#  specified, Python knows to use the value 'hamster' for this parameter.

# REMEMBER - When you use default values, any parameter with a default value needs to be listed 
# after all the parameters that don’t have default values. This allows Python to continue interpreting positional arguments correctly.

# Return values

# A function doesn’t always have to display its output directly. Instead, it can 
# process some data and then return a value or set of values. The value the 
# function returns is called a return value.

# Returning a simple value

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title() # Here, we call the function with full name by using return.

musician = get_formatted_name("alec", "benjamin") # After we return a function, It is necessary to give it a varible like musician here.
print(musician)

# Making an argument optional

def get_formatted_name(first_name, last_name, middle_name=''): # The middle name is optional, so it’s listed last in the 
# definition, and its default value is an empty string
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name("alec", "benjamin")
print(musician)
cricketer = get_formatted_name("mahendra", "dhoni", "singh") # Here we have to take care of positions.
print(cricketer)

# Returning a Dictionary

def build_person(first_name, last_name):
    """Return a dictionary of information abt. a person"""
    person = {"first" : first_name, "last" : last_name} # Like this we can return a dictionary as well
    return person

musician = build_person("alec", "benjamin")
print(musician)

# Using a function with a while loop

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("\nTell me your name:")
    print("(Type 'q' anything to exit.)")
    f_name = input("First name: ")
    if f_name == 'q': # Using these break method is imp. otherwise it will become an Infinite loop!
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello {formatted_name}!")

# Passing a list

def greet_users(names):
    """Greeting all users in the list"""
    for name in names: # Like this with the help of for loop we can greet all the users in list
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ["grace", "faith", "ray"]
greet_users(usernames)

# Modifying a list in a function

def print_models(unprinted_designs, completed_models):
    """Simulate printing each designs until none are left.
    then moving all designs to completed_models"""
    while unprinted_designs:                                 # We set up a list of unprinted designs and an empty list that will hold the 
                                                             # completed models. Then, because we’ve already defined our two functions, 
        current_design = unprinted_designs.pop()             # all we have to do is call them and pass them the right arguments. We call              
        print(f"Printing models: {current_design}!")         # print_models() and pass it the two lists it needs; as expected, print_models()
        completed_models.append(current_design)              # simulates printing the designs. Then we call show_completed_models() and
                                                             # pass it the list of completed models so it can report the models that have 
def show_completed_models(completed_models):                 # been printed. The descriptive function names allow others to read this 
    """Show all the models that were printed"""              # code and understand it, even without comments.
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)                      
                                                             
# Passing an Arbitrary number of Arguments

def make_pizza(*toppings):                                # The asterisk in the parameter name *toppings tells Python to make an 
                                                          # empty tuple called toppings and pack whatever values it receives into this tuple. 
    """List of number of toppings ordered"""
    print(toppings)

make_pizza('peperoni')
make_pizza('cheese', 'paneer', 'chicken')

def make_pizza(*toppings):
    """Summarize our Pizza"""
    print(f"\nThe following toppings are:")
    for topping in toppings:          # Now we use for loop instead print funct. to summarize our pizza.
        print(f"- {topping}")

make_pizza('peperoni')
make_pizza('cheese', 'paneer', 'chicken')

# Mixing Positional and Arbitrary arguments

# If you want a function to accept several different kinds of arguments, the 
# parameter that accepts an arbitrary number of arguments must be placed 
# last in the function definition.

def make_pizza(size, *toppings): # Here if the function needs to take the size of pizza, Then that parameter must come befor parameter *toppings
    """Summarize our Pizza"""
    print(f"\nMaking a pizza of {size}-inch and following topping: ")
    for topping in toppings:
        print(f"- {topping}")

make_pizza( 25, 'peperoni')
make_pizza(30, 'cheese', 'paneer', 'chicken')

# You’ll often see the generic parameter name *args, which collects arbitrary positional 
# arguments like this.

# Using arbitrary keyword arguments

def build_profile(first, last, **user_info):                                   
    """Build a dictionary containing any arbitraty info. of a user"""
    user_info['First name'] = first
    user_info['Last name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location = 'princeton',
                             field = 'physics')
print(user_profile)

 
# The double asterisks before the parameter **user_info cause Python to create 
# an empty dictionary called user_info and pack whatever name-value pairs 
# it receives into this dictionary.

# You’ll often see the parameter name **kwargs used to collect non-specific keyword argument.

# Storing your functions in modules

# Importing an entire module

# To start importing functions, we first need to create a module. A module
# is a file ending in .py that contains the code you want to import into your programm.
# I have created a seperate module pizza.py now I just need to recall it anythime with import function.

import pizza

pizza.make_pizza(25, 'pepporoni')
pizza.make_pizza(30, 'cheese', 'capsicum', 'chicken')

# Importing Specific Functions

# You can also import a specific function from a module. Here’s the general 
# syntax for this approach:

# from module_name import function_name

# You can import as many functions as you want from a module by separating each function’s name with a comma:

# from module_name import function_0, function_1, function_2

# Using as to give a function an Alias

# It's just like giving a nickname to a function when we call it, To make it look simple.

from pizza import make_pizza as mp # If we write like this then we don't need to use dot (.) any further as in 971 and 972

mp(25, 'pepporoni')
mp(30, 'cheese', 'capsicum', 'chicken')

# Using as to give a module an Alias

import pizza as p # It makes our function to call more simpler.

p.make_pizza(25, 'pepporoni')
p.make_pizza(30, 'cheese', 'capsicum', 'chicken')

# Importing all functions in a Module

# You can tell Python to import every function in a module by using the asterisk (*) operator:

from pizza import * # If we write like this, we don't need to use dot (.) any further.

make_pizza(25, 'pepporoni')
make_pizza(30, 'cheese', 'capsicum', 'chicken')

# The asterisk in the import statement tells Python to copy every function from the module pizza into this program file. Because every function 
# is imported, you can call each function by name without using the dot 
# notation. However, it’s best not to use this approach when you’re working 
# with larger modules that you didn’t write: if the module has a function 
# name that matches an existing name in your project, you can get some 
# unexpected results.

                                                        ### CHAPTER - 9 (CLASSES) ###

# Making an object from a class is called instantiation, and you work with 
# instances of a class.

# Creating and using a class

# Creating the Dog class

class Dog:       # The D of dog should be capital
    """A simple attempt to model a dog"""

    def __init__(self, name, age):                       #  A function that’s part of a class is a method. Everything you learned about 
        """Initialize name and age attributes"""         #  functions applies to methods as well; the only practical difference for now is
        self.name = name                                 #  the way we’ll call methods.
        self.age = age

    def sit(self):                                                   # The self parameter is required in the method definition, and it
        """Simulate a dog sitting in response to a command"""        # must come first before the other parameters.   
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} just rolled over.")

# Now we can call this class anytime just like a function.

# Making an instance from a class

my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Accessing attributes

# To access the attributes of an instance, you use dot notation. At v we access 
# the value of my_dog’s attribute name by writing:
# my_dog.name

# Calling methods

# After we create an instance from the class Dog, we can use dot notation to 
# call any method defined in Dog. Let’s make our dog sit and roll over:

my_dog = Dog('Willie', 6)
my_dog.sit()                  # Like this we can call an atrribute stored in class Dog.
my_dog.roll_over()

# Creating multiple instances

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"\nMy dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
                                                   # Like this we can create multiple instances from a class.
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.roll_over()

# Working with Classes and Instances

# The Car Class

class Car:
    """A simple attemp to model a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year

    def get_discriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car("audi", "a4", "2019")
print(my_new_car.get_discriptive_name())

# To make the class more interesting, let’s add an attribute that changes 
# over time. We’ll add an attribute that stores the car’s overall mileage.

# Setting a default value for an attribute

# Let’s add an attribute called odometer_reading that always starts with a 
# value of 0. We’ll also add a method read_odometer() that helps us read each 
# car’s odometer:

class Car:
    """A simple attemp to model a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_discriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car("audi", "a4", "2019")
print(my_new_car.get_discriptive_name())
my_new_car.read_odometer()

# Modifying attribute values

# There are 3 methods to do that, Let's see each one by one.

# Modifying an Attribute's value directly

my_new_car = Car("bmw", "a7", "2017")
print(my_new_car.get_discriptive_name())

my_new_car.odometer_reading = 27     # Like this using dot notation we can directly modify Attributes value.
my_new_car.read_odometer()

# Sometimes you’ll want to access attributes directly like this, but other 
# times you’ll want to write a method that updates the value for you.

# Modifying an attributes value through a method

class Car:
    """A simple attemp to model a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_discriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):                   # here we define a funct. to update a car's mileage each time.
        """Set the odometer value to current reading."""
        self.odometer_reading = mileage


my_new_car = Car("audi", "a4", "2019")
print(my_new_car.get_discriptive_name())

my_new_car.update_odometer(27)
my_new_car.read_odometer()

# We can extend the method update_odometer() to do additional work 
# every time the odometer reading is modified. Let’s add a little logic to 
# make sure no one tries to roll back the odometer reading:

class Car:
    """A simple attemp to model a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 7

    def get_discriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):                   # here we define a funct. to update a car's mileage each time.
        """Set the odometer value to current reading.
        Reject the change if it tries to roll back the odometer"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

my_new_car = Car("audi", "a4", "2019")
print(my_new_car.get_discriptive_name())

my_new_car.update_odometer(6) # this will show us a warning that we can't roll back an odometer. As it's initial value is 7.
my_new_car.read_odometer()

# Increamenting an Attribute's value through a method

# Sometimes you’ll want to increment an attribute’s value by a certain 
# amount rather than set an entirely new value.

class Car:
    """A simple attemp to model a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 7

    def get_discriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"\n{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

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

my_used_car = Car("suburu", "outback", "2015")
print(my_used_car.get_discriptive_name())

my_used_car.update_odometer(25_000) 
my_used_car.read_odometer()

my_used_car.increment_odometer(700) # Like this we add this incremented value in updated value.
my_used_car.read_odometer()

# REMEMBER = You can use methods like this to control how users of your program update values 
# such as an odometer reading, but anyone with access to the program can set the odometer reading to any value by accessing the attribute directly.
# Effective security takes extreme attention to detail in addition to basic checks like those shown here.

# Inheritance

# You don’t always have to start from scratch when writing a class. If the class 
# you’re writing is a specialized version of another class you wrote, you can 
# use inheritance. When one class inherits from another, it takes on the attributes and methods of the first class. The original class is called the parent 
# class, and the new class is the child class.

# The __init__ Method for a Child class

class Car:
    """A simple attemp to model a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_discriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"\n{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

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

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
 
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)       # The super() function at is a special function that allows you to call 
                                                  # a method from the parent class.
 
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_discriptive_name())

# Defining Attributes and Methods for Child class

# Once you have a child class that inherits from a parent class, you can add 
# any new attributes and methods necessary to differentiate the child class 
# from the parent class.

class Car:
    """A simple attemp to model a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_discriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"\n{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

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

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
 
    def __init__(self, make, model, year):

        """Initialize attributes of the parent class.
        Then initialize attributes specific to a electric car"""

        super().__init__(make, model, year)    
        self.battery_size = 75                     # Here, We add an extra attribute to our child class.            

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has {self.battery_size}-kWh battery size.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_discriptive_name())
my_tesla.describe_battery()

# Overriding Methods from the Parent class

# You can override any method from the parent class that doesn’t fit what 
# you’re trying to model with the child class.

class Car:
    """A simple attemp to model a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.fill_gas_tank = 0     # So, let's add a new attribute gas tank to prove what we want to prove.

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

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
 
    def __init__(self, make, model, year):

        """Initialize attributes of the parent class.
        Then initialize attributes specific to a electric car"""

        super().__init__(make, model, year)    
        self.battery_size = 75                     # Here, We add an extra attribute to our child class.            

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has {self.battery_size}-kWh battery size.")
    
    def read_gas_tank(self):                     # As, electric car don't require a gas tank so we define a method in ElectricCar with same name as in Car.
        """Electric cars don't require a gas talk."""   # And so, it will overrid the value in parent class, 
        print(f"This car doesn't require a gas tank, you dumbo!")  # And pass this message.

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_discriptive_name())
my_tesla.describe_battery()
my_tesla.read_gas_tank()

# Instances and Attributes

# When we see our class is becoming lenthy, we can break the into smaal classes to make them understandable.

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

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_discriptive_name())
my_tesla.battery.describe_battery()
my_tesla.read_gas_tank()                # This line tells Python to look at the instance my_tesla, find its battery
                                        # attribute, and call the method describe_battery() that’s associated with the 
                                        # Battery instance stored in the attribute."""
my_tesla.battery.get_range()

# Importing Classes

# As you add more functionality to your classes, your files can get long, even 
# when you use inheritance properly. In keeping with the overall philosophy 
# of Python, you’ll want to keep your files as uncluttered as possible. To help, 
# Python lets you store classes in modules and then import the classes you 
# need into your main program.

# Importing a single class

# Let's make a seperate module car.py
# Okay I have made it now we will import it.

from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_discriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Storing Multiple Classes in a Module

# You can store as many classes as you need in a single module, although 
# each class in a module should be related somehow. The classes Battery
# and ElectricCar both help represent cars, so let’s make a new module 
# car2.py

from car2 import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_discriptive_name())
my_tesla.battery.describe_battery()
my_tesla.read_gas_tank()
my_tesla.battery.get_range()

# Importing Multiple Classes from a Module

# You can import as many classes as you need into a program file. If we 
# want to make a regular car and an electric car in the same file, we need 
# to import both classes, Car and ElectricCar

from car2 import Car, ElectricCar

my_beetle = Car('volkswagon', 'beetle', 2019)
print(my_beetle.get_discriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_discriptive_name())

# Importing an entire Module

# You can also import an entire module and then access the classes you need 
# using dot notation. This approach is simple and results in code that is easy 
# to read.

import car2

my_beetle = car2.Car('volkswagon', 'beetle', 2019)
print(my_beetle.get_discriptive_name())

my_tesla = car2.ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_discriptive_name())

# Importing Module into a Module

# Let's make a new module electric_car.py in which we will add battery and electric car Classes, and At first we
# will import the car module in that module, to make it run.

# Now we can import from each module separately and create whatever kind of car we need.

from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagon', 'beetle', 2019)
print(my_beetle.get_discriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_discriptive_name())

# Using Alias         # It's kind of a pet name to a class

from electric_car import ElectricCar as EC

my_tesla = EC('tesla', 'model s', 2019)
print(my_tesla.get_discriptive_name())

# The Python Standard Library

# The Python standard library is a set of modules included with every Python installation.

# One interesting function from the random module is randint(). This 
# function takes two integer arguments and returns a randomly selected integer between (and including) those numb.

from random import randint
print(randint(1, 7))

# Another useful function is choice(). This function takes in a list or tuple 
# and returns a randomly chosen element.

from random import choice
players = ['john', 'seth', 'brock', 'roman', 'triple h']
first_up = choice(players)
print(first_up.title())

# The random module shouldn’t be used when building security-related 
# applications, but it’s good enough for many fun and interesting projects.

# Styling Classes

# 1. Class names should be written in CamelCase.
# 2. Every class should have a docstring immediately following the class definition. The docstring should be a brief description of what the class does.

                                        ### CHAPTER - 10 (FILES AND EXCEPTIONS) ### 

# Reading from a File

# When you want to work with the information in a text file, the first step 
# is to read the file into memory. You can read the entire contents of a file, or 
# you can work through the file one line at a time.

# Reading an Entire File

# So, I have created a txt file pi_digits with the value of pi in it. Now we will read it.

with open('pi_digits.txt') as file_object: #  The open() function needs one argument: the name of the file you want to open.
    contents = file_object.read()
print(contents)

# Here we will get an extra blank line at last bc, read() returns an empty string when it reaches the end of the file; this empty 
# string shows up as a blank line.
# We can remove it by using rstrip() like this:

with open('pi_digits.txt') as file_object: #  The open() function needs one argument: the name of the file you want to open.
    contents = file_object.read()
print(contents.rstrip())

# File Paths

# So, If our txt file is not stored in the same directory then we need to provide a file path.

with open('Text-files/testing.txt') as file_object:  # Like this we provide the path, as our txt file is in folder named "Text-files".
    contents = file_object.read()
print(contents.rstrip())

# REMEMBER : Windows systems use a backslash (\) instead of a forward slash (/) when displaying 
# file paths, but you can still use forward slashes in your code.

# You can also tell Python exactly where the file is on your computer 
# regardless of where the program that’s being executed is stored. This 
# is called an absolute file path.

file_path = 'D:/coding/python course/python crash course/Text-files/testing.txt'

with open(file_path) as file_object:
    contents = file_object.read()
print(contents)

# Using absolute paths, you can read files from any location on your system.

# REMEMBER : If you try to use backslashes in a file path, you’ll get an error because the backslash is 
# used to escape characters in strings. For example, in the path "C:\path\to\file.txt", 
# the sequence \t is interpreted as a tab. If you need to use backslashes, you can escape 
# each one in the path, like this: "C:\\path\\to\\file.txt". or jus replce backslash with forward slash.

# Reading Line by Line

# When you’re reading a file, you’ll often want to examine each line of the file. 
# You might be looking for certain information in the file, or you might want to 
# modify the text in the file in some way.

file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    for line in file_object:
        print(line)

# Making a list of Lines from a File

# When you use with, the file object returned by open() is only available inside 
# the with block that contains it. If you want to retain access to a file’s contents outside the with block,
# you can store the file’s lines in a list inside the block and then work with that list.

file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# Working with File's contents

# After you’ve read a file into memory, you can do whatever you want with that data.

file_name = 'pi_digits.txt'

with open(file_name) as file_object:  # We start by opening the file and storing each line of digits in a list,
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string)) # Here, we count no. of digits in pi_string.

# We can use strip() instead of rstrip() to remove all the spaces. Like this:
file_name = 'pi_digits.txt'

with open(file_name) as file_object:  # We start by opening the file and storing each line of digits in a list,
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string)) # Here, we count no. of digits in pi_string.

# Now we have a string containing pi to 30 decimal places. The string 
# is 32 characters long because it also includes the leading 3 and a decimal point.

# REMEMBER : When Python reads from a text file, it interprets all text in the file as a string. If you 
# read in a number and want to work with that value in a numerical context, you’ll 
# have to convert it to an integer using the int() function or convert it to a float using 
# the float() function.

# Large Files: one million digits

# We’ll only print just the first 50 decimal places, so we don’t have to watch a million digits scroll by in the terminal.

file_name1 = 'pi_million_digits.txt'
with open(file_name1) as file_object:  # We start by opening the file and storing each line of digits in a list,
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[ :52]}...")
print(len(pi_string))

# Python has no inherent limit to how much data you can work with; you can work with as much data as your system’s memory can handle.

# Is Your Birthday contained in pi

# Now, let's check if our birthday is contained in 1st one million digits of pi.

file_name1 = 'pi_million_digits.txt'
with open(file_name1) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter Your birthday, in the form of mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in 1st million digits of pi!")
else:
    print("Sorry bro! Your birthday doesn't appear in 1st million digits on pi!")

# Writing to a File

# Writing to an Empty File

# To write text to a file, you need to call open() with a second argument telling Python that you want to write to the file. 

file_name = 'programming.txt'

with open(file_name, 'w') as file_object: # So, here we have created a txt file programming and written something to it.
    file_object.write("I love programming!")  # It won't be shown in the terminal tho, but we can directly open and see it.

# The second argument, 'w', tells Python that we want to open the file in write mode. You can open a file
# in read mode ('r'), write mode ('w'), append mode ('a'), or a mode that allows 
# you to read and write to the file ('r+'). If you omit the mode argument, 
# Python opens the file in read-only mode by default.  

# REMEMBER : Python can only write strings to a text file. If you want to store numerical data in a 
# text file, you’ll have to convert the data to string format first using the str() function.

# Writing Multiple Lines

# The write() function doesn’t add any newlines to the text you write. So if 
# you write more than one line without including newline characters, your 
# file may not look the way you want it to.

file_name = 'program.txt'

with open(file_name, 'w') as file_object: # So, here we have created a txt file programming and written something to it.
    file_object.write("I love programming!")
    file_object.write("I love creating new games...") # Here, we won't get the output how we expect it to.
# If you open programming.txt, you’ll see the two lines squished together in 1 line.
# like this : I love programming.I love creating new games.

# Including newlines in your calls to write() makes each string appear on its own line.

file_name = 'program_1.txt'

with open(file_name, 'w') as file_object:
    file_object.write("I love programming!\n")
    file_object.write("I love creating new games...\n")

# The output now appears on separate lines: Like this...
# I love programming.
# I love creating new games.

# Appending to a File

# If you want to add content to a file instead of writing over existing content, you can open the file in append mode. 
file_name = 'program_1.txt'

with open(file_name, 'a') as file_object:        # this will add these new lines to our existing program_1.txt
    file_object.write("I also love singing.\n")
    file_object.write("I also want to make apps in future...\n")

# Exceptions

# Python uses special objects called exceptions to manage errors that arise during a program’s execution. Whenever an error occurs that makes Python 
# unsure what to do next, it creates an exception object. If you write code 
# that handles the exception, the program will continue running. If you don’t 
# handle the exception, the program will halt and show a traceback, which 
# includes a report of the exception that was raised.

# Handling the ZeroDivisionError Exception

# print(7/0) # No, num. can be divided by zero, So obviously python can't do this. It will give an traceback error.
# To solve this error, we will use a try-except block.

# Using try-except blocks

# When you think an error may occur, you can write a try-except block to handle the exception that might be raised.

try:
    print(5/0)
except ZeroDivisionError: # Like this it won't give an error, instead print the next message.
    print("You can't divide any num. by 0! You fool.")

# We put print(5/0), the line that caused the error, inside a try block. If 
# the code in a try block works, Python skips over the except block. If the code 
# in the try block causes an error, Python looks for an except block whose 
# error matches the one that was raised and runs the code in that block.

# Using Exceptions to Prevent Crashes

# Handling errors correctly is especially important when the program has 
# more work to do after the error occurs. This happens often in programs 
# that prompt users for input.

print("Give me two numbers and I will divide them!")
print("Enter 'q' to exit the program.")

while True:
    first_no = input("\nFirst number: ")
    if first_no == 'q':
        break
    second_no = input("Second number: ") # So now, if someone put a 0 in second no. This code will still work.
    if second_no == 'q': 
        break
    try:
        answer = int(first_no) / int(second_no)
    except ZeroDivisionError:
        print("You can't divide any num. by 0! you foooool!")
    else:
        print(answer)        

# It’s bad if the program gets crashed, but it’s also not a good idea to let 
# users see tracebacks. Nontechnical users will be confused by them, and in 
# a malicious setting, attackers will learn more than you want them to know 
# from a traceback. For example, they’ll know the name of your program 
# file, and they’ll see a part of your code that isn’t working properly. A skilled 
# attacker can sometimes use this information to determine which kind of 
# attacks to use against your code.

# Handling the FileNotFoundError Exception

# One common issue when working with files is handling missing files. The 
# file you’re looking for might be in a different location, the filename may 
# be misspelled, or the file may not exist at all. You can handle all of these 
# situations in a straightforward way with a try-except block.

# Let's try to read a file which isn't available.

# file_name = 'alice.txt'

# with open(file_name, encoding='utf-8') as f:
#     contents = f.read()

# There are two changes here. One is the use of the variable f to represent the file object, which is a common convention. The second is the use of 
# the encoding argument. This argument is needed when your system’s default 
# encoding doesn’t match the encoding of the file that’s being read.

# No such file so it will give an error.

# Let's fix this error:

file_name = 'alice.txt'

try:
    with open(file_name, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, this file {file_name} doesn't exist!")

# Analyzing Text

# You can analyze text files containing entire books. Many classic works of literature are available as simple text files because they are in the public domain. 
# The texts used in this section come from Project Gutenberg (http://gutenberg.org/). Project Gutenberg maintains a collection of literary works that are 
# available in the public domain, and it’s a great resource if you’re interested in working with literary texts in your programming projects.

file_name = 'aliceinwonderland.txt'

try:
    with open(file_name, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, this file {file_name} doesn't exist!")
else:
    # Count the approximate no. of letters in the file
    words = contents.split()
    num_words = len(words)
    print(f"The file {file_name} has {num_words} words in it...")

# The split() method separates a string into parts wherever it finds a space and stores all the parts of the string in a list.

# Working with Multiple Files

# Let’s add more books to analyze. But before we do, let’s move the bulk of 
# this program to a function called count_words(). By doing so, it will be easier 
# to run the analysis for multiple books.

def count_words(filename):
    """It is to count the no. of words in each file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, this file {filename} doesn't exist!")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has {num_words} words in it...")

# # So, we have stored our code in a function now we can call it anytime.
# # Now, let's download some books to count their words.

filenames = ['aliceinwonderland.txt', 'siddhartha.txt', 'littlewomen.txt', 'mobidick.txt']
for filename in filenames:
    count_words(filename)

# Failing Silently

# In the previous example, we informed our users that one of the files 
# was unavailable. But you don’t need to report every exception you catch. 

# Python has a pass statement that tells it to do nothing in a block.

def count_words(filename):
    """It is to count the no. of words in each file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has {num_words} words in it...")

filenames = ['aliceinwonderland.txt', 'siddhartha.txt', 'littlewomen.txt', 'mobidick.txt']
for filename in filenames:
    count_words(filename)

# The pass statement also acts as a placeholder. It’s a reminder that you’re 
# choosing to do nothing at a specific point in your program’s execution and that you might want to do something there later.

# Dealing which Errors to Report

# How do you know when to report an error to your users and when to fail silently? If users know which texts are supposed to be analyzed, they might 
# appreciate a message informing them why some texts were not analyzed. If users expect to see some results but don’t know which books are supposed 
# to be analyzed, they might not need to know that some texts were unavailable. Giving users information they aren’t looking for can decrease the 
# usability of your program. Python’s error-handling structures give you finegrained control over how much to share with users when things go wrong; 
# it’s up to you to decide how much information to share.

# Storing Data

# Simplest way to storing users data is by using json module.

# REMEMBER: The JSON (JavaScript Object Notation) format was originally developed for JavaScript. 
# However, it has since become a common format used by many languages, including Python.

# Using json.dump() and json.load()

# Let’s write a short program that stores a set of numbers and another program that reads these numbers back into memory. The first program will 
# use json.dump() to store the set of numbers, and the second program will use json.load()

import json

numbers = ['1', '3', '7', '13', '17', '20', '27']

filename = 'numbers.json' # Here, we store numbers in form of json.
with open(filename, 'w') as f:
    json.dump(numbers, f) # we use the json.dump() function to store the list numbers in the file numbers.json.

# This program has no output, but let’s open the file numbers.json and look at it. The data is stored in a format that looks just like Python.

# Now we will add a program that uses json.load() to read the list back into memory.

import json

filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f) # we use the json.load() function to load the information stored in numbers.json, and we assign it to the variable numbers.

print(numbers)

# This is a simple way to share data between two programs.

# Saving and Reading User-generated Data.

import json

username = input("Tell me your username: ") # Here, we ask user his username and then we will store it.

filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We will remember {username}, whenever you will be back!")

import json

filename = 'username.json'
with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back {username}!")

# we want to retrieve their username from memory if possible; therefore, we’ll start with a try block that attempts to recover the 
# username. If the file username.json doesn’t exist, we’ll have the except block prompt for a username and store it in username.json for next time

import json

# Load the username if it is stored already.
# Otherwise, prompt for the username and store it.

filename = 'username_1.json'
try:
    with open(filename) as f:
        username_1 = json.load(f)
except FileNotFoundError:
    username_1 = input("Tell me your username: ")
    with open(filename, 'w') as f:
        json.dump(username_1, f)
        print(f"We will remember {username_1}, whenever you will be back!")
else:
    print(f"Welcome back {username_1}!")

# Your username will be shown in output, you see if the program was already run at least once.

# we try to open the file username1.json. If this file exists, we read the username back into memory and print a 
# message welcoming back the user in the else block. If this is the first time the user runs the program, username1. 
# json won't exist and a FileNotFoundError will occur. Python will move on to the except block where we prompt the 
# user to enter their username. We then use json.dump() to store the username and print a greeting.

# Refactoring

# Often, you’ll come to a point where your code will work, but you’ll recognize that you could improve the code by breaking it up into a series of functions
# that have specific jobs. This process is called refactoring. Refactoring makes your code cleaner, easier to understand, and easier to extend.

import json

def greet_user():
    """Greet the user by name"""
    filename = 'username_1.json'
    try:
        with open(filename) as f:
            username_1 = json.load(f)
    except FileNotFoundError:
        username_1 = input("Tell me your username: ")
        with open(filename, 'w') as f:
            json.dump(username_1, f)
            print(f"We will remember {username_1}, whenever you will be back!")
    else:
        print(f"Welcome back {username_1}!")

greet_user()

# The function greet_user() is doing more than just greeting the user—it’s also retrieving a stored username if one exists and prompting 
# for a new username if one doesn’t exist. Let’s refactor greet_user() so it’s not doing so many different tasks.

import json

def get_stored_username_1():
    """Get stored username if available"""
    filename = 'username_1.json'
    try:
        with open(filename) as f:
            username_1 = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username_1

def get_new_username_1():
    """Prompt for a new username"""
    username_1 = input("Tell me your username: ")
    filename = 'username_1'
    with open(filename, 'w') as f:
        json.dump(username_1, f)
    return username_1        

def greet_user():
    """Greet the user by name"""
    username_1 = get_stored_username_1()
    if username_1:
        print(f"Wecome back {username_1}!")
    else:
        username_1 = get_new_username_1()
        print(f"We will remember {username_1}, whenever you will be back!")

greet_user()

# This compartmentalization of work is an essential part of writing clear code that will be easy to maintain and extend.

                                                ### CHAPTER - 11 (TESTING YOUR CODE) ###

# In this chapter you’ll learn to test your code using tools in Python’s unittest module.

# Testing a Function

# I have created a function in name_function.py. Now we will test what get_formatted_name does.

from name_function import get_formatted_name

print("Enter 'q' any time to exit")
while True:
    first = input(f"\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input(f"Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly Formatted Name : {formatted_name}.")

# So, This function works, YAY... Testing SUCCESSFULL

# Unit Tests and Test Cases

# The module unittest from the Python standard library provides tools for 
# testing your code. A unit test verifies that one specific aspect of a function’s 
# behavior is correct. A test case is a collection of unit tests that together prove 
# that a function behaves as it’s supposed to, within the full range of situations you expect it to handle.

# A Passing Test

import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Test for name_fuction.py"""

    def test_first_last_name(self):
        """Do names like 'khbbw zxcvb' works?"""
        formatted_name = get_formatted_name('khbbw', 'zxcvb')
        self.assertEqual(formatted_name, 'Khbbw Zxcvb')     # we use one of unittest’s most useful features: an assert method. 
                                # Assert methods verify that a result you received matches the result you expected to receive.

if __name__ == '__main__':
    unittest.main()

#                                           self.assertEqual(formatted_name, 'Khbbw Zxcvb')
# This line says, “Compare the value in formatted_name to the string 'Khbbw Zxcvb'. If 
# they are equal as expected, fine. But if they don’t match, let me know!”

## .
## ----------------------------------------------------------------------
## Ran 1 test in 0.000s

## OK

# Above is the output.
# The dot on the first line of output tells us that a single test passed. 
# The next line tells us that Python ran one test, and it took less than 0.001 seconds to run.
# The final OK tells us that all unit tests in the test case passed.

# A Failing Test

# Let's create a function name_m_function.py which contains a middle name also, then we will test it by giving first and last name only,
# and as we can imagine this test is surely gonna fail.

import unittest
from name_m_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Test for name_m_fuction.py"""

    def test_first_middle_last_name(self):
        """Do names like 'khbbw zxcvb' works?"""
        formatted_name = get_formatted_name('khbbw', 'zxcvb')
        self.assertEqual(formatted_name, 'Khbbw Zxcvb')     # we use one of unittest’s most useful features: an assert method. 
                                # Assert methods verify that a result you received matches the result you expected to receive.

if __name__ == '__main__':
    unittest.main()

# This code is not running here, might be because of these long 2238 lines codes in one fine, but I have tested it, It is running... :)
# This will give this kind of output.

# E
# ======================================================================
# ERROR: test_first_middle_last_name (__main__.NameTestCase)
# Do names like 'khbbw zxcvb' works?
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "D:\python course\python crash course\test.py", line 9, in test_first_middle_last_name
#     formatted_name = get_formatted_name('khbbw', 'zxcvb')
# TypeError: get_formatted_name() missing 1 required positional argument: 'last'

# ----------------------------------------------------------------------
# Ran 1 test in 0.001s

# FAILED (errors=1)

# We can correct this function by making middle name optional like this:

# def get_formatted_name(first, last, middle=''):
#     """Generate a neatly formatted full name."""
#  if middle:
#     full_name = f"{first} {middle} {last}"
#  else:
#     full_name = f"{first} {last}"
#     return full_name.title()

# Testing a Class

# A Variety of Assert Methods

# Assert Methods Available from the unittest Module

# Method                                 Use
# assertEqual(a, b)              Verify that a == b
# assertNotEqual(a, b)           Verify that a != b
# assertTrue(x)                  Verify that x is True
# assertFalse(x)                 Verify that x is False
# assertIn(item, list)           Verify that item is in list
# assertNotIn(item, list)        Verify that item is not in list

### REMEMBER = We can't run another file after running a test file... So, I m doing further codes in hello_world_2.py ###
print("chal gya")