# number_one = input("enter first number") 
# number_two = input("enter second number") 
# total = number_one + number_two 
# print("total is" + total)
# now if we write number_one = 1 number_two = 2 it will give output as total is 44bcoz it will treat them as:
# total = "4" + "4" = 44
# now we will make 1 and 2 int. so we have to write
# number_one = int(input("enter first number"))
# number_two = int(input("enter second number"))
# total = number_one + number_two
# print("total is" + total)
# it will give error as total will be a no. and a no. can't be added with a string (in line 11)
# so we have to write line 11 as to make it string 
# print("total is" + str(total))

# workings

# str
# 4 ---> "4"

# int
# "4" ---> 4

# float 
# "4" ---> 4.0
number1 = float("44")
number2 = str(4)
number3 = int("33")
print(number1 + number3) # means float and int can be added.