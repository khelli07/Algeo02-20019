from flask import Flask, request, json, send_file
from flask_cors import CORS
from numpy.core.fromnumeric import compress
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath
from SVD import *
import os

app = Flask(__name__)
CORS(app)

ALLOWED_EXT = {'png', 'jpg', 'jpeg'}
# Do we need to save the file ?
BACKEND_UPLOAD = join(dirname(realpath(__file__)), 'uploaded_pics\\')
app.config['BACKEND_UPLOAD'] = BACKEND_UPLOAD

def allowed_file(filename):
    return ('.' in filename) and (filename.rsplit('.', 1)[-1].lower() in ALLOWED_EXT)

@app.route('/', methods=['GET'])
def home():
    return "Hello from the API!"

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    file = request.files['file']
   
    if allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(join(app.config['BACKEND_UPLOAD'], filename))
        response = app.response_class(
            response = json.dumps(
                {"message": "Upload image successful!"}), 
                status = 200)
        return response
    else:
        response = app.response_class(
            response = json.dumps(
                {"error": "Extension allowed are .jpg, .jpeg, and .png"}), 
                status = 400)
    
    return response

@app.route('/compressed/<string:imgname>/<int:percent>', methods = ['GET'])
def compressed(imgname, percent):
    file_dir = app.config['BACKEND_UPLOAD']
    img = cv.imread(file_dir + imgname)

    b, g, r = cv.split(img)
    reducedRed = getReducedMatrix(r, percent)
    reducedGreen = getReducedMatrix(g, percent)
    reducedBlue = getReducedMatrix(b, percent)

    compressed = cv.merge((reducedBlue, reducedGreen, reducedRed)).astype('uint8')
    outdir = file_dir + f"{percent}_{imgname}"
    cv.imwrite(outdir, compressed)
    return send_file(outdir)

if __name__ == "__main__":
    app.run(debug=True)