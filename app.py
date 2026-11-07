from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Shrihari"

@app.route("/health")
def health():
    return "ok"
