from flask import Flask, render_template 
from flask_sitemap import Sitemap

app = Flask(
    __name__,
    static_url_path='/static', 
    static_folder='site/static',
    template_folder='site/templates')

app.config['SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS'] = True

sitemap = Sitemap(app=app)


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

@app.route("/robots.txt")
def robots():
    return app.send_static_file('robots.txt')
