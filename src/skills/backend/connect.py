import MySQLdb


def connect():
    conn = MySQLdb.connect(
        host=HOST,
        port=PORT,
        db=DBNAME,
        user=USERNAME,
        passwd=PASSWORDNAME,
        ssl=SSL)

    cur = conn.cursor()
    cur.execute('SELECT version()')

    print(cur.fetchone()[0])

    conn.close()
