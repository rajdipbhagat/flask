from flask import Flask,render_template

app=Flask(__name__)
@app.route('/index')
def index():
    name="Dipak"
    return render_template("template.html",username=name)

if __name__ =="__main__":
    app.run(debug=True)