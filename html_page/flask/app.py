from flask import *
import os

app=Flask(__name__,template_folder='templates', static_folder='static')
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/UPLOAD_FOLDER'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.secret_key = 'super secret key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def hello():
    return render_template("bikeRec1.html")

@app.route('/aboutUs/')
def aboutUs():
    return render_template('aboutUs.html')

@app.route('/upload/')
def upload():
    return render_template('upload.html')


@app.route('/success', methods = ['POST','GET'])  
def success():  
    if request.method == 'POST':  
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('', name=filename))
    return render_template('success.html')
    
if __name__ == '__main__':
    
    app.run()