todo_list = []

while True:
    print("Your current list is", todo_list)
    answer = input("Do you want to add an item? (y/n): ")
    if answer == "Y" or answer == "y":
        item = input("Item > ")
        todo_list.append(item)
    elif answer == "N" or answer == "n":
        print("Your todo list: ", todo_list)
        print("Good luck completing it!")
        break
    else:
        print("Invalid input")
    