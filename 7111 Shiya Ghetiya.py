import matplotlib.pyplot as plt

inventory = []

# ---------------- DISPLAY ----------------
def display_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\nID\tName\tQty\tPrice")
        for item in inventory:
            print(f"{item['id']}\t{item['name']}\t{item['qty']}\t{item['price']}")

# ---------------- ADD ----------------
def add_item():
    pid = int(input("Enter ID: "))
    for item in inventory:
        if item["id"] == pid:
            print("ID already exists.")
            return

    item = {
        "id": pid,
        "name": input("Enter Name: "),
        "qty": int(input("Enter Quantity: ")),
        "price": float(input("Enter Price: "))
    }
    inventory.append(item)
    print("Item added.")

# ---------------- INSERT ----------------
def insert_item():
    pid = int(input("Enter ID: "))

    for item in inventory:
        if item["id"] == pid:
            print("Item already exists. Cannot insert.")
            return

    item = {
        "id": pid,
        "name": input("Enter Name: "),
        "qty": int(input("Enter Quantity: ")),
        "price": float(input("Enter Price: "))
    }

    inventory.append(item)
    print("Item inserted.")

# ---------------- DELETE ----------------
def delete_item():
    pid = int(input("Enter ID to delete: "))
    for item in inventory:
        if item["id"] == pid:
            inventory.remove(item)
            print("Item deleted.")
            return
    print("Item not found.")

# ---------------- UPDATE ----------------
def update_item():
    pid = int(input("Enter ID to update: "))
    for item in inventory:
        if item["id"] == pid:
            item["name"] = input("Enter new name: ")
            item["qty"] = int(input("Enter new quantity: "))
            item["price"] = float(input("Enter new price: "))
            print("Item updated.")
            return
    print("Item not found.")

# ---------------- BAR CHART ----------------
def bar_chart():
    if not inventory:
        print("No data available.")
        return

    names = [item["name"] for item in inventory]
    qtys = [item["qty"] for item in inventory]

    plt.figure()
    plt.bar(names, qtys)
    plt.xlabel("Products")
    plt.ylabel("Quantity")
    plt.title("Bar Chart - Quantity Comparison")
    plt.show()

# ---------------- PIE CHART ----------------
def pie_chart():
    if not inventory:
        print("No data available.")
        return

    names = [item["name"] for item in inventory]
    values = [item["qty"] * item["price"] for item in inventory]

    plt.figure()
    plt.pie(values, labels=names, autopct='%1.1f%%')
    plt.title("Pie Chart - Value Distribution")
    plt.show()

# ---------------- MENU ----------------
while True:
    print("\n--- Inventory Management ---")
    print("1. Add Item")
    print("2. Insert Item")
    print("3. Delete Item")
    print("4. Update Item")
    print("5. Display Inventory")
    print("6. Bar Chart")
    print("7. Pie Chart")
    print("8. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_item()
    elif choice == 2:
        insert_item()
    elif choice == 3:
        delete_item()
    elif choice == 4:
        update_item()
    elif choice == 5:
        display_inventory()
    elif choice == 6:
        bar_chart()
    elif choice == 7:
        pie_chart()
    elif choice == 8:
        print("Exiting...")
        break
    else:
        print("Invalid choice.")
