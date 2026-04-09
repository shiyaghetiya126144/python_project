import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Inventory Management System")
root.geometry("1200x720")
root.config(bg="#f4f6f8")
root.resizable(False, False)

inventory = []

# ---------------- FUNCTIONS ----------------
def clear_fields():
    entry_id.delete(0, tk.END)
    entry_category.delete(0, tk.END)
    entry_company.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_qty.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    search_entry.delete(0, tk.END)

def refresh_table(data=None):
    for row in tree.get_children():
        tree.delete(row)

    display_data = data if data is not None else inventory

    for item in display_data:
        tree.insert("", tk.END, values=(
            item["id"],
            item["category"],
            item["company"],
            item["name"],
            item["qty"],
            item["price"]
        ))

def add_item():
    pid = entry_id.get().strip()
    category = entry_category.get().strip()
    company = entry_company.get().strip()
    name = entry_name.get().strip()
    qty = entry_qty.get().strip()
    price = entry_price.get().strip()

    if not pid or not category or not company or not name or not qty or not price:
        messagebox.showerror("Error", "All fields are required!")
        return

    if any(item["id"] == pid for item in inventory):
        messagebox.showerror("Error", "Product ID already exists!")
        return

    try:
        qty = int(qty)
        price = float(price)
    except ValueError:
        messagebox.showerror("Error", "Quantity must be integer and Price must be numeric!")
        return

    inventory.append({
        "id": pid,
        "category": category,
        "company": company,
        "name": name,
        "qty": qty,
        "price": price
    })

    refresh_table()
    clear_fields()
    messagebox.showinfo("Success", "Item added successfully!")

def delete_item():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Warning", "Please select an item to delete!")
        return

    values = tree.item(selected, "values")
    pid = values[0]

    for item in inventory:
        if item["id"] == pid:
            inventory.remove(item)
            break

    refresh_table()
    clear_fields()
    messagebox.showinfo("Deleted", "Item deleted successfully!")

def update_item():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Warning", "Please select an item to update!")
        return

    pid = entry_id.get().strip()
    category = entry_category.get().strip()
    company = entry_company.get().strip()
    name = entry_name.get().strip()
    qty = entry_qty.get().strip()
    price = entry_price.get().strip()

    if not pid or not category or not company or not name or not qty or not price:
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        qty = int(qty)
        price = float(price)
    except ValueError:
        messagebox.showerror("Error", "Quantity must be integer and Price must be numeric!")
        return

    old_values = tree.item(selected, "values")
    old_pid = old_values[0]

    for item in inventory:
        if item["id"] == old_pid:
            item["id"] = pid
            item["category"] = category
            item["company"] = company
            item["name"] = name
            item["qty"] = qty
            item["price"] = price
            break

    refresh_table()
    clear_fields()
    messagebox.showinfo("Updated", "Item updated successfully!")

def view_product():
    refresh_table()
    messagebox.showinfo("View Product", "All products displayed successfully!")

def search_product():
    keyword = search_entry.get().strip().lower()

    if not keyword:
        messagebox.showwarning("Warning", "Please enter product name, company, category, or ID to search!")
        return

    results = []
    for item in inventory:
        if (keyword in item["id"].lower() or
            keyword in item["category"].lower() or
            keyword in item["company"].lower() or
            keyword in item["name"].lower()):
            results.append(item)

    if results:
        refresh_table(results)
        messagebox.showinfo("Search", f"{len(results)} product(s) found!")
    else:
        refresh_table([])
        messagebox.showinfo("Search", "No matching product found!")

# ---------------- GRAPH 1 ----------------
def qty_graph():
    if not inventory:
        messagebox.showwarning("No Data", "No data available for graph!")
        return

    names = [item["name"] for item in inventory]
    qtys = [item["qty"] for item in inventory]

    plt.figure(figsize=(8, 5))
    plt.bar(names, qtys, color="skyblue")
    plt.xlabel("Product Name")
    plt.ylabel("Quantity")
    plt.title("Product Quantity Comparison")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()

