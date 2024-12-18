import sys
import os

# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from middleware.request_filter import request_filter

from flask import Flask, request


app = Flask(__name__)

@app.before_request
def before_request():
    # Only filter POST requests
    if request.method == "POST":
        if not request_filter(request.form):
            return "Blocked malicious request", 403

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return "POST request received!"
    return "Welcome to the secure app!"

if __name__ == "__main__":
    app.run(debug=True)
