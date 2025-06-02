"""
Module complet de calcul de lot pour MindTraderPro.
Gère tous les cas : SL/TP en pips ou prix, sens du trade, R:R, conversions.
"""

from flask import Blueprint, request, jsonify

calculateur_bp = Blueprint('calculateur', __name__)

@calculateur_bp.route('/calculateur', methods=['POST'])
def calculateur():
    try:
        data = request.json

        capital = float(data.get('capital'))
        risque_pourcentage = float(data.get('risque_pourcentage'))
        devise = data.get('devise', 'USD').upper()
        sens = data.get('sens', 'buy').lower()
        pip_value = float(data.get('pip_value', 10))  # Valeur par défaut pour EURUSD
        prix_entree = float(data.get('prix_entree'))
        stop_loss = data.get('stop_loss')
        take_profit = data.get('take_profit')

        # Détection automatique : SL en pips ou en prix
        if isinstance(stop_loss, dict):
            sl_pips = abs(prix_entree - float(stop_loss.get('prix'))) * (10 ** 5)
        else:
            sl_pips = float(stop_loss)

        # Détection automatique : TP en pips ou en prix
        if isinstance(take_profit, dict):
            tp_pips = abs(float(take_profit.get('prix')) - prix_entree) * (10 ** 5)
        else:
            tp_pips = float(take_profit)

        montant_risque = capital * (risque_pourcentage / 100)
        lot_size = montant_risque / (sl_pips * pip_value)
        potentiel_gain = tp_pips * pip_value * lot_size
        ratio_risk_reward = round(potentiel_gain / montant_risque, 2) if montant_risque > 0 else 0

        return jsonify({
            "status": "success",
            "capital": capital,
            "devise": devise,
            "sens": sens,
            "prix_entree": prix_entree,
            "stop_loss_pips": round(sl_pips, 1),
            "take_profit_pips": round(tp_pips, 1),
            "montant_risque": round(montant_risque, 2),
            "lot_size": round(lot_size, 2),
            "potentiel_gain": round(potentiel_gain, 2),
            "risk_reward": ratio_risk_reward
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400
