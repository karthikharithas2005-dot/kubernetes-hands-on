from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is a secure Flask application running inside a Docker container! Configured by Karthik N H (1BM23IS122)"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
