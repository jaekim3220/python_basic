'''list'''
# lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(lista[:5])
# print(type(lista[:5]))

# list_ex1 = ['a', 'b', 'c', [1,2,3]]
# number = list_ex1[3]
# print(number)
# print(number[0]+number[2])

# lista = ['a', 'b', 'c', 'd', 'e', 'f']
# listb = ['1', '2', '3', '4', '5', '6']
# listc = lista + listb
# print(listc)

'''리스트 값 수정'''
# lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(lista)
# lista[2] = 'h'
# print(lista)
# listb = [1,1,2,3,4,5,1,1]
# print(listb)
'''개수 확인'''
# print(lista.count('a'))
# listb[3] = [0,0,0]
# print(listb)
# print(listb.count([0,0,0]))
'''요소삭제(del, remove)'''
# lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# # del lista[:3]
# # print(lista)
# listb = [1,2,3,4,5,6,7,8]
# # del listb[1:5]
# # print(listb)
# lista.remove('a')
# print(lista)
''''''
# listb=[]
# lista = [1,9,3,4,9,6,7,8,9]
# for n in range(0, len(lista)):
#     if lista[n] != 9:
#         listb = listb + [lista[n]]
# print(listb)

''''''
# count = 0
# for a in range(0, len(lista)):
#     if lista[a-count] == 9:
#         del lista[a-count]
#         count = count + 1
# print(lista)

''''''
# lista = [1, 9, 3, 4, 9, 6, 7, 8, 9]
# for i in range(len(lista)-1, -1, -1):
#     if lista[i] == 9:
#         del lista[i]
# print(lista)

'''리스트'''
# lista = [1, 9, 3, 4, 9, 6, 7, 8, 9]
# lista = [n for n in lista if n != 9]
# print(lista)

'''리스트 추가'''
# #append
# lista = [1,3,5,7]
# lista.append(9)
# lista.append(10)
# print(lista)

# #list insert : index를 지정해 추가
# lista.insert(2,'abc')
# print(lista)

# #list extend : iterable 객체를 list에 추가 시 사용
# listb = [10, 20, 30]
# lista.append(listb)
# print(lista)
# # lista.extend(listb)
# # print(lista)

'''정렬'''
# numa = [5,3,18,4,2,1]
# numa.sort()
# print(numa)

# chlist = ['brad', 'john', 'abc']
# chlist.sort()
# print(chlist)

'''위치반환(확인)'''
# lista = ['김돌쇠', '김갑돌', '김갑순', '김철수']
# print(lista.index('김철수'))
'''마지막요소pop'''
# lastvalue = lista.pop()
# print(lastvalue)

# a = int(input())
# if a % 2 == 0:
#     print("%f is even" %a)
# else:
#     print("%f is odd" %a)

# a = int(input())
# if a % 2 == 0:
#     print(f"{a} is even")
# else:
#     print(f"{a} is odd")

#문자 리스트를 문자열로 만들기
#문자열을 문자 리스트로 만들기
''''''
# lista = ['hello', 'world', 'python']
# st1 = ''
# st2 = st1.join(lista)
# print(st2)
''''''
# lista = ['hello', 'world', 'python']
# st1 = ''
# for a in lista:
#     st1 = st1+a
# print(st1)
''''''
# lista = ['hello', 'world', 'python']
# print(' '.join(lista))
# sta = 'hello world python'
# mysta1 = list(sta)
# mysta2 = sta.split()
# print(mysta1)
# print(mysta2)

'''문자열뒤집기'''
# my_string = 'jaron'
# print(''.join(reversed(my_string)))

'''문자열뒤집기1'''
# my_string = 'bread'
# stList = list(my_string)
# stList.reverse()
# answer = ''.join(stList)
# print(answer)
'''문자열뒤집기2'''
# answer = ''.join(reversed(my_string))
# print(answer)

'''list 복습'''
'''최대값/최소값 구하기 1
리스트의 최대값을 정렬함수, 최댓값함수 없이 for문을 통해 출력'''
lista = [50, 10, 100, 40, 55, 90]
# print(lista)
# maxa = lista[0]
# mina = lista[0]
# for a in lista:
#     if maxa < a:
#         maxa = a
#     if mina > a:
#         mina = a
# print("최대값은 {}입니다.".format(maxa))
# print(f"최소값은 {mina}입니다.")
'''최대값/최소값 구하기 2, min()/max()'''
# mina = min(lista)
# maxa = max(lista)
'''최대값/최소값 구하기 3, sort'''
# mina = sorted(lista)
# print(mina)
# print(mina[0])
# maxa = sorted(lista, reverse=True)
# print(maxa[0])
# lista.sort()
# print(lista)
# print(lista[0])
# lista.sort(reverse=True)
# print(lista)
# print(lista[0])
'''4, len'''
# lista.sort()
# mina = lista[0]
# print(mina)
# maxa = lista[len(lista)-1]
# maxa = lista[-1]
# print(maxa)
