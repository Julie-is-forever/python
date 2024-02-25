
from flask import Flask, render_template, redirect, url_for, request
from tabulate import tabulate
app = Flask(__name__)

movies = []

@app.route('/')
def home():
   return render_template('html.html', movies=movies)
 
   
@app.route('/success/<name>')
def success(name):
   movies.append(name)
   print(tabulate(movies))
   return f"{name} is a great movie. Thank you for your answer, the current answers are {movies} \n\n"

@app.route('/data',methods = ['POST'])
def data():
    user = request.form['fmovie']
    return redirect(url_for('success',name = user))



if __name__ == "__main__":
   app.run(debug=True)