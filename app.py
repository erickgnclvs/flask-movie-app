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
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SECRET_KEY'] = 'fi2o42j3o4ij234o23jjj234jklh'
db = SQLAlchemy(app)

# Create database
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
    return render_template('about.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    return render_template('register.html')
#    # This wil register the user
#
#    # First do get method, to just display the register page
#    if request.method == 'GET':
#        return render_template('register.html')
#
#    # Then do post method, to submit users input
#    else:
#        username = request.form.get('username')
#        password = request.form.get('password')
#        confirmation = request.form.get('confirmation')
#
#        # check for problems
#        if not username or not password or not confirmation:
#            return render_template('error.html')
#
#        if password != confirmation:
#            return render_template('error.html')
#
#        # submit input
#        hash = generate_password_hash(password)
#
#        # check if username not in database
#        #try:
#            #session = 
#        db.engine.execute('INSERT INTO users (username, hash) VALUES (?, ?)', username, hash).execution_options(autocommit=True)
#
#        #except:
#        #    return "cant insert data in db" #render_template('error.html')
#
#
#        #session['user_id'] = session
#
#        return redirect('/')



@app.route('/login', methods=['POST', 'GET'])
def login():
#    """Log user in"""
#
#    # Forget any user_id
#    session.clear()
#
#    # User reached route via POST (as by submitting a form via POST)
#    if request.method == "POST":
#
#        # Declare login variables
#        username = request.form.get('username')
#        password = request.form.get('password')
#
#        # Ensure username was submitted
#        if not username:
#            return 'username was not submited' #render_template('error.html')
#
#        # Ensure password was submitted
#        elif not password:
#            return 'password was not submited' #render_template('error.html')
#
#        # Query database for username
#        userdata = db.engine.execute("SELECT * FROM users WHERE username = ?", username)
#
#        # Ensure username exists and password is correct
#        if len(userdata) != 1 or not check_password_hash(userdata[0]["hash"], password):
#            return 'username doesnt exist or password is incorrect' #render_template('error.html')
#
#        # Remember which user has logged in
#        session["user_id"] = rows[0]["id"]
#
#        # Redirect user to home page
#        return redirect("/")
#
#    # User reached route via GET (as by clicking a link or via redirect)
#    else:
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

