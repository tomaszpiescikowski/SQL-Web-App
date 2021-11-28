from market import app
from flask import render_template, request, url_for, redirect, flash, get_flashed_messages

"""
    Tutaj tworzysz podstrony. Pliki HTML muszą znajdować się w folderze market/templates, żeby działały
    Pliki CSS są w folderze /market/static, ale ich ścieżkę i tak definiujesz w sekcji <head> w pliku HTML.
"""


@app.route('/')
def root_page():
    return render_template('index.html')

@app.route('/strona_leny')
def lena_page():
    return render_template('lena.html')
