"""
Inventory Management System - Enhanced Version
Created for CS 499 - Computer Science Capstone
Enhanced: December 2025

This enhanced version demonstrates:
- Parameterized queries to prevent SQL injection
- Proper database constraints (foreign keys, NOT NULL, CHECK)
- Performance indexes for faster queries
- Comprehensive error handling and transaction management
- Secure credential management
- Query optimization using SQL aggregation
"""

import sqlite3
import os
from typing import List, Tuple, Optional
from contextlib import contextmanager


class DatabaseConfig:
    """
    Manages database configuration securely.
    
    In production, DB_PATH would be loaded from environment variables.
    For this demo, we use a default value.
    """
    DB_PATH = os.environ.get('INVENTORY_DB_PATH', 'inventory_secure.db')


@contextmanager
def get_db_connection():
    """
    Context manager for database connections with automatic cleanup.
    
    Yields:
        sqlite3.Connection: Database connection
        
    Example:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            # perform operations
    """
    conn = None
    try:
        conn = sqlite3.connect(DatabaseConfig.DB_PATH)
        yield conn
        conn.commit()
    except sqlite3.Error as e:
        if conn:
            conn.rollback()
        raise
    finally:
        if conn:
            conn.close()


class InventoryDatabase:
    """
    Manages inventory database with security and performance enhancements.
    
    Security improvements:
    - Parameterized queries prevent SQL injection
    - Input validation on all data
    - Proper error handling
    
    Performance improvements:
    - Indexes on frequently queried columns
    - SQL aggregation instead of Python loops
    - Optimized JOIN queries
    """
    
    @staticmethod
    def create_database() -> None:
        """
        Create database tables with proper constraints and indexes.
        
        Improvements from original:
        - Foreign key constraints for referential integrity
        - NOT NULL constraints on required fields
        - CHECK constraints for data validation
        - Indexes for query performance
        """
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                
                # Enable foreign key support (required for SQLite)
                cursor.execute('PRAGMA foreign_keys = ON')
                
                # Create suppliers table first (referenced by products)
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS suppliers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL UNIQUE,
                        contact TEXT NOT NULL,
                        phone TEXT,
                        email TEXT,
                        CHECK(length(name) > 0),
                        CHECK(length(contact) > 0)
                    )
                ''')
                
                # Create products table with proper constraints
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        description TEXT,
                        price REAL NOT NULL CHECK(price > 0),
                        quantity INTEGER NOT NULL CHECK(quantity >= 0),
                        category TEXT NOT NULL,
                        supplier_id INTEGER,
                        FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
                            ON DELETE SET NULL
                            ON UPDATE CASCADE,
                        CHECK(length(name) > 0),
                        CHECK(length(category) > 0)
                    )
                ''')
                
                # Create performance indexes
                cursor.execute('''
                    CREATE INDEX IF NOT EXISTS idx_product_name 
                    ON products(name)
                ''')
                
                cursor.execute('''
                    CREATE INDEX IF NOT EXISTS idx_product_category 
                    ON products(category)
                ''')
                
                cursor.execute('''
                    CREATE INDEX IF NOT EXISTS idx_product_supplier 
                    ON products(supplier_id)
                ''')
                
                cursor.execute('''
                    CREATE INDEX IF NOT EXISTS idx_supplier_name 
                    ON suppliers(name)
                ''')
                
                print('Database created successfully with constraints and indexes!')
                
        except sqlite3.Error as e:
            print(f'Error creating database: {e}')
            raise
    
    @staticmethod
    def add_product(name: str, desc: str, price: float, qty: int, 
                   category: str, supplier_id: Optional[int]) -> None:
        """
        Add a product using parameterized query to prevent SQL injection.
        
        Args:
            name: Product name
            desc: Product description
            price: Product price (must be > 0)
            qty: Quantity (must be >= 0)
            category: Product category
            supplier_id: Supplier ID (optional)
            
        Raises:
            ValueError: If validation fails
            sqlite3.Error: If database operation fails
        """
        # Input validation
        if not name or not name.strip():
            raise ValueError("Product name cannot be empty")
        
        if not category or not category.strip():
            raise ValueError("Category cannot be empty")
        
        if price <= 0:
            raise ValueError("Price must be greater than 0")
        
        if qty < 0:
            raise ValueError("Quantity cannot be negative")
        
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                
                # SECURE: Parameterized query prevents SQL injection
                cursor.execute('''
                    INSERT INTO products (name, description, price, quantity, category, supplier_id)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (name.strip(), desc, price, qty, category.strip(), supplier_id))
                
                print('Product added successfully!')
                
        except sqlite3.IntegrityError as e:
            if 'FOREIGN KEY' in str(e):
                print(f'Error: Supplier ID {supplier_id} does not exist')
            else:
                print(f'Error adding product: {e}')
            raise
        except sqlite3.Error as e:
            print(f'Database error: {e}')
            raise
    
    @staticmethod
    def search_products(keyword: str) -> List[Tuple]:
        """
        Search products by keyword using parameterized query.
        
        Args:
            keyword: Search term
            
        Returns:
            List of product tuples matching search
        """
        if not keyword:
            return []
        
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                
                # SECURE: Parameterized query with wildcards
                search_term = f'%{keyword}%'
                cursor.execute('''
                    SELECT * FROM products 
                    WHERE name LIKE ? OR description LIKE ?
                ''', (search_term, search_term))
                
                return cursor.fetchall()
                
        except sqlite3.Error as e:
            print(f'Error searching products: {e}')
            return []
    
    @staticmethod
    def update_product(product_id: int, name: str, price: float, qty: int) -> None:
        """
        Update product using parameterized query.
        
        Args:
            product_id: ID of product to update
            name: New product name
            price: New price
            qty: New quantity
            
        Raises:
            ValueError: If validation fails
        """
        # Input validation
        if not name or not name.strip():
            raise ValueError("Product name cannot be empty")
        
        if price <= 0:
            raise ValueError("Price must be greater than 0")
        
        if qty < 0:
            raise ValueError("Quantity cannot be negative")
        
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                
                # SECURE: Parameterized query
                cursor.execute('''
                    UPDATE products 
                    SET name = ?, price = ?, quantity = ?
                    WHERE id = ?
                ''', (name.strip(), price, qty, product_id))
                
                if cursor.rowcount == 0:
                    print('Product not found')
                else:
                    print('Product updated successfully!')
                    
        except sqlite3.Error as e:
            print(f'Error updating product: {e}')
            raise
    
    @staticmethod
    def delete_product(product_id: int) -> None:
        """
        Delete product using parameterized query.
        
        Args:
            product_id: ID of product to delete
        """
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                
                # SECURE: Parameterized query
                cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
                
                if cursor.rowcount == 0:
                    print('Product not found')
                else:
                    print('Product deleted successfully!')
                    
        except sqlite3.Error as e:
            print(f'Error deleting product: {e}')
            raise
    
    @staticmethod
    def get_all_products() -> List[Tuple]:
        """
        Get all products with optimized query.
        
        Returns:
            List of all product tuples
        """
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                
                # Select specific columns instead of SELECT *
                cursor.execute('''
                    SELECT id, name, description, price, quantity, category, supplier_id
                    FROM products
                    ORDER BY name
                ''')
                
                return cursor.fetchall()
                
        except sqlite3.Error as e:
            print(f'Error retrieving products: {e}')
            return []
    
    @staticmethod
    def get_product_by_id(product_id: int) -> Optional[Tuple]:
        """
        Get product by ID using parameterized query.
        
        Args:
            product_id: Product ID to find
            
        Returns:
            Product tuple or None if not found
        """
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                
                # SECURE: Parameterized query
                cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
                
                return cursor.fetchone()
                
        except sqlite3.Error as e:
            print(f'Error retrieving product: {e}')
            return None
    
    @staticmethod
    def get_low_stock(threshold: int) -> List[Tuple]:
        """
        Get products below stock threshold using parameterized query.
        
        Args:
            threshold: Minimum quantity threshold
            
        Returns:
            List of low-stock products
        """
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                
                # SECURE: Parameterized query
                cursor.execute('''
                    SELECT * FROM products 
                    WHERE quantity < ?
                    ORDER BY quantity ASC
                ''', (threshold,))
                
                return cursor.fetchall()
                
        except sqlite3.Error as e:
            print(f'Error retrieving low stock items: {e}')
            return []
    
    @staticmethod
    def add_supplier(name: str, contact: str, phone: str, email: str) -> None:
        """
        Add supplier using parameterized query.
        
        Args:
            name: Supplier name
            contact: Contact person
            phone: Phone number
            email: Email address
            
        Raises:
            ValueError: If validation fails
        """
        # Input validation
        if not name or not name.strip():
            raise ValueError("Supplier name cannot be empty")
        
        if not contact or not contact.strip():
            raise ValueError("Contact name cannot be empty")
        
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                
                # SECURE: Parameterized query
                cursor.execute('''
                    INSERT INTO suppliers (name, contact, phone, email)
                    VALUES (?, ?, ?, ?)
                ''', (name.strip(), contact.strip(), phone, email))
                
                print('Supplier added successfully!')
                
        except sqlite3.IntegrityError as e:
            if 'UNIQUE' in str(e):
                print(f'Error: Supplier name "{name}" already exists')
            else:
                print(f'Error adding supplier: {e}')
            raise
        except sqlite3.Error as e:
            print(f'Database error: {e}')
            raise
    
    @staticmethod
    def get_supplier_products(supplier_id: int) -> Tuple[Optional[Tuple], List[Tuple]]:
        """
        Get supplier and their products using optimized JOIN query.
        
        OPTIMIZATION: Single JOIN query instead of two separate queries.
        
        Args:
            supplier_id: Supplier ID
            
        Returns:
            Tuple of (supplier_info, list_of_products)
        """
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                
                # Get supplier info
                cursor.execute('SELECT * FROM suppliers WHERE id = ?', (supplier_id,))
                supplier = cursor.fetchone()
                
                if not supplier:
                    return (None, [])
                
                # Get products with JOIN for efficiency
                cursor.execute('''
                    SELECT p.* 
                    FROM products p
                    INNER JOIN suppliers s ON p.supplier_id = s.id
                    WHERE s.id = ?
                    ORDER BY p.name
                ''', (supplier_id,))
                
                products = cursor.fetchall()
                
                return (supplier, products)
                
        except sqlite3.Error as e:
            print(f'Error retrieving supplier products: {e}')
            return (None, [])
    
    @staticmethod
    def calculate_inventory_value() -> float:
        """
        Calculate total inventory value using SQL aggregation.
        
        OPTIMIZATION: Uses SQL SUM() instead of Python loop.
        This is dramatically faster for large datasets.
        
        Returns:
            Total inventory value
        """
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                
                # OPTIMIZED: SQL aggregation instead of fetching all rows
                cursor.execute('''
                    SELECT SUM(price * quantity) as total_value
                    FROM products
                ''')
                
                result = cursor.fetchone()
                return result[0] if result[0] is not None else 0.0
                
        except sqlite3.Error as e:
            print(f'Error calculating inventory value: {e}')
            return 0.0
    
    @staticmethod
    def get_all_suppliers() -> List[Tuple]:
        """
        Get all suppliers.
        
        Returns:
            List of supplier tuples
        """
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM suppliers ORDER BY name')
                return cursor.fetchall()
        except sqlite3.Error as e:
            print(f'Error retrieving suppliers: {e}')
            return []


def display_products(products: List[Tuple]) -> None:
    """
    Display products in formatted output.
    
    Args:
        products: List of product tuples
    """
    if not products:
        print('No products found')
    else:
        print('\n--- Products ---')
        for p in products:
            print(f'ID: {p[0]} | Name: {p[1]} | Price: ${p[3]:.2f} | Qty: {p[4]} | Category: {p[5]}')


def display_suppliers(suppliers: List[Tuple]) -> None:
    """
    Display suppliers in formatted output.
    
    Args:
        suppliers: List of supplier tuples
    """
    if not suppliers:
        print('No suppliers found')
    else:
        print('\n--- Suppliers ---')
        for s in suppliers:
            print(f'ID: {s[0]} | Name: {s[1]} | Contact: {s[2]} | Phone: {s[3]} | Email: {s[4]}')


class InventoryUI:
    """Handles user interface with input validation."""
    
    @staticmethod
    def get_valid_integer(prompt: str, min_val: int = None) -> int:
        """Get validated integer input."""
        while True:
            try:
                value = int(input(prompt))
                if min_val is not None and value < min_val:
                    print(f'Error: Value must be at least {min_val}')
                    continue
                return value
            except ValueError:
                print('Error: Please enter a valid number')
    
    @staticmethod
    def get_valid_float(prompt: str, min_val: float = None) -> float:
        """Get validated float input."""
        while True:
            try:
                value = float(input(prompt))
                if min_val is not None and value < min_val:
                    print(f'Error: Value must be at least {min_val}')
                    continue
                return value
            except ValueError:
                print('Error: Please enter a valid number')
    
    @staticmethod
    def get_non_empty_string(prompt: str) -> str:
        """Get non-empty string input."""
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print('Error: Input cannot be empty')
    
    @staticmethod
    def get_optional_integer(prompt: str) -> Optional[int]:
        """Get optional integer input (can be empty)."""
        while True:
            value = input(prompt).strip()
            if not value:
                return None
            try:
                return int(value)
            except ValueError:
                print('Error: Please enter a valid number or leave empty')
    
    @staticmethod
    def display_menu() -> None:
        """Display main menu."""
        print('\n=== Inventory Management System - Enhanced ===')
        print('1. Add Product')
        print('2. View All Products')
        print('3. Search Products')
        print('4. Update Product')
        print('5. Delete Product')
        print('6. Add Supplier')
        print('7. View All Suppliers')
        print('8. View Supplier Products')
        print('9. View Low Stock Items')
        print('10. Calculate Total Inventory Value')
        print('11. Exit')
    
    def run(self) -> None:
        """Main program loop."""
        # Initialize database
        try:
            InventoryDatabase.create_database()
        except sqlite3.Error as e:
            print(f'Fatal error creating database: {e}')
            return
        
        print('Welcome to Inventory Management System - Enhanced Version')
        print('Featuring: Parameterized queries, database constraints, and security!')
        
        while True:
            self.display_menu()
            choice = input('Enter choice: ').strip()
            
            try:
                if choice == '1':
                    self.handle_add_product()
                elif choice == '2':
                    self.handle_view_all_products()
                elif choice == '3':
                    self.handle_search_products()
                elif choice == '4':
                    self.handle_update_product()
                elif choice == '5':
                    self.handle_delete_product()
                elif choice == '6':
                    self.handle_add_supplier()
                elif choice == '7':
                    self.handle_view_suppliers()
                elif choice == '8':
                    self.handle_view_supplier_products()
                elif choice == '9':
                    self.handle_low_stock()
                elif choice == '10':
                    self.handle_inventory_value()
                elif choice == '11':
                    print('Thank you for using Inventory Management System!')
                    break
                else:
                    print('Invalid choice. Please enter a number between 1 and 11.')
            except Exception as e:
                print(f'An error occurred: {e}')
    
    def handle_add_product(self) -> None:
        """Handle adding a new product."""
        name = self.get_non_empty_string('Product name: ')
        desc = input('Description: ')
        price = self.get_valid_float('Price: ', min_val=0.01)
        qty = self.get_valid_integer('Quantity: ', min_val=0)
        category = self.get_non_empty_string('Category: ')
        supplier_id = self.get_optional_integer('Supplier ID (or press Enter to skip): ')
        
        try:
            InventoryDatabase.add_product(name, desc, price, qty, category, supplier_id)
        except (ValueError, sqlite3.Error) as e:
            # Error already printed in add_product method
            pass
    
    def handle_view_all_products(self) -> None:
        """Handle viewing all products."""
        products = InventoryDatabase.get_all_products()
        display_products(products)
    
    def handle_search_products(self) -> None:
        """Handle searching products."""
        keyword = input('Search keyword: ')
        results = InventoryDatabase.search_products(keyword)
        display_products(results)
    
    def handle_update_product(self) -> None:
        """Handle updating a product."""
        pid = self.get_valid_integer('Product ID: ')
        name = self.get_non_empty_string('New name: ')
        price = self.get_valid_float('New price: ', min_val=0.01)
        qty = self.get_valid_integer('New quantity: ', min_val=0)
        
        try:
            InventoryDatabase.update_product(pid, name, price, qty)
        except (ValueError, sqlite3.Error):
            pass
    
    def handle_delete_product(self) -> None:
        """Handle deleting a product."""
        pid = self.get_valid_integer('Product ID to delete: ')
        InventoryDatabase.delete_product(pid)
    
    def handle_add_supplier(self) -> None:
        """Handle adding a supplier."""
        name = self.get_non_empty_string('Supplier name: ')
        contact = self.get_non_empty_string('Contact person: ')
        phone = input('Phone: ')
        email = input('Email: ')
        
        try:
            InventoryDatabase.add_supplier(name, contact, phone, email)
        except (ValueError, sqlite3.Error):
            pass
    
    def handle_view_suppliers(self) -> None:
        """Handle viewing all suppliers."""
        suppliers = InventoryDatabase.get_all_suppliers()
        display_suppliers(suppliers)
    
    def handle_view_supplier_products(self) -> None:
        """Handle viewing supplier and their products."""
        supplier_id = self.get_valid_integer('Supplier ID: ')
        supplier, products = InventoryDatabase.get_supplier_products(supplier_id)
        
        if supplier:
            print(f'\nSupplier: {supplier[1]} | Contact: {supplier[2]}')
            display_products(products)
        else:
            print('Supplier not found')
    
    def handle_low_stock(self) -> None:
        """Handle viewing low stock items."""
        threshold = self.get_valid_integer('Low stock threshold: ', min_val=0)
        low_stock = InventoryDatabase.get_low_stock(threshold)
        print(f'Found {len(low_stock)} low stock items:')
        display_products(low_stock)
    
    def handle_inventory_value(self) -> None:
        """Handle calculating inventory value."""
        value = InventoryDatabase.calculate_inventory_value()
        print(f'Total inventory value: ${value:.2f}')


def main():
    """Main entry point for the application."""
    ui = InventoryUI()
    ui.run()


if __name__ == '__main__':
    main()
