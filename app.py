from flask import Flask, request, jsonify, render_template
from scanner import scan_target

app = Flask(__name__)

# 🏠 Home Route - Serves the Web UI
@app.route('/')
def home():
    return render_template('index.html')  # Make sure index.html is inside the "templates" folder

# 🕵️‍♂️ Vulnerability Scan API
@app.route('/scan', methods=['POST'])
def scan():
    data = request.json
    target = data.get("target")

    if not target:
        return jsonify({"error": "Target IP is required"}), 400

    try:
        scan_results = scan_target(target)
        return jsonify(scan_results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

