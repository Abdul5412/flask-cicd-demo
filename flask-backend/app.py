from flask import Flask, jsonify
import os, socket

app = Flask(__name__)

@app.route('/api/hello')
def hello():
    return jsonify({
        "message": "Hello from Flask backend!",
        "hostname": socket.gethostname(),
        "version": os.getenv("APP_VERSION", "v1")
    })

@app.route('/api/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
