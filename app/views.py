from flask import Blueprint, jsonify, render_template
import mysql.connector

bp = Blueprint('main', __name__)

def execute_query(query, args=(), one=False):
    conn = bp.app.config['get_db_connection']()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, args)
    result = cursor.fetchall()
    conn.close()
    return result[0] if one else result

@bp.route("/api/books")
def data_books_all():
    query = "SELECT * FROM books"
    items = execute_query(query)
    return jsonify(items)

@bp.route("/books")
def books():
    response = data_books_all()
    return response.get_data(as_text=True)

@bp.route("/test")
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

@bp.route("/")
def homepage():
    return render_template("home.html")

@bp.route("/movies")
def movies():
    return render_template("movies.html")

@bp.route("/movie")
def movie():
    return render_template("movie.html")
