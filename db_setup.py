from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client['food_munch_db']

# ── COLLECTION 1: CUSTOMERS ──

db.customers.insert_many([
    {'name': 'Shamil Ahmed',  'email': 'shamil@email.com',  'phone': '9876543210', 'address': 'Tirur, Malappuram, Kerala', 'password': 'pass123', 'joined_date': datetime(2024, 1, 15)},
    {'name': 'Aisha Nair',    'email': 'aisha@email.com',   'phone': '9123456789', 'address': 'Kozhikode, Kerala',         'password': 'pass456', 'joined_date': datetime(2024, 2, 20)},
    {'name': 'Rahul Menon',   'email': 'rahul@email.com',   'phone': '9988776655', 'address': 'Thrissur, Kerala',          'password': 'pass789', 'joined_date': datetime(2024, 3, 10)},
])
print("✅ Customers collection created (3 records)")

# ── COLLECTION 2: MENU ITEMS (8 categories x 5-6 items) ──
db.menu_items.drop()
db.menu_items.insert_many([

    # --- Non-veg Starters ---
    {'name': 'Ginger Fried Chicken',    'category': 'Non-veg Starters', 'price': 320, 'description': 'Crispy chicken tossed in ginger garlic sauce',       'is_veg': False, 'is_available': True, 'image': 'static/images/ginger fried.jpg'},
    {'name': 'Chicken 65',              'category': 'Non-veg Starters', 'price': 280, 'description': 'Spicy deep-fried chicken with curry leaves',          'is_veg': False, 'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-ginger-fried-img.png'},
    {'name': 'Mutton Seekh Kebab',      'category': 'Non-veg Starters', 'price': 380, 'description': 'Minced mutton skewers grilled to perfection',         'is_veg': False, 'is_available': True, 'image': 'static/images/delicious-glazed-chicken-wings-with-sauces-dark-background.jpg'},
    {'name': 'Chicken Tikka',           'category': 'Non-veg Starters', 'price': 350, 'description': 'Marinated chicken chunks grilled in tandoor',         'is_veg': False, 'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-ginger-fried-img.png'},
    {'name': 'Prawn Fry',               'category': 'Non-veg Starters', 'price': 420, 'description': 'Crispy fried prawns with spicy masala coating',       'is_veg': False, 'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-ginger-fried-img.png'},

    # --- Veg Starters ---
    {'name': 'Veg Spring Rolls',        'category': 'Veg Starters', 'price': 180, 'description': 'Crispy rolls stuffed with fresh vegetables',              'is_veg': True, 'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-veg-starters-img.png'},
    {'name': 'Paneer Tikka',            'category': 'Veg Starters', 'price': 260, 'description': 'Marinated paneer cubes grilled with peppers',             'is_veg': True, 'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-veg-starters-img.png'},
    {'name': 'Mushroom 65',             'category': 'Veg Starters', 'price': 220, 'description': 'Spicy crispy fried mushrooms with herbs',                 'is_veg': True, 'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-veg-starters-img.png'},
    {'name': 'Veg Manchurian',          'category': 'Veg Starters', 'price': 200, 'description': 'Fried veg balls in tangy manchurian sauce',               'is_veg': True, 'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-veg-starters-img.png'},
    {'name': 'Aloo Tikki',              'category': 'Veg Starters', 'price': 150, 'description': 'Golden potato patties with mint chutney',                 'is_veg': True, 'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-veg-starters-img.png'},
    {'name': 'Corn Cheese Balls',       'category': 'Veg Starters', 'price': 190, 'description': 'Crispy balls stuffed with corn and cheese',               'is_veg': True, 'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-veg-starters-img.png'},

    # --- Soups ---
    {'name': 'Tomato Soup',             'category': 'Soups', 'price': 150, 'description': 'Fresh tomato soup with cream and basil',                         'is_veg': True,  'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-soup-img.png'},
    {'name': 'Sweet Corn Soup',         'category': 'Soups', 'price': 160, 'description': 'Thick sweet corn soup with vegetable pieces',                    'is_veg': True,  'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-soup-img.png'},
    {'name': 'Chicken Noodle Soup',     'category': 'Soups', 'price': 200, 'description': 'Clear broth with chicken, noodles and vegetables',               'is_veg': False, 'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-soup-img.png'},
    {'name': 'Mushroom Cream Soup',     'category': 'Soups', 'price': 180, 'description': 'Creamy mushroom soup with garlic bread',                         'is_veg': True,  'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-soup-img.png'},
    {'name': 'Hot & Sour Soup',         'category': 'Soups', 'price': 170, 'description': 'Classic hot and sour soup with tofu',                            'is_veg': True,  'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-soup-img.png'},

    # --- Fish & Sea Foods ---
    {'name': 'Grilled Prawns',          'category': 'Fish & Sea Foods', 'price': 480, 'description': 'Juicy grilled prawns with lemon butter sauce',        'is_veg': False, 'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-grilled-seafood-img.png'},
    {'name': 'Fish Fry',                'category': 'Fish & Sea Foods', 'price': 350, 'description': 'Crispy Kerala style spiced fish fry',                 'is_veg': False, 'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-grilled-seafood-img.png'},
    {'name': 'Lobster Masala',          'category': 'Fish & Sea Foods', 'price': 750, 'description': 'Fresh lobster cooked in spicy masala gravy',          'is_veg': False, 'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-grilled-seafood-img.png'},
    {'name': 'Calamari Rings',          'category': 'Fish & Sea Foods', 'price': 400, 'description': 'Crispy fried squid rings with dipping sauce',         'is_veg': False, 'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-grilled-seafood-img.png'},
    {'name': 'Crab Curry',              'category': 'Fish & Sea Foods', 'price': 620, 'description': 'Kerala style crab curry with coconut milk',           'is_veg': False, 'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-grilled-seafood-img.png'},

    # --- Main Courses ---
    {'name': 'Chicken Biryani',         'category': 'Main Courses', 'price': 360, 'description': 'Hyderabadi dum biryani with raita and salan',             'is_veg': False, 'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-hyderabadi-biryani-img.png'},
    {'name': 'Mutton Biryani',          'category': 'Main Courses', 'price': 420, 'description': 'Slow cooked mutton biryani with caramelized onions',      'is_veg': False, 'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-hyderabadi-biryani-img.png'},
    {'name': 'Paneer Butter Masala',    'category': 'Main Courses', 'price': 280, 'description': 'Paneer cubes in rich tomato butter gravy',                'is_veg': True,  'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-hyderabadi-biryani-img.png'},
    {'name': 'Dal Makhani',             'category': 'Main Courses', 'price': 220, 'description': 'Slow cooked black lentils in cream and butter',           'is_veg': True,  'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-hyderabadi-biryani-img.png'},
    {'name': 'Chicken Tikka Masala',    'category': 'Main Courses', 'price': 340, 'description': 'Grilled chicken in spiced creamy tomato sauce',           'is_veg': False, 'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-hyderabadi-biryani-img.png'},
    {'name': 'Veg Fried Rice',          'category': 'Main Courses', 'price': 200, 'description': 'Wok tossed rice with fresh vegetables',                   'is_veg': True,  'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-hyderabadi-biryani-img.png'},

    # --- Noodles ---
    {'name': 'Mushroom Noodles',        'category': 'Noodles', 'price': 220, 'description': 'Stir fried noodles with mushrooms and soy sauce',              'is_veg': True,  'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-mushroom-noodles-img.png'},
    {'name': 'Chicken Hakka Noodles',   'category': 'Noodles', 'price': 260, 'description': 'Indo-Chinese hakka noodles with chicken and veggies',          'is_veg': False, 'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-mushroom-noodles-img.png'},
    {'name': 'Veg Pad Thai',            'category': 'Noodles', 'price': 240, 'description': 'Thai style rice noodles with peanuts and tofu',                'is_veg': True,  'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-mushroom-noodles-img.png'},
    {'name': 'Prawn Noodles',           'category': 'Noodles', 'price': 320, 'description': 'Stir fried noodles with juicy prawns',                         'is_veg': False, 'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-mushroom-noodles-img.png'},
    {'name': 'Singapore Noodles',       'category': 'Noodles', 'price': 280, 'description': 'Spicy thin rice noodles with egg and vegetables',              'is_veg': False, 'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-mushroom-noodles-img.png'},

    # --- Salads ---
    {'name': 'Garden Fresh Salad',      'category': 'Salads', 'price': 180, 'description': 'Fresh garden vegetables with lemon dressing',                   'is_veg': True,  'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-gluten-img.png'},
    {'name': 'Caesar Salad',            'category': 'Salads', 'price': 220, 'description': 'Romaine lettuce, croutons and caesar dressing',                 'is_veg': True,  'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-gluten-img.png'},
    {'name': 'Greek Salad',             'category': 'Salads', 'price': 200, 'description': 'Olives, feta cheese, cucumber and tomatoes',                    'is_veg': True,  'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-gluten-img.png'},
    {'name': 'Chicken Caesar Salad',    'category': 'Salads', 'price': 280, 'description': 'Grilled chicken strips on classic caesar salad',                'is_veg': False, 'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-gluten-img.png'},
    {'name': 'Fruit Salad',             'category': 'Salads', 'price': 160, 'description': 'Fresh seasonal fruits with honey dressing',                     'is_veg': True,  'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-gluten-img.png'},

    # --- Desserts ---
    {'name': 'Chocolate Lava Cake',     'category': 'Desserts', 'price': 250, 'description': 'Warm chocolate cake with molten center and ice cream',        'is_veg': True,  'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-coffee-bourbon-img.png'},
    {'name': 'Gulab Jamun',             'category': 'Desserts', 'price': 120, 'description': 'Soft milk solid dumplings in rose sugar syrup',               'is_veg': True,  'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-coffee-bourbon-img.png'},
    {'name': 'Mango Kulfi',             'category': 'Desserts', 'price': 140, 'description': 'Traditional Indian ice cream with mango flavour',             'is_veg': True,  'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-coffee-bourbon-img.png'},
    {'name': 'Tiramisu',                'category': 'Desserts', 'price': 280, 'description': 'Classic Italian dessert with coffee and mascarpone',          'is_veg': True,  'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-coffee-bourbon-img.png'},
    {'name': 'Rasmalai',                'category': 'Desserts', 'price': 160, 'description': 'Soft paneer discs soaked in sweetened saffron milk',          'is_veg': True,  'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-coffee-bourbon-img.png'},
    {'name': 'Brownie with Ice Cream',  'category': 'Desserts', 'price': 220, 'description': 'Warm fudgy brownie served with vanilla ice cream',            'is_veg': True,  'is_available': True, 'image': 'https://d2clawv67efefq.cloudfront.net/ccbp-responsive-website/em-coffee-bourbon-img.png'},
])
print("✅ Menu items collection created (8 categories, 40+ items)")

