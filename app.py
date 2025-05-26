from flask import Flask, jsonify, send_from_directory
import subprocess

app = Flask(__name__, static_folder='wwwroot')

@app.route('/api/nvidia-smi')
def get_nvidia_smi():
    try:
        result = subprocess.run(['nvidia-smi', '-L'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            return jsonify({'error': 'Failed to run nvidia-smi', 'details': result.stderr}), 500
        return jsonify({'output': result.stdout.strip()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def serve_frontend():
    return send_from_directory('wwwroot', 'index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
