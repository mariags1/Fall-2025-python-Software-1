# asks the user for the ai
import sqlite3

def main():
    # Connect to the database (airports.db should be in the same folder as your script)
    connection = sqlite3.connect("airports.db")
    cursor = connection.cursor()

    # Ask the user for ICAO code
    icao = input("Enter ICAO code: ").strip().upper()

    # Query the database
    cursor.execute("SELECT name, municipality FROM airport WHERE ident = ?", (icao,))
    result = cursor.fetchone()

    if result:
        name, municipality = result
        print(f"Airport name: {name}")
        print(f"Location: {municipality}")
    else:
        print("No airport found with that ICAO code.")

    # Close connection
    connection.close()

if __name__ == "__main__":
    main()