# ── COLLECTION 3: ORDERS ──

db.orders.insert_many([
    {'customer_name': 'Shamil Ahmed', 'customer_email': 'shamil@email.com', 'customer_phone': '9876543210', 'customer_address': 'Tirur, Malappuram, Kerala', 'total_price': 700, 'status': 'Delivered', 'payment_method': 'Online', 'order_date': datetime(2024, 5, 10)},
    {'customer_name': 'Aisha Nair',   'customer_email': 'aisha@email.com',  'customer_phone': '9123456789', 'customer_address': 'Kozhikode, Kerala',         'total_price': 480, 'status': 'Preparing', 'payment_method': 'Cash',   'order_date': datetime(2024, 5, 12)},
])
print("✅ Orders collection created")

# ── COLLECTION 4: ORDER ITEMS ──

db.order_items.insert_many([
    {'order_id': 'ORD001', 'item_name': 'Ginger Fried Chicken', 'quantity': 1, 'price': 320, 'subtotal': 320},
    {'order_id': 'ORD001', 'item_name': 'Tomato Soup',          'quantity': 1, 'price': 150, 'subtotal': 150},
    {'order_id': 'ORD001', 'item_name': 'Gulab Jamun',          'quantity': 1, 'price': 120, 'subtotal': 120},
    {'order_id': 'ORD002', 'item_name': 'Grilled Prawns',       'quantity': 1, 'price': 480, 'subtotal': 480},
])
print("✅ Order items collection created")

