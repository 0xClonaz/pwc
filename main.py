from flask import Flask, request, jsonify
import pwnedpasswords

app = Flask(__name__)

@app.route('/api/v1/check_if_pw_leaked', methods=['GET'])
def check_password():
    password = request.args.get('password')
    if not password:
        return jsonify({'error': 'No password provided'}), 400

   
    pw2 = pwnedpasswords.check(password)
    print(pw2)
    data = {
        'Password': password
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
 
    if pw2 > 0:
        return jsonify({'found_in_leaked_databases': str(pw2), 'leaked': True})
    else:
        return jsonify({'leaked': False})

if __name__ == '__main__':
    app.run(debug=True)
