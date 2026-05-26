from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# ---------- Config ----------
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cart.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# ---------- Cart Model ----------
class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Create DB
with app.app_context():
    db.create_all()

# ---------- View Cart ----------
@app.route("/cart", methods=["GET"])
def view_cart():
    items = CartItem.query.all()

    return jsonify([
        {
            "id": item.id,
            "product_name": item.product_name,
            "quantity": item.quantity
        }
        for item in items
    ])

# ---------- Add to Cart ----------
@app.route("/cart", methods=["POST"])
def add_to_cart():
    data = request.get_json()

    item = CartItem(
        product_name=data["product_name"],
        quantity=data["quantity"]
    )

    db.session.add(item)
    db.session.commit()

    return jsonify({
        "message": "Item added to cart"
    })

# ---------- Remove from Cart ----------
@app.route("/cart/<int:item_id>", methods=["DELETE"])
def remove_item(item_id):
    item = CartItem.query.get(item_id)

    if item:
        db.session.delete(item)
        db.session.commit()

        return jsonify({
            "message": "Item removed"
        })

    return jsonify({
        "message": "Item not found"
    }), 404

# ---------- Clear Cart ----------
@app.route("/cart/clear", methods=["DELETE"])
def clear_cart():
    CartItem.query.delete()
    db.session.commit()

    return jsonify({
        "message": "Cart cleared"
    })

# ---------- Run ----------
if __name__ == "__main__":
    app.run(debug=True)
