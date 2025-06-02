"""
Blueprint pour les routes principales de l'application.
Contient les endpoints de base comme /ping.
"""

from flask import Blueprint, jsonify

# Création du Blueprint
main_bp = Blueprint('main', __name__)

@main_bp.route('/ping', methods=['GET'])
def ping():
    """
    Endpoint de test pour vérifier l'état de l'API.
    Retourne 'pong' avec un code HTTP 200.
    """
    return jsonify({"status": "success", "message": "pong"}), 200
