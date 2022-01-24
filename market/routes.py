from time import sleep
from wsgiref import validate
from market import app, select, insert, delete, update
from flask import render_template, request, url_for, redirect, flash, get_flashed_messages
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from market import delete
app.config['SECRET_KEY'] = 'secretkey'
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


def gatunek_sie_nie_powtarza(form, field):
    NONE_OF_THIS = [str(elem[0]) for elem in select.select_simple('SELECT NAZWA_GATUNKU FROM GATUNKI')]
    if str(field.data) in NONE_OF_THIS:
        raise ValidationError(f'Ten gatunek jest już w bazie')

class WstawGatunek(FlaskForm):
    NAZWA_GATUNKU    = StringField(label="Podaj nazwę nowego gatunku", 
                                           description="Tutaj wpisz swoją wartość!",
                                           validators=[gatunek_sie_nie_powtarza, Length(min=4, max=50)]
                                           )
    submit = SubmitField("Dodaj!")

# PODSTRONY DODAWANIA DANYCH
@app.route('/dodawanie_danych/formularz_gatunku', methods = ["POST", "GET"])
def insert_gatunek_page():
    form = WstawGatunek(request.form)
    NAZWA_GATUNKU  = None
    if request.method == 'POST' and form.validate_on_submit():
        flash('Dodano nowy gatunek!')

        #########################
        NAZWA_GATUNKU  =  form.NAZWA_GATUNKU.data.upper() if type(form.NAZWA_GATUNKU.data) == str else form.NAZWA_GATUNKU.data

        print(NAZWA_GATUNKU )
        print(type(NAZWA_GATUNKU ))


        insert.insert_into_oracle('GATUNKI', 
            [
                "NAZWA_GATUNKU "
            ], 
            [
                NAZWA_GATUNKU 
            ] 
            )

        form.NAZWA_GATUNKU.data = ""
        #########################

        return redirect(url_for('insert_gatunek_page'))

    return render_template('Podstrony/Formularze/f_gatunek.html',
                                NAZWA_GATUNKU = NAZWA_GATUNKU,
                                form = form
                                )

def karma_nie_jest_zajeta(form, field):
    NONE_OF_THIS = [str(elem[0]) for elem in select.select_simple('SELECT NAZWA_KARMY FROM KARMY')]
    if str(field.data) in NONE_OF_THIS:
        raise ValidationError(f'Podana nazwa karmy jest juz zajeta')

class WstawKarme(FlaskForm):
    NAZWA_KARMY  = StringField(label="Podaj nazwę karmy", 
                                           description="Tutaj wpisz swoją wartość!",
                                           validators=[karma_nie_jest_zajeta, Length(min=4, max=50)]
                                           )
    CENA_KG  = FloatField(label="Podaj cenę za kilogram", 
                                            description="Tutaj wpisz swoją wartość!",
                                            validators=[DataRequired()]
                                           )
    PRODUCENT  = StringField(label="Podaj nazwę producenta", 
                                           description="Tutaj wpisz swoją wartość!",
                                           validators=[DataRequired(), Length(min=4, max=50)]
                                           )
    NR_DO_PRODUCENTA  = StringField(label="Podaj numer telefonu do producenta", 
                                           description="Tutaj wpisz swoją wartość!",
                                           validators=[Optional(), Length(min=4, max=50)]
                                           )
    submit = SubmitField("Dodaj!")

@app.route('/dodawanie_danych/formularz_karmy', methods = ["POST", "GET"])
def insert_karma_page():
    form = WstawKarme(request.form)
    NAZWA_KARMY = None
    CENA_KG = None
    PRODUCENT = None
    NR_DO_PRODUCENTA = None

    if request.method == 'POST' and form.validate_on_submit():
        flash('Dodano nową karmę!')

        #########################
        NAZWA_KARMY = form.NAZWA_KARMY.data.upper() if type(form.NAZWA_KARMY.data) == str else form.NAZWA_KARMY.data
        CENA_KG = form.CENA_KG.data.upper() if type(form.CENA_KG.data) == str else form.CENA_KG.data
        PRODUCENT = form.PRODUCENT.data.upper() if type(form.PRODUCENT.data) == str else form.PRODUCENT.data
        NR_DO_PRODUCENTA = form.NR_DO_PRODUCENTA.data.upper() if type(form.NR_DO_PRODUCENTA.data) == str else form.NR_DO_PRODUCENTA.data

        print(NAZWA_KARMY,
                CENA_KG,
                PRODUCENT,
                NR_DO_PRODUCENTA)
        
        print(type(NAZWA_KARMY),
                type(CENA_KG),
                type(PRODUCENT),
                type(NR_DO_PRODUCENTA))


        insert.insert_into_oracle('KARMY', 
            [
                "NAZWA_KARMY",
                "CENA_KG",
                "PRODUCENT",
                "NR_DO_PRODUCENTA"
            ], 
            [
                NAZWA_KARMY,
                CENA_KG,
                PRODUCENT,
                NR_DO_PRODUCENTA
            ] 
            )

        form.NAZWA_KARMY.data = ""
        form.CENA_KG.data = ""
        form.PRODUCENT.data = ""
        form.NR_DO_PRODUCENTA.data = ""
        #########################

        return redirect(url_for('insert_karma_page'))

    return render_template('Podstrony/Formularze/f_karma.html',
                                NAZWA_KARMY = NAZWA_KARMY,
                                CENA_KG = CENA_KG,
                                PRODUCENT = PRODUCENT,
                                NR_DO_PRODUCENTA = NR_DO_PRODUCENTA,
                                form=form
                                )

