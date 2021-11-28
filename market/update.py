from market import conn

# parameters -> (
# table_name<ktora tabele updatowac?>,
# parameter_to_set<SET parameter_to_set = ...>,
# value_to_set<SET parameter_to_set = value_to_set...>,
# parameter_to_where<WHERE parameter_to_where = ...>,
# value_to_where<WHERE parameter_to_where = value_to_where>)


def update_to_oracle_with_where(table_name, parameter_to_set, value_to_set, parameter_to_where, value_to_where):
    try:
        if not ((type(table_name) == str
                    and
                type(parameter_to_set) == str
                    and
                type(parameter_to_where) == str
                )
                    and
                (
                type(value_to_set) == str
                    or
                type(value_to_set) == int
                    or
                type(value_to_set) == float
                )
                    and
                (
                type(value_to_where) == str
                    or
                type(value_to_where) == int
                    or
                type(value_to_where) == float
                )
        ):
            raise Exception

        if type(value_to_set) == str:
            value_to_set = "'" + value_to_set + "'"

        if type(value_to_where) == str:
            value_to_where = "'" + value_to_where + "'"

        cur = conn.cursor()
        update_statement = f"UPDATE {table_name.upper()} SET {parameter_to_set.upper()}={value_to_set} WHERE {parameter_to_where.upper()}={value_to_where}"
        cur.execute(update_statement)

    except Exception as err:
        print(f'{update_statement}\nBlad przy wykonywaniu funkcji update_to_oracle_with_where: ', err)

    else:
        print('Wstawianie danych powiodlo sie.')
        print(f'Wykonano polecenie {update_statement}\n')
        conn.commit()

    finally:
        cur.close()


def update_to_oracle(table_name, parameter_to_set, value_to_set):
    try:
        if not (
                (type(table_name) == str
                    and
                type(parameter_to_set) == str
                )
                    and
                (type(value_to_set) == str
                    or
                 type(value_to_set) == int
                    or
                 type(value_to_set) == float
                )
        ):
            raise Exception

        if type(value_to_set) == str:
            value_to_set = "'" + value_to_set + "'"

        cur = conn.cursor()
        update_statement = f"UPDATE {table_name.upper()} SET {parameter_to_set.upper()}={value_to_set}"
        cur.execute(update_statement)

    except Exception as err:
        print(f'{update_statement}\nBlad przy wykonywaniu funkcji update_to_oracle: ', err)

    else:
        print('Wstawianie danych powiodlo sie.')
        print(f'Wykonano polecenie {update_statement}\n')
        conn.commit()

    finally:
        cur.close()


