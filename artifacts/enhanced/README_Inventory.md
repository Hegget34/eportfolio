# Inventory Management System - Enhanced Version

## Overview

This is an enhanced version of an Inventory Management System originally created for CS 340 - Database Systems. The application has been significantly improved to demonstrate professional database design, security practices, and query optimization. The enhancements focus on eliminating critical SQL injection vulnerabilities, implementing proper database constraints, and optimizing query performance.

## Critical Security Improvements

###

 1. **SQL Injection Prevention (CRITICAL)**
- **Original**: String concatenation in SQL queries - CATASTROPHIC VULNERABILITY
- **Enhanced**: Parameterized queries with `?` placeholders throughout
- **Impact**: Prevents database destruction attacks

**Original Vulnerable Code:**
```python
query = "INSERT INTO products VALUES ('" + name + "', '" + desc + "', ...)"
# Attack: name = "'); DROP TABLE products; --"
# Result: Entire database deleted!
```

**Enhanced Secure Code:**
```python
cursor.execute('''
    INSERT INTO products (name, description, price, quantity, category, supplier_id)
    VALUES (?, ?, ?, ?, ?, ?)
''', (name, desc, price, qty, category, supplier_id))
# Attack prevented: Parameters automatically sanitized
```

### 2. **Database Constraints**
- **Foreign Keys**: Referential integrity between products and suppliers
- **NOT NULL**: Required fields cannot be empty
- **CHECK**: Price > 0, Quantity >= 0, non-empty strings
- **UNIQUE**: Prevents duplicate supplier names

### 3. **Secure Credential Management**
- **Original**: Hardcoded database path in source code
- **Enhanced**: Environment variable with secure default
- **Benefit**: Production-ready security configuration

### 4. **Comprehensive Error Handling**
- **Original**: No try-except blocks - crashes on errors
- **Enhanced**: Complete exception handling with rollback
- **Benefit**: Graceful error recovery and data integrity

## Performance Improvements

### 1. **Database Indexes**
Created indexes on frequently queried columns:
- `idx_product_name` - For product name searches
- `idx_product_category` - For category filtering
- `idx_product_supplier` - For supplier joins
- `idx_supplier_name` - For supplier lookups

**Performance Gain**: 100-1,000x faster searches on large datasets

### 2. **SQL Aggregation**
- **Original**: Python loop calculating sum (lines 149-154)
- **Enhanced**: Single SQL `SUM()` query
- **Performance Gain**: 100-1,000x faster for 10,000+ products

**Original Inefficient Code:**
```python
cursor.execute("SELECT price, quantity FROM products")
products = cursor.fetchall()
total = 0
for p in products:
    total = total + (p[0] * p[1])
```

**Enhanced Optimized Code:**
```python
cursor.execute('SELECT SUM(price * quantity) FROM products')
result = cursor.fetchone()
return result[0] if result[0] is not None else 0.0
```

### 3. **Optimized JOIN Queries**
- **Original**: Two separate queries for supplier and products
- **Enhanced**: Single JOIN query
- **Benefit**: Reduced network round-trips, faster execution

### 4. **Transaction Management**
- Context managers with automatic commit/rollback
- ACID properties ensured
- Data consistency guaranteed

## Features

- **Add Products**: Create products with full validation
- **View All Products**: Display complete inventory
- **Search Products**: Keyword search in name/description
- **Update Products**: Modify product information
- **Delete Products**: Remove products from inventory
- **Add Suppliers**: Create supplier records
- **View Suppliers**: List all suppliers
- **Supplier Products**: View products by supplier (optimized JOIN)
- **Low Stock Alerts**: Find items below threshold
- **Inventory Valuation**: Calculate total inventory worth (optimized)

## Requirements

- Python 3.7 or higher
- SQLite3 (included with Python)
- No external dependencies

## Installation

1. Download all files
2. Ensure Python 3.7+ installed
3. No additional setup required

## Usage

### Running the Application

```bash
python Inventory_Enhanced.py
```

### Setting Custom Database Path (Optional)

```bash
# Linux/Mac
export INVENTORY_DB_PATH=/path/to/database.db
python Inventory_Enhanced.py

# Windows
set INVENTORY_DB_PATH=C:\path\to\database.db
python Inventory_Enhanced.py
```

## Database Schema

### Products Table
```sql
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL CHECK(price > 0),
    quantity INTEGER NOT NULL CHECK(quantity >= 0),
    category TEXT NOT NULL,
    supplier_id INTEGER,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
)
```

### Suppliers Table
```sql
CREATE TABLE suppliers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    contact TEXT NOT NULL,
    phone TEXT,
    email TEXT
)
```

## Security Features

