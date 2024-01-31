
from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('html.html')

   
@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/data',methods = ['POST'])
def data():
    user = request.form['fmovie']
    return redirect(url_for('success',name = user))