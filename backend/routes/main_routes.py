from flask import Blueprint, jsonify, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return jsonify({
        "message": "MindTraderPro backend is running",
        "status": "success",
        "version": "1.0.0"
    })

@main_bp.route('/test-journal')
def test_journal():
    return render_template("journal_tester.html")