def nrtel_sie_nie_powtarza(form, field):
    NONE_OF_THIS = [str(elem[0]) for elem in select.select_simple('SELECT NR_TELEFONU FROM PRACOWNICY')]
    if len(str(field.data)) != 9:
        raise ValidationError(f'Numer telefonu powinien składać się z 9 cyfr') 

    if str(field.data) in NONE_OF_THIS:
        raise ValidationError(f'Ten numer telefonu jest przypisany do innego pracownika') 

class WstawPracownika(FlaskForm):
    NR_TELEFONU  = IntegerField(label="Podaj numer telefonu pracownika", 
                                           description="Tutaj wpisz swoją wartość!",
                                           validators=[nrtel_sie_nie_powtarza]
                                           )
    IMIE  = StringField(label="Podaj imię pracownika", 
                                           description="Tutaj wpisz swoją wartość!",
                                           validators=[DataRequired(), Length(min=2, max=50)]
                                           )
    NAZWISKO  = StringField(label="Podaj nazwisko pracownika", 
                                           description="Tutaj wpisz swoją wartość!",
                                           validators=[DataRequired(), Length(min=2, max=50)]
                                           )
    PLACA_POD  = FloatField(label="Podaj płacę podstawową pracownika", 
                                           description="Tutaj wpisz swoją wartość!",
                                           validators=[DataRequired(message='Wpisz liczbę rzeczywistą, np: 1500.50')]
                                           )
    STAZ  = SelectField(label="Wybierz staz pracownika", 
                                           coerce=str,
                                           validators=[DataRequired()]
                                           )                   
    PLACA_DOD  = FloatField(label="Podaj płacę dodatkową pracownika", 
                                           description="Tutaj wpisz swoją wartość!",
                                           validators=[Optional()]
                                           )
    NAZWA_ZESPOLU  = SelectField(label='Wybierz zespol pracownika', 
                                            coerce=str,
                                            validators=[DataRequired()]
                                            )
    NAZWA_SPECJALIZACJI  = SelectField(label='Wybierz specjalizację pracownika', 
                                            coerce=str,
                                            validators=[DataRequired()]
                                            )
    submit = SubmitField("Dodaj!")


