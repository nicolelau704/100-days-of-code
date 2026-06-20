import art

print(art.logo)

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

first_num = 0.0
second_num = 0.0
answer = ""
calculating = True
continue_calc = "n"
while calculating:
    if answer != "":
        continue_calc = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. ")

    operation = input("+\n-\n*\n/\nPick an operation: ")

    if operation not in calculations:
        print("Sorry, that is not a correct operation. Default operation is '+'")
        operation = "+"
    if continue_calc == "y":
        first_num = answer
        second_num = float(input("What is the second number? "))
        answer = calculations[operation](answer, second_num)
    else: #continue_calc == "n":
        first_num = float(input("What is the first number? "))
        second_num = float(input("What is the second number? "))
        answer = calculations[operation](first_num, second_num)

    print(format_answer(operation, first_num, second_num))
