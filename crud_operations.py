# crud_operations.py
from database import get_db_connection
from datetime import datetime

def create_sale(product_name, quantity, price):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO sales (product_name, sales_date, quantity, price) VALUES (?, ?, ?, ?)',
        (product_name, datetime.now().date(), quantity, price)
    )
    conn.commit()
    conn.close()

def read_sales(start_date=None, end_date=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if start_date and end_date:
        cursor.execute('SELECT * FROM sales WHERE sales_date BETWEEN ? AND ? ORDER BY sales_date', 
                      (start_date, end_date))
    else:
        cursor.execute('SELECT * FROM sales ORDER BY sales_date')
    
    sales = cursor.fetchall()
    conn.close()
    return sales

def update_sale(sale_id, product_name=None, quantity=None, price=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    updates = []
    params = []
    
    if product_name:
        updates.append("product_name = ?")
        params.append(product_name)
    if quantity:
        updates.append("quantity = ?")
        params.append(quantity)
    if price:
        updates.append("price = ?")
        params.append(price)
    
    params.append(sale_id)
    query = f"UPDATE sales SET {', '.join(updates)} WHERE id = ?"
    cursor.execute(query, params)
    conn.commit()
    conn.close()

def delete_sale(sale_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM sales WHERE id = ?', (sale_id,))
    conn.commit()
    conn.close()