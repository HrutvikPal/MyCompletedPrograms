print("Multiple Calculator")
print("This calculator gives a specified number of multiples for a number.")
def multiplecalculator():
    while True:
        try:
            number = (int(input("Enter the number you want multiples of:")))
            number = int(number)
            break
        except ValueError:
            print("Error 19a1 - You have entered a unrecognizable value. Please enter only an integer.")
    while True:
        try:
            mulplenum = (int(input("Enter the number of multiples you want of that number:")))
            mulplenum = int(mulplenum)
            break
        except ValueError:
            print("Error 19a1 - You have entered a unrecognizable value. Please enter only an integer.")
    mulpleoper = (number * mulplenum) + 1
    print("The following are the requested multiples of",number)
    for multiple in range(number,mulpleoper,number):
        print(multiple)
multiplecalculator()
while True:
    try:
        rerun = (str(input("Do you want to rerun this calculator?(yes/no):")))
        while rerun in ("yes","Yes"):
            multiplecalculator()
            rerun = (str(input("Do you want to rerun this calculator?(yes/no):")))
        if rerun in ("no","No"):
            print("Thank you for using this calculator.")
            break
        else:
            print("Error 9a - Invalid input. Please enter only yes or no.")
    except Exception:
        print("Error 1 - Unknown exception. A problem has occurred.")
