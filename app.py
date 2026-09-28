from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///todo.db"
db=SQLAlchemy(app)

class Todo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(300),nullable=True)
    date_created=db.Column(db.DateTime,default=datetime.now())
def __repr__(self):
    return "Task %r>" %self.id



@app.route("/",methods=["POST","GET"])
def index():
    if request.method=="POST":
        task_content=request.form["content"]
        new_task=Todo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"unable to add task {e}"
    else:
        tasks=Todo.query.order_by(Todo.date_created).all()
        return render_template("index.html")


if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)