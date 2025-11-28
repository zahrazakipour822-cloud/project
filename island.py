print("welcome to treasure island")
print("your mission is find the treasure)")
key = input("Where do you go left or right?").lower()
if key == "left":
    key_2=  input("swim or wait?: ")
    if key_2 == "wait":
       door = input("Which door do you go?")
       if door == "Red" or door =="blue":
           print("Game over!")
       elif door == "yellow":
           print("you win")
       else:
           print("you  must choose red,blue,yellow")

    else:
        print("Game over!")
else:
    print("Game over!")