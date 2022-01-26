import cx_Oracle

try:
    cx_Oracle.init_oracle_client(lib_dir=r"<Sciezka instant client>")
    conn = cx_Oracle.connect('<twojlogin>/<twojehaslo>@//admlab2.cs.put.poznan.pl:1521/dblab02_students.cs.put.poznan.pl')
except Exception as err:
    print('Blad podczas proby nawiazania polaczenia: ', err)
else:
    print(conn.version)
    try:
        #Jezeli nawiazano polaczenie, sprobuj utworzyc kursor
        cur = conn.cursor()
        insertstatement = "INSERT INTO CEO_DETAILS(FIRST_NAME, LAST_NAME, COMPANY, AGE) VALUES('Werka', 'Burzynek', 'BTC SP ZOO', 23)"
        cur.execute(insertstatement)
    except Exception as err:
        print('Blad podczas wstawiania danych: ', err)
    else:
        print('Wstawianie danych powiodlo sie')
        conn.commit()
finally:
    cur.close()
    conn.close()
