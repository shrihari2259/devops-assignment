from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from CI/CD"

@app.route("/health")
def health():
    return "ok"