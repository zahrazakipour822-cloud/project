import random

print("Welcome to the Game!")
User =int(input("what do you choose? type 0 for Rock, 1 for Paper, 2 for Scissor\n "))

computer = random.randint(0, 2)
print(f"Computer choose {computer}")

if User >= 3 or User <= 0:
    print("you choose invalid number!")
elif User == 0 and computer == 2:
    print("User is Win!")
elif User == 2 and computer == 0:
    print("User is Lose!")
elif User > computer:
    print("User Win!")
elif computer > User:
    print("computer Wins!")
elif computer == User:
    print("it is draw!")




    


