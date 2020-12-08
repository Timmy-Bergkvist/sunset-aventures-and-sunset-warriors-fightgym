import os
from flask import Flask, render_template, redirect, url_for, request

from sunsetAdventures.routes import sunsetAdventures
from sunsetWariorrs.routes import sunsetWariorrs

app = Flask(__name__)
app.register_blueprint(sunsetAdventures, url_prefix="/sunsetAdventures")
app.register_blueprint(sunsetWariorrs, url_prefix="/sunsetWariorrs")

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)