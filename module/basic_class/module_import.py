#from 폴더 명 import 파일 명 as 약어
#import 폴더 명.파일 명
# import하고싶은 모듈이 있을 경우 import 구문을 사용(상속)
# import module_statements #1 같은 폴더
# from module import module_statements #2 다른 폴더
# import module.module_statements as ms # 2.5 다른 폴더 + 약어
# print(ms.plus(10,20))

import class_statements as cs
c1 = cs.CalculatorKid()
c1.plus(100)
print(f"module_import의 result : {c1.result}")