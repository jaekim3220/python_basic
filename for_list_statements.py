# 유한반복 for 문
'''range 문법 1'''
# for a in range(1,101):
#     print(a)

'''range 문법 2'''
# v1 = list(range(1,11))
# print(v1)

'''range 문법 3'''
# listb = ['a', 'b', 'c', 'd']
# for b in listb:
#     print(b)
# print("---------------")
# for b in range(0, len(listb)):
#     print(b)

'''range 문법 4'''
# import random
# lista = []
# for a in range(0,6):
#     randnum = random.randint(1,45)
#     lista.append(randnum)
#     a+=1
# print(lista)

'''for a in list를 써서 v1 값 모두 출력'''
# v1 = list(range(10, 20))
# for a in v1:
#     print(a)

'''for a in range를 써서 v1[index] 형태로 v1값 모두 출력'''
# v1 = list(range(10, 20))
# for a in range(len(v1)):
#     print(v1[a])

'''for a in 리스트 구문으로는 원본 리스트 데이터 변경 불가'''
# lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for a in lista:
#     a = 100 #이런 방식으로는 원본 lista 값 변경 불가

'''원본 바꾸기 1 while'''
# lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# lista[0] = 100 #있어도 상관 없음
# indexTemp = 0
# while indexTemp < len(lista):
#     lista[indexTemp] = 100
#     indexTemp += 1
# print(lista)
'''원본 바꾸기 1.5 특정 값만 바꾸기'''
# lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# indexTemp = 0
# while indexTemp < len(lista):
#     if indexTemp == 2:
#         lista[indexTemp] = 500
#     indexTemp += 1
# print(lista)

'''원본바꾸기 2 for'''
# lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# lista[5] = 100
# for a in lista:
#     a = 100 #이런 방식으로는 원본 lista 값 변경 불가
# print(lista)
# #직접 리스트의 index로 접근해야 원본을 바꿀 수 있다    
# lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for a in range(len(lista)):
#     lista[a] = 100
# print(lista)

'''원본바꾸기 2.5 특정 값만 바꾸기'''
# lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for a in range(len(lista)):
#     if a == 9:
#         lista[a] = lista[a]*10
# print(lista)

'''리스트 내포(comprehension)'''
'''리스트 생성 방법 중 하나'''
# #방법1
# lista = [0,1,2,3,4,5,6,7,8,9]

# #방법2
# lista = list(range(10))

# #방법3
# lista = []
# for a in range(10):
#     lista.append(a)

# #방법4 comprehension
# lista = [a for a in range(10)]
# print(lista)

# 방법4에서 a*2 값 출력
# lista = [a*2 for a in range(10)]
# print(lista)
# 방법4에서 홀수*2 값 출력
# lista = [a*2 for a in range(10) if a%2 != 0]
# print(lista)

#방법3에 홀수인 값에 2를 곱한 값만 list화
# lista = []
# for a in range(10):
#     if a % 2!= 0:
#         lista.append(a*2)
# print(lista)

'''한 반에 수학 점수가 60점이 넘으면 합격, 60점 미만이면 불합격
lista = [90, 25, 67, 45, 80], list가 학생의 번호 순서대로 있을 때
아래와 같이 출력'''
'''1번 학생은 합격
2번 학생은 불합격'''

'''1'''
# lista = [90, 25, 67, 45, 80]
# num = 1
# for a in lista:
#     if a >= 60:
#         print(f"{num}번 학생 합격")
#     else:
#         print("{}번 학생 불합격".format(num))
#     num += 1
'''2'''
# lista = [90, 25, 67, 45, 80]
# for a in range(len(lista)):
#     if lista[a] >= 60:
#         print(f"{a+1}번 학생 합격")
#     else:
#         print("{}번 학생 불합격".format(a+1))

'''for-break문(for문에서 반드시 break문 써야하는 상황)'''
'''혈액형이 a 형인 고객 선착순 1명만 찾는 상황'''
'''출력 결과 : 4번째 고객이 이벤트에 당첨'''
'''for-break문 1'''
# lista = ['b', 'b', 'ab', 'a', 'b', 'a']
# for a in range(len(lista)):
#     if lista[a] == 'a':
#         print(f"{a+1} 번째 고객이 이벤트에 당첨")
#         break
'''for-break문 2'''
# answer = 0
# lista = ['b', 'b', 'ab', 'a', 'b', 'a']
# for a in range(len(lista)):
#     if lista[a] == 'a':
#         answer = a+1
#         #break 유무 확인
#         break
# print(f"{a+1} 번째 고객이 이벤트에 당첨")

