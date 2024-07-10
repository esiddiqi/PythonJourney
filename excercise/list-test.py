
# Create a List
# Add item to shopping List using add function
# Add Remove item to shopping list using remove function
# Add item




cart = []

def add():

    user_input = input("Enter Items to be added to the list (Separeted by space): ")
    items = user_input.split()
    for item in items:
        cart.append(item)
    print(f"added items are {cart}")


def remove():
    print(f"Currently the items in the lists are..{cart}")
    user_input =  input("Enter which items to be remove from the cart (Separated by space): ")
    items = user_input.split()
    for item in items:
        if item in cart:
            cart.remove(item)
            print(f"Remaining items are : {cart}")


while True:
    user_choice = input("Enter Add, Remove, Show, or Exit: ")


    if user_choice == "add":
        add()
    elif user_choice == "remove":
        remove()
    elif user_choice == "show":
        print(f"Items in the cart are: {cart}")

    elif user_choice == "exit":
        break
    else:
        print("Enter Valid choice Please :)")

















