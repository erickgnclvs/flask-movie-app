# Flask Movie App

Flask Movie App is a simple movie search application built using Flask and the TMDB API. It allows users to search for movies and series by title and displays information such as the titles's release year, genre and plot. The app also allows users to register, login, change password, and add or remove movies/series from their favorites list.

This project was created as a final project for the Harvard CS50 course. You can view a video demo of the project:

[![MY VIDEO SNAPSHOT](https://img.youtube.com/vi/wilkhNr_CL0/0.jpg)](https://www.youtube.com/watch?v=wilkhNr_CL0)

## Installation

To install the dependencies, run:

```bash
pip install -r requirements.txt
```
## Usage
To start the application, run:

```bash
python app.py
```

This will start the Flask development server. You can then access the application by navigating to http://localhost:5000 in your web browser.

## Dependencies
Flask Movie App requires the following dependencies:

- Flask==2.2.2
- Flask-Session==0.4.0
- Flask-SQLAlchemy==3.0.2
- Jinja2==3.1.2
- MarkupSafe==2.1.1
- requests==2.28.1
- SQLAlchemy==1.4.42
- tmdbsimple==2.9.1
- Werkzeug==2.2.2

These dependencies are listed in the *requirements.txt* file and can be installed using *pip*.

## User Functions
Flask Movie App offers the following functions to users:

- Register: Users can register for an account to use the app.
- Login: Users can log in to their account.
- Change Password: Users can change their password after logging in.
- Search Movies: Users can search for movies by title using the search bar on the home page.
- Add to Favorites: Users can add movies to their favorites list by clicking on the heart icon.
- Remove from Favorites: Users can remove movies from their favorites list by clicking on the red heart icon.

## App structure:

/home   /register   /login 
/forgotpassword   /changepassword
/search   /favorites    /add 
/delete    /logout  


## PSEUDOCODE

This is how I started developing it.

<br>

initiate frameworks<br>
initiate api - tmdbsimple<br>
initiate database - sqlalchemy<br>
initiate session - flask session<br>
<br>

**/home** - display a search box redirecting users to /search<br>
if user is logged in:<br>
&emsp;/home<br>
else:<br>
&emsp;/login<br>
&emsp;if user has signed up:<br>
&emsp;&emsp;/home<br>
&emsp;else:<br>
&emsp;&emsp;/register<br>
<br>        
        
**/register** - display a form for registering<br>
form with name, username, thing you love most(secretanswer), password and password confirmation<br>
insert data in database<br>
if succesful:<br>
&emsp;/home<br>
else:<br>
&emsp;error<br>
<br>

**/login** - display a form for loggin in<br>
form with username and password<br>
check database to match data<br>
if succesful:<br>
&emsp;/home<br>
else:<br>
&emsp;error<br>
<br>

**/search** - display the results of the search with a add button redirecting to /add<br>
grab data from forms<br>
search through movies API for terms<br>
if search finds result:<br>
&emsp;display them<br>
else:<br>
&emsp;error<br>
<br>

**/favorites** - display favorites each with a delete button redirecting to /delete<br>
search data from database<br>
if found:<br>
&emsp;display favorites<br>
else:<br>
&emsp;error<br>
<br>

**/add** - add movie to database<br>
grab data from movie brought by /search<br>
try:<br>
&emsp;add data in favorites<br>
&emsp;/favorites<br>
except:<br>
&emsp;error<br>
<br>

**/delete** - delete movie from database<br>
grab data from movie brough by /favorites<br>
try:<br>
&emsp;delete data from favorites<br>
except:<br>
&emsp;error<br>
<br>

**/changepassword** - in navbar user will have a button that redirects here<br>
display a form asking for old password, newpassword and newpassword confirmation<br>
if data match database data:<br>
&emsp;success!<br>
&emsp;/home<br>
else:<br>
&emsp;error<br>
<br>

**/logout** - in navbar user will have a button that redirects here<br>
disconnect user<br>
/home<br>
<br>
