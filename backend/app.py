import os
from flask import Flask, request, json, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath
from SVD import *

app = Flask(__name__)
CORS(app)

ALLOWED_EXT = {'png', 'jpg', 'jpeg'}
BACKEND_UPLOAD = join(dirname(realpath(__file__)), 'uploaded_pics\\')
app.config['BACKEND_UPLOAD'] = BACKEND_UPLOAD

def allowed_file(filename):
    return ('.' in filename) and (filename.rsplit('.', 1)[-1].lower() in ALLOWED_EXT)

@app.route('/', methods=['GET'])
def home():
    return "Hello from the API!"

@app.route('/upload', methods = ['POST'])
def upload():
    file = request.files['file']
   
    if allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(join(app.config['BACKEND_UPLOAD'], filename))
        response = app.response_class(
            response = json.dumps(
                {"message": "Upload image successful!"}), 
                status = 200)

    else:
        response = app.response_class(
            response = json.dumps(
                {"error": "Extension allowed are .jpg, .jpeg, and .png"}), 
                status = 400)
    
    return response

@app.route('/compressed/<string:imgname>/<int:percent>', methods = ['GET'])
def compressed(imgname, percent):
    file_dir = app.config['BACKEND_UPLOAD']
    imgpath = file_dir + imgname
    output_dir = file_dir + f"{percent}_{imgname}"
    if not(os.path.isfile(output_dir)):
        _ = compressImage(imgpath, percent, output_dir)
    return send_file(output_dir, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)