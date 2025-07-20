from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

print("Before app.run()")   # Debug print

if __name__ == "__main__":
    print("Starting Flask app...")  # Debug print
    app.run(debug=True, port=5002)
    print("App has stopped")  # This only prints after server stops