@app.route('/dodawanie_danych/formularz_pracownika', methods=['POST', 'GET'])
def insert_pracownik_page():
    form = WstawPracownika(request.form)
    NR_TELEFONU = None
    IMIE = None
    NAZWISKO = None
    PLACA_POD = None
    STAZ = None
    PLACA_DOD = None
    NAZWA_ZESPOLU = None
    NAZWA_SPECJALIZACJI = None

    #głowne
    NAZWA_ZESPOLU_LISTA = [(elem[0], elem[0]) for elem in select.select_simple('SELECT NAZWA FROM ZESPOLY')]
    NAZWA_SPECJALIZACJI_LISTA = [(elem[0], elem[0]) for elem in select.select_simple('SELECT SPECJALIZACJA FROM TYPY_PRACOWNIKA')]

    form.NAZWA_SPECJALIZACJI.choices = NAZWA_SPECJALIZACJI_LISTA
    form.NAZWA_ZESPOLU.choices = NAZWA_ZESPOLU_LISTA
    form.STAZ.choices = [('TIMESTAMP2022-01-23 08:42:31.12', 'Od teraz'), ('TIMESTAMP2017-01-01 00:00:00.00', 'Od 5 lat'), ('TIMESTAMP2012-01-01 00:00:00.00', 'Od 10 lat'), ('TIMESTAMP2007-01-01 00:00:00.00', 'Od 15 lat')]

    if request.method == 'POST' and form.validate_on_submit():
        flash('Dodano nowego pracownika!')

        #########################
        NR_TELEFONU = form.NR_TELEFONU.data.upper() if type(form.NR_TELEFONU.data) == str else form.NR_TELEFONU.data 
        IMIE = form.IMIE.data.upper() if type(form.IMIE.data) == str else form.IMIE.data 
        NAZWISKO = form.NAZWISKO.data.upper() if type(form.NAZWISKO.data) == str else form.NAZWISKO.data 
        PLACA_POD = form.PLACA_POD.data.upper() if type(form.PLACA_POD.data) == str else form.PLACA_POD.data 
        STAZ = form.STAZ.data.upper() if type(form.STAZ.data) == str else form.STAZ.data 
        PLACA_DOD = form.PLACA_DOD.data.upper() if type(form.PLACA_DOD.data) == str else form.PLACA_DOD.data 
        NAZWA_ZESPOLU = form.NAZWA_ZESPOLU.data.upper() if type(form.NAZWA_ZESPOLU.data) == str else form.NAZWA_ZESPOLU.data 
        NAZWA_SPECJALIZACJI = form.NAZWA_SPECJALIZACJI.data.upper() if type(form.NAZWA_SPECJALIZACJI.data) == str else form.NAZWA_SPECJALIZACJI.data 

        print(NR_TELEFONU,
                IMIE,
                NAZWISKO,
                PLACA_POD,
                STAZ,
                PLACA_DOD,
                NAZWA_ZESPOLU,
                NAZWA_SPECJALIZACJI)

        print(type(NR_TELEFONU),
                type(IMIE),
                type(NAZWISKO),
                type(PLACA_POD),
                type(STAZ),
                type(PLACA_DOD),
                type(NAZWA_ZESPOLU),
                type(NAZWA_SPECJALIZACJI))

        insert.insert_into_oracle('PRACOWNICY', 
            [
                "NR_TELEFONU",
                "IMIE",
                "NAZWISKO",
                "PLACA_POD",
                "STAZ",
                "PLACA_DOD",
                "NAZWA_ZESPOLU",
                "NAZWA_SPECJALIZACJI"
            ], 
            [
                NR_TELEFONU,
                IMIE,
                NAZWISKO,
                PLACA_POD,
                STAZ,
                PLACA_DOD,
                NAZWA_ZESPOLU,
                NAZWA_SPECJALIZACJI
            ] 
            )

        form.NR_TELEFONU.data = ""
        form.IMIE.data = ""
        form.NAZWISKO.data = ""
        form.PLACA_POD.data = ""
        form.STAZ.data = ""
        form.PLACA_DOD.data = ""
        form.NAZWA_ZESPOLU.data = ""
        form.NAZWA_SPECJALIZACJI.data = ""
        #########################

        return redirect(url_for('insert_pracownik_page'))

    return render_template('Podstrony/Formularze/f_pracownik.html',
                                NR_TELEFONU = NR_TELEFONU,
                                IMIE = IMIE,
                                NAZWISKO = NAZWISKO,
                                PLACA_POD = PLACA_POD,
                                STAZ = STAZ,
                                PLACA_DOD = PLACA_DOD,
                                NAZWA_ZESPOLU = NAZWA_ZESPOLU,
                                NAZWA_SPECJALIZACJI = NAZWA_SPECJALIZACJI,
                                form = form
                                )

    

def zespol_sie_nie_powtarza(form, field):
    NONE_OF_THIS = [str(elem[0]) for elem in select.select_simple('SELECT NAZWA FROM ZESPOLY')]
    if str(field.data) in NONE_OF_THIS:
        raise ValidationError(f'Zespol o takiej nazwie juz istnieje') 

class WstawZespol(FlaskForm):
    NAZWA  = StringField(label="Podaj nazwę zespołu", 
                                           description="Tutaj wpisz swoją wartość!",
                                           validators=[zespol_sie_nie_powtarza, Length(min=4, max=50)]
                                           )
    LICZBA_CZLONKOW  = IntegerField(label="Podaj liczbę członków zespołu", 
                                            description="Tutaj wpisz swoją wartość!",
                                            validators=[DataRequired(), NumberRange(min=1, max=200)]
                                           )
    submit = SubmitField("Dodaj!")

