from app import app

@app.route("/")
def index():
    return "<h1>Welcome to SQA Practice!</h1>"

@app.route("/module-details")
def module_details():
    return "<h1>Module Details</h1>"