import psycopg2

#Verbindung mit der Datenbank aufbauen
con=psycopg2.connect(
    host = '192.168.136.132',
    database = 'benjamin',
    user = 'benjamin',
    password = 'benjamin')

#Verbindung erfolgreich check
print ('Finally - Verbindung erfolgreich')

cursor = con.cursor()

postgres_insert_query = """INSERT INTO playground (type, color, location, install_date) VALUES ('rutsche', 'lila', 'south', '2021-05-07')"""
cursor.execute(postgres_insert_query)

con.commit()
print('Eintrag zu playground hinzugefügt')

#Verbindung mit der Datenbank beenden
cursor.close()
con.close()
