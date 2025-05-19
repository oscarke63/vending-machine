products = {
    'A1': {'name': 'Soda', 'price': 20.0},
    'A2': {'name': 'Chips', 'price': 30.0},
    'A3': {'name': 'Candy Bar', 'price': 40.0},
    'A4': {'name': 'Water', 'price': 50.0},
    'A5': {'name': 'Juice', 'price': 60.0},

}

def display_menu():
    print("Available Items:")
    for code, product in products.items():
        print(f"{code}: {product['name']} - ${product['price']:.2f}")
def select_item():
    item_code = input("Enter Item Code: ")
    if item_code in products:
        item = products[item_code]
        print(f"You selected: {item['name']} - ${item['price']:.2f}")
        return item_code, item
    else:
        print("Invalid item code. Please try again.")
        return None, None
def process_payment(item):
    if item is None:
        return 0, 0

    price = item['price']
    while True:
        try:
            money_inserted = float(input(f"Enter payment amount (Total: ${price:.2f}): $"))
            if money_inserted < price:
                print(f"Insufficient funds. You still need ${price - money_inserted:.2f}. Please try again.")
            else:
                change = money_inserted - price
                print(f"Payment accepted. Change to return: ${change:.2f}")
                return money_inserted, change
        except ValueError:
            print("Invalid input. Please enter a valid amount of money.")
def validate_input():
    while True:
        item_code, item = select_item()
        if item_code:
            payment_received, change = process_payment(item)
            if payment_received > 0:
                return item_code, item, payment_received, change
        else:
            choice = input("Do you want to try again? (y/n): ").strip().lower()
            if choice == 'n':
                print("Exiting. Thank you for using the vending machine!")
                break
def main():
    while True:
        display_menu()
        item_code, item, payment_received, change = validate_input()

        if item_code:
            print(f"Thank you for purchasing {item['name']}!")
            print(f"Your change is: ${change:.2f}")
        continue_transaction = input("Would you like to make another purchase? (y/n): ").strip().lower()
        if continue_transaction == 'n':
            print("Thank you for using the Smart Vending Machine. Goodbye!")
            break
display_menu()