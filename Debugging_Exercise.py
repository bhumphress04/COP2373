def calculate_discount(price, discount_rate):
    # Calculate the discount amount if values are valid numbers
    if isinstance(price, (int, float)) and isinstance(discount_rate, (int, float)):
        return price * discount_rate
    else:
        print(f"Error: Invalid data -> price={price}, discount_rate={discount_rate}")
        return None


def apply_discount(price, discount_amount):
    # Subtract discount from price if discount is valid
    if discount_amount is not None:
        return price - discount_amount
    else:
        return None


def main():
    products = [
        {"name": "Laptop", "price": 1000, "discount_rate": 0.1},
        {"name": "Smartphone", "price": 800, "discount_rate": 0.15},
        {"name": "Tablet", "price": "500", "discount_rate": 0.2},  # Wrong type on purpose
        {"name": "Headphones", "price": 200, "discount_rate": 0.05}
    ]

    for product in products:
        print(f"\nProcessing {product['name']}...")

        price = product["price"]
        discount_rate = product["discount_rate"]

        discount_amount = calculate_discount(price, discount_rate)
        final_price = apply_discount(price, discount_amount)

        if discount_amount is not None and final_price is not None:
            print(f"Original Price: ${price}")
            print(f"Discount Amount: ${discount_amount}")
            print(f"Final Price: ${final_price}")
        else:
            print("⚠️ Could not calculate discount because the data was invalid.")


if __name__ == "__main__":
    main()