@app.route('/dodawanie_danych/formularz_zespolu', methods=["POST", "GET"])
def insert_zespol_page():
    form = WstawZespol(request.form)
    NAZWA = None
    LICZBA_CZLONKOW = None

    if request.method == 'POST' and form.validate_on_submit():
        flash('Dodano nowy zespol!')

        #########################
        NAZWA = form.NAZWA.data.upper() if type(form.NAZWA.data) == str else form.NAZWA.data
        LICZBA_CZLONKOW = form.LICZBA_CZLONKOW.data.upper() if type(form.LICZBA_CZLONKOW.data) == str else form.LICZBA_CZLONKOW.data

        print(NAZWA, LICZBA_CZLONKOW)
        
        print(type(NAZWA), type(LICZBA_CZLONKOW))


        insert.insert_into_oracle('ZESPOLY', 
            [
                "NAZWA",
                "LICZBA_CZLONKOW"
            ], 
            [
                NAZWA,
                LICZBA_CZLONKOW
            ] 
            )

        form.NAZWA.data = ""
        form.LICZBA_CZLONKOW.data = ""
        #########################

        return redirect(url_for('insert_zespol_page'))

    return render_template('Podstrony/Formularze/f_zespol.html',
                                NAZWA = NAZWA,
                                LICZBA_CZLONKOW = LICZBA_CZLONKOW,
                                form = form
                                )

def none_of_animal_id(form, field):
    NONE_OF_ID = [int(elem[0]) for elem in select.select_simple('SELECT IDENTYFIKATOR_ZWIERZECIA FROM ZWIERZETA')]
    if int(field.data) in NONE_OF_ID:
        raise ValidationError(f'ID {field.data} jest juz zajete')


def data_format(form, field):
    temp = str(field.data)
    przeszlo = False
    try:
        temp = temp.split(':')
        if (len(temp) == 2 and
            len(temp[0]) == 2 and
            len(temp[1]) == 2 and
            temp[0][0] in ['0', '1', '2'] and 
            temp[0][1] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  and 
            temp[1][0] in ['0', '1', '2', '3', '4', '5'] and 
            temp[1][1] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
            ):
                przeszlo = True
    except:
        pass
    if not przeszlo:
        raise ValidationError(f'Data musi być podana w formacie "HH:MM" np. 06:30 lub 23:15')
   

class WstawZwierze(FlaskForm):
    IDENTYFIKATOR_ZWIERZECIA = IntegerField(label="Podaj identyfikator zwierzęcia", 
                                           description="Tutaj wpisz swoją wartość!",
                                           validators=[none_of_animal_id]
                                           )
    PORA_KARMIENIA = StringField(label="Podaj porę karmienia zwierzęcia", 
                                           description="Tutaj wpisz swoją wartość!",
                                           validators=[data_format, Length(min=4, max=5)]
                                           )
    ILOSC_KARMY = FloatField(label="Podaj ilość karmy dla zwierzęcia", 
                                           description="Tutaj wpisz swoją wartość!",
                                           validators=[DataRequired(message='Wpisz liczbę rzeczywistą, np: 10.3')]
                                           )
    WIEK = IntegerField(label="Podaj wiek zwierzęcia", 
                                           description="Tutaj wpisz swoją wartość!",
                                           validators=[DataRequired(), NumberRange(min=1, max=300)]
                                           )
    IMIE = StringField(label="Podaj imie zwierzęcia", 
                                           description="Tutaj wpisz swoją wartość!",
                                           validators=[DataRequired(), Length(min=3, max=50)]
                                           )                                 
    WLASCICIEL = StringField(label="Podaj imie wlasciciela zwierzęcia", 
                                           description="Tutaj wpisz swoją wartość!",
                                           validators=[DataRequired(), Length(min=3, max=50)]
                                           )
    KARMA = SelectField(label='Wybierz karmę zwierzęcia', 
                                            coerce=str,
                                            validators=[DataRequired()]
                                            )
    GATUNEK = SelectField(label='Wybierz gatunek zwierzęcia', 
                                            coerce=str,
                                            validators=[DataRequired()]
                                            )
    RODZINA = SelectField(label='Wybierz rodzinę zwierzęcia', 
                                            coerce=str,
                                            validators=[DataRequired()]
                                            )
    GROMADA = SelectField(label='Wybierz gromadę zwierzęcia', 
                                            coerce=str,
                                            validators=[DataRequired()]
                                            )
    AZYL = SelectField(label='Wybierz azyl zwierzęcia', 
                                            coerce=int,
                                            validators=[DataRequired()]
                                            )
    submit = SubmitField("Dodaj!")



