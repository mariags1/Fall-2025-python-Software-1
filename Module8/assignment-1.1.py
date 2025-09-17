import mysql.connector

from exercise.MySQL import result

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'mariasiitonen',
    password = 'metropolia',
    autocommit = True,
)

# asks the user for the airport ICAO code
ICAO_code = input("Give airport ICAO code: ").upper()

# fetches the information of the airport with that code
SQL = f"SELECT name, municipality FROM airport WHERE ident='{ICAO_code}'"
sql_cursor = connection.cursor()
sql_cursor.execute(SQL)
result = sql_cursor.fetchone()

# prints the location and name of the airport
print(f"Airport name: {result[0]} Location: {result[1]}")
