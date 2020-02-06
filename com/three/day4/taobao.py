# import requests
# import re
# import json
# num = 0
# while True:
#     url = "https://s.taobao.com/list?spm=a21bo.2017.201867-links-0.34.5af911d9OFwQC7&q=%E6%96%B0%E5%93%81&cat=50344007&style=grid&seller_type=taobao&bcoffset=0&s="+str(num)
#     num += 60
#     headers = {
#         "cookie":'miid=153511782174515670; cna=6t4uFoTEh2cCAWp5BLo46YHO; thw=cn; t=ae5838bd9497e1a76069e2d4ba77f9fc; _m_h5_tk=87ad022c93ede07b829a2092ffd534ff_1577419331712; _m_h5_tk_enc=a3eb69019a052190f3ac686df6edac17; cookie2=1a154e3ef222855b01d7842fc0d539b1; _tb_token_=e8bef74e0f8be; v=0; unb=2966099965; uc3=id2=UUGk2KchQeR69w%3D%3D&nk2=sDCHGNB0Wmc%3D&vt3=F8dBxdguzFvXByxrbqM%3D&lg2=URm48syIIVrSKA%3D%3D; csg=ad696c73; lgc=%5Cu5F71%5Cu6708%5Cu4EA1%5Cu68A6; cookie17=UUGk2KchQeR69w%3D%3D; dnk=%5Cu5F71%5Cu6708%5Cu4EA1%5Cu68A6; skt=adf9d969053a6e78; existShop=MTU3NzQxMTQ1OA%3D%3D; uc4=nk4=0%40ssiUGmDewcVoFXblQWdqMgu%2BAQ%3D%3D&id4=0%40U2OT6EjMfBlOAPaWoPB9qmXSVFjI; tracknick=%5Cu5F71%5Cu6708%5Cu4EA1%5Cu68A6; _cc_=VFC%2FuZ9ajQ%3D%3D; tg=0; _l_g_=Ug%3D%3D; sg=%E6%A2%A65d; _nk_=%5Cu5F71%5Cu6708%5Cu4EA1%5Cu68A6; cookie1=UR3ecoeU%2B0GOnO5Cnr6MxubgH31KJxW%2BzrEEsS8Anwo%3D; mt=ci=14_1; enc=YzQhHem2FaDQG1Ppfuu5pEB1NSOVCRKZ1u%2F5se0nfFLreUGQ5jfFQZiEemp%2BbKN1Q1KwYYjea%2FK7U3axjMBFfQ%3D%3D; JSESSIONID=02CC922E6B82388165C1734959251C4E; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; uc1="cookie15=WqG3DMC9VAQiUQ%3D%3D"; hng=CN%7Czh-CN%7CCNY%7C156; l=cBP3Q3ePq3En1J6yBOCwhurza77tMIRAguPzaNbMi_5aq6AfMg7OobZPyFv6cjWd9gYB4Eq8ar99-etkmmbMwU7FPiAd.; isg=BMrKo7YtoAATli8RhAj_3pqwG7Bsu04Vzqj351QDDp3YB2rBPEpkJMV1EzN-98at',
#     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
#     }
#     result = requests.get(url,headers=headers).text
#     rule = "g_page_config = (.*?);"
#     print(json.loads(re.findall(rule,result)[0]))
