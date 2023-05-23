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

# c = 1234.5678
# print(int(c))

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

'''제곱/제곱근'''
# print(2**10)
# print(pow(2, 10))

# import math
# print(math.sqrt(1024))

'''multi line'''
# a = 'hello''\n''world'
# b = '''hello

# world'''
# print(a)
# print(b)

# python's easy
# a = "python's"+" easy"
# print(a)
'''a = "python is\teasy"
print(a)'''

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
# c = a*2+b
# print(c)

# a = "python's fun"
# print(a[3])

# a = "python's fun python's fun python's fun python's fun"
# print(len(a))
# print(a[-1])
# print(a[-3])

# a = "abcdefghijk"
# print(a[:-4:-1])

'''문자열 슬라이싱'''
# a = "python is fun"
# print(a[:6:])
# print(a[6::])
# print(a[::2])
# print(a[2:6:2])
# a = "20220505children's_day"
# date = a[:8]
# day = a[8:]
# print(date)
# print(day)

'''문자열 포맷팅'''
# % 기호 문자 출력
names = ['kim', 'park', 'lee']
for name in names:
    print('my name is %s' % name)
 
# % 기호 정수 출력
money = 10000
s2 = 'give me %d won' % money
print(s2)
 
# % 기호 실수 출력
d = 3.141592
print('value %f' % d)