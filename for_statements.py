'''range 문법'''
# for a in range(1,101):
#     print(a)

''''''
# v1 = list(range(1,11))
# print(v1)

''''''
# listb = ['a', 'b', 'c', 'd']
# for b in listb:
#     print(b)
# print("---------------")
# for b in range(0, len(listb)):
#     print(b)

''''''
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
# for b in range(len(v1)):
#     print(v1[b])

'''for a in 리스트 구문으로는 원본 리스트 데이터 변경 불가'''
# lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for a in lista:
#     a = 100 #이런 방식으로는 원본 lista 값 변경 불가

'''원본 바꾸기1'''
# lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# lista[5] = 100
# indexTemp = 0
# while indexTemp<len(lista):
#     lista[indexTemp] = 100
#     indexTemp += 1
'''원본 바꾸기1 정답'''
# lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# indexTemp = 0
# while indexTemp < len(lista):
#     lista[indexTemp] = 100
#     indexTemp += 1
# print(lista)

'''원본바꾸기2'''
# lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# lista[5] = 100
# for a in lista:
#     a = 100 #이런 방식으로는 원본 lista 값 변경 불가
# print(lista)
# #직접 리스트의 index로 접근해야 원본을 바꿀 수 있다    
# for a in range(len(lista)):
#     lista[a] = 100
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


# *2 출력
# lista = [a*2 for a in range(10)]
# print(lista)

#방법3에 홀수인 값에 2를 곱한 값만 list화
lista = []
for a in range(10):
    if a % 2!= 0:
        lista.append(a*2)
print(lista)