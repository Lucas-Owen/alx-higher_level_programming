#!/usr/bin/python3
"""
Thi script displays all values in the states table of hbtn_0e_0_usa
where name matches the argument passed
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
        state_name = argv[4]
        query = """
                SELECT * FROM states
                WHERE BINARY name='{:s}'
                ORDER BY id ASC;
                """.format(state_name)
        cursor.execute(query)
        for row in cursor.fetchall():
            print(row)
        cursor.close()
        db.close()
    except Exception as e:
        print(e)
