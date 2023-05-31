'''lambda함수
함수를 간편히 표현하기 위한 방식
함수를 변수에 담기 위한 방식'''
# # lambda 매개변수
# def add(a,b):
#     return a+b
# print(add(1,2))
# add_lambda = lambda a,b: a+b
# print(add_lambda(1,2))

'''매개변수 a를 입력 시 a의 제곱이 출력되는 lambda 함수'''
# pow_lambda = lambda a: pow(a,2)
# print(pow_lambda(5))

'''list에 lambda함수를 담아서 사용 가능'''
# a = int(input("a 값 : "))
# b = int(input("b 값 : "))
# cal_list = [lambda a,b:a+b, lambda a,b:a-b, lambda a,b:a*b, lambda a,b:a/b]
# print(int(cal_list[3](a,b)))
# cal_dict = {'plus':lambda a,b:a+b, 'min':lambda a,b:a-b, \
#             'multi':lambda a,b:a*b, 'divide':lambda a,b:a/b}
# print(cal_dict['plus'](4,2))

'''lambda로 입력한 매개변수가 짝수면 True, 홀수면 False'''
# def oddornot(a):
#     if a%2==0:
#         return True
#     else:
#         return False
# print(oddornot(8))
# oddornot = lambda a : True if a%2 ==0 else False
# print(oddornot(4))


'''map 함수 : 대상이 되는 리스트를 사용해 새로운 리스트 생성
특정 함수와 반복 가능한 자료형을 입력받아 
특정 함수가 수행한 결과 값을 return하는 함수(변환)'''
# # map(함수, 리스트 또는 튜플 등)
# def two_times(a):
#     return a*2
# lst = list(map(two_times, [1,2,3,4,5]))
# print(lst)
# # map, lambda 함수를 사용해 입력 list의 제곱 값을 담은 list 출력
# lst = list(map(lambda a:pow(a,2),[1,2,3,4,5]))
# print(lst)


'''filter 함수 : 대상이 되는 리스트에서 함수를 적용해 특정한 조건으로 값 걸러내기
함수를 적용해 참/거짓 조건으로 값 걸러내기(판단)'''
# def trueOrnot(a):
#     if a > 0:
#         return True
#     else:
#         return False
# lst = list(filter(trueOrnot,[-1,4,0,-4,68,8]))
# print(lst)
# # lambda를 사용한 삼항연산자 
# lst = list(filter((lambda a: True if a> 0 else False), [-1,4,0,-4,68,8]))
# print(lst) #filter 함수는 판단
# lst = list(map((lambda a: True if a> 0 else False), [-1,4,0,-4,68,8]))
# print(lst) #map 함수는 변환

'''함수형 프로그래밍(filter, map, lambda)을 사용해 
주어진 list에서 홀수만 추출'''
# lista = [12,34,76,5,9,87,23,21,40]
# lst = list(filter(lambda a: True if a%2!=0 else False, lista))
# print(lst)
# # 홀수를 제곱한 값 출력(map,list)
# lista = [12,34,76,5,9,87,23,21,40]
# lst = list(map(lambda a:pow(a,2),\
#                (filter(lambda a: True if a%2!=0 else False, lista))))
# print(lst)

'''sum : 주어진 자료 총 합
'''
# print(sum([1,2,3]))
# lista = [12,34,76,5,9,87,23,21,40]
# lsumst = sum(list(filter(lambda a: True if a%2!=0 else False, lista)))
# print(lsumst)

'''문자 -> 아스키코드(ord()), 아스키코드 -> 문자(chr())'''

'''절댓값 abs'''
'''map 사용 절대값'''
# lista = [1,3,5,-3,-58,59,-129,-98,-37]
# lst = list(map(abs, lista))
# print(lst)

'''변수 a 입력 시 n! 결과 값 유도'''
# # 그냥 함수
# def factorial(a):
#     result = 1
#     for a in range(1,a+1):
#         result *= a
#     return result
# a = int(input("입력 값 : "))
# print(f'{a}!은 {factorial(a)}')

'''재귀함수
함수내에서 함수 자기 자신을 호출하는 함수
반드시 재귀함수를 종료하는 조건이 요구됨'''
# def test(a):
#     if a ==1:
#         return 1
#     return a+test(a-1)
# result = test(10)
# print(result)
'''재귀함수(팩토리얼)'''
# def test(a):
#     if a == 1:
#         return 1
#     return a * test(a-1)
# a = int(input("입력 값 : "))
# print(test(a))
# # result = test(4)
# # print(result)
'''재귀함수 반드시 쓰는 상황
반복의 횟수를 알 수 없을 때'''
'''5개의 숫자 중 2개씩 숫자를 추출하는 경우의 수를 구하고자 한다
2개씩 숫자를 추출해 list에 담아 마지막에 모든 리스트를 출력'''

'''재귀함수 아님 lista의 2개씩의 조합을 구해 리스트에 담아 출력'''
# lista = [10,20,30,40,50]
# new_list = []
# count = 0
# for a in range(len(lista)):
#     for b in range(a+1, len(lista)):
#         new_list.append([lista[a], lista[b]])
# print(new_list)

'''review 
재귀함수 아님(다중 for문) lista의 3개씩의 조합을 구해 리스트에 담아 출력'''
# lista = [10,20,30,40,50]
# new_list = []
# count = 0
# for a in range(len(lista)):
#     for b in range(a+1, len(lista)):
#         # new_list.append([lista[a], lista[b]])
#         for c in range(a+2, len(lista)):
#             new_list.append([lista[a], lista[b], lista[c]])
# print(new_list)

'''재귀함수화
lista의 3개씩의 조합을 구해 리스트에 담아 출력'''
# def recur(lista, total_list, temp_list, n, m):
#     if m == 0:
#         total_list.append(temp_list[:]) #list의 count값을 물어볼 경우 이 부분을 count로
#         return
#     for a in range(len(lista)):
#         temp_list.append(lista[a])
#         recur(lista, total_list, temp_list, a+1, m-1)
#         temp_list.pop()

# input1 = [10,20,30,40,50]
# total_list = []
# input2 = 3
# print(input1, total_list, [], input2)

