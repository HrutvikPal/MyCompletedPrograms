print("Calculator")


def calculator():
    print("The following are the operations available:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    while True:
        try:
            operation = (input("Enter the operation number as mentioned above for the operation:"))
            operation = int(operation)
            break
        except ValueError:
            print("Error 19a2 - You have entered a unrecognizable value. Please enter only a option number.")
    while operation >= 5:
        while True:
            try:
                print("Error 19a2 - You have entered a unrecognizable value. Please enter only a option number.")
                operation = (input("Enter the operation number as mentioned above for the operation:"))
                operation = int(operation)
                break
            except ValueError:
                print("Error 19a2 - You have entered a unrecognizable value. Please enter only a option number.")
    if operation == 1:
        print("You have chosen addition.")
        while True:
            try:
                num1 = (input("Enter first number:"))
                num1 = float(num1)
                break
            except ValueError:
                print("Error 19c - You have entered a unrecognizable value. Please enter only an float value.")
        while True:
            try:
                num2 = (input("Enter second number:"))
                num2 = float(num2)
                break
            except ValueError:
                print("Error 19c - You have entered a unrecognizable value. Please enter only an float value.")
        sum = num1 + num2
        print("The sum is", sum)
    elif operation == 2:
        print("You have chosen subtraction.")
        print("In format number1 - number2.")
        while True:
            try:
                num1 = (input("Enter first number:"))
                num1 = float(num1)
                break
            except ValueError:
                print("Error 19c - You have entered a unrecognizable value. Please enter only an float value.")
        while True:
            try:
                num2 = (input("Enter second number:"))
                num2 = float(num2)
                break
            except ValueError:
                print("Error 19c - You have entered a unrecognizable value. Please enter only an float value.")
        difference = num1 - num2
        print("The difference is", difference)
    elif operation == 3:
        print("You have chosen multiplication.")
        while True:
            try:
                num1 = (input("Enter first number:"))
                num1 = float(num1)
                break
            except ValueError:
                print("Error 19c - You have entered a unrecognizable value. Please enter only an float value.")
        while True:
            try:
                num2 = (input("Enter second number:"))
                num2 = float(num2)
                break
            except ValueError:
                print("Error 19c - You have entered a unrecognizable value. Please enter only an float value.")
        product = num1 * num2
        print("The product is", product)
    elif operation == 4:
        print("You have chosen division.")
        print("In format number1/number2.")
        while True:
            try:
                num1 = (input("Enter first number:"))
                num1 = float(num1)
                break
            except ValueError:
                print("Error 19c - You have entered a unrecognizable value. Please enter only an float value.")
        while True:
            try:
                num2 = (input("Enter second number:"))
                num2 = float(num2)
                break
            except ValueError:
                print("Error 19c - You have entered a unrecognizable value. Please enter only an float value.")
        while num2 == 0:
            while True:
                try:
                    print("Error 19e - You have entered a zero for the divisor. Please enter the divisor again.")
                    num2 = (input("Enter second number:"))
                    num2 = float(num2)
                    break
                except ValueError:
                    print("Error 19c - You have entered a unrecognizable value. Please enter only an float value.")
        quotient_value = num1 / num2
        quotient = round(quotient_value, 3)
        print("The quotient, rounded to three decimal places, is", quotient)


calculator()
while True:
    try:
        rerun = (str(input("Do you want to rerun this calculator?(yes/no):")))
        while rerun in ("yes","Yes"):
            calculator()
            rerun = (str(input("Do you want to rerun this calculator?(yes/no):")))
        if rerun in ("no","No"):
            print("Thank you for using this calculator.")
            break
        else:
            print("Error 9a - Invalid input. Please enter only yes or no.")
    except Exception:
        print("Error 1 - Unknown exception. A problem has occurred.")
