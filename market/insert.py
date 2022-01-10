# table_name            <nazwa tabli np. pracownicy>
# list_of_parameters    <nazwy kolumn do insertu w postaci listy np. [id_prac, imie, nazwisko, etat, placa_pod...]>
# list_of_arguments     <wartości do wpisania w kolumny z list_of_parameters np. [23, 'jan', 'brzechwa', 'pisarz'...]>
from market import conn

def insert_into_oracle(table_name, list_of_parameters, list_of_arguments):
    try:
        list_of_parameters_string = "("
        list_of_arguments_string = "("

        if type(table_name) != str:
            print(f'Nazwa tabeli musi byc stringiem!: {type(table_name)}')
            raise Exception

        for parameter in list_of_parameters:
            if type(parameter) == str:
                list_of_parameters_string += parameter.upper() + ','
            else:
                print(f'Zly typ danych w parametrze: {type(parameter)}')
                raise Exception

        for argument in list_of_arguments:
            if type(argument) == int:
                list_of_arguments_string += str(argument) + ","
            elif type(argument) == float:
                list_of_arguments_string += str(argument) + ","
            elif type(argument) == str:
                list_of_arguments_string += "'" + argument.upper() + "',"
            else:
                print(f'Zly typ danych w argumencie: {type(argument)}')
                raise Exception

        list_of_parameters_string = list_of_parameters_string[:len(list_of_parameters_string)-1] + ')'
        list_of_arguments_string = list_of_arguments_string[:len(list_of_arguments_string) - 1] + ')'

        cur = conn.cursor()
        insert_statement = f"INSERT INTO {table_name.upper()} {list_of_parameters_string} VALUES {list_of_arguments_string}"
        cur.execute(insert_statement)

    except Exception as err:
        print(f'{insert_statement}\nBlad przy wykonywaniu funkcji insert_into_oracle: ', err)

    else:
        print(f'Wstawianie danych powiodlo sie.\nWykonano polecenie {insert_statement}\n')
        conn.commit()
    finally:
        cur.close()


