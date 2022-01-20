from market import app, select, insert
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



from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
app.config['SECRET_KEY'] = 'secretkey'

class WstawZwierze(FlaskForm):
    IDENTYFIKATOR_ZWIERZECIA = IntegerField(label="Podaj identyfikator zwierzęcia", 
                                           description="Tutaj wpisz swoją wartość!",
                                           validators=[DataRequired()]
                                           )
    PORA_KARMIENIA = StringField(label="Podaj porę karmienia zwierzęcia", 
                                           description="Tutaj wpisz swoją wartość!",
                                           validators=[DataRequired(), Length(min=1, max=20, message="Wymagana dlugosc to przedzial od 1 do 20 znakow.")]
                                           )
    ILOSC_KARMY = FloatField(label="Podaj ilość karmy dla zwierzęcia", 
                                           description="Tutaj wpisz swoją wartość!",
                                           validators=[DataRequired()]
                                           )
    WIEK = IntegerField(label="Podaj wiek zwierzęcia", 
                                           description="Tutaj wpisz swoją wartość!",
                                           validators=[DataRequired(), NumberRange(min=1, message="Ta wartosc musi byc wieksza niz 0")]
                                           )
    IMIE = StringField(label="Podaj imie zwierzęcia", 
                                           description="Tutaj wpisz swoją wartość!",
                                           validators=[DataRequired(), Length(min=1, max=50)]
                                           )                                    
    WLASCICIEL = StringField(label="Podaj imie wlasciciela zwierzęcia", 
                                           description="Tutaj wpisz swoją wartość!",
                                           validators=[DataRequired(), Length(min=1, max=50)]
                                           )   
    KARMA = StringField(label="Podaj nazwe karmy zwierzęcia", 
                                           description="Tutaj wpisz swoją wartość!",
                                           validators=[DataRequired(), Length(min=1, max=50)]
                                           )                                          
    GATUNEK = StringField(label="Podaj gatunek zwierzęcia", 
                                           description="Tutaj wpisz swoją wartość!",
                                           validators=[DataRequired(), Length(min=1, max=50)]
                                           )
    RODZINA = StringField(label="Podaj rodzine zwierzęcia", 
                                           description="Tutaj wpisz swoją wartość!",
                                           validators=[DataRequired(), Length(min=1, max=50)]
                                           )                                      
    GROMADA = StringField(label="Podaj gromade zwierzęcia", 
                                           description="Tutaj wpisz swoją wartość!",
                                           validators=[DataRequired(), Length(min=1, max=50)]
                                           )
    AZYL = IntegerField(label="Podaj azyl zwierzęcia", 
                                           description="Tutaj wpisz swoją wartość!",
                                           validators=[DataRequired(), NumberRange(min=1, message="Ta wartosc musi byc wieksza niz 0")]
                                           )                                      
    submit = SubmitField("Dodaj zwierze do zoo")

@app.route('/dodawanie_danych/formularz_zwierzecia', methods = ['GET', 'POST'])
def insert_zwierze_page():
    if request.method == 'GET':
        IDENTYFIKATOR_ZWIERZECIA = None
        PORA_KARMIENIA = None
        ILOSC_KARMY = None
        WIEK = None
        IMIE = None
        WLASCICIEL = None
        KARMA = None
        GATUNEK = None
        RODZINA = None
        GROMADA = None
        AZYL = None

        form = WstawZwierze()

        if form.validate_on_submit():
            IDENTYFIKATOR_ZWIERZECIA = form.IDENTYFIKATOR_ZWIERZECIA.data
            PORA_KARMIENIA = form.PORA_KARMIENIA.data
            ILOSC_KARMY = form.ILOSC_KARMY.data
            WIEK = form.WIEK.data
            IMIE = form.IMIE.data
            WLASCICIEL = form.WLASCICIEL.data
            KARMA = form.KARMA.data
            GATUNEK = form.GATUNEK.data
            RODZINA = form.RODZINA.data
            GROMADA = form.GROMADA.data
            AZYL = form.AZYL.data

            # insert.insert_into_oracle('ZWIERZETA', 
            # [
            #     "IDENTYFIKATOR_ZWIERZECIA",
            #     "PORA_KARMIENIA",
            #     "ILOSC_KARMY",
            #     "WIEK",
            #     "IMIE",
            #     "WLASCICIEL",
            #     "KARMA",
            #     "GATUNEK",
            #     "RODZINA",
            #     "GROMADA",
            #     "AZYL"
            # ], 
            # [
            #     IDENTYFIKATOR_ZWIERZECIA,
            #     PORA_KARMIENIA,
            #     ILOSC_KARMY,
            #     WIEK,
            #     IMIE,
            #     WLASCICIEL,
            #     KARMA,
            #     GATUNEK,
            #     RODZINA,
            #     GROMADA,
            #     AZYL
            # ] 
            # )


            form.IDENTYFIKATOR_ZWIERZECIA.data = ""
            form.PORA_KARMIENIA.data = ""
            form.ILOSC_KARMY.data = ""
            form.WIEK.data = ""
            form.IMIE.data = ""
            form.WLASCICIEL.data = ""
            form.KARMA.data = ""
            form.GATUNEK.data = ""
            form.RODZINA.data = ""
            form.GROMADA.data = ""
            form.AZYL.data = ""
            
        return render_template('Podstrony/Formularze/f_zwierze.html',
                                IDENTYFIKATOR_ZWIERZECIA = IDENTYFIKATOR_ZWIERZECIA,
                                PORA_KARMIENIA = PORA_KARMIENIA,
                                ILOSC_KARMY = ILOSC_KARMY,
                                WIEK = WIEK,
                                IMIE = IMIE,
                                WLASCICIEL = WLASCICIEL,
                                KARMA = KARMA,
                                GATUNEK = GATUNEK,
                                RODZINA = RODZINA,
                                GROMADA = GROMADA,
                                AZYL = AZYL,
                                form = form
                                )

    return redirect(url_for('insert_zwierze_page'))





