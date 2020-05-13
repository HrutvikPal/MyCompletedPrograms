print("Une Division Queer")
print("The title means 'a queer division' in French.")
print("The dividend is the number that is to be divided.")
print("The divisor is the number that the dividend is being divided with.")


def program():
    def queer_division(dividend,divisor):
        if dividend % divisor == 0:
            quotient = dividend/divisor
            quotient = int(quotient)
            print("The result is",quotient,",with no remainder.")
        else:
            pure_quotient = dividend/divisor
            remainder = dividend % divisor
            reformed_dividend = dividend - remainder
            reformed_quotient = reformed_dividend/divisor
            reformed_quotient = int(reformed_quotient)
            print("The quotient is",reformed_quotient,",with a remainder of",remainder,".")
            print("The exact division with decimals is",pure_quotient,".")

    while True:
        try:
            num1 = (input("Enter the dividend:"))
            num1 = float(num1)
            break
        except ValueError:
            print("Error 19c - You have entered a unrecognizable value. Please enter only float input.")
    while True:
        try:
            num2 = (input("Enter the divisor:"))
            num2 = float(num2)
            break
        except ValueError:
            print("Error 19c - You have entered a unrecognizable value. Please enter only float input.")
    queer_division(num1,num2)


program()
while True:
    try:
        rerun = (str(input("Do you want to rerun the divider?(yes/no):")))
        while rerun in ("yes","Yes"):
            program()
            rerun = (str(input("Do you want to rerun the divider?(yes/no):")))
        if rerun in ("no","No"):
            print("Thank you for using the divider.")
            break
        else:
            print("Error 9a - Invalid input. Please enter only yes or no.")
    except Exception:
        print("Error 1 - Unknown exception. A problem has occurred.")
