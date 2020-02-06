import requests

url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=CI5Eppv31wVQ5xWkMjf3pdL4&client_secret=BVKh6oSefWGGdky5M9mMGIGRGKXKkHTP'


res = requests.get(url=url)
ac = res.json()['access_token']

headers = {
    'Content-Type':'application/x-www-form-urlencoded'
}

import base64

with open('mzt3.png','rb') as r:
    img = r.read()
    img = base64.b64encode(img)

url2 = 'https://aip.baidubce.com/rest/2.0/solution/v1/img_censor/v2/user_defined?access_token='+ac

data = {
    'image': img
}

res = requests.post(url=url2,headers=headers,data=data)
print(res.text)