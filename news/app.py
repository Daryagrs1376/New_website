from flask import Flask, request, jsonify
from sms_service import send_sms 
import random

app = Flask(__name__)

@app.route('/send-code', methods=['POST'])
def send_verification_code():
    data = request.json
    phone_number = data.get('phone_number')

    if not phone_number:
        return jsonify({"error": "شماره موبایل الزامی است"}), 400

    verification_code = random.randint(1000, 9999)
    send_sms(phone_number, verification_code)

    return jsonify({"message": "کد تایید ارسال شد!"})

if __name__ == "__main__":
    app.run(debug=True)
