from flask import Blueprint, request, jsonify, send_file
from services.journal_service import create_entry, get_all_entries, update_entry, delete_entry
import os
from datetime import datetime
import openai
from werkzeug.utils import secure_filename
import csv

journal_bp = Blueprint('journal', __name__, url_prefix='/api/journal')

@journal_bp.route('', methods=['POST'])
def add_entry():
    data = request.json
    create_entry(data)
    return jsonify({'status': 'success', 'message': 'Trade ajouté'}), 201

@journal_bp.route('', methods=['GET'])
def get_entries():
    entries = get_all_entries()
    return jsonify(entries)

@journal_bp.route('/<int:entry_id>', methods=['PUT'])
def modify_entry(entry_id):
    data = request.json
    update_entry(entry_id, data)
    return jsonify({'status': 'success', 'message': 'Trade modifié'})

@journal_bp.route('/<int:entry_id>', methods=['DELETE'])
def remove_entry(entry_id):
    delete_entry(entry_id)
    return jsonify({'status': 'success', 'message': 'Trade supprimé'})

@journal_bp.route('/transcription', methods=['POST'])
def transcribe_audio():
    audio_file = request.files['audio']
    path = os.path.join('uploads', secure_filename(audio_file.filename))
    audio_file.save(path)

    openai.api_key = os.getenv("OPENAI_API_KEY")

    with open(path, "rb") as f:
        transcript = openai.Audio.transcribe("whisper-1", f)

    return jsonify({
        'status': 'success',
        'transcription': transcript['text'],
        'audio_path': path
    })

@journal_bp.route('/export', methods=['GET'])
def export_csv():
    entries = get_all_entries()
    filename = f"journal_export_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"
    path = os.path.join('exports', filename)
    os.makedirs('exports', exist_ok=True)

    with open(path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['date', 'paire', 'type', 'lot', 'entry', 'sl', 'tp', 'rr', 'gain', 'note', 'tag', 'audio_path']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in entries:
            writer.writerow(entry)

    return send_file(path, as_attachment=True)