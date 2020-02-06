import requests
import json
data={
    "adultCount": 1,
    "arrivalCityId": 1,
    "arrivalCountryName": "中国",
    "arrivalProvinceId": 1,
    "cabin": "Y_S",
    "cabinEnum": "Y_S",
    "childCount": 0,
    "departCountryName": "中国",
    "departProvinceId": 1,
    "departureCityId": 1,
    "directFlight": "false",
    "extGlobalSwitches": {
        "roundTabModeSwitch": "false",
        "splitRoundBuildUpSwitch": "false",
        "splitRoundFlightsSwitch": "false",
        "useAllRecommendSwitch": "true"
    },
    "extensionAttributes": {
        "LoggingSampling": "false",
        "isFlightIntlNewUser": "false"
    },
    "flightSegments": [
        {
            "arrivalCityCode": "TYO",
            "arrivalCityId": 228,
            "arrivalCityName": "东京",
            "arrivalCityTimeZone": 540,
            "arrivalCountryId": 78,
            "arrivalCountryName": "日本",
            "arrivalProvinceId": 11079,
            "departureCityCode": "BJS",
            "departureCityId": 1,
            "departureCityName": "北京",
            "departureCityTimeZone": 480,
            "departureCountryId": 1,
            "departureCountryName": "中国",
            "departureDate": "2019-12-31",
            "departureProvinceId": 1,
            "timeZone": 480},
        {
            "arrivalCityCode": "BJS",
            "arrivalCityId": 1,
            "arrivalCityName": "北京",
            "arrivalCityTimeZone": 480,
            "arrivalCountryId": 1,
            "arrivalCountryName": "中国",
            "arrivalProvinceId": 1,
            "departureCityCode": "TYO",
            "departureCityId": 228,
            "departureCityName": "东京",
            "departureCityTimeZone": 540,
            "departureCountryId": 78,
            "departureCountryName": "日本",
            "departureDate": "2020-01-03",
            "departureProvinceId": 11079,
            "timeZone": 540,
        }],
    "flightWay": "D",
    "flightWayEnum": "RT",
    "infantCount": 0,
    "isMultiplePassengerType": 0,
    "segmentNo": 1,
    "transactionID": "130bebfd511f40cfbc6d36b034b0d8d9",
}
url = "https://flights.ctrip.com/international/search/api/search/batchSearch?v=0.025481565278044682"
headers = {
'cookie':'_abtest_userid=da08cf5c-7725-429c-9cb0-352f40e746d0; _RF1=124.64.16.94; _RSG=oQaOL2MZT1DD3MAWoXWtxB; _RDG=28bf1d38b561a72c972e8b62abb9ceaeea; _RGUID=d05d8d60-9562-46b2-bef7-821ca02960cd; MKT_Pagesource=PC; _ga=GA1.2.1518832385.1577689629; _gid=GA1.2.1831744200.1577689629; MKT_CKID=1577689630317.xt1xy.h108; MKT_CKID_LMT=1577689630319; FlightIntl=Search=[%22BJS|%E5%8C%97%E4%BA%AC(BJS)|1|BJS|480%22%2C%22TYO|%E4%B8%9C%E4%BA%AC(TYO)|228|TYO|540%22%2C%222019-12-31%22%2C%222020-01-03%22]; Union=OUID=index&AllianceID=4897&SID=155952&SourceID=&createtime=1577756232&Expires=1578361031568; _gat=1; appFloatCnt=2; _jzqco=%7C%7C%7C%7C1577689631028%7C1.1272046461.1577689630311.1577756236533.1577756244488.1577756236533.1577756244488.undefined.0.0.6.6; __zpspc=9.2.1577756231.1577756244.3%232%7Csp0.baidu.com%7C%7C%7C%25E6%2590%25BA%25E7%25A8%258B%7C%23; _bfi=p1%3D10320672928%26p2%3D10320669438%26v1%3D8%26v2%3D6; _bfa=1.1577689621646.wdw89.1.1577689621646.1577756228537.2.9; _bfs=1.5',
'origin':'https://flights.ctrip.com',
'referer':'https://flights.ctrip.com/international/search/round-bjs-tyo?depdate=2019-12-31_2020-01-03&cabin=y_s&adult=1&child=0&infant=0&searchid=j1060138106-1577756356708-1519543oD-0',
'sec-fetch-mode':'cors',
    "content-type": "application/json;charset=UTF-8",
'sec-fetch-site':'same-origin',
'sign':'3d182348bb9ad252a78a1aa2b4439334',
'transactionid':'1a13977a4a5549b6936bb6a6e640671a',
'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
}
res = requests.post(url,headers=headers,json=data)
print(res.text)
