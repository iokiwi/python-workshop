def greet(name):
    pass


def greet_v2(name, greeting="Hello"):
    """ Greets one or people by name
        :names: One or more names
    """
    pass


def greet_v3(*names, greeting="Hello"):
    """ Greets one or people by name
        :names: One or more names
    """
    pass


def add_to_cart(item, cart=[]):
    """ Adds an item to the shopping cart
        :param item: The name of an item to add to our cart as a string
        :param cart: An optional cart
        :returns: A list of items in our cart
    """
    pass


def main():
    # Example 1
    print("-- Example 1 --")
    greet("Alice")

    # Example 2
    print("-- Example 2 --")
    greet_v2("Alice")
    greet_v2("Alice", greeting="Guten Tag")

    # Example 3
    print("-- Example3 --")
    greet_v3("Alice", "Bob")

    # Alternatively we can call
    args = ("Eve", "Dave")
    greet_v3(*args)

    # Example 4
    print("-- Example 4 --")
    cart_1 = add_to_cart("Apples")
    cart_1 = add_to_cart("Bananas", cart_1)
    print(f"Cart 1 contains: {cart_1}")

    cart_2 = add_to_cart("Grapes")
    print(f"Cart 2 contains: {cart_2}")

    # Example 4
    print("Example 4")


if __name__ == "__main__":
    main()