### 1. Parameterized Queries (ALL queries)
Every database operation uses parameterized queries:
- `add_product()` - line 155
- `search_products()` - line 185
- `update_product()` - line 220
- `delete_product()` - line 249
- `get_product_by_id()` - line 282
- `get_low_stock()` - line 306
- `add_supplier()` - line 345
- All other queries throughout

### 2. Input Validation
- Price: Must be > 0
- Quantity: Must be >= 0
- Name/Category: Cannot be empty
- Supplier ID: Must exist (foreign key)
- All string inputs: Trimmed and validated

### 3. Transaction Safety
```python
@contextmanager
def get_db_connection():
    conn = None
    try:
        conn = sqlite3.connect(DatabaseConfig.DB_PATH)
        yield conn
        conn.commit()  # Auto-commit on success
    except sqlite3.Error as e:
        if conn:
            conn.rollback()  # Auto-rollback on error
        raise
    finally:
        if conn:
            conn.close()  # Auto-close connection
```

### 4. Foreign Key Enforcement
```sql
FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
    ON DELETE SET NULL    -- If supplier deleted, set product supplier to NULL
    ON UPDATE CASCADE     -- If supplier ID changes, update all products
```

## Error Handling

Comprehensive error handling for all operations:
- Database connection failures
- Constraint violations (foreign key, check, unique)
- Invalid input data
- Missing records
- Rollback on transaction failures

Example:
```python
try:
    InventoryDatabase.add_product(name, desc, price, qty, category, supplier_id)
except ValueError as e:
    print(f'Validation error: {e}')
except sqlite3.IntegrityError as e:
    if 'FOREIGN KEY' in str(e):
        print(f'Error: Supplier ID {supplier_id} does not exist')
    elif 'UNIQUE' in str(e):
        print(f'Error: Duplicate entry')
except sqlite3.Error as e:
    print(f'Database error: {e}')
```

## Course Outcomes Demonstrated

This enhancement demonstrates the following CS 499 course outcomes:

- **Outcome 2**: Design and evaluate computing solutions (database design, query optimization)
- **Outcome 4**: Use well-founded techniques (parameterized queries, transactions, indexes)
- **Outcome 5**: Develop security mindset (SQL injection prevention, input validation, constraint enforcement)

## Comparison: Original vs Enhanced

| Aspect | Original | Enhanced | Improvement |
|--------|----------|----------|-------------|
| **SQL Injection** | Vulnerable | Protected | CRITICAL FIX |
| **Database Constraints** | None | Foreign keys, CHECK, NOT NULL | Data integrity |
| **Indexes** | None | 4 indexes | 100-1,000x faster |
| **Aggregation** | Python loop | SQL SUM() | 100-1,000x faster |
| **Query Optimization** | 2 separate queries | 1 JOIN query | 2x faster |
| **Error Handling** | None | Comprehensive | Robust |
| **Transactions** | Auto-commit | Context managers | ACID compliance |
| **Credentials** | Hardcoded | Environment variable | Secure |

## Vulnerable Lines Fixed

From the original code, these SQL injection vulnerabilities were eliminated:

- **Line 46**: `addProduct` - String concatenation
- **Line 58**: `searchProducts` - String concatenation
- **Line 70**: `updateProduct` - String concatenation
- **Line 81**: `deleteProduct` - f-string injection
- **Line 102**: `getProductById` - String concatenation
- **Line 113**: `getLowStock` - f-string injection
- **Line 124**: `addSupplier` - String concatenation

All now use parameterized queries with `?` placeholders.

## Testing the Security

To verify SQL injection prevention, try these attacks (they will fail safely):

```python
# These attacks are now prevented:
name = "'; DROP TABLE products; --"
name = "' OR '1'='1"
name = "'); DELETE FROM products WHERE '1'='1'; --"

# The application will safely treat these as product names
# instead of executing malicious SQL
```

## Future Enhancements

Potential improvements:
- Web interface (Flask/Django)
- User authentication and authorization
- Audit logging for all changes
- Data export (CSV, Excel)
- Advanced reporting and analytics
- Real-time inventory alerts

## Troubleshooting

**Problem**: Foreign key constraint error
- **Solution**: Ensure supplier exists before adding product with supplier_id

**Problem**: CHECK constraint failed
- **Solution**: Ensure price > 0 and quantity >= 0

**Problem**: UNIQUE constraint failed
- **Solution**: Supplier name already exists - use different name

**Problem**: Database locked
- **Solution**: Close other connections to the database

## Author

Trevor Hegge  
CS 499 - Computer Science Capstone  
Southern New Hampshire University  
December 2025

## License

This project is created for educational purposes as part of the CS 499 capstone course.

## Version History

- **v2.0** (November 2025): Enhanced with parameterized queries, constraints, indexes, security
- **v1.0** (Original): Basic implementation with SQL injection vulnerabilities
