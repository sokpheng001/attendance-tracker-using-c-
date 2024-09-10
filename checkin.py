from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)

# Replace with your actual bot token and chat ID
TELEGRAM_BOT_TOKEN = "Your token"
TELEGRAM_CHAT_ID = "you chat ID"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    response = requests.post(url, json=payload)
    return response.json()

@app.route('/checkin')
def checkin():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', timestamp=current_time)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5466)