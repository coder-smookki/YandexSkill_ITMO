import mysql.connector

conn = mysql.connector.connect(
    host="rc1b-7ap37y1reqrnu47t.mdb.yandexcloud.net",
    user="mytable",
    password="utmoyandexadmin",
    database="utmo"
)

# Проверяем, что подключение установлено
if conn.is_connected():
    print("Connected to MySQL database")

user_id = 'user123'
language = 'en'

query = "INSERT INTO mytable (id, user_id, language) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE language=%s"
values = (1, user_id, language, language)

cursor = conn.cursor()
cursor.execute(query, values)
conn.commit()

# Фиксируем изменения в базе данных
conn.commit()

# Закрываем курсор и подключение
cursor.close()
conn.close()
