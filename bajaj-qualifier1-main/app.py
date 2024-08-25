from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        data = request.json.get('data', [])
        print(f"Received data: {data}")
        numbers = [x for x in data if x.isdigit()]
        alphabets = [x for x in data if x.isalpha()]
        highest_alphabet = max(alphabets, key=str.upper) if alphabets else ""
        response = {
            "is_success": True,
            "user_id": "rishitha_chowdary_cherukuri",  # Replace with your actual full name and DOB
            "email": "rishitha.21bce7023@vitapstudent.ac.in",  # Replace with your actual email
            "roll_number": "21BCE7023",  # Replace with your actual roll number
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": [highest_alphabet] if highest_alphabet else []
        }
        return jsonify(response), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"is_success": False, "error": str(e)}), 400

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
