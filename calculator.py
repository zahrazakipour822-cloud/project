def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
dic ={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
}
def calculator():
    first_number = float(input("Enter first number: "))
    should_contineu = True
    while should_contineu:
        for symbol in dic:
            print(symbol)
        opration_symbol= (input("Enter opration symbol: "))
        second_number = float( input("Enter second number: "))
        answer = dic[opration_symbol](first_number, second_number)
        print(f"{first_number} {opration_symbol} {second_number} = {answer}")

        chioce = input(f"Type Y to continue with {answer} or type N to start new calculating: ")

        if chioce == "Y":
            first_number = answer
        else:
            should_contineu = False
        calculator()
calculator()








