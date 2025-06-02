import sys
import os
import tempfile
import openai
from flask import request
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Blueprint, request, jsonify
from services.journal_service import insert_journal_entry, get_all_journal_entries

journal_bp = Blueprint('journal', __name__)

@journal_bp.route('/journal', methods=['POST'])
def ajouter_entree_journal():
    try:
        data = request.json

        required_fields = [
            'pair', 'entry', 'sl', 'tp', 'result',
            'risked_amount', 'strategy', 'emotion', 'respected_plan'
        ]
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
            "message": str(e)}
        ), 500


@journal_bp.route('/journal', methods=['GET'])
def lire_journal():
    try:
        entries = get_all_journal_entries()
        return jsonify({
            "status": "success",
            "data": entries
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

import tempfile
import openai
from flask import request

@journal_bp.route('/journal/transcription', methods=['POST'])
def transcrire_note_vocale():
    """
    Transcrit un fichier audio ou vidéo (mp3, wav, mp4, m4a, etc.)
    en texte via l'API Whisper (OpenAI).
    """
    try:
        if 'audio' not in request.files:
            return jsonify({"status": "error", "message": "Fichier audio manquant"}), 400

        audio_file = request.files['audio']

        # Sauvegarde temporaire
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_audio:
            audio_file.save(temp_audio.name)

            # Transcription avec OpenAI Whisper
            openai.api_key = os.getenv("OPENAI_API_KEY")
            transcription = openai.Audio.transcribe("whisper-1", open(temp_audio.name, "rb"))

        return jsonify({
            "status": "success",
            "transcription": transcription["text"]
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
