'''dictionary(map)'''
#다른 language의 map 또는 hashmap과 유사한 자료형
#json이라는 자료 형태와 유사함

#특징 1 중복 불가
# dic1 = {'이름' : '홍길동', '나이' : 25, '성별' : '남'}
# dic1 = {'이름' : '홍길동', '나이' : 25, '성별' : '남', '성별' : '여'}
# print(dic1)
#딕셔너리의 기본호출 방식은 변수명[key]
# print(dic1['나이'])
# print(dic1.get('성별'))

#리스트는 a = [value, ...]
#딕셔너리는 a= {key:value}, ... 튜플은 a = (value, ...)

#특징 2 key, value 값으로 이루어져 순서가 의미 없음, index로 접근 불가
#key를 가지고 value를 검색할 때 해시 함수를 통해 index를 찾다보니, 매우 빠른 속도 보장

'''예제'''
# dic1 = {'이름' : '홍길동', '나이' : 25, '몸무게' : 60, '성별' : '남', '성별' : '여'}
'''key:value 추가'''
# print(dic1)
# dic1['신분'] = '학생'
# print(dic1)
'''key:value 삭제'''
# del dic1['성별']
# print(dic1)

'''딕셔너리 수정/추가'''
# days_in_month = {"1월":31, "2월":28, "3월":31}
# days_in_month["2월"] = 29
# days_in_month["4월"] = 30
# print(days_in_month)

'''수정/삭제'''
# dic = {'one' : 1, 'two' : 2}
# print(dic)
# dic['three'] = 3    # 값을 추가합니다  {'one' : 1, 'two' : 2, 'three' : 3}
# print(dic)
# dic['one'] = 11     # 값을 수정합니다  {'one' : 11, 'two' : 2, 'three' : 3}
# print(dic)
# del(dic['one'])     # 값을 삭제합니다  {'two' : 2, 'three' : 3}
# print(dic)
# dic.pop('two')      # 값을 삭제합니다  {'three' : 3}
# print(dic)

'''keys/values 목록만 뽑아낼 때'''
# keyList = dic1.keys()
# print(keyList)
# valList = dic1.values()
# print(valList)

'''keylist에서 각각의 값을 출력'''
# for k in keyList:
#     print(k)

'''value 유도1'''
# for v in dic1.values():
#     print(v)

'''value 유도2'''
# valList = dic1.values()
# print(valList)
# for v in valList:
#     print(v)

'''key을 출력해주는 for문 안에서 value도 같이 출력1'''
# for k,v in dic1.items():
#     print("key 값 {}, value 값 {}".format(k,v))
#     print(f"key 값 {k}, value 값 {v}")

'''key을 출력해주는 for문 안에서 value도 같이 출력2'''
# for k in keyList:
#     print(k)
#     print(dic1[k])

'''for문을 사용해 key 값, value 값이 담긴 list 생성1'''
# key_value_list = []
# for k in keyList:
#     key_value_list.append((k, dic1[k]))
# print(key_value_list)

'''for문을 사용해 key 값, value 값이 담긴 list 생성2'''
# key_list = []
# value_list = []
# for k in keyList:
#     key_list.append(k)
#     value_list.append(dic1[k])
# print(key_list, value_list)

'''딕셔너리의 확장(추가) : update 함수(list의 extend)'''
# dic1 = {'a':1, 'b':2, 'c':3}
# dic2 = {'a':2, 'd':4, 'f':5}
# print(dic1)
# dic1.update(dic2)
# print(dic1)

'''리스트를 딕셔너리로 변환1'''
# lista = ['A', 'A', 'B', 'O', 'O', 'AB', 'AB']
# dica = {}
# for a in lista:
#     if a not in dica:
#         dica[a] = 1
#     else:
#         dica[a] += 1
# print(dica)

'''리스트를 딕셔너리로 변환2'''
# lista = ['A', 'A', 'B', 'O', 'O', 'AB', 'AB']
# dica = {}
# for a in lista:
#     if a not in dica.keys():
#         dica[a] = lista.count(a)
# print(dica)

'''완주하지 못한 선수1'''
# participant = ["mislav", "stanko", "mislav", "ana"]
# completion = ["stanko", "ana", "mislav"]

# for person in participant:
#     if person in completion:
#         completion.remove(person)
#     else:
#         print(person)

'''완주하지 못한 선수2'''
# participant = ["mislav", "stanko", "mislav", "ana"]
# completion = ["stanko", "ana", "mislav"]
# dictc = {}
# for c in completion:
#     if c not in dictc.keys():
#         dictc[c] = 1
#     else:
#         dictc[c] += 1
# for p in participant:
#     if p in dictc.keys() and dictc[p] > 0:
#         dictc[p] -= 1
#     else:
#         print(p)

