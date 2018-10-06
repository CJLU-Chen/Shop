import urllib.request as r
req=r.Request('http://www.baidu.com')
try:
   r.urlopen(req)
except urllib.error.HTTPError as e:
   print(e.code)
   print(e.read())