@app.route('/dodawanie_danych/formularz_zwierzecia', methods = ['GET', 'POST'])
def insert_zwierze_page():
    form = WstawZwierze(request.form)
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
    #pomocnicze
    IDENTYFIKATOR_AZYLU_LISTA = [elem[0] for elem in select.select_simple('SELECT IDENTYFIKATOR_AZYLU FROM AZYLE')]
    NAZWA_AZYLU_LISTA = [elem[0] for elem in select.select_simple('SELECT NAZWA_AZYLU FROM AZYLE')]
    #głowne
    NAZWA_GATUNKU_LISTA = [(elem[0], elem[0]) for elem in select.select_simple('SELECT NAZWA_GATUNKU FROM GATUNKI')]
    NAZWA_KARMY_LISTA = [(elem[0], elem[0]) for elem in select.select_simple('SELECT NAZWA_KARMY FROM KARMY')]
    NAZWA_GROMADY_LISTA = [(elem[0], elem[0]) for elem in select.select_simple('SELECT NAZWA_GROMADY FROM GROMADY')]
    NAZWA_RODZINY_LISTA = [(elem[0], elem[0]) for elem in select.select_simple('SELECT NAZWA_RODZINY FROM RODZINY')]
    AZYLE_LISTA = [(IDENTYFIKATOR_AZYLU_LISTA[i], NAZWA_AZYLU_LISTA[i]) for i in range(len(IDENTYFIKATOR_AZYLU_LISTA))]

    form.KARMA.choices = NAZWA_KARMY_LISTA
    form.RODZINA.choices = NAZWA_RODZINY_LISTA
    form.GATUNEK.choices = NAZWA_GATUNKU_LISTA
    form.GROMADA.choices = NAZWA_GROMADY_LISTA
    form.AZYL.choices = AZYLE_LISTA

    if request.method == 'POST' and form.validate_on_submit():
        flash('Dodano nowe zwierze!')

        #########################
        IDENTYFIKATOR_ZWIERZECIA = form.IDENTYFIKATOR_ZWIERZECIA.data.upper() if type(form.IDENTYFIKATOR_ZWIERZECIA.data) == str else form.IDENTYFIKATOR_ZWIERZECIA.data
        PORA_KARMIENIA = form.PORA_KARMIENIA.data.upper() if type(form.PORA_KARMIENIA.data) == str else form.PORA_KARMIENIA.data
        ILOSC_KARMY = form.ILOSC_KARMY.data.upper() if type(form.ILOSC_KARMY.data) == str else form.ILOSC_KARMY.data
        WIEK = form.WIEK.data.upper() if type(form.WIEK.data) == str else form.WIEK.data
        IMIE = form.IMIE.data.upper() if type(form.IMIE.data) == str else form.IMIE.data
        WLASCICIEL = form.WLASCICIEL.data.upper() if type(form.WLASCICIEL.data) == str else form.WLASCICIEL.data
        KARMA = form.KARMA.data.upper() if type(form.KARMA.data) == str else form.KARMA.data
        GATUNEK = form.GATUNEK.data.upper() if type(form.GATUNEK.data) == str else form.GATUNEK.data
        RODZINA = form.RODZINA.data.upper() if type(form.RODZINA.data) == str else form.RODZINA.data
        GROMADA = form.GROMADA.data.upper() if type(form.GROMADA.data) == str else form.GROMADA.data
        AZYL = form.AZYL.data.upper() if type(form.AZYL.data) == str else form.AZYL.data

        print(IDENTYFIKATOR_ZWIERZECIA,
            PORA_KARMIENIA,
            ILOSC_KARMY,
            WIEK,
            IMIE,
            WLASCICIEL,
            KARMA,
            GATUNEK,
            RODZINA,
            GROMADA,
            AZYL)
        
        print(type(IDENTYFIKATOR_ZWIERZECIA),
            type(PORA_KARMIENIA),
            type(ILOSC_KARMY),
            type(WIEK),
            type(IMIE),
            type(WLASCICIEL),
            type(KARMA),
            type(GATUNEK),
            type(RODZINA),
            type(GROMADA),
            type(AZYL))

        insert.insert_into_oracle('ZWIERZETA', 
            [
                "IDENTYFIKATOR_ZWIERZECIA",
                "PORA_KARMIENIA",
                "ILOSC_KARMY",
                "WIEK",
                "IMIE",
                "WLASCICIEL",
                "KARMA",
                "GATUNEK",
                "RODZINA",
                "GROMADA",
                "AZYL"
            ], 
            [
                IDENTYFIKATOR_ZWIERZECIA,
                PORA_KARMIENIA,
                ILOSC_KARMY,
                WIEK,
                IMIE,
                WLASCICIEL,
                KARMA,
                GATUNEK,
                RODZINA,
                GROMADA,
                AZYL
            ] 
            )

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
        #########################

        return redirect(url_for('insert_zwierze_page'))

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

def typ_sie_nie_powtarza(form, field):
    NONE_OF_THIS = [str(elem[0]) for elem in select.select_simple('SELECT SPECJALIZACJA FROM TYPY_PRACOWNIKA')]
    if str(field.data) in NONE_OF_THIS:
        raise ValidationError(f'Taka specjalizacja pracownika jest juz w bazie') 

