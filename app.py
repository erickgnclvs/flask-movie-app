from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

# Start Flask
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


@app.route('/')
def index():
    return redirect('/home')


@app.route('/home', methods=['POST', 'GET'])
def home():
    return render_template('about.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    return render_template('sorry.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('sorry.html')


@app.route('/favorites', methods=['POST', 'GET'])
def favorites():
    return render_template('sorry.html')


@app.route('/add', methods=['POST', 'GET'])
def add():
    return render_template('sorry.html')


@app.route('/delete', methods=['POST', 'GET'])
def delete():
    return render_template('sorry.html')


@app.route('/changepassword', methods=['POST', 'GET'])
def changepassword():
    return render_template('sorry.html')


@app.route('/logout', methods=['POST', 'GET'])
def logout():
    return render_template('sorry.html')


@app.route('/search', methods=['POST', 'GET'])
def search():
    return render_template('sorry.html')


@app.route('/forgotpassword', methods=['POST', 'GET'])
def password():
    return render_template('sorry.html')


if __name__ == '__main__':
    app.run(debug=True)

