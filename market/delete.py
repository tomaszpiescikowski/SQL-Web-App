# table_name              <ktora tabele usuwac>,
# parameter_to_where      <WHERE parameter_to_where <sign> ...>,
# sign                    <WHERE <parameter_to_where> >= 12>,
# value_to_where          <WHERE parameter_to_where <sign>> value_to_where>)


def delete_from_oracle_with_where(table_name, parameter_to_where, sign, value_to_where):
    try:
        if not (
                (   # Nazwy kolumn z tabeli muszą być stringami
                    type(table_name) == str and
                    type(parameter_to_where) == str and
                    # Uznajemy że znak przekazywany jest jako string
                    type(sign) == str
                )
                and
                (   # Wartość w tabeli musi być stringiem, intigerem albo floatem
                    type(value_to_where) == str or
                    type(value_to_where) == int or
                    type(value_to_where) == float)
        ):
            # W przeciwnym razie przerywamy funkcję
            raise Exception

        # Jeżeli ustawiana wartość jest stringiem, to musimy dodać do zapytania SQL cudzysłowia
        if type(value_to_where) == str:
            value_to_where = "'" + value_to_where + "'"

        cur = conn.cursor()
        delete_statement = f"DELETE FROM {table_name.upper()} WHERE {parameter_to_where.upper()}{sign}{value_to_where}"
        cur.execute(delete_statement)

    except Exception as err:
        print(f'{delete_statement}\nBlad przy wykonywaniu funkcji delete_from_oracle_with_where: ', err)
    else:
        print(f'Usuwanie danych powiodlo sie.\nWykonano polecenie {delete_statement}\n')
        conn.commit()
    finally:
        cur.close()