class WstawTypPracownika(FlaskForm):
    SPECJALIZACJA   = StringField(label="Podaj nazwę specjalizacji", 
                                           description="Tutaj wpisz swoją wartość!",
                                           validators=[typ_sie_nie_powtarza, Length(min=4, max=50)]
                                           )
    submit = SubmitField("Dodaj!")

@app.route('/dodawanie_danych/formularz_typu_pracownika', methods=['POST', 'GET'])
def insert_typ_prac_page():
    form = WstawTypPracownika(request.form)
    SPECJALIZACJA = None
    if request.method == 'POST' and form.validate_on_submit():
        flash('Dodano nowy typ pracownika!')

        #########################
        SPECJALIZACJA = form.SPECJALIZACJA.data.upper() if type(form.SPECJALIZACJA.data) == str else form.SPECJALIZACJA.data

        print(SPECJALIZACJA)
        print(type(SPECJALIZACJA))


        insert.insert_into_oracle('TYPY_PRACOWNIKA', 
            [
                "SPECJALIZACJA"
            ], 
            [
                SPECJALIZACJA
            ] 
            )

        form.SPECJALIZACJA.data = ""
        #########################

        return redirect(url_for('insert_typ_prac_page'))

    return render_template('Podstrony/Formularze/f_typ_prac.html',
                                SPECJALIZACJA = SPECJALIZACJA,
                                form = form
                                )

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




class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class UsunZwierze(FlaskForm):
    checkbox = MultiCheckboxField('Label', choices=str)
    submit = SubmitField("Usun zwierze!")


# PODSTRONY USUWANIA DANYCH
@app.route('/usuwanie_danych/usuwanie_zwierzat', methods = ["POST", "GET"])
def delete_zwierze_page():
    form = UsunZwierze(request.form)
    form.checkbox.choices = [(elem[0], elem[0]) for elem in select.select_simple('SELECT IDENTYFIKATOR_ZWIERZECIA FROM ZWIERZETA')]

    if form.validate_on_submit():
        mapped = [int(x) for x in form.checkbox.data]
        for i in range(len(mapped)):
            delete.delete_from_oracle_with_where("ZWIERZETA", "IDENTYFIKATOR_ZWIERZECIA", '=', mapped[i])
        return redirect(url_for('delete_zwierze_page'))

    nazwa_tabeli_do_wyswietlenia = 'ZWIERZETA'
    if nazwa_tabeli_do_wyswietlenia != 'brak':
        dane_tabeli_do_wyswietlenia = select.select_simple(f"SELECT * FROM {nazwa_tabeli_do_wyswietlenia.upper()}")
        naglowki_tabeli_do_wyswietlenia = select.select_simple(f"SELECT COLUMN_NAME FROM USER_TAB_COLUMNS WHERE TABLE_NAME = '{nazwa_tabeli_do_wyswietlenia.upper()}'")
        if dane_tabeli_do_wyswietlenia == [] or dane_tabeli_do_wyswietlenia == "BRAK DANYCH":
            dane_tabeli_do_wyswietlenia = [["--" for i in range(len(naglowki_tabeli_do_wyswietlenia))]]
        naglowki_tabeli_do_wyswietlenia = [i[0] for i in naglowki_tabeli_do_wyswietlenia]
        return render_template('Podstrony/Usuwanie/usun_zwierze.html', form=form, headings=naglowki_tabeli_do_wyswietlenia, data=dane_tabeli_do_wyswietlenia)
    else:
        return render_template('Podstrony/Usuwanie/usun_zwierze.html', form=form ,headings=[], data=[])



class UsunKarme(FlaskForm):
    checkbox = MultiCheckboxField('Label', choices=str)
    submit = SubmitField("Usun karme!")

