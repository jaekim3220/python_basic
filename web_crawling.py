# '''웹 크롤링
# import requests
# from bs4 import BeautifulSoup는
# 외장 라이브러리 -> 별도설치 요구
# pip 패키지 tool 사용 python 설치 시 동시에 pip 설치'''

'''http 통신 : 웹으로 주고받는 통신 프로토콜
http 통신의 위해서는 http 통신 규격에 맞게 requests를 서버로 전달
requests는 header와 body로 구성, 마찬가지로 응답(response)로 header와 body로 구성'''

'''감독, 제작비 정보 추출'''
#개발자 도구의 elements에서 잘 찾아볼것(복습 안 하면 모름)
import requests
from bs4 import BeautifulSoup
# url1 = 'https://ko.wikipedia.org/wiki/%EC%95%84%EB%B0%94%ED%83%80:_%EB%AC%BC%EC%9D%98_%EA%B8%B8'
# header = {'User-Agent' : 'Mozilla/5.0'} #절대 spec을 다르게 선언하지 말 것
# response = requests.get(url1, headers=header)
# html_response = BeautifulSoup(response.text, 'html.parser')
# print(html_response) #html 요소 출력
# '''감독 정보 추출
# tag 정보를 가지고 html_response에서 원하는 정보 추출'''
# director_info1 = html_response.select_one\
#     ('table.infobox > tbody > tr:nth-of-type(3) > td').get_text() # 감독 데이터 파싱
# print(director_info1) # 파싱한 데이터 출력
# '''제작비 정보 추출
# tag 정보를 가지고 html_response에서 원하는 정보 추출'''
# for sup in html_response.find_all('sup'): # sup 정보 제외하기: [1]
#     sup.decompose()
# budget_info = html_response.select_one\
#      ('table.infobox > tbody > tr:nth-of-type(16) > td').get_text() # 제작비 데이터 파싱
# print(budget_info) # 파싱한 데이터 출력
# print(f"아바타 감독은 {director_info1}, 제작비는 {budget_info}")


'''코인 시세정보 AIP url'''
# import json
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
#         print(f"{a['symbol']}의 가격은 {a['lastPrice']}입니다")


'''csv(엑셀) 파일 parsing - pandas, matplotlib을 사용한 시각화'''
import seaborn
from matplotlib import pyplot
import pandas
file_path = r'C:\Users\jehyu\Desktop\nationalsupport\tips.csv'
csv_data = pandas.read_csv(file_path)
print(csv_data)
#성별에 따른 tip의 출력
tip_by_gender = csv_data.groupby('gender')['tip'].agg(['mean', 'std']).reset_index()
seaborn.barplot(x='gender', y='mean', data=tip_by_gender, yerr = tip_by_gender['mean'], capsize = 0.1)
seaborn.despine() #테두리 삭제
pyplot.title('average tip per gender')
pyplot.xlabel('gender')
pyplot.ylabel('average tip')
pyplot.show()
#날짜별 tip 출력
# tip_by_day = csv_data.groupby('day')['tip'].agg(['mean', 'std']).reset_index()