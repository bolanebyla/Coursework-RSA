from flask import Flask, render_template, request

from rsa import RSA

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/generate_values', methods=['POST'])
def generate_values():
    number = request.form.get('number')
    last_name = request.form.get('last_name')
    if not number or not last_name:
        return 'Bad Request', 400
    try:
        coder = RSA(number=int(number), last_name=last_name)
    except Exception as e:
        return 'Bad Request', 400
    return coder.__dict__


@app.route('/api/encrypt', methods=['POST'])
def encrypt():
    data = request.form.get('data')
    e = request.form.get('e')
    n = request.form.get('n')
    if not data or not e or not n:
        return 'Bad Request', 400
    if len(e) > 5 or len(n) > 5:
        return 'Bad Request', 400

    try:
        encrypted_data = RSA.encrypt(data=data, e=int(e), n=int(n))
    except Exception as e:
        return 'Bad Request', 400
    return {'encrypted_data': encrypted_data}


@app.route('/api/decrypt', methods=['POST'])
def decrypt():
    data = list(map(int, request.form.get('data').split(',')))
    d = request.form.get('d')
    n = request.form.get('n')
    if not data or not d or not n:
        return 'Bad Request', 400
    try:
        decrypted_data = RSA.decrypt(data=data, d=int(d), n=int(n))
    except Exception as e:
        return 'Bad Request', 400
    return {'decrypted_data': decrypted_data}


if __name__ == '__main__':
    app.run(debug=True)
