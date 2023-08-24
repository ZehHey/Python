# Crie um código em Python que teste se o site google.com está acessível pelo computador usado.

import urllib
import urllib.request
a = 'http://google.com'
try:
    site = urllib.request.urlopen(a)
except:
    print('Erro!')
else:
    print('OK')

