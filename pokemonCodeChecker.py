import requests
import time
import json
from configparser import ConfigParser
if __name__ == '__main__':
    try:
		config = ConfigParser()
		
		config.read('settings.ini')
		session_id = config.get('Session','session_id')
		source_codes = config.get('Global','source_codes')

		print session_id
		
		cookies = {
			'main_session_id': session_id,
			'op_session_id': session_id
		}

		headers = {
		}

		with open("CheckedCodes-"+time.strftime("%Y%m%d-%H%M%S")+".txt",'a',0) as cc:
			with open(source_codes) as sc:
				for cnt, line in enumerate(sc):
					data = [
						('code', line)
					]
					response = requests.post('https://www.pokemon.com/us/pokemon-trainer-club/verify_code/', headers=headers, cookies=cookies, data=data)
					code_json = json.loads(response.text)
					print response.text
					if code_json['valid']:
						cc.write("{},{},{} \n".format(code_json['valid'],code_json['coupon_code'],code_json['coupon_title'].encode('utf-8')))
					else:
						cc.write("{},{},{} \n".format(code_json['valid'],code_json['coupon_code'],code_json['error_message'].encode('utf-8')))						
			sc.close
		cc.close
    except:
        import sys
        print sys.exc_info()[0]
        import traceback
        print traceback.format_exc()
        print "Press Enter to continue ..." 
        raw_input()