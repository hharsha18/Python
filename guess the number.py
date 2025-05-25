import random
print("Harsha D S,USN:1AY24AI041,SEC:M")
n=int(input("Enter the value of n:"))
choices = (1,n)
User_guess=int(input("Guess an number from 1 to n: "))
print("User guess: ",User_guess)
computer_choice = random.choice(choices)
print("computer choice: ",computer_choice )
if User_guess == computer_choice:
    print("You have guessed the right number")
else:
    print("You have failed to guess the right number")        
