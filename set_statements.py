'''set은 딕셔너리와 마찬가지로 index가 없고 중복이 없다'''
'''list의 중복을 제거하기 위해 list를 가지고 set으로 형변환 시키는 방식도 사용'''
# s1 = {'이름', '나이', '성별'}
# print(len(s1))
# l1 = ['이름', '나이', '성별']
# s1 = set(l1)
# print(s1)
# s1 = set(['이름', '나이', '성별'])
# s2 = set('test')
# print(s2)
# print(s1[0]) #index가 없으므로 불가

'''예제'''
# 혈액형의 종류
# lista = ['A', 'A', 'A', 'B', 'B', 'AB', 'O']
# seta = set(lista)
# print(f"혈액형의 종류 : {len(seta)}개")
'''seta 값을 하나씩 출력'''
# for a in seta:
#     print(a)

'''합집합'''
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8])
# s3 = s1|s2
# print(s3)
# s3 = s1.union(s2)
# print(s3)
# s3 = s1 and s2
# print(s3)
# s1 = set([1,2,3,4,5,6])
# s2 = set([4,5,6,7,8])
# s3 = s1.intersection(s2)
# print(s3)

'''difference'''
# print(s2.difference(s1))

'''add'''
# s1 = {1,2,3,4,5,6}
# s1.add(7)
# print(s1)

'''update(추가)'''
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,-10,-5])
# s1.update(s2)
# print(s1)

'''remove/discard'''
# s1.remove(6)
# # s1.remove(6) #지울게 없으면 type에러
# s1.discard(6) #지울게 없어도 에러 없음
# print(s1)

'''boolean(불형)타입'''
#in, not in : in(또는 not in) 뒤에 iterable한 자료형이 나온다.
#a in lista, a not in lista, a in dicta.keys()
#비어있는 값들은 거짓, 값이 들어있으면 참
listA = [1,2,3]
while listA:
    print("참이다")
    listA.pop() #무한 방지