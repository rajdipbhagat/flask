from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "This is Home-Page"

@app.route("/register")
def register():
    return "This is register Page"

@app.route("/login")
def login():
    return "This is login Page"

if __name__ == "__main__":
    app.run(debug=True)