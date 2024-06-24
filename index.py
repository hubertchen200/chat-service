from api import create_app
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

# app = create_app()

@app.route('/health')
def health():
    return "I am good."

# if __name__ == '__main__':
#     app.run(debug=True, port=8081, host='0.0.0.0')


# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return 'Hello, World!'

# @app.route('/about')
# def about():
#     return 'About'