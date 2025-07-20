print("Test script started")

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, world!"

if __name__ == "__main__":
    print("Starting minimal Flask server on port 5001")
    app.run(debug=True, port=5001)
    print("Minimal Flask server stopped")
