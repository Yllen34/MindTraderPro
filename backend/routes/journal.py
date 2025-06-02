"""
Journal de trading - module de création d'entrées de journal utilisateur.
"""

from flask import Blueprint, request, jsonify

journal_bp = Blueprint('journal', __name__)

# Stockage temporaire en mémoire (à remplacer par une BDD)
journal_entries = []

@journal_bp.route('/journal', methods=['POST'])
def ajouter_entree_journal():
    """
    Enregistre un trade dans le journal de l'utilisateur.
    """
    try:
        data = request.json

        required_fields = ['pair', 'entry', 'sl', 'tp', 'result', 'risked_amount', 'strategy', 'emotion', 'respected_plan']
        for field in required_fields:
            if field not in data:
                return jsonify({"status": "error", "message": f"Champ requis manquant : {field}"}), 400

        entry = {
            "pair": data['pair'],
            "entry": float(data['entry']),
            "sl": float(data['sl']),
            "tp": float(data['tp']),
            "result": data['result'],  # 'win', 'loss', 'be'
            "risked_amount": float(data['risked_amount']),
            "strategy": data['strategy'],
            "emotion": data['emotion'],  # libre : "confiant", "stressé", etc.
            "respected_plan": bool(data['respected_plan']),
            "commentaire": data.get('commentaire', ""),
        }

        journal_entries.append(entry)

        return jsonify({"status": "success", "message": "Trade ajouté au journal", "data": entry}), 201

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