# ---------------- GRAPH 2 ----------------
def comp_graph():
    if not inventory:
        messagebox.showwarning("No Data", "No data available for graph!")
        return

    labels = [f"{item['company']} - {item['name']}" for item in inventory]
    qtys = [item["qty"] for item in inventory]

    plt.figure(figsize=(8, 6))
    plt.pie(qtys, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title("Company and Product Comparison")
    plt.tight_layout()
    plt.show()

def select_item(event):
    selected = tree.focus()
    if not selected:
        return

    values = tree.item(selected, "values")

    entry_id.delete(0, tk.END)
    entry_category.delete(0, tk.END)
    entry_company.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_qty.delete(0, tk.END)
    entry_price.delete(0, tk.END)

    entry_id.insert(0, values[0])
    entry_category.insert(0, values[1])
    entry_company.insert(0, values[2])
    entry_name.insert(0, values[3])
    entry_qty.insert(0, values[4])
    entry_price.insert(0, values[5])

# ---------------- TITLE ----------------
title = tk.Label(root, text="INVENTORY MANAGEMENT SYSTEM", font=("Arial", 22, "bold"),
                 bg="#2c3e50", fg="white", pady=10)
title.pack(fill=tk.X)

# ---------------- FORM FRAME ----------------
form_frame = tk.Frame(root, bg="white", bd=2, relief=tk.RIDGE)
form_frame.place(x=20, y=70, width=350, height=430)

tk.Label(form_frame, text="Product ID", font=("Arial", 12, "bold"), bg="white").place(x=20, y=20)
entry_id = tk.Entry(form_frame, font=("Arial", 12), bd=2, relief=tk.GROOVE)
entry_id.place(x=150, y=20, width=160)

tk.Label(form_frame, text="Category", font=("Arial", 12, "bold"), bg="white").place(x=20, y=70)
entry_category = tk.Entry(form_frame, font=("Arial", 12), bd=2, relief=tk.GROOVE)
entry_category.place(x=150, y=70, width=160)

tk.Label(form_frame, text="Company", font=("Arial", 12, "bold"), bg="white").place(x=20, y=120)
entry_company = tk.Entry(form_frame, font=("Arial", 12), bd=2, relief=tk.GROOVE)
entry_company.place(x=150, y=120, width=160)

tk.Label(form_frame, text="Product Name", font=("Arial", 12, "bold"), bg="white").place(x=20, y=170)
entry_name = tk.Entry(form_frame, font=("Arial", 12), bd=2, relief=tk.GROOVE)
entry_name.place(x=150, y=170, width=160)

tk.Label(form_frame, text="Quantity", font=("Arial", 12, "bold"), bg="white").place(x=20, y=220)
entry_qty = tk.Entry(form_frame, font=("Arial", 12), bd=2, relief=tk.GROOVE)
entry_qty.place(x=150, y=220, width=160)

tk.Label(form_frame, text="Price", font=("Arial", 12, "bold"), bg="white").place(x=20, y=270)
entry_price = tk.Entry(form_frame, font=("Arial", 12), bd=2, relief=tk.GROOVE)
entry_price.place(x=150, y=270, width=160)

tk.Label(form_frame, text="Search", font=("Arial", 12, "bold"), bg="white").place(x=20, y=330)
search_entry = tk.Entry(form_frame, font=("Arial", 12), bd=2, relief=tk.GROOVE)
search_entry.place(x=150, y=330, width=160)

# ---------------- BUTTON FRAME ----------------
btn_frame = tk.Frame(root, bg="#f4f6f8")
btn_frame.place(x=20, y=520, width=350, height=180)

btn_style = {"font": ("Arial", 10, "bold"), "width": 15, "bd": 0, "fg": "white", "cursor": "hand2"}

# Row 1
tk.Button(btn_frame, text="1. Add Item", bg="#28a745", command=add_item, **btn_style).grid(row=0, column=0, padx=6, pady=6)
tk.Button(btn_frame, text="2. Delete Item", bg="#dc3545", command=delete_item, **btn_style).grid(row=0, column=1, padx=6, pady=6)

# Row 2
tk.Button(btn_frame, text="3. Update Item", bg="#007bff", command=update_item, **btn_style).grid(row=1, column=0, padx=6, pady=6)
tk.Button(btn_frame, text="4. View Product", bg="#17a2b8", command=view_product, **btn_style).grid(row=1, column=1, padx=6, pady=6)

# Row 3
tk.Button(btn_frame, text="5. Search Product", bg="#6f42c1", command=search_product, **btn_style).grid(row=2, column=0, padx=6, pady=6)
tk.Button(btn_frame, text="Qty Graph", bg="#fd7e14", command=qty_graph, **btn_style).grid(row=2, column=1, padx=6, pady=6)

# Row 4
tk.Button(btn_frame, text="Comp Graph", bg="#20c997", command=comp_graph, **btn_style).grid(row=3, column=0, padx=6, pady=6)
tk.Button(btn_frame, text="Clear", bg="#6c757d", command=clear_fields, **btn_style).grid(row=3, column=1, padx=6, pady=6)

# Row 5
tk.Button(btn_frame, text="Exit", bg="#343a40", command=root.destroy, **btn_style).grid(row=4, column=0, columnspan=2, pady=10)

# ---------------- TABLE FRAME ----------------
table_frame = tk.Frame(root, bg="white", bd=2, relief=tk.RIDGE)
table_frame.place(x=390, y=70, width=780, height=630)

columns = ("Product ID", "Category", "Company", "Product Name", "Quantity", "Price")
tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=28)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor=tk.CENTER, width=120)

tree.column("Company", width=130)
tree.column("Product Name", width=150)

scroll_y = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=scroll_y.set)

tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

tree.bind("<ButtonRelease-1>", select_item)

# ---------------- RUN APP ----------------
root.mainloop()
