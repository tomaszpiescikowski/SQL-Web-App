# list_of_parameters    <nazwy kolumn do selectu w postaci listy np. [id_prac, imie, nazwisko, etat, placa_pod...]>
# table_name            <nazwa tabli np. pracownicy>
# parameter_to_where    <WHERE parameter_to_where = ...>
# sign                  <znak pomiedzy parametrem WHERE a wartoscia>
# value_to_where        <WHERE parameter_to_where <= value_to_where>)
# parameter_to_order    <ORDER BY parameter_to_order <value_to_order>>,
# value_to_order        <rosnąco - ASC, malejąco - DESC>


def select_from_oracle(list_of_parameters, table_name, parameter_to_where, sign, value_to_where, parameter_to_order, value_to_order):
    try:
        list_of_parameters_string = ""

        for parameter in list_of_parameters:
            if type(parameter) == str:
                list_of_parameters_string += parameter.upper() + ','
            else:
                print(f'Zly typ danych w parametrze: {type(parameter)}')
                raise Exception

        if not (
                (  # Nazwy kolumn z tabeli muszą być stringami
                    type(table_name) == str and
                    type(parameter_to_order) == str and
                    type(parameter_to_where) == str and
                    # Uznajemy że znak przekazywany jest jako string
                    type(sign) == str
                )
                and
                (  # ASC/DESC musi byc stringiem
                    type(value_to_order) == str
                )
                and
                (  # Wartość w tabeli musi być stringiem, intigerem albo floatem
                    type(value_to_where) == str or
                    type(value_to_where) == int or
                    type(value_to_where) == float
                )
        ):
            # W przeciwnym razie przerywamy funkcję
            raise Exception

        # Jeżeli ustawiana wartość jest stringiem, to musimy dodać do zapytania SQL cudzysłowia
        if type(value_to_where) == str:
            value_to_where = "'" + value_to_where + "'"

        cur = conn.cursor()
        select_statement = f"SELECT {list_of_parameters_string[:len(list_of_parameters_string)-1].upper()} " \
                           f"FROM {table_name.upper()} " \
                           f"WHERE {parameter_to_where.upper()}{sign}{value_to_where} " \
                           f"ORDER BY {parameter_to_order.upper()} {value_to_order.upper()}"
        cur.execute(select_statement)

    except Exception as err:
        print(f'{select_statement}\nBlad przy wykonywaniu funkcji select_from_oracle: ', err)
    else:
        print(f'Wyswietlanie danych powiodlo sie.\nWykonano polecenie {select_statement}\n')
        list_of_results = cur.fetchall()
        for result in list_of_results:
            print(*result)
        conn.commit()
    finally:
        cur.close()

