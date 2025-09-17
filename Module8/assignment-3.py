import mysql.connector
from geopy.distance import geodesic
from exercise.MySQL import result

def get_airport_coordinates(icao_code):
    connection = mysql.connector.connect(
        host = '127.0.0.1',
        port = 3306,
        database = 'flight_game',
        user = 'mariasiitonen',
        password = 'metropolia',
        autocommit = True,
    )
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao_code}'"
    sql_cursor = connection.cursor()
    sql_cursor.execute(sql)
    result = sql_cursor.fetchone()
    return result

def run_airport_distance():
    icao_code_1 = input("Enter the ICAO code of the first airport: ").upper()
    icao_code_2 = input("Enter the ICAO code of the first airport: ").upper()
    airport_1 = get_airport_coordinates(icao_code_1)
    airport_2 = get_airport_coordinates(icao_code_2)
    distance = geodesic(airport_1, airport_2)
    print(f"Distance between {icao_code_1} and {icao_code_2}: {distance} kilometers")

run_airport_distance()
