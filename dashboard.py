# dashboard.py
import matplotlib.pyplot as plt
from io import BytesIO
from crud_operations import read_sales
from datetime import datetime, timedelta

def generate_dashboard():
    # Get sales data for the last 30 days
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=30)
    sales = read_sales(start_date, end_date)
    
    if not sales:
        return None
    
    # Calculate statistics
    total_sales = sum(sale[3] for sale in sales)
    total_revenue = sum(sale[3] * sale[4] for sale in sales)
    
    # Find best-selling product
    product_sales = {}
    for sale in sales:
        product_sales[sale[1]] = product_sales.get(sale[1], 0) + sale[3]
    best_seller = max(product_sales.items(), key=lambda x: x[1])
    
    # Create visualization
    plt.figure(figsize=(10, 6))
    products = list(product_sales.keys())
    quantities = list(product_sales.values())
    plt.bar(products, quantities)
    plt.title('Product Sales (Last 30 Days)')
    plt.xlabel('Product')
    plt.ylabel('Quantity Sold')
    plt.xticks(rotation=45)
    
    # Save plot to bytes
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    plt.close()
    
    # Create HTML report
    html_report = f"""
    <h1>Sales Dashboard - {end_date}</h1>
    <h2>Summary Statistics</h2>
    <p>Total Items Sold: {total_sales}</p>
    <p>Total Revenue: ${total_revenue:,.2f}</p>
    <p>Best Selling Product: {best_seller[0]} ({best_seller[1]} units)</p>
    <h2>Sales Visualization</h2>
    <img src="cid:sales_chart">
    """
    
    return html_report, img_buffer