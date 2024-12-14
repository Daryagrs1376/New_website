from kavenegar import *
from kavenegar import KavenegarAPI, APIException, HTTPException


def send_sms(phone_number, verification_code):
    try:
        api = KavenegarAPI('Your-API-Key') 
        params = {
            'receptor': phone_number, 
            'message': f'کد تایید شما: {verification_code}'
        }
        response = api.sms_send(params)
        print(f"SMS Response: {response}")
        
    except APIException as e:
        print(f"API Exception: {e}")
        
    except HTTPException as e:
        print(f"HTTP Exception: {e}")
