from flask import Flask, render_template, redirect, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from helpers import login_required
from werkzeug.security import check_password_hash, generate_password_hash


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
database = SQLAlchemy(app)


@app.route('/')
def index():
    return redirect('/home')


@app.route('/home', methods=['POST', 'GET'])
@login_required
def home():
    return render_template('about.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    return render_template('sorry.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return render_template('error.html')

        # Ensure password was submitted
        elif not request.form.get("password"):
            return render_template('error.html')

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return render_template('error.html')

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route('/favorites', methods=['POST', 'GET'])
@login_required
def favorites():
    return render_template('sorry.html')


@app.route('/add', methods=['POST', 'GET'])
@login_required
def add():
    return render_template('sorry.html')


@app.route('/delete', methods=['POST', 'GET'])
@login_required
def delete():
    return render_template('sorry.html')


@app.route('/changepassword', methods=['POST', 'GET'])
@login_required
def changepassword():
    return render_template('sorry.html')


@app.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    return render_template('sorry.html')


@app.route('/search', methods=['POST', 'GET'])
@login_required
def search():
    return render_template('sorry.html')


@app.route('/forgotpassword', methods=['POST', 'GET'])
def password():
    return render_template('sorry.html')


if __name__ == '__main__':
    app.run(debug=True)

