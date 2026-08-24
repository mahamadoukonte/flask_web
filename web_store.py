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


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/products")
def products():
    # collections =[ 'men', 'women', 'kids']
    return render_template("products.html", collections = PRODUCTS)


@app.route("/products/<int:product_id>", methods=['GET', 'POST'])
def product_detail(product_id):
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if product is None:
        abort(404)
        
    if request.method == 'POST':
        # Retrieve form data submitted from product_detail.html
        quantity = request.form.get('quantity', 1)
        
        # Cart handling logic goes here (e.g., storing in flask session)
        print(f"Added product ID {product_id} with quantity {quantity} to cart.")
        
        # Redirect after POST to prevent accidental duplicate submissions on page refresh
        return redirect(url_for('products'))

    return render_template("product_detail.html", product=product)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)