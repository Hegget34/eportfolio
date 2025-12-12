# Inventory Management System
# Created for CS 340 - Database Systems

import sqlite3

# Database credentials hardcoded - BAD PRACTICE!
DB_PATH = 'inventory.db'

def createDatabase():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create tables without proper constraints
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT,
            price REAL,
            quantity INTEGER,
            category TEXT,
            supplier_id INTEGER
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS suppliers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            contact TEXT,
            phone TEXT,
            email TEXT
        )
    ''')
    
    # No indexes created
    
    conn.commit()
    conn.close()

def addProduct(name, desc, price, qty, category, supplier_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # SQL Injection vulnerability - using string concatenation!
    query = "INSERT INTO products (name, description, price, quantity, category, supplier_id) VALUES ('" + name + "', '" + desc + "', " + str(price) + ", " + str(qty) + ", '" + category + "', " + str(supplier_id) + ")"
    
    cursor.execute(query)
    conn.commit()
    conn.close()
    print('Product added successfully!')

def searchProducts(keyword):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Another SQL injection vulnerability
    query = "SELECT * FROM products WHERE name LIKE '%" + keyword + "%' OR description LIKE '%" + keyword + "%'"
    cursor.execute(query)
    
    results = cursor.fetchall()
    conn.close()
    return results

def updateProduct(product_id, name, price, qty):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # SQL injection vulnerability
    query = "UPDATE products SET name='" + name + "', price=" + str(price) + ", quantity=" + str(qty) + " WHERE id=" + str(product_id)
    cursor.execute(query)
    
    conn.commit()
    conn.close()

def deleteProduct(product_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # No error handling
    query = f"DELETE FROM products WHERE id={product_id}"
    cursor.execute(query)
    conn.commit()
    conn.close()

def getAllProducts():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Retrieving all columns even if not needed - inefficient
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    
    conn.close()
    return products

def getProductById(product_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # SQL injection vulnerability
    query = "SELECT * FROM products WHERE id = " + str(product_id)
    cursor.execute(query)
    
    product = cursor.fetchone()
    conn.close()
    return product

def getLowStock(threshold):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT * FROM products WHERE quantity < {threshold}")
    results = cursor.fetchall()
    
    conn.close()
    return results

def addSupplier(name, contact, phone, email):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # SQL injection vulnerability
    query = "INSERT INTO suppliers (name, contact, phone, email) VALUES ('" + name + "', '" + contact + "', '" + phone + "', '" + email + "')"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

def getSupplierProducts(supplier_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # No JOIN optimization, making multiple queries
    cursor.execute(f"SELECT * FROM products WHERE supplier_id = {supplier_id}")
    products = cursor.fetchall()
    
    cursor.execute(f"SELECT * FROM suppliers WHERE id = {supplier_id}")
    supplier = cursor.fetchone()
    
    conn.close()
    return supplier, products

def calculateInventoryValue():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Inefficient - retrieving all data instead of using SQL aggregation
    cursor.execute("SELECT price, quantity FROM products")
    products = cursor.fetchall()
    
    total = 0
    for p in products:
        total = total + (p[0] * p[1])
    
    conn.close()
    return total

def displayProducts(products):
    if len(products) == 0:
        print('No products found')
    else:
        print('\n--- Products ---')
        for p in products:
            print(f'ID: {p[0]} | Name: {p[1]} | Price: ${p[3]} | Qty: {p[4]} | Category: {p[5]}')

def menu():
    print('\n=== Inventory Management System ===')
    print('1. Add Product')
    print('2. View All Products')
    print('3. Search Products')
    print('4. Update Product')
    print('5. Delete Product')
    print('6. Add Supplier')
    print('7. View Low Stock Items')
    print('8. Calculate Total Inventory Value')
    print('9. Exit')
    return input('Enter choice: ')

def main():
    # Initialize database
    createDatabase()
    
    while True:
        choice = menu()
        
        if choice == '1':
            name = input('Product name: ')
            desc = input('Description: ')
            price = float(input('Price: '))
            qty = int(input('Quantity: '))
            category = input('Category: ')
            supplier_id = int(input('Supplier ID: '))
            addProduct(name, desc, price, qty, category, supplier_id)
            
        elif choice == '2':
            products = getAllProducts()
            displayProducts(products)
            
        elif choice == '3':
            keyword = input('Search keyword: ')
            results = searchProducts(keyword)
            displayProducts(results)
            
        elif choice == '4':
            pid = int(input('Product ID: '))
            name = input('New name: ')
            price = float(input('New price: '))
            qty = int(input('New quantity: '))
            updateProduct(pid, name, price, qty)
            print('Product updated!')
            
        elif choice == '5':
            pid = int(input('Product ID to delete: '))
            deleteProduct(pid)
            print('Product deleted!')
            
        elif choice == '6':
            name = input('Supplier name: ')
            contact = input('Contact person: ')
            phone = input('Phone: ')
            email = input('Email: ')
            addSupplier(name, contact, phone, email)
            print('Supplier added!')
            
        elif choice == '7':
            threshold = int(input('Low stock threshold: '))
            low_stock = getLowStock(threshold)
            print(f'Found {len(low_stock)} low stock items:')
            displayProducts(low_stock)
            
        elif choice == '8':
            value = calculateInventoryValue()
            print(f'Total inventory value: ${value:.2f}')
            
        elif choice == '9':
            break

if __name__ == '__main__':
    main()
