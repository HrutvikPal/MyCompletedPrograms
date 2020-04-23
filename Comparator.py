print("Comparator")
print("This program tells you which is the greater of the numbers you enter.")
def comparator():
    while True:
        try:
            num1 = (input("Enter the first number to compare:"))
            num1 = float(num1)
            break
        except ValueError:
            print("Error 19a1 - You have entered a unrecognizable value. Please enter only an integer.")
    while True:
        try:
            num2 = (input("Enter the second number to compare:"))
            num2 = float(num2)
            break
        except ValueError:
            print("Error 19c - You have entered a unrecognizable value. Please enter only an float value.")
    if num1 > num2:
        print(num1,"is the greater number.")
        print(num2,"is the smaller number.")
    elif num1 < num2:
        print(num2,"is the greater number.")
        print(num1,"is the smaller number.")
    else:
        print("The numbers are equal.")
comparator()

while True:
    try:
        rerun = (str(input("Do you want to rerun the comparator?(yes/no):")))
        while rerun in ("yes","Yes"):
            comparator()
            rerun = (str(input("Do you want to rerun the comparator?(yes/no):")))
        if rerun in ("no","No"):
            print("Thank you for using the comparator.")
            break
        else:
            print("Error 9a - Invalid input. Please enter only yes or no.")
    except Exception:
        print("Error 1 - Unknown exception. A problem has occurred.")


