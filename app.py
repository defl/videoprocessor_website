from flask import Flask, render_template

app = Flask(
    __name__,
    static_url_path='/static', 
    static_folder='site/static',
    template_folder='site/templates')


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/getting_started")
def getting_started():
    return render_template('getting_started.html')

@app.route("/commercial_alternatives")
def commercial_alternatives():
    return render_template('commercial_alternatives.html')
