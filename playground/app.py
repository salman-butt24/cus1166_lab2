
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/welcome/<string:student_name>")
def welcome(student_name):
    return render_template("welcome.html", student_name = student_name)


@app.route("/roster/<string:grade_view>")
def roster(grade_view):
    class_roster = [("Salman", "A", "Senior"), ("Arbaaz", "B+", "Junior"),
                    ("Shahhan", "B+", "Senior"), ("Mahnoor", "B", "Sophomore"),
                    ("Ramsha", "A", "Sophomore"), ("Ahad", "C+", "Junior"),
                    ("Roha", "C", "Freshman"), ("Palwasha", "C-", "Freshman")]
    return render_template("roster.html", class_roster = class_roster, grade_view = grade_view)


if __name__ == "__main__":
    app.run()
