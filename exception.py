'''예외처리 : try except finally 구문
프로그램 실행 중간에 예외가 발생해도 강제 종료 방지'''
# while True:
#     try:
#         #분자 입력 first
#         first = int(input("분자 입력 : "))
#         #분모 입력 second
#         second = int(input("분모 입력 : "))
#         print(first/second)
#         #문제 발생 시 이후 action은 except
#     except ZeroDivisionError as zd:
#         print(f"{zd} 오류")
#     except ValueError as ve:
#         print(f"{ve} 오류")
#     except Exception:
#         print(f"{Exception} 오류")
#     finally: #문제 유무 관계 없이 무조건 실행
#         print("결과 확인")

#부모클래스 raise exception(에러 강제)를 통해 
#자식클래스로 overriding(재정의)유도
'''에러 강제 예시'''
# class Bird:
#     def fly(self):
#         raise Exception
# class Eagle(Bird):
#     pass
# eagle1 = Eagle()
# eagle1.fly()