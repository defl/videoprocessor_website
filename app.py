from flask import Flask, render_template

app = Flask(
    __name__,
    static_url_path='/static', 
    static_folder='site/static',
    template_folder='site/templates')


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/faq")
def faq():
    return render_template('faq.html')

@app.route("/getting_started")
def getting_started():
    return render_template('getting_started.html')

@app.route("/manual")
def manual():
    return render_template('manual.html')

@app.route("/debugging")
def debugging():
    return render_template('debugging.html')

@app.route("/commercial_video_processors")
def commercial_video_processors():
    return render_template('commercial_video_processors.html')
