import flask
from flask import request, jsonify, abort


app = flask.Flask(__name__, template_folder='templates')
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello World!</h1>"

@app.route('/login', methods=['GET'])
def login():
    return flask.render_template('login.html')

@app.route('/login-form', methods=['POST'])
def login_form():
    if not request.form:
        abort(400)
    login_data = request.form
    if login_data['username'] == 'admin' and login_data['password'] == 'admin':
        return jsonify({'status': 'ok'}), 200
    
    return jsonify({'status': 'ERROR'}), 400

if __name__ == '__main__':
    app.run('127.0.0.1', 5000)
