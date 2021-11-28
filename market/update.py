from market import conn

# table_name            <ktora tabele updatowac?>,
# parameter_to_set      <SET parameter_to_set = ...>,
# value_to_set          <SET parameter_to_set = value_to_set...>,
# parameter_to_where    <WHERE parameter_to_where = ...>,
# sign                  <znak pomiedzy parametrem WHERE a wartoscia>
# value_to_where        <WHERE parameter_to_where = value_to_where>)


def update_to_oracle_with_where(table_name, parameter_to_set, value_to_set, parameter_to_where, sign, value_to_where):
    try:
        if not (
                (  # Nazwy kolumn z tabeli muszą być stringami
                    type(table_name) == str and
                    type(parameter_to_set) == str and
                    type(parameter_to_where) == str and
                    # Uznajemy że znak przekazywany jest jako string
                    type(sign) == str
                )
                and
                (  # Wartość w tabeli musi być stringiem, intigerem albo floatem
                    type(value_to_set) == str or
                    type(value_to_set) == int or
                    type(value_to_set) == float
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
        if type(value_to_set) == str:
            value_to_set = "'" + value_to_set + "'"

        # Jeżeli ustawiana wartość jest stringiem, to musimy dodać do zapytania SQL cudzysłowia
        if type(value_to_where) == str:
            value_to_where = "'" + value_to_where + "'"

        cur = conn.cursor()
        update_statement = f"UPDATE {table_name.upper()} SET {parameter_to_set.upper()}={value_to_set} WHERE {parameter_to_where.upper()}{sign}{value_to_where}"
        cur.execute(update_statement)

    except Exception as err:
        print(f'{update_statement}\nBlad przy wykonywaniu funkcji update_to_oracle_with_where: ', err)
    else:
        print(f'Modyfikowanie danych powiodlo sie.\nWykonano polecenie {update_statement}\n')
        conn.commit()
    finally:
        cur.close()


def update_to_oracle(table_name, parameter_to_set, value_to_set):
    try:
        if not (
                (   # Nazwy kolumn z tabeli muszą być stringami
                    type(table_name) == str and
                    type(parameter_to_set) == str
                )
                and
                (   # Wartość w tabeli musi być stringiem, intigerem albo floatem
                    type(value_to_set) == str or
                    type(value_to_set) == int or
                    type(value_to_set) == float
                )
        ):
            # W przeciwnym razie przerywamy funkcję
            raise Exception

        # Jeżeli ustawiana wartość jest stringiem, to musimy dodać do zapytania SQL cudzysłowia
        if type(value_to_set) == str:
            value_to_set = "'" + value_to_set + "'"

        cur = conn.cursor()
        update_statement = f"UPDATE {table_name.upper()} SET {parameter_to_set.upper()}={value_to_set}"
        cur.execute(update_statement)

    except Exception as err:
        print(f'{update_statement}\nBlad przy wykonywaniu funkcji update_to_oracle: ', err)
    else:
        print(f'Modyfikowanie danych powiodlo sie.\nWykonano polecenie {update_statement}\n')
        conn.commit()
    finally:
        cur.close()
