# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "Codazone"  

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    for i in stores:
        print("- %s" %i.name)

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    for i in stores:
        if i.name == store_name:
            return i
    print("Invalid Store Name!")
    return False

def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    print("Type the store name to browse its content or type \"checkout\" to finish shopping.")
    print_stores()
    while(True):
        opt = input("> ")
        if opt == "checkout" or opt == "Checkout":
            return "check"
        for i in stores:
            if opt == i.name:
                return i
        print("Invalid option, try again.")




def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    print("-----------------------\n%s \n" % picked_store.name)
    for i in picked_store.products:
        print(i)
    print("\n Type the name of the product to added it to your cart, type \"exit\" to go back, or type \"checkout\" if you are done shopping.")
    while(True):
        opt = input("> ")
        if opt == "checkout":
            return "check"
        if opt == "exit":
            return "exit"
        for i in picked_store.products:
            if opt == i.name:
                cart.products.append(i)
                break
        else:
            print("Invalid option, try again.")


def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    while(True):
        picked = pick_store()
        if picked == "check":
            cart.checkout()
            return
        opt = pick_products(cart, picked)
        if opt == "check":
            cart.checkout()
            return


def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
