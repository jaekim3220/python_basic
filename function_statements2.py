'''복습 연습문제(사용자 정의 함수)'''
'''키보드로 반지름의 길이를 입력, 원의 넓이를 구하는 함수를 만들어 결과 출력'''
# def circleSize(num1):
#     # show = 0
#     # for a in range(num1):
#     #     show = (pow(num1,2))*3.14
#     show = (pow(num1,2))*3.14
#     return show
# num1 = int(input("반지름 길이 : "))
# result = circleSize(num1)
# print("원의 넓이 : {}".format(str(result)))

'''복습 연습문제 (입력 값 없는 함수)'''
'''hello1() 호출 시 hello1 python 출럭, 
print(hello2()) 호출 시 hello2 python 출력'''
# def hello1():
#     print("hello1 python")

# def hello2():
#     answer = "hello2 python"
#     return answer

# hello1()
# print(hello2()) #return 존재
# print(hello1())

'''복습 연습문제 (입력 값의 수가 정해져 있지 않고 multiple한 함수)'''
'''입력한 값을 모두 더하는 함수 한수보다 for문 사용'''
# def mySum(*args): # *는 all이라는 의미를 가짐
#     # print(args)
#     # return 0 
#     # return sum(args) #이거 말고 for문 사용
#     answer = 0
#     for a in args:
#         answer += a
#     return answer
# totalvalue = mySum(1,2,3,4,5)
# print(totalvalue)

'''복습 예제 2개 이상의 리턴 값이 있는 경우'''
# def myCall(a, b):
#     result1 = a+b
#     result2 = a-b
#     result3 = a*b
#     return result1, result2, result3
# callvalue = myCall(5,1)
# print(f"첫 번째 결과 값 : {callvalue[0]}")
# print(f"두 번째 결과 값 : {callvalue[1]}")
# print(f"세 번째 결과 값 : {callvalue[2]}")

'''예제 함수에서 default 값 미리 세팅 전'''
# def myCall(a, b, c):
#     if c == 'plus':
#         result = a+b
#     elif c == 'min':
#         result = a-b
#     elif c == 'multi':
#         result = a*b
#     return result
# callresult1 = myCall(5, 1, 'plus')
# callresult2 = myCall(5, 1, 'min')
# callresult3 = myCall(5, 1, 'multi')
# print(f"덧셈 : {callresult1}, 뺄셈 : {callresult2}, 곱셈 : {callresult3}")

'''예제 함수에서 default 값 미리 세팅 후
(default 세팅 후 다른 default 값 진행 시 앞의 default 값 덮어쓰기)'''
# def myCall(a, b, c='plus'):
#     if c == 'plus':
#         result = a+b
#     elif c == 'min':
#         result = a-b
#     elif c == 'multi':
#         result = a*b
#     return result
# callresult1 = myCall(5, 1)
# callresult2 = myCall(5, 1, 'min')
# callresult3 = myCall(5, 1, 'multi')
# print(f"덧셈 : {callresult1}, 뺄셈 : {callresult2}, 곱셈 : {callresult3}")

'''매개변수 input의 순서를 맞추지 않아도
원하는 매개변수 자리에 값을 넣어 함수 호출 방법'''
# def whoRU(name, age, gender):
#     print(f"이름 : {name}, 나이 : {age}, 성별 : {gender}")
# whoRU(age=19,name='홍길동', gender='남자')

'''default 값 세팅(옵션 덮어쓰기) + 매개변수 값을 넣어 호출
print 2개를 사용해 줄바꿈 없이 hello world 출력'''
# print('hello', end = '')
# print(' world')

'''지역변수(함수 내부 변수, 함수내에서 유효)
전역변수(함수 밖 변수, 함수내에서도 인식 가능 수정불가)'''
# a = 100
# def sum(a,b):
#     #여기서 a 값은 100인가 10인가?
#     #전역변수인 a=100보다, 함수내에서 선언한 a=10을 우선 인식
#     result = a+b
#     return result
# result = sum(10,20)
# print(result) 
# #함수내의 result라는 변수는 함수 밖에서는 인식 불가
# #result를 print 가능한 이유는 함수내에서 어떤 값을 return 했기 때문
# print(a)
'''함수내에서 전역변수에 영향을 끼치는 방법(global)'''
# #기본적으로 함수내에서 함수밖 전역변수 수정 불가
# #저장되는 메모리 위치가 다르기 때문
# result = 0
# def sum(a):
#     # global result #존재유무 확인해볼 것
#     result += a
#     return result
# value = sum(10)
# print(value)

'''for문 변수(문제없음)
for문마다 같은 변수를 사용하는 것은 전역변수이기는 하지만
재할당을 해서 사용하는 것이므로 rest되서 문제가 없음'''
# lista = [10,20,30,40]
# for a in range(len(lista)):
#     print(a)
# print('\n')
# for a in range(len(lista)):
#     print(a)
# print(a)
'''2중 for문 사용 시 문제될 여지가 있음
상위의 for문의 변수를 잃어버리게 됨'''
# lista = [10,20,30,40]
# for a in range(len(lista)):
#     for a in range(len(lista)):
#         print(a)
#         print('\n')
#         print(a)

'''객체는 힙메모리 영역에 저장, 함수 내에서도 접근해 추가/수정이 가능'''
# lista = [2,3,4]
# def appendtest(in1, in2):
#     in1.append(in2)
# appendtest(lista, 5)
# print(lista)

'''지역변수가 함수호출이 끝난 뒤에도 남는 경우
메모리 낭비와 다른 함수에서 해당 변수명 사용이 불가한 불편함 야기'''
# def test1(result):
#     result += 10
#     return result
# def test2():
#     result += 100
#     return result
# a = test1(20)
# print(a)
# b = test2(20)
# print(b)

'''선택정렬 함수화'''
def mySort(lista):  
    for a in range(len(lista)-1): 
        for b in range(a+1, len(lista)):
            if lista[a] > lista[b]:
                temp = lista[a]
                lista[a] = lista[b]
                lista[b] = temp
lst = [56,78,21,12,5,89,2,54,87] 
#객체는 함수 내에서 원본변경 가능 return 선택, 객체 아닌건 함수 내에서 원본변경 불가 return 필수
mySort(lst)
#return 필요 없음(lst 값이 아닌 lst의 메모리 주소를 전달), 원본을 바꿀 경우 return 필요
print(lst)

''''''
# lista = [5,1,2]
# listb = lista
# print(id(lista))
# print(id(listb))
# import copy
# listb = copy.copy(lista)
# print(id(listb))
# print(listb)
# lista[0] = listb[1]
# print(lista)
