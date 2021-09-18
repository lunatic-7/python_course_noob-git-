# EXERCISE NUMBER GUESSING GAME.
import random  # to run random function. 1st we have to import random func.

winning_no = random.randint(1, 10)  # this func. is use to bring any random no.
guess = 1
number = int(input("guess a no. b/w 1 to 10 :"))
game_over = False

while not game_over:
    if number == winning_no:
        print(f"you win, and you guessed the no. in {guess} times.")
        game_over = True
    else:
        if number < winning_no:
            print("too low!")
            guess += 1 
            number = int(input("guess again : "))
        else:
            print("too high!")
            guess += 1
            number = input("guess again : ")








#  number == winning_no:
#     print(winning_no)
#     print("YOU WIN!!!!")
# else:  # this condition is called nested if else.
#     if number < winning_no:
#         print("too low!")
#     else:
#         print("too high!")