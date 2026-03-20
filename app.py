from flask import Flask , request , redirect , url_for , render_template

app = Flask(__name__)

task = []
@app.route("/")
def home():
    return render_template("index.html",tasks = task)

@app.route("/add", methods=["POST"])
def add():
    name = request.form["task"]
    task.append(name)
    return redirect(url_for("home"))

@app.route("/delete/<int:index>")
def delete(index):
    if index < len(task):
        task.pop(index)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)