'''for문을 이용한 구구단'''
'''5단 출력
5x1 = 5
5x2 = 10
5x3 = 15'''
# dan = 5
# for a in range(1,10):
#     result = dan*a
#     print(f"{dan}X{a} = {result}")

'''while문을 이용한 구구단'''
# dan = 5
# a = 0
# while a < 9:
#     result = dan*(a+1)
#     print(f"{dan}X{a+1} = {result}")
#     a+=1

'''입력한 숫자를 계산하는 구구단'''
# while True:
#     while True:
#         dan = int(input("계산할 구구단 : "))
#         for a in range(1,10):
#             result = dan*a
#             print(f"{dan}X{a} = {result}")
#         break

'''while 사용한 구구단 5단~9단까지 한꺼번에 출력'''
# dan = 4
# while dan < 9:
#     dan += 1
#     for a in range(1,10):
#         print(f"{dan}X{a} = {dan*a}")

'''lista[0], lista[1]의 자리를 바꾸기'''
# lista = [10,20,30,40,50]
# lista[0] = lista[1]
# lista[1] = lista[0]
# print(lista)
# #위 방식의 문제점 인지
# temp = lista[0]
# lista[0] = lista[1]
# lista[1] = temp
# print(lista)

'''for문을 이용한 정렬 알고리즘(sort 미사용)'''
# lista = [93, 34, 62, 57, 9, 54]
# # print(sorted(lista))
# lista.sort()
# print(lista)

'''2중 for문'''

'''1 선택 정렬 (0번째 index부터 가장 작은 값을 채워나가는 방식)'''
#첫 번째 for : 바꾸고자하는 자리의 index or 반복 횟수
#두 번째 for : 대상이 되는 수의 길이 or 각 반복마다 실행되는 작업의 횟수
'''오름차순'''
# lista = [93, 34, 62, 57, 9, 54, 87, 15, 84]
# for a in range(len(lista)-1): #range로 index 값에 접근 (채워나가야 할 index)
#     # 마지막 자릿수는 궂이 비교할 필요가 없음
#     for b in range(a+1, len(lista)): # (비교의 대상이 되는 index)
#         #반복 횟수를 1회 줄이기 위해 a+1, 안해도 값은 정확
#         if lista[a] > lista[b]:
            # temp = lista[a]
            # lista[a] = lista[b]
            # lista[b] = temp
# print(lista)
'''내림차순'''
# lista = [93, 34, 62, 57, 9, 54, 87, 15, 84]
# for a in range(len(lista)-1): #range로 index 값에 접근 (채워나가야 할 index)
#     for b in range(a+1, len(lista)): # (비교의 대상이 되는 index)
#         if lista[a] < lista[b]:
#             temp = lista[a]
#             lista[a] = lista[b]
#             lista[b] = temp
# print(lista)

'''2 버블 정렬'''
# lista = [93, 34, 62, 57, 9, 54, 87, 15, 84]
# for a in range(len(lista)-1):
#     for b in range(0, len(lista)-a-1): #indexover 방지로 -1
#         if lista[b] > lista[b+1]:
#             lista[b], lista[b+1] = lista[b+1], lista[b]

# print(lista)

'''행렬의 덧셈'''
# lista = [[1,2,3],[2,3,4]]
# listb = [[3,4,5],[5,6,7]]
# print(len(lista))
# print(len(lista[0]))
#힌트 : [[lista[0][0]+listb[0][0], lista[0][1]+listb[0][1]],\
# [lista[1][0]+listb[1][0], lista[1][1]+listb[1][1]]]

# listsum = []
# for a in range(len(lista)): 
#     new = []
#     for b in range(len(lista[a])):
#         sum = lista[a][b] + listb[a][b]
#         new.append(sum)
#     listsum.append(new)
# print(listsum)
