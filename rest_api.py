import os

from flask import Flask, request, redirect, \
    url_for, render_template, \
    send_from_directory, send_file
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'store'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
    return render_template("index.html")


# @app.route('/store/<filename>')
# def get_uploaded_file(filename):
#     return send_from_directory(
#         app.config['UPLOAD_FOLDER'],
#         filename
#     )


@app.route('/download/<path:filename>')
def download_file(filename):
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(path):
        return send_file(path, as_attachment=True)
    return redirect(url_for('upload_file'))


@app.route('/delete/<path:filename>')
def delete_file(filename):
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(path):
        os.remove(path)
    return redirect(url_for('upload_file'))


def del_files_in_path(path):
    filenames = []
    for root, dirs, files in os.walk(path):
        for filename in files:
            filenames.append(filename)
    for filename in filenames:
        file = os.path.join(path, filename)
        os.remove(file)


def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        print(path, '- dir already exists')


# create_dir(UPLOAD_FOLDER)
# del_files_in_path(UPLOAD_FOLDER)


app.run()
