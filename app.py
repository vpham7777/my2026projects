from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# MUST have exactly these 3 products with these specific IDs for your tests to pass!
PRODUCTS = [
    {
        "id": 101,
        "name": "Developer Coffee Mug",
        "price": 15.00,
        "stock": "In Stock",
    },
    {
        "id": 102,
        "name": "Mechanical Keyboard",
        "price": 89.99,
        "stock": "Low Stock",
    },
    {
        "id": 103,
        "name": "Python Sticker Pack",
        "price": 4.50,
        "stock": "Out of Stock",
    },
]


@app.route("/")
def home():
  return render_template("index.html", products=PRODUCTS)


@app.route("/login", methods=["POST"])
def login():
  username = request.form.get("username")
  password = request.form.get("password")

  if username == "admin" and password == "admin123":
    return "<h1>Welcome, Admin!</h1><p id='status'>Success</p>"
  return "<h1>Invalid Credentials</h1><p id='status'>Failed</p>"


if __name__ == "__main__":
  app.run(port=5000)
