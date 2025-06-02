from flask import Blueprint, render_template, jsonify

# Création du blueprint principal
main_bp = Blueprint('main', __name__)

# Route de test simple pour vérifier le bon fonctionnement
@main_bp.route('/ping')
def ping():
    return jsonify({"message": "pong"})

# Route pour afficher l'interface du journal de trading
@main_bp.route('/test-journal')
def test_journal():
    return render_template('test_journal_complet.html')