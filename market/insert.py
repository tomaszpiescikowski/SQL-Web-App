from market import conn

# parameters -> (pracownicy, [id_prac, imie, nazwisko, etat, placa_pod...], [23, 'jan', 'brzechwa', 'pisarz', 3120...])
def insert_into_oracle(table_name, list_of_parameters, list_of_arguments):
    try:
        list_of_parameters_string = "("
        list_of_arguments_string = "("

        for parameter in list_of_parameters:
            if type(parameter) == int:
                list_of_parameters_string += str(parameter) + ','
            elif type(parameter) == str:
                list_of_parameters_string += parameter.upper() + ','
            else:
                print(f'Zly typ danych w parametrze: {type(parameter)}')

        for argument in list_of_arguments:
            if type(argument) == int:
                list_of_arguments_string += str(argument) + ","
            elif type(argument) == str:
                list_of_arguments_string += "'" + argument.upper() + "',"
            else:
                print(f'Zly typ danych w argumencie: {type(argument)}')

        list_of_parameters_string = list_of_parameters_string[:len(list_of_parameters_string)-1] + ')'
        list_of_arguments_string = list_of_arguments_string[:len(list_of_arguments_string) - 1] + ')'

        table_name_string = str(table_name)

        cur = conn.cursor()
        insert_statement = f"INSERT INTO {table_name_string.upper()} {list_of_parameters_string} VALUES {list_of_arguments_string}"
        cur.execute(insert_statement)

    except Exception as err:
        print('Blad przy wykonywaniu funkcji insert_into_oracle: ', err)

    else:
        print('Wstawianie danych powiodlo sie.')
        print(f'Wykonano polecenie {insert_statement}\n')
        conn.commit()
    finally:
        cur.close()


