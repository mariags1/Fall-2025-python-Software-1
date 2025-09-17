import mysql.connector

from exercise.MySQL import result


def get_airports_by_country(country_code):
    # make the database connection
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='mariasiitonen',
        password='metropolia',
        autocommit=True,
    )

    # make the query to the database
    SQL = f"SELECT type, COUNT(*) as airport_count FROM airport WHERE iso_country = '{country_code}' GROUP BY type ORDER BY airport_count DESC;"
    sql_cursor = connection.cursor()
    sql_cursor.execute(SQL)
    # return the result
    result = sql_cursor.fetchall()
    return result

def run_country_program():
    # asks user the country code
    country_code = input("Give country code: ").upper()
    airports = get_airports_by_country(country_code)
       # print the airports in that country organized by airport type
    print(f"Airports in {country_code}: ")
    for airport in airports:
        print(f"{airport[1]} {airport[0]} airports")

run_country_program()