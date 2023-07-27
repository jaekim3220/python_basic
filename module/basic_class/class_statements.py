'''클래스 사용 : 같은 기능의 함수의 집합, 객체를 만들기 위해 사용'''
'''사직연산 함수가 있을 때 같은 기능을 하므로 Calculator라는 클래스에 모아둘 수 있음'''
'''명명 규칙 : 일반적으로 클래스는 대문자로 시작하고 변수 명, 함수 명은 소문자로 시작'''
# # 함수의 집합으로서의 클래스 -> 일반적이지 않은 형태
# class Calculator:
#     result = 0
#     def plus(a,b):
#         return a+b
#     def minus(a,b):
#         return a-b
#     def multiply(a,b):
#         return a*b
#     def divide(a,b):
#         return a/b
# print(Calculator.plus(10,20))
# # 위 클래스는 클래스 내에서 누적된 값을 변수로 갖고 있지 않음(문제점)

'''클래스 변수 접근 가능 방법 1 : 클래스명.변수'''
# # 누적을 위해 result 사용
# class Calculator:
#     result = 0
#     def plus(a):
#         Calculator.result += a
#     def minus(a):
#         Calculator.result -= a
#     def multiply(a):
#         Calculator.result *= a
#     def divide(a):
#         Calculator.result /= a
# Calculator.plus(10)
# print(Calculator.result)
# Calculator.minus(5)
# print(Calculator.result)

'''방법 2 : classmethod 데코레이터 사용'''
# class Calculator:
#     result = 0
#     @classmethod
#     def plus(cls,a):
#         #class 내에서 선언된 함수는 매서드라고 부른다
#         cls.result += a
#     def minus(a):
#         Calculator.result -= a
#     def multiply(a):
#         Calculator.result *= a
#     def divide(a):
#         Calculator.result /= a
# Calculator.plus(10)
# print(Calculator.result)
# Calculator.minus(5)
# print(Calculator.result)

'''객체 생성
객체의 사용 이유, 클래스의 복제본 (복제본, 인스턴스라고 부름)
클래스 중복제거 : 변수와 함수의 재활용 어려움 해결'''
# # 객체 형식의 클래스 기본 구조(객체 생성 시 매서드 내의 첫 번째 매개 변수는 객체를 의미)
#객체가 생성될 때 __init__은 가장 먼저 실행
# __init__ : 생성자(클래스가 객체화 될 때 가장 먼저 실행됨, 객체변수 초기 값 세팅)
# class Calculator:
#     def __init__(self): 
#         self.result = 0
# #클래스 내의 함수의 매개 변수가 2개 이상일 때 첫 번째 매개 변수는 객체를 의미
#     def plus(self, a):
#         self.result += a
#     def minus(self, a):
#         self.result -= a
#     def multiply(self, a):
#         self.result *= a
#     def devide(self, a):
#         self.result /= a
# aCompany = Calculator()
# aCompany.plus(100)
# print(aCompany.result)

'''초기 값(매개 변수) 설정'''
# # 초기 값 result와 self.result는 다른 값
# class Calculator:
#     def __init__(self, result): 
#         self.result = result
# #클래스 내의 함수의 매개 변수가 2개 이상일 때 첫 번째 매개 변수는 객체를 의미
#     def plus(self, a):
#         self.result += a
#     def minus(self, a):
#         self.result -= a
#     def multiply(self, a):
#         self.result *= a
#     def devide(self, a):
#         self.result /= a
# #클래스 생성 시 매개 변수(result)를 통해 초기 값 세팅 가능
# aCompany = Calculator(1000)
# print(aCompany.result)
# bCompany = Calculator(2000)
# print(bCompany.result)

'''class 연습 문제'''
'''person이라는 클래스 생성, 생성자(__init__)로 name, age, gender, email이라는 
매개변수를 받아서 각각의 객체 변수를 생성
register 매서드를 만들고 해당 매서드에서는 myInfo라는 객체변수에 이름,나이,성별,email 정보를 
문자열로 담는다
2명의 person을 만들어 print(p1.myInfo), print(p2.myInfo) + 오늘 날짜 추출'''
# import datetime
# class Person():
#     def __init__(self, name, age, gender, email):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.email = email
#         self.signDate = str(datetime.datetime.now())

#     def register(self): #객체 변수를 받는다
#         self.myInfo = (self.name, self.age, self.gender, self.email, self.signDate)
# p1 = Person('김재현', 26, '남', 'jehyunkim21@naver.com')
# p1.register()
# print(p1.myInfo)

# self.myInfo = self.name + self.age + self.gender + self.email
# p1 = Person('김재현', '26', '남', 'jehyunkim21@naver.com')
# p1.register()

'''class의 상속 - 부모 class에서의 기능을 자식 class에서 물려받음
class 자식클래스명(부모클래스명) 형식으로 선언'''
class Calculator:
    def __init__(self):
        self.result = 0
    def plus(self, a):
        self.result += a
    def minus(self, a):
        self.result -= a
    def multiply(self, a):
        self.result *= a
#Calculator 상속 후 매소드 추가 가능
class CalculatorKid(Calculator):
    def devide(self, a):
        self.result /= a
    #같은 함수명에 다른 매개변수를 추가한 매소드 (overloading)-파이썬에서 지원안함
    # def devide(self, a, b):
    #     self.result /= (a + b)
    #부모 기능을 재선언 하면 자식의 기능을 우선해 덮어쓰기(overriding)
    def multiply(self, a):
        self.result *= (a + 1)
    def printCalObject(self):
        return self.result
# 상속될 코드를 print 할 때 아래의 코드 입력
if __name__ == "__main__":
    ck1 = CalculatorKid()
    ck1.plus(100)
    print(ck1.result)
    # print(ck1)
