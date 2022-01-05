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




# PODSTRONY DODAWANIA DANYCH
@app.route('/dodawanie_danych/formularz_azylu')
def insert_azyl_page():
    return render_template('Podstrony/Formularze/f_azyl.html')

@app.route('/dodawanie_danych/formularz_biletu')
def insert_bilet_page():
    return render_template('Podstrony/Formularze/f_bilet.html')

@app.route('/dodawanie_danych/formularz_gatunku')
def insert_gatunek_page():
    return render_template('Podstrony/Formularze/f_gatunek.html')

@app.route('/dodawanie_danych/formularz_gromady')
def insert_gromada_page():
    return render_template('Podstrony/Formularze/f_gromada.html')

@app.route('/dodawanie_danych/formularz_karmy')
def insert_karma_page():
    return render_template('Podstrony/Formularze/f_karma.html')

@app.route('/dodawanie_danych/formularz_pawilonu')
def insert_pawilon_page():
    return render_template('Podstrony/Formularze/f_pawilon.html')

@app.route('/dodawanie_danych/formularz_pracwonika')
def insert_pracownik_page():
    return render_template('Podstrony/Formularze/f_pracownik.html')

@app.route('/dodawanie_danych/formularz_rodziny')
def insert_rodzina_page():
    return render_template('Podstrony/Formularze/f_rodzina.html')

@app.route('/dodawanie_danych/formularz_zespolu')
def insert_zespol_page():
    return render_template('Podstrony/Formularze/f_zespol.html')

@app.route('/dodawanie_danych/formularz_zwierzecia')
def insert_zwierze_page():
    return render_template('Podstrony/Formularze/f_zwierze.html')

@app.route('/dodawanie_danych/formularz_typu_azylu')
def insert_typ_azylu_page():
    return render_template('Podstrony/Formularze/f_typ_azylu.html')

@app.route('/dodawanie_danych/formularz_typu_pracownika')
def insert_typ_prac_page():
    return render_template('Podstrony/Formularze/f_typ_prac.html')




# PODSTRONY PRZEGLĄDANIA DANYCH
@app.route('/przegladanie_danych/przegladanie_podstawowe')
def select_advanced_page():
    return render_template('Podstrony/Przegladanie/zaawansowane.html')

@app.route('/przegladanie_danych/przegladanie_zaawansowane')
def select_basic_page():
    return render_template('Podstrony/Przegladanie/podstawowe.html')





# PODSTRONY USUWANIA DANYCH
@app.route('/usuwanie_danych/usuwanie_zwierzat')
def delete_zwierze_page():
    return render_template('Podstrony/Usuwanie/usun_zwierzeta.html')

