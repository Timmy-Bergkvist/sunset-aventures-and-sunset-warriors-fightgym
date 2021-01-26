from flask import Blueprint
from flask import Flask, render_template, redirect, url_for, request

sunsetWarriors = Blueprint("sunsetWarriors", __name__, static_folder="static", template_folder="templates")

@sunsetWarriors.route("/home")
def home():
    return render_template("SW-Home.html")


@sunsetWarriors.route("/about")
def about():
    return render_template("SW-About.html")


@sunsetWarriors.route("/contact")
def contact():
    return render_template("SW-Contact.html")


@sunsetWarriors.route("/gallery")
def gallery():
    return render_template("SW-Gallery.html")


@sunsetWarriors.route("/training")
def training():
    return render_template("SW-Training.html")

