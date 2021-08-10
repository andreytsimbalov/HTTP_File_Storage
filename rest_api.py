# https://flask-russian-docs.readthedocs.io/ru/latest/patterns/fileuploads.html

import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/store'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# @app.route("/", methods=["POST", "GET"])
# def index():
#     args = {"method": "GET"}
#     if request.method == "POST":
#         file = request.files["file"]
#         if bool(file.filename):
#             file_bytes = file.read(app.config['MAX_CONTENT_LENGTH'])
#             args["file_size_error"] = len(file_bytes) == app.config['MAX_CONTENT_LENGTH']
#         args["method"] = "POST"
#     return render_template("index.html", args=args)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            print("allowed_file")
            print(file.filename)
            filename = secure_filename(file.filename)
            # filename = file.filename
            print("1")
            print(filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            path = app.config['UPLOAD_FOLDER'] + '/' + filename
            print(path)

            # file.save(path)
            file.save('/store/' + filename)
            print("2")

            # return redirect(url_for('uploaded_file',
            #                         filename=filename))
        else:
            print("NOT allowed_file")
    print("3")

    # return render_template("index.html", args={"method": request.method})
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

from flask import send_from_directory

@app.route('/store/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


app.run()

