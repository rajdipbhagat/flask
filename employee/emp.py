from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///asd.db'
db = SQLAlchemy(app)
db.create_all()

@app.route("/main", method=['GET','POST'])
def check():
    return render_template("emp.html")

class User(db.Model):
    eid=db.Column(db.Integer, primary_key=True)
    ename=db.Column(db.String(80))

    def __repr__(self):
        return '<User %r>' % self.sname


if __name__ == "__main__":
    app.run(debug=True)

