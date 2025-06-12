# main.py
from crud_operations import *
from database import initialize_database

def main():
    initialize_database()
    
    while True:
        print("\nSales Management System")
        print("1. Add New Sale")
        print("2. View Sales")
        print("3. Update Sale")
        print("4. Delete Sale")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            product = input("Product name: ")
            quantity = int(input("Quantity: "))
            price = float(input("Price per unit: "))
            create_sale(product, quantity, price)
            print("Sale recorded successfully!")
            
        elif choice == '2':
            print("\nAll Sales:")
            sales = read_sales()
            for sale in sales:
                print(f"ID: {sale[0]}, Product: {sale[1]}, Date: {sale[2]}, Qty: {sale[3]}, Price: ${sale[4]}")
                
        elif choice == '3':
            sale_id = int(input("Enter sale ID to update: "))
            print("Leave blank to keep current value")
            product = input("New product name: ") or None
            quantity = input("New quantity: ")
            quantity = int(quantity) if quantity else None
            price = input("New price: ")
            price = float(price) if price else None
            update_sale(sale_id, product, quantity, price)
            print("Sale updated successfully!")
            
        elif choice == '4':
            sale_id = int(input("Enter sale ID to delete: "))
            delete_sale(sale_id)
            print("Sale deleted successfully!")
            
        elif choice == '5':
            print("Exiting...")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()