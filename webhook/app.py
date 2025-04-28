from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/trigger', methods=['POST'])
def trigger():
    os.system("helm rollback myapp 1")  # Rolls back to revision 1
    return "Rollback triggered", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
