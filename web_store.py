from flask import Flask, render_template, redirect, url_for, abort, request
app = Flask(__name__)

PRODUCTS = [
    {'id': 1, 'name': 'NIKE ONE', 'price': '134', 'image': 'NIKE_Clt.jpg', 'description': 'Premium Nike athletic outfit with maximum comfort.'},
    {'id': 2, 'name': 'Nike Air Max 2', 'price': '84', 'image': 'shoes_7.avif', 'description': 'Classic style meets modern cushioning.'},
    {'id': 3, 'name': 'NIKE Kids 2', 'price': '84', 'image': 'k11.avif', 'description': 'Durable and comfortable activewear for kids.'},
    {'id': 4, 'name': 'shoes 2', 'price': '92', 'image': 'shoes_1.avif', 'description': 'Lightweight running shoes designed for speed.'},
    {'id': 5, 'name': 'NIKE Jacket', 'price': '94', 'image': 'Jack_1.avif', 'description': 'Weather-resistant lightweight zip jacket.'},
    {'id': 6, 'name': 'NIKE short', 'price': '44', 'image': 'Nike_short_2.avif', 'description': 'Breathable shorts designed for training.'},
    {'id': 7, 'name': 'Nike Sandal 2', 'price': '84', 'image': 'shoes_10.avif', 'description': 'Casual slip-on sandals for everyday wear.'},
    {'id': 8, 'name': 'NIKE Kids', 'price': '54', 'image': 'K1.avif', 'description': 'Flexible everyday shoes built for energetic kids.'},
    {'id': 9, 'name': 'NIKE WHOLE', 'price': '194', 'image': 'NIKE_Whole.jpg', 'description': 'Complete athletic performance set.'},
    {'id': 10, 'name': 'NIKE FASH', 'price': '99', 'image': 'Accessoires.avif', 'description': 'Essential sporting and casual accessories.'},
    {'id': 11, 'name': 'NIKE TWO', 'price': '84', 'image': 'header_2.jpg', 'description': 'Modern activewear set with ergonomic fit.'},
    {'id': 12, 'name': 'NIKE SF', 'price': '64', 'image': 'header_3.jpg', 'description': 'Versatile performance top for all workouts.'}
]

cart_items = []

def is_item_in_cart(product_id_p):

    counter =0
    for item in cart_items:
        if item['id'] == product_id_p:

            return True, counter
        counter += 1
    return False, counter


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/products")
def products():
    # collections =[ 'men', 'women', 'kids']
    return render_template("products.html", collections = PRODUCTS)

@app.route("/products/<int:product_id>")
def product_detail(product_id):

    select_product = None

    for product in PRODUCTS:
        if product['id'] == product_id:
            select_product = product
            break

    if select_product == None:
        abort(404)

    return render_template("product_detail.html", product = select_product )

@app.route('/cart')
def cart():
    product_id = request.args.get('product_id', type=int)
    quantity = request.args.get('quantity', default=1, type=int)

    total_price = 0
    
    # global total_item
    # global subtotal
    # global total_price

    if product_id:
        for item in PRODUCTS:
            if item["id"]==product_id:
                subtotal = int(item['price']) * quantity

                if is_item_in_cart(product_id)[0]== False:
                    cart_items.append({'id': item['id'],
                                       'name': item['name'],
                                       'price': item['price'],
                                       'image': item['image'],
                                       'quantity': quantity,
                                       'sub_total': subtotal})
                else:
                    index = is_item_in_cart(product_id)[1]
                    cart_items[index]['quantity'] = quantity
                        
                # cart_items.append(item)
                # total_item = quantity
                break
    total_price += subtotal

    return render_template("cart.html", cart= cart_items, total_price= total_price )

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
