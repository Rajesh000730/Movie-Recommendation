
from flask import Flask, render_template, request, redirect
details= {"title" : " ",
"hero" :  " ",
"heroine" : " ",
"date" :" ",
"duration" : " ",
"genre" : " ",
 "imdb" : " ",
"production":" ",
"url":" ",
"herourl" : " ",
"heroineurl" : " "}
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/movie")
def movie():
    if(details['title'] == " " or details['hero'] == " " or details['heroine'] == " "):
        return render_template('error.html')
    else:    
        return render_template('recommendation.html', title=details['title'], hero=details['hero'], heroine=details['heroine'], date=details['date'], duration=details['duration'],
        genre=details['genre'], imdb=details['imdb'], production=details['production'], url=details['url'], herourl=details['herourl'], heroineurl=details['heroineurl'])

@app.route("/recommendation", methods=["POST"])
def recommend():
    global details
    details['title'] = request.form['title'] 
    details['hero'] = request.form['hero']
    details['heroine'] = request.form['heroine']
    details['date'] = request.form['date']
    details['duration'] = request.form['duration']
    details['genre'] = request.form['genre']
    details['imdb'] = request.form['imdb']
    details['production'] = request.form['production']
    details['url'] = request.form['url']
    details['herourl'] = request.form['herourl']
    details['heroineurl'] = request.form['heroineurl']
    if(details['title'] == " "):
        return "failed"
    else:
        return "success"    

if __name__ == '__main__':
    app.run(debug=True)  
else:   
    print("false")      