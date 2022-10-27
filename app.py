from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

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

