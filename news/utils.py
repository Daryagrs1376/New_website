import os
from kavenegar import KavenegarAPI, APIException, HTTPException

def send_sms(phone_number, message):
    
    try:
        api_key = os.getenv('KAVENEGAR_API_KEY', '5A526F323961334F783863366A72537149675954337A565257322B744E6850654C32392F3650377A71594D3D')
        api = KavenegarAPI(api_key)

        params = {
            'receptor': "09227207457", 
            'sender': '1000596446', 
            'message': "salaaam", 
        }

        response = api.sms_send(params)
        return {'status': 'success', 'response': response}

    except APIException as e:
        print(f"API Exception: {e.args}")
        return {'status': 'failed', 'error': str(e)}
    
    except HTTPException as e:
        print(f"HTTP Exception: {e.args}")
        return {'status': 'failed', 'error': str(e)}