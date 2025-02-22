from flask import Flask, jsonify
from flask_cors import CORS
import threading

app = Flask(__name__)
CORS(app)  # Allow API calls from React & Tkinter

@app.route('/data')
def get_data():
    return jsonify({"message": "Hello from Flask!"})

# Run Flask in a separate thread
def run_flask():
    app.run(debug=True, port=5000, use_reloader=False)  # Avoid reloading issues

if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
