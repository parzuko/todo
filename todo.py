todo_list = []

def get_item_input():
    item = input("Item > ")
    todo_list.append(item)

def say_goodbye_to_user():
    print("Your todo list: ", todo_list)
    print("Good luck completing it!")
        

while True:
    print("Your current list is", todo_list)
    answer = input("Do you want to add an item? (y/n): ")
    if answer == "Y" or answer == "y":
        get_item_input()
    elif answer == "N" or answer == "n":
        say_goodbye_to_user()
        break
    else:
        print("Invalid input")


    