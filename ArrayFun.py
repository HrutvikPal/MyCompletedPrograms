print("Array Creator and Reviewer")
print("This program creates integer arrays for you and allows you to review them.")
import array
arr = array.array('i', [])


def createarr():
    while True:
        try:
            length = (int(input("Specify the number of values you want in the array:")))
            length = int(length)
            break
        except ValueError:
            print("Error 19a1 - You have entered a unrecognizable value. Please enter only an integer value.")
    if length == 1:
        while True:
            try:
                value = input("Enter first value:")
                value = int(value)
                arr.append(value)
                print("Value entered.")
                break
            except ValueError:
                print("Error 19c - You have entered a unrecognizable value. Please enter only an integer value.")
    if length != 1:
        while True:
            try:
                value = input("Enter first value:")
                value = int(value)
                arr.append(value)
                print("Value entered.")
                break
            except ValueError:
                print("Error 19c - You have entered a unrecognizable value. Please enter only an integer value.")
        for i in range(2, length + 1):
            while True:
                try:
                    value = input("Enter next value:")
                    value = int(value)
                    arr.append(value)
                    print("Value",i,"entered.")
                    i += 1
                    break
                except ValueError:
                    print("Error 19c - You have entered a unrecognizable value. Please enter only an integer value.")
    print("Your requested array is:")
    print(arr)


def options():
    print("Do you want to either:")
    print("1.Create a new array")
    print("2.Delete existing values or add other values to your array")
    print("3.Type in a value you entered to see its key (review)")
    print("4.Exit program")


createarr()
options()
selecopt = (int(input("Enter the option number as mentioned above to select it:")))
while selecopt >= 5:
    while True:
        try:
            print("Error 19a2 - You have not entered a recognizable value. Please enter only a option number.")
            selecopt = (int(input("Enter the option number as mentioned above to select it:")))
            selecopt = int(selecopt)
            break
        except ValueError:
            print("Error 19a2 - You have not entered a recognizable value. Please enter only a option number.")
while selecopt == 1:
    print("In doing so, you delete the earlier array that you created.")
    arr = array.array('i', [])
    createarr()
    options()
    selecopt = (int(input("Enter the option number as mentioned above to select it:")))
while selecopt == 2:
    while True:
        try:
            adsub = (str(input("Press 'a' to add a value and 'r' to remove one:")))
            if adsub in ("a","A"):
                while True:
                    try:
                        adnum = (int(input("Specify the number of values you want to add in the array:")))
                        adnum = int(adnum)
                        break
                    except ValueError:
                        print("Error 19a1 - You have entered a unrecognizable value. Please enter only an integer value.")
                if adnum == 1:
                    while True:
                        try:
                            value = input("Enter the value:")
                            value = int(value)
                            arr.append(value)
                            print("The value has been added.")
                            break
                        except ValueError:
                            print("Error 19c - You have entered a unrecognizable value. Please enter only an integer value.")
                elif adnum != 1:
                    while True:
                        try:
                            value = input("Enter the first value to add:")
                            value = int(value)
                            arr.append(value)
                            break
                        except ValueError:
                            print("Error 19c - You have entered a unrecognizable value. Please enter only an integer value.")
                    valuenum = len(arr) + 1
                    print("Value", valuenum, "added.")
                    for i in range(2, adnum + 1):
                        while True:
                            try:
                                value = input("Enter next value to add:")
                                value = int(value)
                                arr.append(value)
                                break
                            except ValueError:
                                print(
                                    "Error 19c - You have entered a unrecognizable value. Please enter only an integer value.")
                        valuenum = len(arr) + 1
                        print("Value", valuenum, "added.")
                        i += 1
                print("Your new array is:")
                print(arr)
                options()
                selecopt = (int(input("Enter the option number as mentioned above to select it:")))
            elif adsub in ("r","R"):
                remnum = (int(input("Enter the number of values you want to remove:")))
                print("You must enter the value you want to delete.")
                if remnum == 1:
                    value = (int(input("Enter value to remove:")))
                    while True:
                        try:
                            arr.remove(value)
                            print("Value removed.")
                            break
                        except ValueError:
                            print("Error 15a - The value you have entered is not in the array.")
                            value = (int(input("Enter value to remove:")))
                elif remnum != 1:
                    remval = remnum + 1
                    value = (int(input("Enter value to remove:")))
                    while True:
                        try:
                            arr.remove(value)
                            print("Value removed.")
                            break
                        except ValueError:
                            print("Error 15a - The value you have entered is not in the array.")
                            value = (int(input("Enter value to remove:")))
                    for i in range(2, remval):
                        value = (int(input("Enter next value to remove:")))
                        while True:
                            try:
                                arr.remove(value)
                                print("Value removed.")
                                i += 1
                                break
                            except ValueError:
                                print("Error 15a - The value you have entered is not in the array.")
                                value = (int(input("Enter value to remove:")))
                print("Your new array is:")
                print(arr)
                options()
                selecopt = (int(input("Enter the option number as mentioned above to select it:")))
            else:
                print("Error 9a - Invalid input. Please enter only 'a' or 'r'.")
        except Exception:
            print("Error 1 - Unknown exception. A problem has occurred.")
while selecopt == 3:
    print("To know the key of the value, you must first enter the value.")
    while True:
        try:
            value = (input("Enter the value:"))
            value = int(value)
            break
        except ValueError:
            print("Error 19c - You have entered a unrecognizable value. Please enter only an integer value.")
    key = 0
    valnum = 1
    for val in arr:
        while True:
            try:
                if val == value:
                    # Can also use key = arr.index(value) for key, instead of increment.
                    print(key, "is the key of the value you entered. However, it is value", valnum, "in the array.")
                    key += 1
                    valnum += 1
                break
            except Exception:
                print("Error 20a - The value you entered is not a array value.")
                print("Here is the array you created:")
                print(arr)
    options()
    selecopt = (int(input("Enter the option number as mentioned above to select it:")))
if selecopt == 4:
    print("Thank you for using this program.")
