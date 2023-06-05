# file 시스템 입/출력 라이브러리 : open
# open 함수는 w : 덮어쓰기, r : read, a : 추가
# open 시 해당 파일 명이 없으면 자동 생성

# f = open("text.txt", 'w') # txt파일 생성

'''write'''
# f = open("text.txt", 'w', encoding="UTF-8")
# for i in range(0,10):
#     data = "%d번째 줄\n" %i
#     f.write(data)
# f.close()

# '''read'''
# f = open("text.txt", 'r', encoding="UTF-8")
# ## 첫 번째 줄만 가져오는 함수
# line = f.readline()
# print(line)
# f.close()
# # while, if 문으로 readline으로 전체 출력
# f = open("text.txt", 'r', encoding="UTF-8")
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)
# f.close()
''''''
# f = open("text.txt", 'r', encoding = "UTF-8")
# # readlines : 데이터를 리스트 형태로 라인별로 담아준다
# lines = f.read()
# print(lines)

'''a 옵션으로 추가모드'''
# f = open("text.txt", 'a', encoding = "UTF-8")
# # 0~9 번째 줄입니다 -> 10번째~19번째 줄입니다.
# for i in range(10,20):
#     data = "%d번째 줄\n" %i
#     f.write(data)
# f.close()

'''파이썬에서 객체 생성 후 힙 메모리에 객체를 할당, 
객체 사용이 끝나면 객체를 close할 필요는 없음
파이썬에는 GC(Garbage Collector)가 내장돼 자동으로 사용 빈도가
낮은 데이터는 메모리에서 삭제
파일 시스템은 그렇지 못하므로 수동으로 닫아야 메모리 낭비 방지'''

#os 라이브러리 활용한 디렉터리 내부 파일 검색
# 모든 폴더까지 검색
# 파일, 디렉토리 목록을 뽑아내는 listdir 함수 사용

import os 
searchDir = r'C:\Users\jehyu\Desktop\nationalsupport'
dirList = os.listdir(searchDir)
for dir in dirList:
    filename = os.path.join(searchDir, dir) #폴더 명 찾기
    if os.path.isdir(filename):
        dirList2 = os.listdir(filename)
        for dir2 in dirList2:
            dirTuple2 = os.path.splitext(dir2)
            if(dirTuple2[1]=='.py'):
                fullPath = os.path.join(filename, dir2)
                print(fullPath)
    dirTuple = os.path.splitext(dir)
    if(dirTuple[1]=='.py'):
        fullPath = os.path.join(searchDir, dir)
        print(fullPath)
'''재귀함수화
예외처리 포함 안됨'''
# import os 
# def searchRecur(searchDir):
#     # searchDir = r'C:\Users\jehyu\Desktop\nationalsupport'
#     dirList = os.listdir(searchDir)
#     if not dirList:
#         return
#     for dir in dirList:
#         filename = os.path.join(searchDir, dir)
#         if os.path.isdir(filename):
#             searchRecur(filename)
#         dirTuple = os.path.splitext(dir)
#         if(dirTuple[1]=='.py'):
#             fullPath = os.path.join(searchDir, dir)
#             print(fullPath)
# # searchDir = r'C:\Users\jehyu\Desktop\nationalsupport'
# searchDir = r'C:' #C에서 뒤지기
# searchRecur(searchDir)

'''강제종료 방지(try, exception)'''
# import os 
# def searchRecur(searchDir):
#     try:
#         # searchDir = r'C:\Users\jehyu\Desktop\nationalsupport'
#         dirList = os.listdir(searchDir)
#         if not dirList:
#             return
#         for dir in dirList:
#             filename = os.path.join(searchDir, dir)
#             if os.path.isdir(filename):
#                 searchRecur(filename)
#             dirTuple = os.path.splitext(dir)
#             if(dirTuple[1]=='.py'):
#                 fullPath = os.path.join(searchDir, dir)
#     except Exception:
#             print(fullPath)
# searchDir = r'C:\Users\jehyu\Desktop\nationalsupport'
# # searchDir = r'C:' #C에서 뒤지기
# searchRecur(searchDir)