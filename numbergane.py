import random
playing = True
number = str(random. randint (10,25))
print("I will generate a number from 10-25 and you have to guess the number one digit at a time")
while playing:
    guess = input("Give me your best guess \n")
    if number == guess:
       print("You have perfect guess, You won !")    
       break
    else:
       print("Try again !")