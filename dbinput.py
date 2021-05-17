import psycopg2


#Verbindung mit der Datenbank aufbauen
con=psycopg2.connect(
    host = input('Geben Sie bitte die IP Adresse der Datenbank ein mit der Sie sich verbinden möchten: '),
    database = input('Geben Sie bitte den Namen der Datenbank ein mit der Sie sich verbinden möchten: '),
    user = input('Geben Sie bitte Ihren Benutzernamen ein: '),
    password = input('Geben Sie bitte Ihr Passwort ein: '))

print('Verbindung mit der postgreSQL Datenbank wird hergestellt ...')

#Verbindung erfolgreich check
print ('Verbindung mit der postgreSQL Datenbank erfolgreich hergestellt!')

#Cursor erstellen
cursor = con.cursor()

#Datenbank input abfragen
inputType = "'" + input('Geben Sie bitte den Typ des Spielzeugs ein: ') + "'"
inputColor = "'" + input('Geben Sie bitte den Farbe des Spielzeugs ein: ') + "'"
inputLocation = "'" + input('Geben Sie bitte den Ort des Spielzeugs ein(mögliche Orte: north, south, west, east): ') + "'"
inputInstall_date = "'" + input('Geben Sie bitte das Datum ein, an dem Sie das Spielzeug aufgestellt haben: ') + "'"

postgres_insert_query = """INSERT INTO playground (type, color, location, install_date) VALUES (""" + inputType + ', ' + inputColor + ', ' + inputLocation +  ', ' + inputInstall_date + ')'
cursor.execute(postgres_insert_query)

con.commit()
print('Eintrag zu playground hinzugefügt')

#Verbindung mit der Datenbank beenden
cursor.close()
con.close()
