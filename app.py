from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/home')

@app.route('/home')
def home():
    return render_template('index.html')


#todo

    

if __name__ == '__main__':
    app.run(debug=True)

