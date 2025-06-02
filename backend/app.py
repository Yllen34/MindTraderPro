"""
Fichier principal de l'application Flask.
Initialise l'application, charge la configuration et configure les extensions.
"""

from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Chargement des variables d'environnement
load_dotenv()

def create_app():
    """Factory pour créer et configurer l'application Flask."""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')
    CORS(app, resources={r"/*": {"origins": "*"}})

    # Enregistrement des blueprints
    register_blueprints(app)

    return app

def register_blueprints(app):
    """Enregistre les blueprints pour les routes."""
    from routes.main_routes import main_bp
    from routes.calculateur import calculateur_bp
    from routes.journal import journal_bp

    app.register_blueprint(main_bp, url_prefix='/api')
    app.register_blueprint(calculateur_bp, url_prefix='/api')
    app.register_blueprint(journal_bp, url_prefix='/api')

# Création de l'application
app = create_app()

@app.route('/')
def serve_frontend():
    """Sert le fichier HTML principal du frontend."""
    frontend_path = os.path.join(os.path.dirname(__file__), '..', 'frontend')
    return send_from_directory(frontend_path, 'main.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=os.getenv('FLASK_DEBUG', 'False') == 'True')
