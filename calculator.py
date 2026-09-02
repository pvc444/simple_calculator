def calculator(num1, num2, operators):
    if operators == "+":
        return num1 + num2

    elif operators == "-":
        return num1 - num2

    elif operators == "*":
        return num1 * num2

    elif operators == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "cant be divided by zero"

while True:

# گرفتن عدد اول
    while True:
        try:
            num1 = float(input("enter the first number:"))
            break
        except ValueError:
            print("thats not a number! please enter a number")

# گرفتن عدد دوم
    while True:
        try:
            num2 = float(input("enter the second number:"))
            break
        except ValueError:
            print("thats not a number! please enter a number")

# گرفتن عملگر
    while True:
        operators = input("enter one of the followings: +, -, /, *.")

        if operators == "+" or operators == "-" or operators == "*" or operators == "/":
            result = calculator(num1, num2, operators)
            print(result)
            break

        else:
            print("operators not available")

# دوباره اجرا کردن
    again = input("do you want to calculate again? (y/n): ").lower()

    while again != "y" and again != "n":
        print("please enter y or n!")
        again = input("do you want to calculate again? (y/n): ").lower()

    if again == "n":
        print("Goodbye")
        break
