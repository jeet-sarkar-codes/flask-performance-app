from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Jeet’s Performance API"

@app.route('/hello')
def hello():
    return "Hello from Jeet!"

if __name__ == '__main__':
    app.run(debug=True)