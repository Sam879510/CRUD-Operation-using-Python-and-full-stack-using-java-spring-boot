# app.py (Backend)
from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'yourpassword',
    'database': 'kals_inventory'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/api/beers', methods=['GET'])
def get_beers():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM beer_inventory')
    beers = cursor.fetchall()
    conn.close()
    return jsonify(beers)

@app.route('/api/request', methods=['POST'])
def create_request():
    data = request.get_json()
    beer_id = data['beer_id']
    promo_item = data['promo_item']
    quantity = data['quantity']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Check available quantity
        cursor.execute('SELECT quantity FROM beer_inventory WHERE id = %s', (beer_id,))
        current_qty = cursor.fetchone()[0]
        
        if current_qty < quantity:
            return jsonify({'error': 'Not enough stock available'}), 400
        
        # Update inventory
        cursor.execute(
            'UPDATE beer_inventory SET quantity = quantity - %s WHERE id = %s',
            (quantity, beer_id)
        )
        conn.commit()
        
        # In a real app, you would also create a request record in another table
        return jsonify({'message': 'Request processed successfully'})
    
    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)}), 500
    
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)