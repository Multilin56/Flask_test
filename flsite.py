from flask import Flask, render_template, make_response

app = Flask(__name__)

menu = [{"title": "Главная", "url": "/"},
        {"title": "Добавить статью", "url": "/add_post"}]

@app.route("/")
def index():
    # content = render_template('index.html', menu=menu, posts=[])
    # res = make_response(content)
    # res.headers['Content-Type'] = 'text/plain'
    # res.headers['Server'] = 'flasksite'
    # return res

    img = None
    with app.open_resource( app.root_path + "/static/images/ava.png", mode="rb") as f:
        img = f.read()

    if img is None:
        return "None image"

    res = make_response(img)
    res.headers['Content_Type'] = 'image/png'
    return res
 

if __name__ == '__main__':
    app.run(debug=True)