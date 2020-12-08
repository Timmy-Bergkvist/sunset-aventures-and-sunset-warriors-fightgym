from flask import Blueprint
from flask import Flask, render_template, redirect, url_for, request

sunsetWariorrs = Blueprint("sunsetWariorrs", __name__, static_folder="static", template_folder="templates")

@sunsetWariorrs.route("/home")
def home():
    return render_template("SW-Home.html")


@sunsetWariorrs.route("/about")
def about():
    return render_template("SW-About.html")


@sunsetWariorrs.route("/contact")
def contact():
    return render_template("SW-Contact.html")


@sunsetWariorrs.route("/gallery")
def gallery():
    return render_template("SW-Gallery.html")


@sunsetWariorrs.route("/training")
def training():
    return render_template("SW-Training.html")

