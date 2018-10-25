from menu_manager import MenuManager


def load_manager():
    manager = MenuManager()
    return manager


def show_user_menu():
    menu = """\
    MENU
(a) Add an item
(d) Delete an item
(v) View the menu
(x) Exit
 :  """
    choice = input(menu)
    if choice == 'a':
        add_item_to_menu()
    elif choice == 'd':
        remove_item_from_menu()
    elif choice == 'v':
        show_restaurant_menu()
    elif choice == 'x':
        save_menu_to_file()
    else:
        print("Invalid option")


def show_restaurant_menu():
    menu_str = "\tMENU\n"
    for item in manager.menu['items']:
        menu_str += f"{item['name'] + ':':20} {item['price']}\n"
    print(menu_str)


def add_item_to_menu():
    name = input("Enter the name of the item: ")
    price = input("Enter the price of the item: ")
    manager.add_item(name, price)
    # Make sure to save to file
    save_menu_to_file()


def remove_item_from_menu():
    name = input("Enter the name of the item: ")
    removed = manager.remove_item(name.strip())
    if removed:
        print(f"{name} was removed from the menu.")
        # Make sure to save to file
        save_menu_to_file()
    else:
        print(f"{name} could not be removed from the menu.")


# DRY - Don't Repeat Yourself!
# Instead of saving the menu and then printing a message to the user each
# time, I put these statements in a function so that it can be re-used.
def save_menu_to_file():
    manager.save_to_file()
    print("Menu saved successfully")

# Note: in this case, the exercise does not require a menu to be
# shown repetitively (again and again). It is simply shown once.

# 'manager' will be referred to in the functions above.
manager = load_manager()
show_user_menu()
