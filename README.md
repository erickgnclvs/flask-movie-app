# This is my CS50 Final Project. 

After 5 months of CS50, I finally started my final project. 

It is going to be a Web Application in which you will be able to select movies and series from a database fed by IMDb API and add them to a favorites list

It will be implemented on Python 3.10.6 with Flask 2.2.2.

App structure:

    /home   /register   /login    /forgotpassword   /changepassword   /search   /favorites    /add    /delete    /logout  

# TODO: Remove cinemagoer and add API

<h2>//PSEUDOCODE</h2>
<br>

initiate frameworks<br>
initiate api<br>
initiate database<br>
initiate session<br>
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

**/forgotpassword** - in login screen user will have a button that redirects here<br>
display a form asking for username and secretanswer (thing you love most)<br>
if data match database data:<br>
&emsp;display a form with newpassword and newpassword confirmation<br>
else:<br>
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
