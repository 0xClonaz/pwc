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
        
@app.route('/api/v1/search_email', methods=['GET'])
def search_email():
    email = request.args.get('email')
    if not email:
        return jsonify({'error': 'No email provided'}), 400

    url = "https://api-experimental.snusbase.com/data/search"
    headers = {
        "Auth": "sbx39mh542d0oshydtx3oes9whn1ay",
        "Content-Type": "application/json"
    }
    data = {
        "terms": [email],
        "types": ["email"],
        "wildcard": False
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to fetch data from Snusbase'}), response.status_code


if __name__ == '__main__':
    app.run(debug=True)
