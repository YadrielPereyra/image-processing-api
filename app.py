from flask import Flask, request, jsonify, send_from_directory
from PIL import Image
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided.'}), 400
    file = request.files['file']
    filename = secure_filename(file.filename)
    path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(path)

    # Process image (convert to grayscale as example)
    img = Image.open(path).convert('L')
    processed_path = os.path.join(PROCESSED_FOLDER, filename)
    img.save(processed_path)

    return jsonify({'message': f'File {filename} uploaded and processed.'})

@app.route('/files', methods=['GET'])
def list_files():
    files = os.listdir(PROCESSED_FOLDER)
    return jsonify({'processed_files': files})

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(PROCESSED_FOLDER, filename, as_attachment=True)

@app.route('/delete/<filename>', methods=['DELETE'])
def delete_file(filename):
    path = os.path.join(PROCESSED_FOLDER, filename)
    if os.path.exists(path):
        os.remove(path)
        return jsonify({'message': f'{filename} deleted.'})
    else:
        return jsonify({'error': 'File not found.'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
