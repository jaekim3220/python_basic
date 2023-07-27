'''while문 활용한 나만의 리스트 만들기'''
'''리스트 크기를 입력 받아 그 크기만큼 임의 숫자를 리스트에 추가,
리스트의 크기와 값 전체를 출력. 모든 값은 키보드로 입력, 
list 크기는 함수를 통해 도출
list의 크기는 10이하'''
# while True:
#     listsize = int(input("리스트 크기 : "))
#     if listsize > 10 or listsize <= 0:
#         print("잘못된 값 입력")
#         continue
#     a = 0
#     lista = []
#     while a < listsize:        
#         listvalue = int(input("리스트 값 : "))
#         lista.append(int(listvalue))
#         a += 1
#     print(lista)
#     break
    

'''while문 사용한 원본 바꾸기 '''
# lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# listnum = 0
# while listnum < len(lista):
#     lista[listnum] = pow(int(listnum)+1,2)
#     listnum += 1
# print(lista)

'''dictionary_comprehension1'''
# students = ["Alice", "Bob", "Charlie", "David"]
# result = {"{}번".format(number): name for number, name in enumerate(students)}
# print(result)
'''comprehension1'''
# students = ["Alice", "Bob", "Charlie", "David"]
# scores = [90, 85, 95, 80]
# result = {student: score for student, score in zip(students, scores)}
# print(result)
'''comprehension1'''
# students = ["Alice", "Bob", "Charlie", "David"]
# result = {students[i]: scores[i] for i in range(len(students))}
# print(result)