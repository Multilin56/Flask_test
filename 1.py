from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', title="Про Flask!")

@app.route("/about")
def about():
    return "<h1> Про Flask </h1>"

if __name__ == '__main__':
    app.run()