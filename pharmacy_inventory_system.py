# Smart Pharmacy Inventory & Sales Management System
# This program processes medicine sales, updates stock, and calculates revenue.

def get_integer(prompt, minimum=0):
    """Get a valid whole number from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value < minimum:
                print(f"Please enter a whole number of at least {minimum}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_price(prompt):
    """Get a valid non-negative medicine price."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Price cannot be negative.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid price.")


print("\n=== SMART PHARMACY INVENTORY & SALES MANAGEMENT ===")

medicine_count = get_integer("How many different medicines do you want to process? ", 1)

total_revenue = 0.0       # Accumulator for successful sales.
restock_count = 0         # Counter for medicines with stock below 10.
processed_count = 0       # Counter for medicines entered and processed.

for medicine_number in range(1, medicine_count + 1):
    print(f"\n--- Medicine {medicine_number} ---")

    while True:
        medicine_name = input("Enter medicine name: ").strip()
        if medicine_name:
            break
        print("Medicine name cannot be empty.")

    available_stock = get_integer("Enter available stock: ")
    price_per_unit = get_price("Enter price per unit (Rs.): ")
    quantity_sold = get_integer("Enter quantity sold: ")

    processed_count += 1

    # Complete the sale only when the requested quantity is in stock.
    if quantity_sold <= available_stock:
        sale_amount = price_per_unit * quantity_sold
        remaining_stock = available_stock - quantity_sold
        total_revenue += sale_amount

        print(f"\nMedicine: {medicine_name}")
        print(f"Total Sales: Rs. {sale_amount:,.2f}")
        print(f"Remaining Stock: {remaining_stock}")

        if remaining_stock < 10:
            print("WARNING: Low stock! Restocking required.")
            restock_count += 1
    else:
        # An unsuccessful sale does not add to revenue or reduce stock.
        remaining_stock = available_stock
        print(f"\nMedicine: {medicine_name}")
        print("Sale could not be completed: requested quantity is not available.")
        print(f"Available Stock: {available_stock}")
        print(f"Remaining Stock: {remaining_stock}")

        if remaining_stock < 10:
            print("WARNING: Low stock! Restocking required.")
            restock_count += 1

# Display the final pharmacy report.
print("\n========== FINAL PHARMACY REPORT ==========")
print(f"Total Medicines Processed: {processed_count}")
print(f"Total Pharmacy Revenue: Rs. {total_revenue:,.2f}")
print(f"Medicines Requiring Restocking: {restock_count}")
print("============================================")
