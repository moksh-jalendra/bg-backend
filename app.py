from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from bg import bg_remove
import os

app = Flask(__name__)
# Enable CORS so your frontend at 127.0.0.1:5500 can talk to Render
CORS(app)

upload_folder = "uploads"
os.makedirs(upload_folder, exist_ok=True)

@app.route('/')
def home():
    r@app.route('/')
def home():
    # This lets you verify the code version just by visiting the URL
    return {
        "status": "online",
        "version": "v2-rembg-portable", 
        "engine": "u2netp"
    }, 200

@app.route('/task', methods=['POST'])
def test_image():
    if "myImage" not in request.files:
        return jsonify({"error": "No file sent"}), 400
    
    file = request.files["myImage"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    try:
        # Save the incoming file
        filepath = os.path.join(upload_folder, file.filename)
        file.save(filepath)
        
        # Process the background removal
        bg_remove(filepath)

        # Send the processed image back to the frontend
        return send_file("photo-withoutbg.png", mimetype='image/png')
    
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({"error": "Server processed failed. Likely out of memory."}), 500

if __name__ == '__main__':
    # Render uses Gunicorn, but this allows for local testing
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)