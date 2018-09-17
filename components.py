# CLASSES AND METHODS
class Store():
    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        self.name = name
        self.products = []

    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        self.products.append(product)

    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        print("- %s" %self.name)
        for i in self.products:
            print(i)


class Product():
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        
        return ("      Name: %s \n      Description: %s \n      Price: %.3f KD\n"%(self.name, self.description, self.price))


class Cart():
    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        self.products = []

    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        self.products.append(product)

    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        total = 0.0
        for i in self.products:
            total = total + i.price
        return total


    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        print("\nReceipt:")
        for i in self.products:
            print("- %s (KD %.3f)" %(i.name, i.price))
        print("Total price: %.3f KD" %self.get_total_price())

    def checkout(self):
        """
        Does the checkout.
        """
        if self.get_total_price() == 0:
            print("\nYour cart is empty... :(")
            return
        self.print_receipt()
        while(True):
            opt = input("Confirm order? (y/n)\n> ")
            if opt == 'y' or opt == 'Y':
                print("Your order has been placed")
                break
            elif opt == 'n' or opt == 'N':
                print("Your order has been Cancelled")
                break
            else:
                print("Invalid option... Type \"y\" to confirm or \"n\" to cancel")


