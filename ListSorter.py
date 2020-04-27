from time import sleep
print("List Sorter")
print("This program sorts the list you enter either in ascending or descending order.")
def_list = []


def unsorted_list():
    print("Follow the instructions for sorting the list.")
    sleep(1)
    print("1.Enter the number of elements, or values that your list has.")
    while True:
        try:
            length = (int(input("Number of elements in list:")))
            length = int(length)
            break
        except ValueError:
            print("Error 19a1 - You have entered a unrecognizable value. Please enter only an integer value.")
    print("Processing...")
    sleep(2)
    while length == 1 or length == 0:
        while True:
            try:
                print("Error 10a - An list with one or no elements is unsortable. Please try again.")
                length = (int(input("Number of elements in list:")))
                length = int(length)
                print("Processing...")
                sleep(2)
                break
            except ValueError:
                print("Error 19a1 - You have entered a unrecognizable value. Please enter only an integer value.")
    if length != 1:
        print("2.Next, enter the values in the list one by one.")
        while True:
            try:
                value = input("Enter first value:")
                value = float(value)
                def_list.append(value)
                print("Value 1 entered.")
                break
            except ValueError:
                print(
                    "Error 19c - You have entered a unrecognizable value. Please enter only an integer or float value.")
        for i in range(2, length + 1):
            while True:
                try:
                    value = input("Enter next value:")
                    value = float(value)
                    def_list.append(value)
                    print("Value", i, "entered.")
                    break
                except ValueError:
                    print(
                        "Error 19c - You have entered a unrecognizable value. Please enter only an integer or float value.")
            i += 1
    print("The list you want to sort is:")
    globals()['def_list'] = def_list
    print(*def_list, sep=", ")


def sorter():
    print("3.Now that you entered the list, choose the way you want to sort them by.")
    while True:
        try:
            sort_type = (input("Press 'a' if you want to sort it in ascending order or 'd' if you want to sort it in descending order:"))
            if sort_type in ("a","A"):
                def selection_sort(list):
                    for i in range(len(list)):
                        min_position = i
                        for j in range(i + 1, len(list)):
                            if list[j] < list[min_position]:
                                min_position = j
                        list[i], list[min_position] = list[min_position], list[i]
                    print("The sorted list:")
                    print(list)
                print("Sorting list...")
                sleep(2)
                selection_sort(def_list)
            elif sort_type in ("d","D"):
                def selection_sort(list):
                    for i in range(len(list)):
                        min_position = i
                        for j in range(i + 1, len(list)):
                            if list[j] > list[min_position]:
                                min_position = j
                        list[i], list[min_position] = list[min_position], list[i]
                    print("The sorted list:")
                    print(list)

                print("Sorting list...")
                sleep(2)
                selection_sort(def_list)
            else:
                print("Error 9b - Invalid input. Please enter only 'a' or 'd'.")
        except Exception:
            print("Error 1 - Unknown exception. A problem has occurred.")


unsorted_list()
sorter()
while True:
    try:
        rerun = (str(input("Do you want to rerun the sorter?(yes/no):")))
        while rerun in ("yes","Yes"):
            unsorted_list()
            sorter()
            rerun = (str(input("Do you want to rerun the sorter?(yes/no):")))
        if rerun in ("no","No"):
            print("Thank you for using the sorter.")
            break
        else:
            print("Error 9a - Invalid input. Please enter only yes or no.")
    except Exception:
        print("Error 1 - Unknown exception. A problem has occurred.")
