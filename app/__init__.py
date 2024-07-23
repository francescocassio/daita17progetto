from flask import Flask
from .config import Config
import mysql.connector


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    app.config.from_pyfile('config.py', silent=True)

    # Crea la connessione al database
    def get_db_connection():
        return mysql.connector.connect(
            host=app.config['MYSQL_DATABASE_HOST'],
            user=app.config['MYSQL_DATABASE_USER'],
            password=app.config['MYSQL_DATABASE_PASSWORD'],
            database=app.config['MYSQL_DATABASE_DB']
        )

    app.config['get_db_connection'] = get_db_connection

    # Importa e registra le route
    from . import views
    app.register_blueprint(views.bp)

    return app
