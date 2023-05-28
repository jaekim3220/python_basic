'''if 문법'''
# #얼마를 가지고 있습니까
# n = int(input("얼마가 있는가? "))
# if n >= 30000:
#     print("택시를 타시오")
# else:
#     print("도보")

'''(if elif else)'''
'''~중 하나만을 실행시키고자 할 경우 elif를 if에 종속시켜 작성'''
# a = 10
# if a>1:
#     print("if")
# elif a > 100:
#     print("elif")
# else:
#     print("else")

'''if (if else)'''
# a = 10
# if a>1: 
#     print("if")
# if a > 100:
#     print("elif")
# else: #if a > 100:에 종속
#     print("else")

'''if문 한 줄로 작성 조건부표현식(상한연산자)'''
# a = 0
# if a < 1: print("a는 1보다 작다"); print(";은 줄 구분을 위해 사용")

'''삼항연산자 1'''
'''실행문을 실행하기 위해보다 참인 경우, 
거짓인 경우의 값을 쉽게 result에 담기위해 사용'''
# a = 10
# (print("\'a\'는 10보다 크다")) if a>10 else print("\'a\'는 10보다 작다")

'''삼항연산자 2'''
# a = 10
# print('\'a\'는 10보다 크다') if a>10 else print("\'a\'는 10보다 작다")

# a = 10
# result = '\'a\'는 10보다 크다' if a>10 else "\'a\'는 10보다 작다"
# print(result)

'''삼항연산자 예시'''
# lista = list(range(1,11))
# print(lista)
# num = int(input("숫자 입력 : "))
# print("입력한 숫자 존재") if num in lista else print("입력한 숫자가 없음")

'''if 연습문제 1'''
# suitcase = int(input("짐의 무게 : "))
# if suitcase >= 10:
#     money = (suitcase//10)*10000
#     print(f"짐의 무게는 {suitcase}kg, 수수료는 {money}원입니다.")
#     print("짐의 무게는 {%d}kg, 수수료는 {%d}원입니다."%(suitcase, money))
# else:
#     print("수수료 무료입니다.")

'''if 연습문제 2'''
# money = int(input("가진 돈 : "))
# hunger = str(input("yes/no : "))
# result = "밥을 사 먹으시오" if money > 5000 and hunger == 'yes' \
# else '집에 가시오'
# print(result)

'''비교연산자 is(==)'''
# 숫자, 문자, bool의 경우 데이터 pool에서 만들어서 재활용
# 그래서 값 비교 시 메모리 주소가 아니라 데이터 pool에서 값을 비교
