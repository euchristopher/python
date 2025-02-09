import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except urllib.error.URLError:
    print("O programa nao conseguiu acessar o site Pudim no momento.")
else:
    print("O programa conseguiu acessar o site Pudim!")
