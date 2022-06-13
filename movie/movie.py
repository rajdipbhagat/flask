from datetime import datetime
from flask import Flask,render_template
import os

#print(os.path)
app=Flask(__name__)

@app.route("/")
def home_page():
    today = datetime.today()
    day_name = today.strftime("%a")
    return render_template("home.html", day = day_name)

@app.route("/movie")
def movie_page():
    return render_template("movie.html") 





if __name__==("__main__"):
    app.run(debug=True)

