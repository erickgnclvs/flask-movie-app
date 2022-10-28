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

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'fi2o42j3o4ij234o23jjj234jklh'
db = SQLAlchemy(app)

# Set database
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    hash = db.Column(db.String(128))

    def set_password(self, password):
        self.hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hash, password)


# Create database
with app.app_context():
    db.create_all()

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route('/')
def index():
    return redirect('/home')


@app.route('/home', methods=['POST', 'GET'])
@login_required
def home():
    return render_template('about.html')

@app.route('/about', methods=['GET'])
def about():
    # This displays what the project is going to be and my Instagram and GitHub
    return render_template('about.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    # This will register the user
    # Thanks https://www.youtube.com/c/MrAmithsChannel for the help!

    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        userdata = Users(
            username = username,
            hash = password,
        )

        userdata.set_password(password)
        db.session.add(userdata)
        db.session.commit()
        return redirect('/')

    # This will render the registration form
    else:
        return render_template('register.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
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

