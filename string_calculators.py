# a = 3
# b = 4

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)

'''숫자->문자'''
# a = 10
# b = 20
# print(str(a)+str(b))

'''정수'''
# c = 1234.5678
# print(int(c))

'''반올림'''
# a = round(1.23456)
# b = round(1.23456, 0)
# c = round(1.23456, 1)
# d = round(1.23456, 2)
# e = round(1.23456, 3)
# f = round(1.23456, 4)

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)

'''제곱'''
# print(2**10)
# print(pow(2, 10))
'''제곱근'''
# import math
# print(math.sqrt(1024))

'''multi line'''
# a = 'hello''\n''world'
# b = '''hello

# \tworld'''
# print(a)
# print(b)

# python's easy
# a = 'python\'s'+" easy" # "python\'s"+" easy"
# print(a)
# a = "python is\teasy"
# print(a)

#쌍따옴표(")는 파이썬에서 문자를 의미한다
# print("쌍따옴표(\")는 파이썬에서 문자를 의미한다")

'''문자열 + *'''
'''a라는 변수에 python이라는 문자열을 담고,
b라는 변수에 is fun 이라는 문자열을 담는다
C에 a와 b라는 문자열을 더한 값을 넣어 출력'''
# a = 'python '
# b = 'is fun'
# c = a+b
# print(c)
'''python python is fun이라는 문자열 출력'''
# a = 'python '
# b = 'is fun'
# c = a*2+b
# print(c)

'''특정 순서 출력'''
# a = "python's fun"
# print(a[3])
# a = "abcdefghijk"
# print(a[:-4:-1])

'''길이, 특정 순서 출력'''
# a = "python's fun python's fun python's fun python's fun"
# print(len(a))
# print(a[-1])
# print(a[-3])

'''특정 단어 출력 (for)'''
# a = "python's fun python's fun python's fun python's fun"
# for char in a:
#     if char == 'p':
#         print(char)

'''특정 단어 출력 (if)'''
# a = "python's fun python's fun python's fun python's fun"
# for char in a:
#     if char != 'p':
#         continue
#     print(char)

'''문자열 슬라이싱'''
# a = "python is fun"
# print(a[:6])
# print(a[6:])
# print(a[::2])
# a = "pythonisfun"
# print(a[2:7:2])

# a = "20220505children's_day"
# date = a[:8]
# day = a[8:]
# print(date)
# print(day)

'''문자열 포맷팅'''
# #문자 출력 %s
# names = ['kim', 'park', 'lee']
# for name in names:
#     print('my name is %s' % name)
 
# #기호 정수 출력 %d
# money = 10000
# s2 = 'give me %d won' % money
# print(s2)
 
# # 실수 출력 %f
# d = 3.141592
# print('value %f' % d)

# language = input("좋아하는 언어 입력 ")
# times = input("학습 시간 입력 ")
# sentense = "나는 %s 언어를 %d시간 공부합니다." % (language, int(times))
# print(sentense)
# sentense = "\n나는 "+ language + " 언어를 " + str(times) + "시간 공부합니다."
# print(sentense)

# old = input("나이를 입력 하세요 ")
# wei = input("체중을 입력하세요 ")
# test = "my age is %d, and weight is %f kg" % (int(old), float(wei))
# print(test)

'''문자열 함수'''
# a = "python"
# print(a.count('o'))
# print(a.find('o'))
# print(a.index('o'))
# print(a.find('x')) #find는 도출 값 없으면 -1
# print(a.index('x')) #index는 도출 값 없으면 error

# word = input("아무 문자 입력 : ")
# search = input("찾으려는 문자 : ")
# result = word.find(search)
# if result == -1:
#     print("찾는 문자 없음")
# else:
#     print("찾는 문자는 %d 번째에 있습니다." % int(result+1))

'''문자열 양쪽 공백 없do는 함수 strip'''
# a = '   hello world  '
# b = '\thello world\t'
# print(a.strip())
# print(b)
# myid = input("id 입력 ")
# mypw = input("pw 입력 ")
# print("ID는 %s, 비밀번호는 %s" % (str(myid), str(mypw)))

'''upper'''
# a = "hello"
# print(a.upper())
'''repale'''
# a = 'time to study python'
# print(a)
# print(a.replace('python', 'java'))

'''문자열 분할 함수 split'''
# a = 'time   to   study   python'
# b = a.split()
# print(b)
# b = a.split(" ")
# print(b)
# b = a.split("t")
# print(b)

# x = float(input("숫자 입력 "))
# y = 2.5 * pow(x, 2) + 3.3 * x + 6
# print(y)

'''3개의 단어를 키보드로 입력 받아 단어의 첫 글자 추출 후 단어의 약자를 출력'''
# word1 = input(str("단어 1 "))
# word2 = input(str("단어 2 "))
# word3 = input(str("단어 3 "))
# print("첫 번째 단어 : %s" % word1)
# print("두 번째 단어 : %s" % word2)
# print("세 번째 단어 : %s" % word3)
# print("========================")
# abbr = word1[0]+word2[0]+word3[0]
# print(abbr.upper())