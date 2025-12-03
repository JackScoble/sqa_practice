from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/module-details")
def module_details():
    return "<h1>Module Details</h1>"