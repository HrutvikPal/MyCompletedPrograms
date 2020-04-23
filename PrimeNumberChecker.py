print("Prime Number Checker")
print("This calculator tells you if the number you entered is a prime or not.")


def checker():
    while True:
        try:
            number = (input("Enter the number:"))
            number = int(number)
            break
        except ValueError:
            print("Error 19a1 - You have entered a unrecognizable value. Please enter only an integer.")
    if number == 2:
        print("2 is a prime number.")
    elif number == 1:
        print("1 is not a prime number or composite number. It is a unique number.")
    else:
        for primenum in range(2,number):
            if number % primenum == 0:
                print(number,"is not a prime number. It is a composite number.")
                break
        else:
            print(number,"is a prime number.")

    
checker()
while True:
    try:
        rerun = (str(input("Do you want to rerun the checker?(yes/no):")))
        while rerun in ("yes","Yes"):
            checker()
            rerun = (str(input("Do you want to rerun the checker?(yes/no):")))
        if rerun in ("no","No"):
            print("Thank you for using the checker.")
            break
        else:
            print("Error 9a - Invalid input. Please enter only yes or no.")
    except Exception:
        print("Error 1 - Unknown exception. A problem has occurred.")
