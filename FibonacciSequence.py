print("Fibonacci Sequence Printer")
print("This program prints the Fibonacci Sequence based on your input.")
def fibseq():
    print("You can print the Fibonacci Sequence by either:")
    print("1.Entering the number of sequence numbers you want")
    print("2.Entering the upper limit for the Fibonacci Sequence")
    while True:
        try:
            fibseqtype = (int(input("Enter the print method number as mentioned above for it:")))
            fibseqtype = int(fibseqtype)
            break
        except ValueError:
            print("Error 19a2 - You have entered a unrecognizable value. Please enter only a option number.")
    if fibseqtype == 1:
        while True:
            try:
                number = (input("Enter the number of Fibonacci Sequence numbers you want:"))
                number = int(number)
                break
            except ValueError:
                print("Error 19a1 - You have entered a unrecognizable value. Please enter only an integer.")
        while number <= 0:
            print("Error 18a - You cannot enter a negative number or zero for this input. Please try again.")
            while True:
                try:
                    number = (input("Enter the number of Fibonacci Sequence numbers you want:"))
                    number = int(number)
                    break
                except ValueError:
                    print("Error 19a1 - You have entered a unrecognizable value. Please enter only an integer.")
        if number == 1:
            print("Your requested sequence of 1 number is:")
            print(0)
        if number >= 2:
            print("Your requested sequence of",number,"numbers is:")
            a = 0
            print(a)
            b = 1
            print(b)
            number = number + 1
            for i in range(3,number):
                c = a + b
                a = b
                b = c
                print(c)
    elif fibseqtype == 2:
        while True:
            try:
                number = (input("Enter the upper limit for the Fibonacci sequence:"))
                number = int(number)
                break
            except ValueError:
                print("Error 19a1 - You have entered a unrecognizable value. Please enter only an integer.")
        while number < 0:
            print("Error 18a - You cannot enter a negative number or zero for this input. Please try again.")
            while True:
                try:
                    number = (input("Enter the upper limit for the Fibonacci sequence:"))
                    number = int(number)
                    break
                except ValueError:
                    print("Error 19a1 - You have entered a unrecognizable value. Please enter only an integer.")
        if number == 0:
            print("Your requested sequence is:")
            print(0)
        if number == 1:
            print("Your requested sequence is:")
            print(0)
            print(1)
        if number >= 2:
            print("Your requested sequence is:")
            a = 0
            print(a)
            b = 1
            print(b)
            number = number + 1
            for i in range(3,number):
                c = a + b
                a = b
                b = c
                if c >= number:
                    break
                print(c)
    else:
        print("Error 21c - The option you have entered is not an operation number.Press 'yes' to rerun the calculator.")
fibseq()
while True:
    try:
        rerun = (str(input("Do you want to rerun this program?(yes/no):")))
        while rerun in ("yes","Yes"):
            fibseq()
            rerun = (str(input("Do you want to rerun this program?(yes/no):")))
        if rerun in ("no","No"):
            print("Thank you for using this program.")
            break
        else:
            print("Error 9a - Invalid input. Please enter only yes or no.")
    except Exception:
        print("Error 1 - Unknown exception. A problem has occurred.")

