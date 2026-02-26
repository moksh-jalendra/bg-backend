from flask import Flask , request , jsonify , send_file
from flask_cors import CORS
from bg import bg_remove
import os 

app = Flask('__name__')
CORS(app)

upload_folder = "uploads"
os.makedirs(upload_folder,exist_ok=True)

@app.route('/task' , methods=['GET' , 'POST'])
def test_image():
    if "myImage" not in request.files:
        return jsonify({"eroor":"no file sent"}) , 400
    file = request.files["myImage"]
    if file.filename == "":
        return jsonify({"errors":"no file selected"})
    if file :
        filepath = os.path.join(upload_folder,file.filename)
        file.save(filepath)
        bg_remove(filepath)

        return send_file("photo-withoutbg.png" , mimetype= 'image/png')
    

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)