@app.route('/usuwanie_danych/usuwanie_karmy', methods = ['POST', 'GET'])
def delete_karma_page():
    form = UsunKarme(request.form)
    form.checkbox.choices = [(elem[0], elem[0]) for elem in select.select_simple('SELECT NAZWA_KARMY FROM KARMY')]

    if form.validate_on_submit():
        mapped = [str(x) for x in form.checkbox.data]
        for i in range(len(mapped)):
            delete.delete_from_oracle_with_where("KARMY", "NAZWA_KARMY ", '=', mapped[i])
        return redirect(url_for('delete_karma_page'))

    nazwa_tabeli_do_wyswietlenia = 'KARMY'
    if nazwa_tabeli_do_wyswietlenia != 'brak':
        dane_tabeli_do_wyswietlenia = select.select_simple(f"SELECT * FROM {nazwa_tabeli_do_wyswietlenia.upper()}")
        naglowki_tabeli_do_wyswietlenia = select.select_simple(f"SELECT COLUMN_NAME FROM USER_TAB_COLUMNS WHERE TABLE_NAME = '{nazwa_tabeli_do_wyswietlenia.upper()}'")
        if dane_tabeli_do_wyswietlenia == [] or dane_tabeli_do_wyswietlenia == "BRAK DANYCH":
            dane_tabeli_do_wyswietlenia = [["--" for i in range(len(naglowki_tabeli_do_wyswietlenia))]]
        naglowki_tabeli_do_wyswietlenia = [i[0] for i in naglowki_tabeli_do_wyswietlenia]
        return render_template('Podstrony/Usuwanie/usun_karme.html', form=form, headings=naglowki_tabeli_do_wyswietlenia, data=dane_tabeli_do_wyswietlenia)
    else:
        return render_template('Podstrony/Usuwanie/usun_karme.html', form=form ,headings=[], data=[])


class UsunGatunek(FlaskForm):
    checkbox = MultiCheckboxField('Label', choices=str)
    submit = SubmitField("Usun gatunki!")

@app.route('/usuwanie_danych/usuwanie_gatunku', methods = ['POST', 'GET'])
def delete_gatunek_page():
    form = UsunGatunek(request.form)
    form.checkbox.choices = [(elem[0], elem[0]) for elem in select.select_simple('SELECT NAZWA_GATUNKU FROM GATUNKI')]

    if form.validate_on_submit():
        mapped = [str(x) for x in form.checkbox.data]
        for i in range(len(mapped)):
            delete.delete_from_oracle_with_where("GATUNKI", "NAZWA_GATUNKU ", '=', mapped[i])
        return redirect(url_for('delete_gatunek_page'))

    nazwa_tabeli_do_wyswietlenia = 'GATUNKI'
    if nazwa_tabeli_do_wyswietlenia != 'brak':
        dane_tabeli_do_wyswietlenia = select.select_simple(f"SELECT * FROM {nazwa_tabeli_do_wyswietlenia.upper()}")
        naglowki_tabeli_do_wyswietlenia = select.select_simple(f"SELECT COLUMN_NAME FROM USER_TAB_COLUMNS WHERE TABLE_NAME = '{nazwa_tabeli_do_wyswietlenia.upper()}'")
        if dane_tabeli_do_wyswietlenia == [] or dane_tabeli_do_wyswietlenia == "BRAK DANYCH":
            dane_tabeli_do_wyswietlenia = [["--" for i in range(len(naglowki_tabeli_do_wyswietlenia))]]
        naglowki_tabeli_do_wyswietlenia = [i[0] for i in naglowki_tabeli_do_wyswietlenia]
        return render_template('Podstrony/Usuwanie/usun_gatunek.html', form=form, headings=naglowki_tabeli_do_wyswietlenia, data=dane_tabeli_do_wyswietlenia)
    else:
        return render_template('Podstrony/Usuwanie/usun_gatunek.html', form=form ,headings=[], data=[])


class UsunPracownika(FlaskForm):
    checkbox = MultiCheckboxField('Label', choices=str)
    submit = SubmitField("Usun pracowników!")

@app.route('/usuwanie_danych/usuwanie_pracownikow', methods = ['POST', 'GET'])
def delete_pracownik_page():
    form = UsunPracownika(request.form)
    form.checkbox.choices = [(elem[0], elem[0]) for elem in select.select_simple('SELECT NR_TELEFONU FROM PRACOWNICY')]

    if form.validate_on_submit():
        mapped = [int(x) for x in form.checkbox.data]
        for i in range(len(mapped)):
            delete.delete_from_oracle_with_where("PRACOWNICY", "NR_TELEFONU ", '=', mapped[i])
        return redirect(url_for('delete_pracownik_page'))

    nazwa_tabeli_do_wyswietlenia = 'PRACOWNICY'
    if nazwa_tabeli_do_wyswietlenia != 'brak':
        dane_tabeli_do_wyswietlenia = select.select_simple(f"SELECT * FROM {nazwa_tabeli_do_wyswietlenia.upper()}")
        naglowki_tabeli_do_wyswietlenia = select.select_simple(f"SELECT COLUMN_NAME FROM USER_TAB_COLUMNS WHERE TABLE_NAME = '{nazwa_tabeli_do_wyswietlenia.upper()}'")
        if dane_tabeli_do_wyswietlenia == [] or dane_tabeli_do_wyswietlenia == "BRAK DANYCH":
            dane_tabeli_do_wyswietlenia = [["--" for i in range(len(naglowki_tabeli_do_wyswietlenia))]]
        naglowki_tabeli_do_wyswietlenia = [i[0] for i in naglowki_tabeli_do_wyswietlenia]
        return render_template('Podstrony/Usuwanie/usun_pracownika.html', form=form, headings=naglowki_tabeli_do_wyswietlenia, data=dane_tabeli_do_wyswietlenia)
    else:
        return render_template('Podstrony/Usuwanie/usun_pracownika.html', form=form ,headings=[], data=[])

