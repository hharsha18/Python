import random 
choices = ['rock','paper','scissor']
user_choice=input("Enter your choice(rock,paper,scissor): ")
computer_choice = random.choice(choices)
print(computer_choice)

if user_choice==computer_choice:
    print("It's a tie")
elif (user_choice == 'rock' and computer_choice == 'scissor') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissor' and computer_choice == 'paper'):
     print("You WIN")
elif (user_choice == 'scissor' and computer_choice == 'rock') or (user_choice == 'rock' and computer_choice == 'paper') or  (user_choice == 'paper' and computer_choice == 'scissor'):
     print("You LOSE")
else:
     print("Invalid input.Please select rock,paper,scissor")     
