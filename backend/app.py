"""
Fichier principal de l'application Flask.
Initialise l'application, charge la configuration et configure les extensions.
"""

from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Chargement des variables d'environnement
load_dotenv()

def create_app():
    """Factory pour créer et configurer l'application Flask."""
    
    # Initialisation de Flask
    app = Flask(__name__)
    
    # Configuration de la clé secrète
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')
    
    # Activation de CORS pour toutes les routes
    CORS(app, resources={r"/*": {"origins": "*"}})
    
    # Enregistrement des blueprints (routes)
    register_blueprints(app)
    
    return app

def register_blueprints(app):
    """Enregistre les blueprints pour les routes."""
    
    # Import dynamique pour éviter les dépendances circulaires
    from routes.main_routes import main_bp
    
    app.register_blueprint(main_bp, url_prefix='/api')

# Création de l'application
app = create_app()

@app.route('/')
def index():
    """Route racine pour vérifier le déploiement."""
    return jsonify({
        "status": "success",
        "message": "MindTraderPro backend is running",
        "version": "1.0.0"
    })

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'False') == 'True')
