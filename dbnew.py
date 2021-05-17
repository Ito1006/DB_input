import psycopg2
#Von der Config.py wird die Function config importiert
from config import config

#Verbindung mit der Datenbank aufbauen
params = config()
print('Verbindung mit der postgreSQL Datenbank wird hergestellt ...')
con = psycopg2.connect(**params)

#Verbindung erfolgreich check
print ('Verbindung mit der postgreSQL Datenbank erfolgreich hergestellt!')

cursor = con.cursor()

postgres_insert_query = """INSERT INTO playground (type, color, location, install_date) VALUES ('rutsche', 'lila', 'south', '2021-05-07')"""
cursor.execute(postgres_insert_query)

con.commit()
print('Eintrag zu playground hinzugefügt')

#Verbindung mit der Datenbank beenden
cursor.close()
con.close()
