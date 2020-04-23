print("Factorial Calculator")
print("This program gives you the factorial value of the number you enter.")
def factorialcal(num):
    facval = 1
    numval = num + 1
    for multival in range(1,numval):
        facval = facval * multival
    return facval
def program():
    while True:
        try:
            number = (input("Enter the number to get its factorial:"))
            number = int(number)
            break
        except ValueError:
            print("Error 19a1 - You have entered a unrecognizable value. Please enter only an integer.")
    factorial = factorialcal(number)
    print ("The factorial of",number,"is",factorial)
program()
while True:
    try:
        rerun = (str(input("Do you want to rerun this calculator?(yes/no):")))
        while rerun in ("yes","Yes"):
            program()
            rerun = (str(input("Do you want to rerun this calculator?(yes/no):")))
        if rerun in ("no","No"):
            print("Thank you for using this calculator.")
            break
        else:
            print("Error 9a - Invalid input. Please enter only yes or no.")
    except Exception:
        print("Error 1 - Unknown exception. A problem has occurred.")
