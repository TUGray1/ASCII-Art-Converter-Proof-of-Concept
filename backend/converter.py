from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np

app = Flask(__name__)
CORS(app)

ASCII_CHARS = ' .:-=+*#%@'

@app.route('/convert', methods=['POST'])
def convert_to_ascii():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image provided'}), 400
        
        file = request.files['image']
        
        image_bytes = file.read()
        nparr = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
        
        if img is None:
            return jsonify({'error': 'Invalid image format'}), 400
        
        width = 80
        aspect_ratio = img.shape[0] / img.shape[1]
        height = int(width * aspect_ratio * 0.5)
        
        img_resized = cv2.resize(img, (width, height))
        
        ascii_art = ''
        for row in img_resized:
            for pixel in row:
                char_index = int((pixel / 255) * (len(ASCII_CHARS) - 1))
                ascii_art += ASCII_CHARS[char_index]
            ascii_art += '\n'
        
        return jsonify({
            'success': True,
            'ascii': ascii_art,
            'width': width,
            'height': height
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'Server is running!'})

if __name__ == '__main__':
    print("Starting Flask server on http://localhost:5000")
    app.run(debug=True, port=5000)