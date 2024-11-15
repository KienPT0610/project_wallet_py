from flask import render_template, request, redirect, url_for

def index():
    return render_template('index.html')