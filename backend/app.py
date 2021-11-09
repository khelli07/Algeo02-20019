from flask import Flask, request, json
from flask_cors import CORS
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath
from SVD import hello

app = Flask(__name__)
CORS(app)

ALLOWED_EXT = {'png', 'jpg', 'jpeg'}
BACKEND_UPLOAD = join(dirname(realpath(__file__)), 'uploaded_pics\\')
app.config['BACKEND_UPLOAD'] = BACKEND_UPLOAD

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT

@app.route('/', methods=['GET'])
def home():
    return {'message': hello()}

@app.route('/upload', methods = ['POST'])
def upload():
    file = request.files['file']
    if not file:
        return "No image uploaded", 400
    elif allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(join(app.config['BACKEND_UPLOAD'], filename))
        return {"filename": file.filename,
            "message": "Image successfully uploaded"}, 200
    else:
        return "Extension allowed are .jpg, .jpeg, and .png", 403

@app.route('/SVD')
def SVD():
    return "Ini svd"

if __name__ == "__main__":
    app.run(debug=True)