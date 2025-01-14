import random

print("Hi! Im' going to try to guess your age.")
name = input("whats is your name? ")

lst_guesses = []

guessed = False
while(guessed == False):
    guess = random.randint(15,30)
    user_response = input("Are you "+str(guess)+ "years old? ")
    if user_response == 'y' or user_response == 'Y':
        print(f"Hahaha! {name} is " + str(guess)+ " years old! I geussed it!")
    else:
        print("Darn.")