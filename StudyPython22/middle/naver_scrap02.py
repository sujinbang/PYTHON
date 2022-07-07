# 네이버 웹페이지 긁어오기2
import requests as req

res = req.get('https://www.google.com')
#print(res.status_code)
print(res.content)
