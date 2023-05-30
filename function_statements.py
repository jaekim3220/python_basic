'''특정 input 값이 있을 때 
해당 값을 복잡한 로직을 통해 연산 한다고 가정
해당 연산은 매우 빈번하게 사용 된다고 가정'''

# def myFunc(myInput):
#     # calc = (((myInput+10)*20)/10)**2
#     calc = (myInput+10)**2
#     return calc
# # myInput = int(input("입력 값 : "))
# # result = myFunc(myInput)
# result = myFunc(10)
# print(int(result))

'''사용자의 input을 받아 input 값의 누적 합 더하기'''
'''input 100 = 1+2+3+...+100'''
'''myPlusFunc 함수 구현'''
# def myPlusFunc(myinput):
#     sum = 0
#     for a in range(1, myinput+1):
#         sum += a
#         # print(sum) #sum 변화 확인용으로 넣은 것
#     return sum
# myinput = int(input("입력 값 : "))
# result = myPlusFunc(myinput)
# print(int(result))

'''input 값 2개를 받아 input을 서로 더한 뒤 *2만큼의 결과를 return
이후 해당 값을 호출해 호출된 결과 값을 result에 담아 출력'''

# def myFunction(myinput1, myinput2):
#     myresult = (myinput1 + myinput2)*2
#     return myresult
# myinput1 = int(input("입력 값1 : "))
# myinput2 = int(input("입력 값2 : "))
# result = myFunction(myinput1, myinput2)
# # result = myFunction(100, 50)
# print(int(result))

'''list의 index 함수를 쓰지 않고 for 또는 while문을 통해
몇 번째 인덱스에 있는 값인지 print'''
# lista = [1,4,6,9]
# for a in range(len(lista)):
#     if lista[a] == 9:
#         print(f"index 번호는 : {a}")
#         break # break 생략 가능

'''위의 for문을 활용해 myIndex라는 함수 생성
input 값이 2개(list, 찾고자 하는 값), 
print는 함수 내에서 하지 않고 return에 값을 담는다'''
# lista = [1,4,6,9]
# def myIndex(myinput1, myinput2):
#     result = -1 #index는 거짓일 경우 -1임
#     for a in range(len(myinput1)):
#         if lista[a] == myinput2:
#             result = a
#             break
#     return result
# r1 = myIndex(lista, 9)
# print(r1)

'''함수 내에서 print'''
# lista = [1,4,6,9]
# def myIndex(myinput1, myinput2):
#     result = -1 #index는 거짓이면 -1 출력
#     for a in range(len(myinput1)):
#         if lista[a] == myinput2:
#             print(a)
#             break
# myIndex(lista, 9)

