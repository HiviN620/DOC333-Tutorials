customers = []
orders = []
sales = []

while True:
    print("\n1) Register Customer\n2) Place Order\n3) View Sales\n4) Show Customer\n5) Show Order\n6) Exit")
    choice = input("Choice: ")
    
    if choice == "1":
        cid = input("Customer ID: ")
        name = input("Name: ")[:20]
        dob = input("Birth Date: ")
        phone = input("Phone: ")[:10]
        address = input("Address: ")
        if any(c[0] == cid for c in customers):
            print("Customer ID already exists!\n")
        else:
            customers.append((cid, name, dob, phone, address))
            print("Customer Registered!\n")
    
    elif choice == "2":
        cid = input("Customer ID: ")
        found = False
        for c in customers:
            if c[0] == cid:
                found = True
                break
        if found:
            oid = input("Order ID: ")
            if any(o[0] == oid for o in orders):
                print("Order ID already exists!\n")
            else:
                bid = input("Branch Code: ")
                date = input("Date: ")
                total = 0
                items = []
                
                for i in range(3):
                    name = input("Item Name: ")
                    qty = int(input("Quantity: "))
                    price = float(input("Unit Price: "))
                    total += qty * price
                    items.append((name, qty, price))
                    more = input("More items? (Yes/No): ").lower()
                    if more != "yes":
                        break
                
                orders.append((oid, cid, bid, date, items, total))
                sales.append((bid, date, total))
                print("Order Placed!\n")
        else:
            print("Customer not found!\n")
    
    elif choice == "3":
        bid = input("Branch Code: ")
        date = input("Date: ")
        total_sales = 0
        for s in sales:
            if s[0] == bid and s[1] == date:
                total_sales += float(s[2])
        print("Sales:", total_sales, "\n")
    
    elif choice == "4":
        cid = input("Customer ID: ")
        found = False
        for c in customers:
            if c[0] == cid:
                print("Customer Details:", c)
                found = True
                break
        if not found:
            print("Customer not found!\n")
    
    elif choice == "5":
        oid = input("Order ID: ")
        found = False
        for o in orders:
            if o[0] == oid:
                print("Order Details:", o)
                found = True
                break
        if not found:
            print("Order not found!\n")
    
    elif choice == "6":
        break
    
    else:
        print("Invalid choice!\n")
        