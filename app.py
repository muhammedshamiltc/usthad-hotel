from flask import Flask, render_template, jsonify, request, session, redirect
from pymongo import MongoClient
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'foodmunch_secret_key_2024'
CORS(app)

# Connect to MongoDB
client = MongoClient('mongodb+srv://shamil:ustad1234@ustad-hotel.y3bu4iu.mongodb.net/?appName=ustad-hotel')
db = client['food_munch_db']
    
def serialize(doc):
    doc['_id'] = str(doc['_id'])
    return doc

# ── PAGES ──
@app.route('/')
def home():
    if 'user' in session:
        return render_template('index.html')
    return redirect('/signup')

@app.route('/signup')
def signup_page():
    return render_template('signup.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

# ── API: SIGN UP ──
@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.json
    if db.customers.find_one({'email': data['email']}):
        return jsonify({'success': False, 'message': 'Email already registered!'})
    db.customers.insert_one({
        'name': data['name'],
        'email': data['email'],
        'phone': data['phone'],
        'address': data['address'],
        'password': data['password'],
        'joined_date': datetime.now()
    })
    return jsonify({'success': True, 'message': 'Account created!'})

# ── API: LOGIN ──
@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    user = db.customers.find_one({'email': data['email'], 'password': data['password']})
    if user:
        session['user'] = {
            'name': user['name'],
            'email': user['email'],
            'phone': user['phone'],
            'address': user['address']
        }
        return jsonify({'success': True, 'message': 'Login successful!'})
    return jsonify({'success': False, 'message': 'Wrong email or password!'})

# ── API: SESSION CHECK ──
@app.route('/api/session')
def check_session():
    if 'user' in session:
        return jsonify({'logged_in': True, 'user': session['user']})
    return jsonify({'logged_in': False})

# ── API: LOGOUT ──
@app.route('/api/logout')
def logout():
    session.pop('user', None)
    return jsonify({'success': True})

# ── API: GET MENU ──
@app.route('/api/menu')
def get_menu():
    items = list(db.menu_items.find())
    return jsonify([serialize(i) for i in items])

# ── API: PLACE ORDER ──
@app.route('/api/order', methods=['POST'])
def place_order():
    data = request.json
    items = data['items']
    total = sum(i['price'] * i['quantity'] for i in items)

    order = {
        'customer_name': data['customer_name'],
        'customer_email': data['customer_email'],
        'customer_phone': data['customer_phone'],
        'customer_address': data['customer_address'],
        'items': items,
        'total_price': total,
        'payment_method': data['payment_method'],
        'status': 'Received',
        'order_date': datetime.now()
    }
    result = db.orders.insert_one(order)
    order_id = str(result.inserted_id)

    for item in items:
        db.order_items.insert_one({
            'order_id': order_id,
            'item_name': item['item_name'],
            'quantity': item['quantity'],
            'price': item['price'],
            'subtotal': item['price'] * item['quantity']
        })

    return jsonify({'success': True, 'order_id': order_id, 'items': items, 'total': total})

if __name__ == '__main__':
    app.run(debug=True)
