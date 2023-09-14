#!/usr/bin/python3
"""
This script takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""


if __name__ == '__main__':
    from sys import argv
    if len(argv) != 5:
        print(f"""Usage: ./{argv[0].replace("./", "")}"""
              """ username password database_name name_to_search""")
        exit(1)
    import MySQLdb
    params = {
        'host': 'localhost',
        'user': argv[1],
        'password': argv[2],
        'database': argv[3],
        'port': 3306
    }
    try:
        db = MySQLdb.connect(**params)
        cursor = db.cursor()
        city_name = argv[4].replace('\'', "\\\'").replace(
            '\"', '\\"').replace(';', '\\;')
        query = """
                SELECT cities.name FROM cities
                INNER JOIN states
                ON states.id = cities.state_id AND states.name='{:s}'
                ORDER BY cities.id ASC;
                """.format(city_name)
        cursor.execute(query)
        results = [name[0] for name in cursor.fetchall()]
        print(', '.join(results))
        cursor.close()
        db.close()
    except Exception as e:
        print(e)
