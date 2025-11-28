from random import randint
def game(level):
    if level == "easy":
        max_attempts = 10
    else:
        max_attempts = 5
    random_number = randint(1,100)
    guss = None
    attempts = 0
    while attempts < max_attempts and guss != random_number:
        guss = int(input("enter a number between 1 and 100: "))
        attempts += 1
        if guss > random_number:
            print(f"too high")

        elif guss < random_number:
            print(f"too low")
        elif guss == random_number:
            print(f"you got it ! ")
        else:
            print(f"you choose invalid number the correct number is {random_number} ")

        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"you have {remaining_attempts}  attempts ")
        else:
            print(f"your attempts  is finished")
print("Welcome to guss number game !")
print("I am thinking of a number between 1 and 100.")
choose_level = input("Choose a difficulty level:hard or easy:")
if choose_level == "easy":
    game("easy")
else:
    game("hard")

