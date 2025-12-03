from app import app
from flask import render_template, request, redirect, url_for

accounts = [
    {"username": "user1", "email": "user1@example.com", "password": "pass1"},
    {"username": "user2", "email": "user2@example.com", "password": "pass2"}
]

@app.route("/")
def index(username=None):
    return render_template("index.html")

@app.route("/module-details")
def module_details():
    return render_template("module_details.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email_or_username = request.form["email_or_username"]
        password = request.form["password"]
        for account in accounts:
            if (account["username"] == email_or_username or account["email"] == email_or_username) and account["password"] == password:
                return redirect(url_for("index", username=account["username"]))
        return "Invalid credentials. Please try again."
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        if any(acc["username"] == username for acc in accounts):
            return "Username already exists. Please choose a different one."
        accounts.append({"username": username, "email": email, "password": password})
        return redirect(url_for("index", username=username))
    return render_template("register.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")