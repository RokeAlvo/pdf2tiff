import os

from flask import render_template, request, send_file
from werkzeug.utils import secure_filename

from pdf2tiff import app
from pdf2tiff.utilites.pdf2tiff import pdf2tiff
from tempfile import TemporaryDirectory, gettempdir


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


# uploads_dir = os.path.join(app.instance_path, 'uploads')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        img = request.files['img']
        uploads_dir = TemporaryDirectory()
        file_name = os.path.join(uploads_dir.name, secure_filename(img.filename))
        img.save(file_name)
        tiff_img = pdf2tiff(file_name)

        return send_file(
            # directory=some_directory,
            tiff_img,
            # mimetype='application/pdf',
            attachment_filename='ohhey.tiff'
        )

    return render_template('index.html')
