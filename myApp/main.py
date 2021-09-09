
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
title = " "
hero =  " "
heroine = " "
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/movie")
def movie():
    return render_template('recommendation.html', title=title, hero=hero, heroine=heroine)

@app.route("/recommendation", methods=["POST"])
def recommend():
    global title    
    global hero
    global heroine
    title = request.form['title'] 
    hero = request.form['hero'] 
    heroine = request.form['heroine'] 
    return "success"      
if __name__ == '__main__':
    app.run(debug=True)  
else:   
    print("false")      