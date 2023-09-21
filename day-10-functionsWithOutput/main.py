"""
def format_name(f_name, l_name):
    Take a first and last name and format it to return the title case version of the name
    result = (f_name + " " + l_name).title()
    return f"{result}"


formated_string = format_name("carol", "andrade")
print(formated_string)


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year):
        return 29

    return month_days[month-1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


--------------------------------

end = False


def sum(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


while not end:
    n1 = float(input("What's the first number? \n"))
    operator = input("Pick an operator + - * /: \n")
    n2 = float(input("What's the seconde number? \n"))
    final_result = 0

    if operator == "+":
        final_result = sum(n1, n2)
    elif operator == "-":
        final_result = subtract(n1, n2)
    elif operator == "*":
        final_result = multiply(n1, n2)
    elif operator == "/":
        final_result = divide(n1, n2)

    print(f"{final_result}")

    finish = input("Type 'y' to continue or 'n' to finish: ")
    if finish == "n":
        end = True

    """

from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
