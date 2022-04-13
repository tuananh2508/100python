import art

print(art.logo)

def add(var1, var2):
    return var1 + var2

def subtract(var1, var2):
    return var1 - var2

def multiply(var1, var2):
    return var1 * var2

def divide(var1, var2):
    return var1/var2    

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    num1 = float(input("What is the first number: "))

    loop = True

    for symbol in operation:
        print(symbol)

    while loop:
        operation_symbol = input("Pick a operation: ")
        num2 = float(input("What is the next number: "))
        calculation = operation[operation_symbol]
        answer = float(calculation(num1, num2))
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        should_continue = input(f"Do you want to continue calculating with {answer} or type 'n' to restart the caculator: ")
        if should_continue == "y":
            num1 = answer
        else:
            loop = False
            calculator()

calculator()
