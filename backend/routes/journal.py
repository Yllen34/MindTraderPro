from flask import Blueprint, request, jsonify
from services.journal_service import insert_journal_entry

journal_bp = Blueprint('journal', __name__)

@journal_bp.route('/journal', methods=['POST'])
def ajouter_entree_journal():
    """
    Enregistre une entrée dans le journal de trading.
    Les champs requis sont : pair, entry, sl, tp, result, risked_amount, strategy, emotion, respected_plan.
    Le champ commentaire est facultatif.
    """
    try:
        data = request.json

        required_fields = ['pair', 'entry', 'sl', 'tp', 'result', 'risked_amount', 'strategy', 'emotion', 'respected_plan']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    "status": "error",
                    "message": f"Champ requis manquant : {field}"
                }), 400

        insert_journal_entry(data)

        return jsonify({
            "status": "success",
            "message": "Trade ajouté au journal avec succès."
        }), 201

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
