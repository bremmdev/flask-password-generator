from flask import Flask, request, jsonify
import secrets
import string

app = Flask(__name__)

@app.route('/')
def index():
    password_length, with_specials = get_params()
    
    if password_length > 32:
        return jsonify({'error': 'Password length must be less than 32 characters.'}), 400

    return jsonify(generate_password(password_length, with_specials))


def get_params():
    try:
        password_length = int(request.args.get('length', default=8))
    except ValueError:
        password_length = 8
    with_specials = request.args.get('specials', default='yes').lower() != 'no'
    return password_length, with_specials

def generate_password(length, with_specials):
    charlist = [*string.ascii_letters, *string.digits]
    if with_specials:
        charlist += [*string.punctuation]
    return ''.join([secrets.choice(charlist) for i in range(length)])

if __name__ == "__main__":
    app.run()