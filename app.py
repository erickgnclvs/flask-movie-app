from flask import Flask, render_template, redirect, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from helpers import login_required
from werkzeug.security import check_password_hash, generate_password_hash
from imdb import Cinemagoer

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


# Initiate Cinemagoer
ia = Cinemagoer()


@app.route('/')
def index():
    return redirect('/home')


@app.route('/home')
@login_required
def home():
    # This will render the search form - in tests
    return render_template('index.html')

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
            flash('Please fill all the fields')
            return redirect('/register')
        
        elif password != confirmation:
            flash("Passwords don't match!")
            return redirect('/register')
        
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
                session['user'] = user.id
                flash("You have succesfully registered!")
                return redirect('/home')

            # If it fails...
            except:
                flash('Username already exists :(')
                return redirect('/register')

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
            flash('Please fill all the fileds')
            return redirect('/login')

        # Fetch user data from database
        user = Users.query.filter_by(username=username).first()

        # Check password
        if user.check_password(password):
            session['user'] = user.id

###################### This part I'm changing, tryin to implement flash messages
###################### Also changed layout.html
###################### Trying to implement flash messages
###################### It has worked wonders

            flash("You are successfuly logged in!")  
            return redirect('/home')      
        
        # If passwords don't match
        else:
            flash('Wrong password')
            return redirect('/login')

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
@login_required
def changepassword():
    # This will change the users password
    if request.method == "POST":
        password = request.form.get('password')
        newpassword = request.form.get('newpassword')
        confirmation = request.form.get('confirmation')

        # Check for errors
        if not password or not newpassword or not confirmation:
            flash('Please fill all spaces')
            return redirect('/changepassword')

        elif newpassword != confirmation:
            flash("Passwords don't match")
            return redirect('/changepassword')

        else:
            # Fetch user data from database to check password
            user_id = session['user']
            user = Users.query.filter_by(id=user_id).first()
            
            # Check if password is correct
            if user.check_password(password):

        #############################################################################
        ####### This part is deleting the password from db and not updating #########
        #############################################################################

        ####### Fixed it ############################################################ 
              
                # Try to insert into database
                try:
                    hash = generate_password_hash(newpassword)
                    Users.query.filter_by(id=user_id).update(dict(hash=hash))
                    db.session.commit()
                    flash('Password updated')
                    return redirect('/changepassword')
                
                # If it fails...
                except:
                    flash('There was an error trying to change your password :(')
                    return redirect('/changepassword')

            # If wrong password
            else:
                flash('Wrong password')
                return redirect('/changepassword')

    # This will render the change password form
    else:
        return render_template('changepassword.html')


@app.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    # This will clear the user session
    try:
        session.clear()
        flash("You have logged out")
        return redirect('/')
    
    # If it fails there is a message
    except:
        flash("Some error have ocurred")
        return redirect('/')

@app.route('/search')
@login_required
def search():
    # This will search for movies - in tests
    # Search for keyword
    # Grab movie ids 
    # Create data with id, title, year, type, cover url
    # Pass data to template
    

    q = request.args.get('q')
    result = ia.search_movie(q)

    data = []

    for movie in result:
        if movie['kind'] == 'movie' or movie['kind'] == 'tv series' and movie['full-size cover url'] and movie['full-size cover url'] != "https://m.media-amazon.png":
            data.append({
                    'id': movie.getID(),
                    'cover': movie['full-size cover url'],
                    'title': movie['title'],
                    'kind': movie['kind'],
                    'year':  movie.get('year', ''),
                    })
    
    
    # Print data for console checking
    print(data)
    return render_template('index.html', data=data)


@app.route('/forgotpassword', methods=['POST', 'GET'])
def password():
    return render_template('sorry.html')


# Regular Python run statement (with debug)
if __name__ == '__main__':
    app.run(debug=True)

