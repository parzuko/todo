todo_list = []

while True:
    answer = input("Do you want to add an item? (y/n): ")
    if answer == "N" or answer == "n":
        print("Your todo list is: ", todo_list)
        break
    elif answer == "Y" or answer == "y":
        item = input("Item > ")
        todo_list.append(item)
        print("Your todo list is: ", todo_list)
    else:
        print("Invalid input")
    