import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def format_answer(op, n1, n2):
    """Displays the complete calculation"""
    if op == "+":
        return f"{n1} + {n2} = {n1 + n2}"
    elif op == "-":
        return f"{n1} - {n2} = {n1 - n2}"
    elif op == "*":
        return f"{n1} * {n2} = {n1 * n2}"
    else:
        return f"{n1} / {n2} = {n1 / n2}"

calculations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    #Display the logo at the beginning of the calculator
    print(art.logo)

    #Get the first number from the user
    first_num = float(input("What is the first number? "))

    calculating = True
    while calculating:
        #Ask the user for the operation
        operation = input("+\n-\n*\n/\nPick an operation: ")

        #Restart the calculator if the operation is not valid
        if operation not in calculations:
            print("Sorry, that is not a correct operation.")
            calculator()

        #Ask the user for the second number
        second_num = float(input("What is the second number? "))

        #Get the answer
        answer = calculations[operation](first_num, second_num)

        #Display the answer
        print(format_answer(operation, first_num, second_num))

        #Ask user if they want to continue the calculation with the previous answer or start a new one
        continue_calc = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. ")

        #Continue the calculation using the previous answer as the first number
        if continue_calc == "y":
            first_num = float(answer)
        #Start a new calculation by calling the same function again to make it start over
        else:
            calculating = False
            print("\n" * 50)
            calculator()

calculator()