import urllib
import url.request

try:
	site = urllib.request.urlopen('http://www.pudim.com.br')
except:
	print('Deu ruim.')
else:
	print('Tudo ok.')