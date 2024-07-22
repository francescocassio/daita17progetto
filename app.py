import json
import os

import mysql.connector
from flask import Flask, jsonify, render_template

app = Flask(__name__)
# database MySQL
# Carica configurazione di base
app.config.from_object('config.DevelopmentConfig')

# Sovrascrivi con configurazione locale, se esiste
if os.path.exists('config_local.py'):
    app.config.from_object('config_local.DevelopmentConfig')

# Crea il dizionario db_config basato sulle configurazioni di Flask
db_config = {
    'host': app.config['MYSQL_DATABASE_HOST'],
    'user': app.config['MYSQL_DATABASE_USER'],
    'password': app.config['MYSQL_DATABASE_PASSWORD'],
    'database': app.config['MYSQL_DATABASE_DB']
}

# Funzione per creare una connessione al database
def create_db_connection():
    return mysql.connector.connect(**db_config)

# Funzione per eseguire query SQL
def execute_query(query, params=None):
    connection = create_db_connection()
    cursor = connection.cursor(dictionary=True)
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


#route di esempio
@app.route("/api/books")
def data_books_all():
    query = "SELECT * FROM books"
    items = execute_query(query)
    return jsonify(items)
#
@app.route("/books")
def books():
    data=data_books_all()
    return data.get_json()

@app.route("/test")
def test():
    response = data_books_all()

    # Accesso ai dati della response
    data = response.get_data(as_text=True)
    status_code = response.status_code
    headers = response.headers
    mimetype = response.mimetype
    content_type = response.content_type
    json_data = response.get_json()

    # Stampa delle informazioni per debug
    print(f"Data: {data}")
    print(f"Status Code: {status_code}")
    print(f"Headers: {headers}")
    print(f"MIME Type: {mimetype}")
    print(f"Content Type: {content_type}")
    print(f"JSON Data: {json_data}")

    # Restituisce i dati JSON
    return jsonify(json_data)

#fine route di esempio


@app.route("/")
def homepage():
    return render_template("home.html")



@app.route("/movies")
def movies():

    return render_template("movies.html")

@app.route("/movie")
def movie():

    return render_template("movie.html")



if __name__ == '__main__':
    app.run(debug=True)
