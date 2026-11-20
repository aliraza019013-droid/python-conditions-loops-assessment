"""Smart Pharmacy Inventory & Sales Management System.

Processes several medicines: checks stock, completes sales, updates
remaining stock, warns about low stock and prints a revenue report.
"""

import math

LOW_STOCK_LIMIT = 10  # remaining stock below this triggers a warning


def read_text(prompt):
    """Ask for a non-empty text value."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: This field cannot be empty. Please try again.")


def read_int(prompt, minimum):
    """Ask for a whole number >= minimum."""
    while True:
        text = input(prompt).strip()
        try:
            value = int(text)
        except ValueError:
            print("Error: Please enter a whole number.")
            continue
        if value < minimum:
            print(f"Error: Value must be at least {minimum}.")
        else:
            return value


def read_price(prompt):
    """Ask for a price greater than zero."""
    while True:
        text = input(prompt).strip()
        try:
            value = float(text)
        except ValueError:
            print("Error: Please enter a valid number.")
            continue
        if not math.isfinite(value) or value <= 0:
            print("Error: Price must be greater than 0.")
        else:
            return value


def process_sale(stock, price, quantity):
    """Return (sale_completed, sales_amount, remaining_stock)."""
    if quantity > stock:                       # not enough stock: no sale
        return False, 0.0, stock
    return True, quantity * price, stock - quantity


def is_low_stock(remaining_stock):
    """True when remaining stock is below the low-stock limit."""
    return remaining_stock < LOW_STOCK_LIMIT


def read_medicine(number):
    """Collect the four inputs for one medicine."""
    print(f"\nMedicine {number}:")
    name = read_text("Medicine name: ")
    stock = read_int("Available stock: ", 0)
    price = read_price("Price per unit: ")
    quantity = read_int("Quantity sold: ", 1)
    return name, stock, price, quantity


def main():
    print("=== Smart Pharmacy Inventory & Sales Management System ===")
    try:
        count = read_int("How many different medicines do you want to process? ", 1)

        total_revenue = 0.0        # accumulator
        processed = 0              # counter
        restock_needed = 0         # counter

        for number in range(1, count + 1):
            name, stock, price, quantity = read_medicine(number)
            completed, amount, remaining = process_sale(stock, price, quantity)

            print(f"\nMedicine: {name}")
            if completed:
                print(f"Total Sales: Rs. {amount:.2f}")
            else:
                print(f"Sale rejected: only {stock} units in stock, {quantity} requested.")
                print("Total Sales: Rs. 0.00")
            print(f"Remaining Stock: {remaining}")

            if is_low_stock(remaining):
                print("WARNING: Low stock! Restocking required.")
                restock_needed += 1

            total_revenue += amount
            processed += 1
    except EOFError:
        print("\nError: Input ended before all values were entered.")
        return

    print("\n--- Final Pharmacy Report ---")
    print(f"Total Medicines Processed: {processed}")
    print(f"Total Pharmacy Revenue: Rs. {total_revenue:.2f}")
    print(f"Medicines Requiring Restocking: {restock_needed}")


if __name__ == "__main__":
    main()
