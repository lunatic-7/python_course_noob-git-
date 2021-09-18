def make_pizza(size, *toppings): # Here if the function needs to take the size of pizza, Then that parameter must come befor parameter *toppings
    """Summarize our Pizza"""
    print(f"\nMaking a pizza of {size}-inch and following topping: ")
    for topping in toppings:
        print(f"- {topping}")

# I have created this function to import it anytime...