# @app.route('/insert', methods=["POST", "GET"])
# def insertion():
#     if request.method == 'POST':
#         form = request.form
#         identyfikator_zwierzecia = int(form['identyfikator_zwierzecia'])
#         pora_karmienia = str(form['pora_karmienia'])
#         ilosc_karmy = float(form['ilosc_karmy'])
#         wiek = int(form['wiek'])
#         imie = str(form['imie'])
#         wlasciciel = str(form['wlasciciel'])
#         karma = str(form['karma'])
#         gatunek = str(form['gatunek'])
#         rodzina = str(form['rodzina'])
#         gromada = str(form['gromada'])
#         azyl = int(form['azyl'])

#         print(  "Wstawiam do: ZWIERZETA",
#                 identyfikator_zwierzecia,
#                 pora_karmienia,
#                 ilosc_karmy,
#                 wiek,
#                 imie,
#                 wlasciciel,
#                 karma,
#                 gatunek,
#                 rodzina,
#                 gromada,
#                 azyl)
        
#         insert.insert_into_oracle('ZWIERZETA', 
#         [
#             'identyfikator_zwierzecia', 
#             'pora_karmienia', 
#             'ilosc_karmy', 
#             'wiek', 
#             'imie', 
#             'wlasciciel',
#             'karma',
#             'gatunek',
#             'rodzina',
#             'gromada',
#             'azyl'
#         ], 
#         [
#             identyfikator_zwierzecia,
#             pora_karmienia,
#             ilosc_karmy,
#             wiek,
#             imie,
#             wlasciciel,
#             karma,
#             gatunek,
#             rodzina,
#             gromada,
#             azyl
#         ] 
#     )

#         return render_template('Podstrony/Formularze/f_zwierze.html')
    
#     return redirect('Podstrony/Formularze/f_zwierze.html')


@app.route('/dodawanie_danych/formularz_typu_azylu')
def insert_typ_azylu_page():
    return render_template('Podstrony/Formularze/f_typ_azylu.html')

@app.route('/dodawanie_danych/formularz_typu_pracownika')
def insert_typ_prac_page():
    return render_template('Podstrony/Formularze/f_typ_prac.html')




# PODSTRONY PRZEGLĄDANIA DANYCH
# 10.01.2022 TOMASZ P.
@app.route('/przegladanie_danych/przegladanie_zaawansowane')
def select_advanced_page():
    nazwa_tabeli_do_wyswietlenia = request.args.get('tabela', default='brak', type=str)
    if nazwa_tabeli_do_wyswietlenia != 'brak':
        dane_tabeli_do_wyswietlenia = select.select_simple(f"SELECT * FROM {nazwa_tabeli_do_wyswietlenia.upper()}")
        naglowki_tabeli_do_wyswietlenia = select.select_simple(f"SELECT COLUMN_NAME FROM USER_TAB_COLUMNS WHERE TABLE_NAME = '{nazwa_tabeli_do_wyswietlenia.upper()}'")
        if dane_tabeli_do_wyswietlenia == [] or dane_tabeli_do_wyswietlenia == "BRAK DANYCH":
            dane_tabeli_do_wyswietlenia = [["--" for i in range(len(naglowki_tabeli_do_wyswietlenia))]]
        naglowki_tabeli_do_wyswietlenia = [i[0] for i in naglowki_tabeli_do_wyswietlenia]
        return render_template('Podstrony/Przegladanie/zaawansowane.html', headings=naglowki_tabeli_do_wyswietlenia, data=dane_tabeli_do_wyswietlenia)
    else:
        return render_template('Podstrony/Przegladanie/zaawansowane.html', headings=[], data=[])

# 10.01.2022 TOMASZ P.
@app.route('/przegladanie_danych/przegladanie_podstawowe')
def select_basic_page():
    nazwa_tabeli_do_wyswietlenia = request.args.get('tabela', default='brak', type=str)
    if nazwa_tabeli_do_wyswietlenia != 'brak':
        dane_tabeli_do_wyswietlenia = select.select_simple(f"SELECT * FROM {nazwa_tabeli_do_wyswietlenia.upper()}")
        naglowki_tabeli_do_wyswietlenia = select.select_simple(f"SELECT COLUMN_NAME FROM USER_TAB_COLUMNS WHERE TABLE_NAME = '{nazwa_tabeli_do_wyswietlenia.upper()}'")
        if dane_tabeli_do_wyswietlenia == [] or dane_tabeli_do_wyswietlenia == "BRAK DANYCH":
            dane_tabeli_do_wyswietlenia = [["--" for i in range(len(naglowki_tabeli_do_wyswietlenia))]]
        naglowki_tabeli_do_wyswietlenia = [i[0] for i in naglowki_tabeli_do_wyswietlenia]
        return render_template('Podstrony/Przegladanie/podstawowe.html', headings=naglowki_tabeli_do_wyswietlenia, data=dane_tabeli_do_wyswietlenia)
    else:
        return render_template('Podstrony/Przegladanie/podstawowe.html', headings=[], data=[])





# PODSTRONY USUWANIA DANYCH
@app.route('/usuwanie_danych/usuwanie_zwierzat')
def delete_zwierze_page():
    return render_template('Podstrony/Usuwanie/usun_zwierzeta.html')

