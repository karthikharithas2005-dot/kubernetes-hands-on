from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Jenkins Multi-Stage Pipeline! Engineered by Karthik N H (1BM23IS122)"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
