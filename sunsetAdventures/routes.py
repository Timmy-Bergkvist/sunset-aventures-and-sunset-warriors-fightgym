from flask import Blueprint
from flask import Flask, render_template, redirect, url_for, request

sunsetAdventures = Blueprint('sunsetAdventures', __name__, static_folder="static", template_folder="templates")

@sunsetAdventures.route("/home")
def home():
    return render_template("SA-Home.html")


@sunsetAdventures.route("/about")
def about():
    return render_template("SA-About.html")


@sunsetAdventures.route("/contact")
def contact():
    return render_template("SA-Contact.html")


@sunsetAdventures.route("/gallery")
def gallery():
    return render_template("SA-Gallery.html")


@sunsetAdventures.route("/adventures")
def adventures():
    return render_template("SA-Adventures.html")