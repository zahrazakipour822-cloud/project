print("welcome to rollercoaster!")
height = int(input("enter your height: "))
bill = 0
if height >= 120:
    print("you can ride!")
    age = int(input("enter your age: "))
    if age <= 12:
        bill = 5
        print("you must pay 5$")
    elif 12 <= age <= 18:
        bill = 7
        print("you must pay $")

    elif 45 <= age <= 55:
        print("you must pay 0$")
    else:
        bill = 7
        print("you must pay 7$")

    wants_photo = input("wants photo? (Y/N): ")
    if wants_photo == "Y":
        bill += 3
    print(f"your bill is {bill}")
else:
    print("yiu can not ride you must be taller!")