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

@app.route("/register", methods=["GET", "POST"])
def register():
    if app.request.method == "POST":
        username = app.request.form["username"]
        email = app.request.form["email"]
        password = app.request.form["password"]
        if any(acc["username"] == username for acc in accounts):
            return "Username already exists. Please choose a different one."
        accounts.append({"username": username, "email": email, "password": password})
        return render_template("index.html", username=username)
    return render_template("register.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")