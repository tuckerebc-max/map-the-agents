from flask import Flask, render_template, request, jsonify, send_file
import os
from Model import get_response
from zip import ziped

app = Flask(__name__)
hist = {}
list = []

@app.route('/')
def hello_world():
    item1 = list[0] if len(list) == 1 else None
    return render_template("index.html", name=hist, mess=item1)

@app.route('/', methods=["POST", "GET"])
def he():
    if request.method == "POST":
        name = request.form["message"]
        list.clear()
        list.append(name)
        response = get_response(name)
        hist[name.capitalize()] = response
        upload_result = upload_file()
        print(upload_result['message'])
        if upload_result['message'] == "File uploaded successfully":
            ziped()
    return hello_world()

@app.route('/download')
def download():
    return send_file('Zipped file.zip', as_attachment=True)

def upload_file():
    file = request.files['file']
    if file.filename == "":
        return {'message': 'File uploaded unsuccessfully'}
    upload_folder = 'static/uploded/cast'
    file.filename = "bot.json"
    file.save(os.path.join(upload_folder, file.filename))
    return {'message': 'File uploaded successfully'}

if __name__ == "__main__":
    app.run(debug=True)
