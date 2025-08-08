from flask import Flask, request, jsonify, render_template, send_file, abort
from flask_cors import CORS
import csv
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)  # später kannst du hier origins=["https://deine-seite.de"] setzen

PASSWORT = "12345678910"  # DEIN Passwort für beide Downloads!

@app.route('/api/signup', methods=['POST'])
def signup():
    email = request.json.get('email')
    if not email:
        return jsonify({'success': False, 'message': 'Keine E-Mail übergeben.'}), 400

    # E-Mails aus CSV einlesen
    emails = set()
    if os.path.exists('emails.csv'):
        with open('emails.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            emails = {row[0].strip().lower() for row in reader if row}

    if email.strip().lower() in emails:
        return jsonify({'success': False, 'message': 'Du bist bereits eingetragen!'}), 400

    # Neue E-Mail speichern
    with open('emails.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([email])

    return jsonify({'success': True, 'message': 'Danke! Sie erhalten gleich eine Bestätigungs-E-Mail.'})


@app.route('/api/track_click', methods=['POST'])
def track_click():
    data = request.json
    button = data.get('button', 'unknown')
    timestamp = datetime.now().isoformat(timespec='seconds')

    with open('button_clicks.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([button, timestamp])

    return jsonify({'success': True})


@app.route('/api/track_view', methods=['POST'])
def track_view():
    timestamp = datetime.now().isoformat(timespec='seconds')

    with open('page_views.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp])

    return jsonify({'success': True})

# === Download-Endpunkt für emails.csv ===
@app.route('/download-emails')
def download_emails():
    pw = request.args.get("pw", "")
    if pw != PASSWORT:
        abort(403)
    return send_file('emails.csv', as_attachment=True)

# === Download-Endpunkt für button_clicks.csv ===
@app.route('/download-clicks')
def download_clicks():
    pw = request.args.get("pw", "")
    if pw != PASSWORT:
        abort(403)
    return send_file('button_clicks.csv', as_attachment=True)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
