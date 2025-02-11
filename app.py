from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to My Flask App</h1><p>My name is Adnan Shaikh</p>"

if __name__ == '__main__':
    app.run(debug=True)
