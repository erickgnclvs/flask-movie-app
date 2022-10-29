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

# Clear all sessions

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
        confirmation = request.form.get('confirmation')

        # Check for errors
        if not username or not password or not confirmation:
            print('please fill all spaces')
            return render_template('error.html')
        
        elif password != confirmation:
            print('passwords dont match')
            return render_template('error.html')
        
        # If no errors then register
        else:

            # Try to register
            try:
                user = Users(
                    username = username,
                    hash = password,
                )

                user.set_password(password)
                db.session.add(user)
                db.session.commit()
                return redirect('/')

            # If it fails...
            except:
                print('couldnt insert into database')
                return render_template('error.html')

    # This will render the registration form
    else:
        return render_template('register.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    # This will log the user in
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Handle errors
        if not username or not password:
            print('please fill all spaces')
            return render_template('error.html')

        # Fetch user data from database
        user = Users.query.filter_by(username=username).first()

        # Check password
        if user.check_password(password):
            session['user'] = user.id
            return redirect('/')    
        
        # If passwords don't match
        else:
            print('wrong password')
            return 'error'

    # This will render the login form
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
#@login_required
def changepassword():
    # This will change the users password
    if request.method == "POST":
        password = request.form.get('password')
        newpassword = request.form.get('newpassword')
        confirmation = request.form.get('confirmation')

        # Check for errors
        if not password or not newpassword or not confirmation:
            print('please fill all spaces')
            return render_template('error.html')

        elif newpassword != confirmation:
            print('passwords dont match')
            return render_template('error.html')

        else:
            # Fetch user data from database
            user_id = session['user']
            user = Users.query.filter_by(id=user_id).first()
            
            # Check password
            if user.check_password(password):
                
                # Try to insert into database
                try:
                    #user = Users(
                    #    hash = password,
                    #)

                    user.hash = user.set_password(password)
                    #db.session.update(user)
                    db.session.commit()
                    return "succes"#redirect('/')

                # If it fails...
                except:
                    print('couldnt insert into database')
                    return render_template('error.html')

            # If wrong password
            else:
                print('wrong password')
                return redirect('/')

    # This will render the change password form
    else:
        return render_template('changepassword.html')


@app.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    # This will clear the user session
    session.clear()
    return redirect('/')


@app.route('/search', methods=['POST', 'GET'])
@login_required
def search():
    return render_template('sorry.html')


@app.route('/forgotpassword', methods=['POST', 'GET'])
def password():
    return render_template('sorry.html')


if __name__ == '__main__':
    app.run(debug=True)

