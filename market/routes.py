from market import app
from flask import render_template, request, url_for, redirect, flash, get_flashed_messages

"""
    Tutaj tworzysz podstrony. Pliki HTML muszą znajdować się w folderze market/templates, żeby działały
    Pliki CSS są w folderze /market/static, ale ich ścieżkę i tak definiujesz w sekcji <head> w pliku HTML.
"""


# STRONA GŁÓWNA
@app.route('/')
def root_page():
    return render_template('index.html')



# STRONY PODSTAWOWE
@app.route('/usuwanie_danych')
def delete_choose_page():
    return render_template('Podstrony/usun.html')

@app.route('/przegladanie_danych')
def select_choose_page():
    return render_template('Podstrony/przegladaj.html')

@app.route('/edycja_danych')
def update_choose_page():
    return render_template('Podstrony/edytuj.html')

@app.route('/dodawanie_danych')
def insert_choose_page():
    return render_template('Podstrony/dodaj.html')



# PODSTRONY EDYCJI DANYCH
@app.route('/edytowanie_danych/edycja_azylu')
def update_azyl_page():
    return render_template('Podstrony/Edycja/edycja_azyl.html')

@app.route('/edytowanie_danych/edycja_biletu')
def update_bilet_page():
    return render_template('Podstrony/Edycja/edycja_bilet.html')

@app.route('/edytowanie_danych/edycja_gatunku')
def update_gatunek_page():
    return render_template('Podstrony/Edycja/edycja_gatunek.html')

@app.route('/edytowanie_danych/edycja_gromady')
def update_gromada_page():
    return render_template('Podstrony/Edycja/edycja_gromada.html')

@app.route('/edytowanie_danych/edycja_karmy')
def update_karma_page():
    return render_template('Podstrony/Edycja/edycja_karma.html')

@app.route('/edytowanie_danych/edycja_pawilonu')
def update_pawilon_page():
    return render_template('Podstrony/Edycja/edycja_pawilon.html')

@app.route('/edytowanie_danych/edycja_pracwonika')
def update_pracownik_page():
    return render_template('Podstrony/Edycja/edycja_pracownik.html')

@app.route('/edytowanie_danych/edycja_rodziny')
def update_rodzina_page():
    return render_template('Podstrony/Edycja/edycja_rodzina.html')

@app.route('/edytowanie_danych/edycja_zespolu')
def update_zespol_page():
    return render_template('Podstrony/Edycja/edycja_zespol.html')

@app.route('/edytowanie_danych/edycja_zwierzecia')
def update_zwierze_page():
    return render_template('Podstrony/Edycja/edycja_zwierze.html')

@app.route('/dodawanie_danych/edycja_typu_azylu')
def update_typ_azylu_page():
    return render_template('Podstrony/Edycja/edycja_typ_azylu.html')

@app.route('/dodawanie_danych/edycja_typu_pracownika')
def update_typ_prac_page():
    return render_template('Podstrony/Edycja/edycja_typ_prac.html')


