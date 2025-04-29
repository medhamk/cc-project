# from flask import Flask, request
# import os

# app = Flask(__name__)

# @app.route('/trigger', methods=['POST'])
# def trigger():
#     os.system("helm rollback myapp 1")  # Rolls back to revision 1
#     return "Rollback triggered", 200

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/trigger', methods=['POST'])
def trigger_rollback():
    release_name = "myapp"

    try:
        history_output = subprocess.check_output(
            ["helm", "history", release_name, "--output", "json"]
        ).decode("utf-8")

        import json
        history = json.loads(history_output)

        if len(history) < 2:
            return "No previous revision to rollback to.", 400

        # Get the second last revision (previous one)
        previous_revision = history[-2]['revision']

        subprocess.check_output(
            ["helm", "rollback", release_name, str(previous_revision)]
        )

        return f"Rolled back {release_name} to revision {previous_revision}", 200

    except subprocess.CalledProcessError as e:
        return f"Helm error: {e.output.decode('utf-8')}", 500
    except Exception as ex:
        return f"Unexpected error: {str(ex)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
