from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask on Kubernetes! Deployed by Karthik N H (USN: 1BM23IS122)"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=15000)
