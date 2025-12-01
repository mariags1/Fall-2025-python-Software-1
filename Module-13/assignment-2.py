from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = "airports.db"   # <-- your course database file


def get_airport_by_icao(icao):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute(
        "SELECT ident, name, municipality FROM airport WHERE ident = ?",
        (icao.upper(),)
    )
    row = cursor.fetchone()
    connection.close()
    return row


@app.route("/airport/<icao>", methods=["GET"])
def airport_info(icao):
    airport = get_airport_by_icao(icao)

    if airport is None:
        return jsonify({"error": "Airport not found"}), 404

    ident, name, municipality = airport

    result = {
        "ICAO": ident,
        "Name": name,
        "Location": municipality
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
