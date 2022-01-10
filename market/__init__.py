from flask import Flask
import cx_Oracle

try:
    cx_Oracle.init_oracle_client(lib_dir=r"C:\\Users\\tomek\Desktop\\ProjektSQL\\instantclient_21_3")
    conn = cx_Oracle.connect('inf145418/inf145418@//admlab2.cs.put.poznan.pl:1521/dblab02_students.cs.put.poznan.pl')
except Exception as err:
    print('Blad podczas proby nawiazania polaczenia: ', err)
else:
    print('Polaczenie nawiazane pomyslnie. Wersja: ', conn.version)

app = Flask(__name__)

from market import routes, insert, update, delete, select