# ── COLLECTION 5: RESERVATIONS ──

db.reservations.insert_many([
    {'customer_name': 'Shamil Ahmed', 'phone': '9876543210', 'date': '2024-06-15', 'time': '7:00 PM', 'guests': 4, 'status': 'Confirmed'},
    {'customer_name': 'Rahul Menon',  'phone': '9988776655', 'date': '2024-06-18', 'time': '8:00 PM', 'guests': 2, 'status': 'Pending'},
])
print("✅ Reservations collection created")

# ── COLLECTION 6: REVIEWS ──

db.reviews.insert_many([
    {'customer_name': 'Shamil Ahmed', 'item_name': 'Chicken Biryani', 'rating': 5, 'comment': 'Absolutely delicious! Best biryani ever.',   'date': datetime(2024, 5, 11)},
    {'customer_name': 'Aisha Nair',   'item_name': 'Grilled Prawns',  'rating': 4, 'comment': 'Fresh and well cooked. Loved it!',           'date': datetime(2024, 5, 13)},
    {'customer_name': 'Rahul Menon',  'item_name': 'Mushroom Noodles','rating': 5, 'comment': 'Perfect flavour, will order again!',         'date': datetime(2024, 5, 14)},
])
print("✅ Reviews collection created")

print("")
print("🎉 All 6 collections ready in food_munch_db!")
print("   → customers, menu_items, orders, order_items, reservations, reviews")
