# pip install mysql-connector-python : mysql, 파이썬 연동 라이브러리
# import mysql.connector
# try :
#     # connector에 db 연결 객체를 담는다"
#     connector = mysql.connector.connect(
#         host = "localhost", port = "3406", 
#         user = "root", password = "1234",
#         database = "board")
#     cursor = connector.cursor()
# except mysql.connector.Error as err:
#     print(err)
# '''커서 객체는 데이터베이스에서 
# 쿼리의 결과를 검색하고 순회하는데 사용되는 객체'''
# add_data = "INSERT INTO author (name, email) VALUES(%s, %s)" # %s로 변수화
# data = ("John", "hello3@naver.com")
# try:
#     cursor.execute(add_data, data)
#     connector.commit()
# except mysql.connector.Error as err:
#     print(err)
# cursor.close()
# connector.close()

'''위는 python과 mysql을 연결하는 코드'''

# import json
# import requests
# url2 = "https://api.binance.com/api/v3/ticker/24hr"
# response = response = requests.get(url2)
# data_json = json.loads(response.text)
# # print(data_json)
# # BTC price 출력, key는 "symbol" if ~~ == "BTCUSDT", lsatPrice를 key로 값을 get
# # 코인 이름, 가격 확인 코드
# # for a in data_json:
# #     print(a['symbol'])
# #     print(a['lastPrice'])
# for a in data_json:
#     if a['symbol'] == 'BTCUSDT':
'''위는 코인 정보 긁어오는 코드 web_crawling.py'''

# 코일 시세를 10초에 한 번씩 db insert
import time
import json
import requests
import mysql.connector
while True:
    url = "https://api.binance.com/api/v3/ticker/24hr"
    response = requests.get(url)
    data_json = json.loads(response.text)
    for a in data_json: 
        if a['symbol'] == "BTCUSDT":
            try:
                connector = mysql.connector.connect(host="localhost", port="3406", user="root", password="1234", database="practice")
                cursor = connector.cursor()
            except mysql.connector.Error as err:
                print(err)
            add_data = "INSERT INTO coin_price (coin_name, last_price) VALUES(%s, %s)"
            data = ("BTCUSDT", a['lastPrice'])
            try:
                cursor.execute(add_data, data)
                connector.commit()
            except mysql.connector.Error as err:
                print(err)
            cursor.close()
            connector.close()
    time.sleep(10)