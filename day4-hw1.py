from operator import mul  # Lesson 5: Assignments | Python Functions

# 1. The Calculator App

# Task 1
#*args
def addition(*numbers):
    return print(sum(numbers))

def substraction(*numbers):

    return print(numbers[0] - numbers[1])

def multiplication(*numbers):
    return print(numbers[0] * numbers[1])

def division(*numbers):
    return print(numbers[0] / numbers[1])



intro_msg = "This is a basic calculator with which you can perform addition, substraction, multiplication and division using two numbers. If you wish to quit just type 'quit'"
print(intro_msg)


while True:
    operation = input("Which operation would you like to use?\n")
    if operation.lower() in ["add", "addation"]:
        first = int(input("Enter your first number:\n"))
        second = int(input("Enter your second number:\n"))
        addition(first, second)
        # break
    elif operation.lower()  in ["substraction", "substract"]:
        first = int(input("Enter your first number:\n"))
        second = int(input("Enter your second number:\n"))
        substraction(first, second)
        # break
    elif operation.lower() in ["multiplication", "multiply"]:
        first = int(input("Enter your first number:\n"))
        second = int(input("Enter your second number:\n"))
        multiplication(first, second)
        # break
    elif operation.lower() in ["division", "divide"]:
        first = int(input("Enter your first number:\n"))
        second = int(input("Enter your second number:\n"))
        division(first, second)
        # break
    elif operation.lower() == "quit":
        break
    else:
        input("You've entered an invalid input. Press 'enter' to try again.\n ")
# 2. The Shopping List Maker

list = []

def add_items(item):
    return list.append(item)
def remove_items(item):
    return list.remove(item) 
def entire_list(list):
    return print(list)


while True:
    start = input("Do you want to add or remove an item to your list? If you don't want to do anything enter 'quit'.\n")
    if start.lower() == "add":
        item_to_add = input("What item do you want to add?\n")
        add_items(item_to_add)
        print(f"You've succesfully added {item_to_add} to the list. Here's how it looks now:\n{list}")

    elif start.lower() == "remove":
        item_to_remove = input(f"Which item do you want to remove?\n{list}\n")
        list.remove(item_to_remove.lower())
        print(f"You've succesfully removed {item_to_remove} to the list. Here's how it looks now:\n{list}")

    elif start.lower() == "quit":
        print(f"Here's your list:\n{list}")
        break
    else:
        input("You've entered an invalid input. Press 'enter' to try again\n ")