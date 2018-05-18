import requests
import time
import json
from configparser import ConfigParser
if __name__ == '__main__':
    try:
		config = ConfigParser()
		
		config.read('settings.ini')
		session_id = config.get('Session','session_id')
		source_codes = config.get('Global','redeem_codes')
		csrf_token = config.get('Session','csrf_token')

		print ("session_id:" + session_id)
		print ("csrf_token:" + csrf_token)
		
		cookies = {
			'main_session_id': session_id,
			'op_session_id': session_id,
			'django_language':'en',
			'_sdsat_businessUnit':'pcom',
			'_sdsat_Language':'en',
			's_ppvl':'https%253A%2F%2Fwww.pokemon.com%2Fus%2Fpokemon-trainer-club%2Fenter-codes%2C57%2C57%2C934%2C1680%2C934%2C1680%2C1050%2C1%2CL',
			'_sdsat_Internal/External':'external',
			's_ppv':'https%253A%2F%2Fwww.pokemon.com%2Fus%2Fpokemon-trainer-club%2Fenter-codes%2C57%2C57%2C934%2C1680%2C934%2C1680%2C1050%2C1%2CL',
			's_sq':'pcomprod%252Ctpciglobalprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fwww.pokemon.com%25252Fus%25252Fpokemon-trainer-club%25252Fenter-codes%2526link%253DClaim%252520Now%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fwww.pokemon.com%25252Fus%25252Fpokemon-trainer-club%25252Fenter-codes%2526oid%253DClaim%252520Now%2526oidt%253D3%2526ot%253DSUBMIT'
		}

		headers = {
			'Origin':'https://www.pokemon.com',
			'Accept-Encoding':'gzip, deflate, br',
			'Accept-Language':'en-US,en;q=0.9',
			'Upgrade-Insecure-Requests':'1',
			'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36',
			'Content-Type':'application/x-www-form-urlencoded',
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Cache-control':'max-age=0',
			'Referer':'https://www.pokemon.com/us/pokemon-trainer-club/enter-codes',
			'Connection':'keep-alive'
		}

		with open(source_codes) as sc:
			for cnt, line in enumerate(sc):
				strippedLine = line.replace("-","").rstrip()
				payload={'csrfmiddlewaretoken':csrf_token,'code':strippedLine,'hidden_code':strippedLine}
				response = requests.post('https://www.pokemon.com/us/pokemon-trainer-club/enter-codes', headers=headers, cookies=cookies, data=payload)
				for item in response.text.split("\n"):
					if strippedLine in item:
						print item.strip()
		sc.close
    except:
        import sys
        print sys.exc_info()[0]
        import traceback
        print traceback.format_exc()
        print "Press Enter to continue ..." 
        raw_input()
