import datetime

# Database dictionaries
customers = {}
orders = {}
sales = {"B001": {}, "B002": {}, "B003": {}, "B004": {}}

# Register a new customer
def register_customer():
    customer_id = input("Enter Customer ID (Cxxx): ")
    name = input("Enter Customer Name (Max 20 chars): ")[:20]
    birth_date = input("Enter Birth Date (YYYY-MM-DD): ")
    phone = input("Enter Telephone Number (10 digits): ")[:10]
    address = input("Enter Address: ")
    
    customers[customer_id] = {
        "name": name,
        "birth_date": birth_date,
        "phone": phone,
        "address": address
    }
    print("Customer registered successfully!\n")

# Place a customer order
def place_order():
    customer_id = input("Enter Customer ID: ")
    if customer_id not in customers:
        print("Customer not found!\n")
        return
    
    order_id = input("Enter Order ID (ODxx): ")
    branch_code = input("Enter Branch Code (Bxxx): ")
    date = input("Enter Date (YYYY-MM-DD): ")
    total_amount = 0
    order_items = []
    
    for _ in range(3):
        item_name = input("Enter Item Name: ")
        quantity = int(input("Enter Quantity: "))
        unit_price = float(input("Enter Unit Price: "))
        total = quantity * unit_price
        total_amount += total
        order_items.append({"item": item_name, "quantity": quantity, "unit_price": unit_price, "total": total})
        
        more_items = input("Do you want to add more items (Yes/No)? ").strip().lower()
        if more_items != "yes":
            break
    
    orders[order_id] = {
        "customer_id": customer_id,
        "branch_code": branch_code,
        "date": date,
        "items": order_items,
        "total_amount": total_amount
    }
    
    sales[branch_code][date] = sales[branch_code].get(date, 0) + total_amount
    print("Order placed successfully!\n")

# View daily sales amount
def view_daily_sales():
    branch_code = input("Enter Branch Code: ")
    date = input("Enter Date (YYYY-MM-DD): ")
    sales_amount = sales.get(branch_code, {}).get(date, 0)
    print(f"Daily Sales Amount: {sales_amount}\n")

# Display customer details
def display_customer():
    customer_id = input("Enter Customer ID: ")
    if customer_id in customers:
        print(customers[customer_id])
    else:
        print("Customer not found!\n")

# Display order details
def display_order():
    order_id = input("Enter Order ID: ")
    if order_id in orders:
        print(orders[order_id])
    else:
        print("Order not found!\n")

# Main menu
def main_menu():
    while True:
        print("\nABC Supermarket\nMain Menu")
        print("1) Register a new customer")
        print("2) Place a customer order")
        print("3) View daily sales amount of a given branch")
        print("4) Display customer details")
        print("5) Display order details")
        print("6) Exit")
        choice = input("Your Choice: ")
        
        if choice == "1":
            register_customer()
        elif choice == "2":
            place_order()
        elif choice == "3":
            view_daily_sales()
        elif choice == "4":
            display_customer()
        elif choice == "5":
            display_order()
        elif choice == "6":
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main_menu()
