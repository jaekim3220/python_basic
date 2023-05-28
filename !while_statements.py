'''while문 기본구조'''
# 조건식이 참인 경우 무한 반복

'''0~4 반복'''
# a = 0
# while a<5:
#     print(str(a+1)+"번 반복")
#     a += 1 
'''1~5 반복'''
# a = 0
# while a<5:
#     a += 1 
#     print(str(a)+"번 반복")

'''1~1000까지 반복 1'''
# a = 0
# while a <1000: 
#     a += 1
#     print(str(a)+"번 반복")
'''1~1000까지 반복 2'''
# a = 1
# while a <1001: 
#     print(str(a)+"번 반복")
#     a += 1

'''1~1000까지 모두 더한 값'''
# a = 0
# while a <1000: 
#     a += 1
#     print(sum(a))

'''1~1000까지 모두 더한 평균 값 1'''
# a = 0
# sum = 0
# while a < 1000:
#     a += 1
#     sum += a
# print(sum)
'''a = 1000일 경우 break'''
# a = 0
# sum = 0
# while a < 1000:
#     a += 1
#     sum += a
#     if a == 1000:
#         break
# print(sum)
'''1~1000까지 모두 더한 평균 값 2'''
# a = 0
# suma = 0
# while a < 1001:
#     suma += a
#     a += 1
# print(suma)

'''while문에서 break를 써서 반복문 종료'''
'''if문을 사용한 xxx한 조건에 break'''

'''suma > 1000일 경우 break 1'''
# a = 1
# suma = 0
# while a < 1000:
#     suma += a
#     a += 1
#     if suma > 1000:
#         break
# print(suma)
'''suma > 1000일 경우 break 2'''
# a = 0
# suma = 0
# while a < 1000:
#     a += 1
#     suma += a
#     if suma > 1000:
#         break
# print(suma)

'''a == 500일 경우 break'''
# a = 1
# suma = 0
# while True:
#     suma += a
#     if a == 500:
#         break
#     a += 1
# print(suma)

'''a == 500일 경우 break 2'''
# a = 0
# suma = 0
# while a < 1000:
#     a += 1
#     suma += a
#     if a == 500:
#         break
# print(suma)

'''1~1000 중 홀수만 더하는 경우(break 아님)'''
# a = 0
# sum = 0
# while a < 1000:
#     a += 1
#     if a % 2 != 0:
#         sum += a
# print(sum)

'''continue 구문을 만나면 다시 반복문 조건으로 이동(잘못된 구문 피하기용)'''
'''불필요한 로직을 수행하지 않고 다시 조건으로 이동'''
# a = 0
# while a < 1000:
#     print('hello')
#     continue

'''continue 사용문(홀수만 덧셈)'''
# a = 0
# sum = 0
# while a < 1000:
#     a += 1
#     if a % 2 == 0:
#         continue #짝수일 경우 현재의 반복을 중지, 다음 반복으로 이동
#     sum += a
# print(sum)

'''continue로 if-else 조건물 간략화 가능'''
# while True:
#     angle = int(input("입력 각도 "))
#     if (angle > 180)|(angle <= 0):
#         print('잘못된 값')
#         continue
#     if 0 < angle < 90:
#         print("예각")
#     elif angle == 90:
#         print('직각')
#     elif 90 < angle < 180:
#         print('둔각')
''''''
# while True:
#     inputa = int(input("입력 번호 "))
#     if inputa == 4:
#         print("종료")
#         break
#     if inputa == 1:
#         print("one")
#     elif inputa == 2:
#         print("two")
#     elif inputa == 3:
#         print('three')
#     else:
#         print('잘못된 값')

'''while문 활용한 나만의 리스트 만들기'''
'''리스트 크기를 입력 받아 그 크기만큼 임의 숫자를 리스트에 추가,
리스트의 크기와 값 전체를 출력. 모든 값은 키보드로 입력, 
list 크기는 함수를 통해 도출
list의 크기는 10이하'''
'''
리스트 크기 : 
리스트 크기를 10 이하로 다시 할당 : 
리스트에 값을 할당해라 : 
리스트에 값을 할당해라 : 
---
리스트에 값을 할당해라 :
크기 x의 리스트 []가 할당
'''
'''오답-심지어 틀림(바로 아래께 정답   )'''
# list_size = int(input("리스트 크기 : "))
# while list_size > 10:
#     print("리스트 크기를 10 이하로 다시 할당 : ")
# if list_size <= 10:
#     print("리스트 값 : {}".format(list_size))
#     new_list = list(range(list_size))
#     print(new_list)
#     print(f"크기 {list_size}의 {new_list}리스트 할당")
''''''
# list_size = int(input("리스트 크기: "))
# while list_size > 10:
#     print("리스트 크기를 10 이하로 다시 할당하세요.")
#     list_size = int(input("리스트 크기: "))
# print("리스트 값: {}".format(list_size))
# new_list = list(range(1, list_size + 1))
# print(new_list)
# print("크기 {}의 {} 리스트 할당".format(list_size, new_list))

'''정답1'''
# while True:
#     list_size = int(input("리스트 크기 : "))
#     if list_size>10 or list_size <= 0:
#         print('다시 입력')
#         continue
#     a = 0
#     lista = []
#     while a < list_size:
#         listValue = input('리스트 값 : ')
#         lista.append(int(listValue))
#         a+=1
#     print( lista)
#     break
'''정답2 if-else'''
# while True:
#     list_size = int(input("리스트 크기: "))
#     if list_size > 10 or list_size <= 0:
#         print("다시 입력")
#     else:
#         a = 0
#         lista = []
#         while a < list_size:
#             listValue = input("리스트 값 입력: ")
#             lista.append(listValue)
#             a += 1
#         print(lista)
#         break

'''로또 번호 생성기'''
'''랜덤 값 추출하는 파이썬 라이브러리 random'''
# import random
# print(random.randint(1,45))

'''리스트 크기가 6개인 리스트를 while을 써 오늘의 로또번호 6개 생성'''
# import random
# while True:
#     lotto_size = int(input("크기 : "))
#     if lotto_size != 6:
#         print("다시 입력")
#         continue
#     lista = []
#     while len(lista) < 6:
#         random_num = random.randint(1, 45)
#         if random_num not in lista:
#             lista.append(random_num)
#     print(lista)
#     break
'''답(중복 숫자 도출 가능)'''
# import random
# a = 0
# lista = []
# while a < 6:
#     randnum = random.randint(1,45)
#     lista.append(randnum)
#     a+=1
# print(lista)
'''답(중복 숫자 배제)'''
# import random
# a = 0
# lista = []
# while a < 6:
#     randnum = random.randint(1,45)
#     if randnum not in lista:
#         lista.append(randnum)
# print(lista)