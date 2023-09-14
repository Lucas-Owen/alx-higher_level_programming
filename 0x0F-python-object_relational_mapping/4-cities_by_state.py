#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == '__main__':
    from sys import argv
    if len(argv) != 4:
        print(f"""Usage: ./{argv[0].replace("./", "")} """
              """username password database_name""")
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
        query = """
                SELECT * FROM cities
                ORDER BY id ASC;
                """
        cursor.execute(query)
        for row in cursor.fetchall():
            print(row)
        cursor.close()
        db.close()
    except Exception as e:
        print(e)