class UsunZespol(FlaskForm):
    checkbox = MultiCheckboxField('Label', choices=str)
    submit = SubmitField("Usun zespoly!")

@app.route('/usuwanie_danych/usuwanie_zespolow', methods = ['POST', 'GET'])
def delete_zespol_page():
    form = UsunZespol(request.form)
    form.checkbox.choices = [(elem[0], elem[0]) for elem in select.select_simple('SELECT NAZWA FROM ZESPOLY')]

    if form.validate_on_submit():
        mapped = [str(x) for x in form.checkbox.data]
        for i in range(len(mapped)):
            delete.delete_from_oracle_with_where("ZESPOLY", "NAZWA ", '=', mapped[i])
        return redirect(url_for('delete_zespol_page'))

    nazwa_tabeli_do_wyswietlenia = 'ZESPOLY'
    if nazwa_tabeli_do_wyswietlenia != 'brak':
        dane_tabeli_do_wyswietlenia = select.select_simple(f"SELECT * FROM {nazwa_tabeli_do_wyswietlenia.upper()}")
        naglowki_tabeli_do_wyswietlenia = select.select_simple(f"SELECT COLUMN_NAME FROM USER_TAB_COLUMNS WHERE TABLE_NAME = '{nazwa_tabeli_do_wyswietlenia.upper()}'")
        if dane_tabeli_do_wyswietlenia == [] or dane_tabeli_do_wyswietlenia == "BRAK DANYCH":
            dane_tabeli_do_wyswietlenia = [["--" for i in range(len(naglowki_tabeli_do_wyswietlenia))]]
        naglowki_tabeli_do_wyswietlenia = [i[0] for i in naglowki_tabeli_do_wyswietlenia]
        return render_template('Podstrony/Usuwanie/usun_zespol.html', form=form, headings=naglowki_tabeli_do_wyswietlenia, data=dane_tabeli_do_wyswietlenia)
    else:
        return render_template('Podstrony/Usuwanie/usun_zespol.html', form=form ,headings=[], data=[])

class UsunTyp(FlaskForm):
    checkbox = MultiCheckboxField('Label', choices=str)
    submit = SubmitField("Usun specjalizacje!")

@app.route('/usuwanie_danych/usuwanie_specjalizacji', methods = ['POST', 'GET'])
def delete_typ_prac_page():
    form = UsunTyp(request.form)
    form.checkbox.choices = [(elem[0], elem[0]) for elem in select.select_simple('SELECT SPECJALIZACJA FROM TYPY_PRACOWNIKA')]

    if form.validate_on_submit():
        mapped = [str(x) for x in form.checkbox.data]
        for i in range(len(mapped)):
            delete.delete_from_oracle_with_where("TYPY_PRACOWNIKA", "SPECJALIZACJA ", '=', mapped[i])
        return redirect(url_for('delete_typ_prac_page'))

    nazwa_tabeli_do_wyswietlenia = 'TYPY_PRACOWNIKA'
    if nazwa_tabeli_do_wyswietlenia != 'brak':
        dane_tabeli_do_wyswietlenia = select.select_simple(f"SELECT * FROM {nazwa_tabeli_do_wyswietlenia.upper()}")
        naglowki_tabeli_do_wyswietlenia = select.select_simple(f"SELECT COLUMN_NAME FROM USER_TAB_COLUMNS WHERE TABLE_NAME = '{nazwa_tabeli_do_wyswietlenia.upper()}'")
        if dane_tabeli_do_wyswietlenia == [] or dane_tabeli_do_wyswietlenia == "BRAK DANYCH":
            dane_tabeli_do_wyswietlenia = [["--" for i in range(len(naglowki_tabeli_do_wyswietlenia))]]
        naglowki_tabeli_do_wyswietlenia = [i[0] for i in naglowki_tabeli_do_wyswietlenia]
        return render_template('Podstrony/Usuwanie/usun_specjalizacje.html', form=form, headings=naglowki_tabeli_do_wyswietlenia, data=dane_tabeli_do_wyswietlenia)
    else:
        return render_template('Podstrony/Usuwanie/usun_specjalizacje.html', form=form ,headings=[], data=[])


