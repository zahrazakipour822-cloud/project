print("welcome to python pizza Deliveries!")
size = input("enter size pizza do you want: S, M or L: ")
pepperoni =input("Do you want pepperoni? yes or no: ")
extra_cheese = input("Do you want extra cheese? yes or no: ")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("you typed wrong")
if pepperoni == "yes":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "yes":
    bill += 1
print(f"your bill is {bill}")





