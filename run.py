import os
from flask import Flask, render_template, redirect, url_for, request

from flask_assets import Environment, Bundle
from utility.assets import bundles

from sunsetAdventures.routes import sunsetAdventures
from sunsetWarriors.routes import sunsetWarriors

from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)
assets = Environment(app)
assets.register(bundles)

app.register_blueprint(sunsetAdventures, url_prefix="/sunsetAdventures")
app.register_blueprint(sunsetWarriors, url_prefix="/sunsetWarriors")

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)