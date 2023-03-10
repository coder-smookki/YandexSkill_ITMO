import MySQLdb


def connect():
    conn = MySQLdb.connect(
        host="rc1b-7ap37y1reqrnu47t.mdb.yandexcloud.net",
        port=3306,
        db="utmo",
        user="mytable",
        passwd="utmoyandexadmin",
        ssl={'ca': '~/.mysql/root.crt'})

    cur = conn.cursor()
    cur.execute('SELECT version()')

    print(cur.fetchone()[0])

    conn.close()