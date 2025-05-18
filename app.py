from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Docker! This is a Flask app running in a Docker container."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
