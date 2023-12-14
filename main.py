from flask import Flask, render_template, request, send_file,jsonify, session, redirect, url_for,send_from_directory

import os


app = Flask(__name__, static_folder='static')
app.secret_key = 'meni_the_coder'

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/png')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/thankyou')
def thanks():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)
