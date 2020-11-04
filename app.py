from flask import Flask, render_template, request,send_from_directory,render_template_string,flash
from werkzeug.utils import secure_filename
from hwptohtml import change_to_html
import os
import stat

app = Flask(__name__)

@app.route('/')
def render_file():
    return render_template('submit.html')


@app.route('/filedownload', methods = ['GET', 'POST'])
def download_file():
    if request.method == "POST":
        pass
    if request.method == "GET":
        url=request.args.get("url")
        print(url)
    

if __name__ == '__main__':
    app.run(debug = True)
