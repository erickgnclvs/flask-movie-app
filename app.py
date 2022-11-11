from flask import Flask, render_template, redirect, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from helpers import login_required
from werkzeug.security import check_password_hash, generate_password_hash
import tmdbsimple as tmdb


# TODO:
# Finish writing app.py
# Style the page with Bootstrap


# Start Flask
app = Flask(__name__)

# Make sure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'fi2o42j3o4ij234o23jjj234jklh'
db = SQLAlchemy(app)

# Set database
# Create users table
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    hash = db.Column(db.String(128))

    def set_password(self, password):
        self.hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hash, password)

# Create favorites table
class Favorites(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer)

# Create database
with app.app_context():
    db.create_all()


# Connect TMDB API 
tmdb.API_KEY = 'b0c85929904b01fc66d943266877e630'

# Set timeout for requests
# 5 seconds, for both connect and read
tmdb.REQUESTS_TIMEOUT = 5


@app.route('/')
def index():
    # This will redirect the user to HOME
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
    # This display the favorites list
    # TODO:


    return render_template('favorites.html')

@app.route('/add', methods=['POST', 'GET'])
@login_required
def add():
    # This will add a movie to the the favorites list
    # Grab movie id from search results "Add to favorites" button
    id = request.form.get('id')
    print(id)

    # Try searching id on Movies
    try:
        movie = tmdb.Movies(id)
        result = movie.info()
        print(result)
        
    # Try searching id on TV series
    except:
        tv = tmdb.TV(id)
        result = tv.info()
        print(result)

    data = []


    # TODO:
    # Add movie to database

    # Display favorites
    return redirect('/favorites')

@app.route('/delete', methods=['POST', 'GET'])
@login_required
def delete():
    # This will delete a movie from the favorites list
    # TODO:

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
    # This will search for movies and series
    # Search for keyword
    # Iterate through result 
    # Create data with id, title, year, kind, cover
    # Pass data to template

    # Initiate search class from TMDB module
    search = tmdb.Search()

    # Store request in a variable
    query = request.args.get('q')

    # Search for results (stored in search.results)
    search.multi(query=query)

    # Create a list
    data = []

    # Iterate through result
    for movie in search.results:
        
        # If its movie or series
        if movie['media_type'] == 'tv' or movie['media_type'] == 'movie':

            # If there is a poster
            if movie['poster_path'] and movie['poster_path'] != None:

                # If its a movie append information on data list
                if movie['media_type'] == 'movie':
                    data.append({
                        'id' : movie['id'],
                        'cover' : movie['poster_path'],
                        'title' : movie['title'],
                        'kind' : movie['media_type'],
                        'year' : movie['release_date'][0:4]
                    })
                # If its a tv series append information on data list
                if movie['media_type'] == 'tv':
                    data.append({
                        'id' : movie['id'],
                        'cover' : movie['poster_path'],
                        'title' : movie['name'],
                        'kind' : movie['media_type'],
                        'year' : movie['first_air_date'][0:4]
                    })

    # Render index.html passing data
    return render_template('index.html', data=data)

@app.route('/forgotpassword', methods=['POST', 'GET'])
def password():
    # This will reset user's password when forgotten
    # TODO:

    return render_template('sorry.html')

# Regular Python run statement (with debug)
if __name__ == '__main__':
    app.run(debug=True)

