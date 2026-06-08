'''
모듈이란?
- .py 파일을 의미
    프로그램 내 코드 재사용성을 높이기 위해 모듈단위로 코드를 관리
- 모듈에 작성된 변수, 함수, 클래스 등은 외부레서 import해 사용가능
- 단, _, __ 으로 시작하는 이름은 '내부용 (private)'라는 관례가 있음
    -> 외부에서 import해서 사용하는 것을 지양함
- import * -> 모듈 내 모든 변수, 함수, 클래스 가져오기
    -> 단 _, __로 시작하는 변수, 함수, 클래스는 자동 제외


'''
#파이썬 내장 모듈 math 가져오기
import math

# from _07_module.skn import my_math

print('math.pi', math.pi)

# dir(모듈명) 내장함수 : 해당 모듈의 사용 가능한 속성/함수 등을 나열
print('dir(math)', dir(math))
#dir() 내장함수 : 현재 모듈(_02_modulel.py)의 사용가능한 속성/함수 등을 나열
print('dir():', dir())

#모듈명 확인
#import 시에는 모듈명.py
#현재 모듈 실행 시에는 __main__반환
print('__name__:', __name__)
print('math.__name__:', math.__name__)

print('-'*50)

# 사용자 정의 모듈 가져오기
# import skn.mymath
# 파아썬 패키지로 모듈 가져오기
# from skn import my_math

# import skn.my_math as ms
# print(ms.get_circle_area(4))
# print(ms.pi)
# print(ms.x)
# print('mymath.__z ', ms.__z)

# import * 이용해서 모두 가져오기
# from skn.my_math import *
# print(get_circle_area(4))
# print(pi)
# print(x)
# print('mymath.__z ', __z) # 얘만 안됨
# NameError: name '__z' is not defined
# import * 로 가져올 시 private 변수(__)는 가져오지 않는다


'''import 모듈 별창 처리'''
#import 모듈명 / import 패키지명.모듈명 : 지정된 모듈 가져오기
# -> 사용법 : 모듈명.변수명 / 패키지명.모듈명.변수명

# from 패키지명 import 모듈명 : 지정된 패키지에서 모듈 가져오기
# -> 사용법 : 모듈명.변수명

# import 모듈명 as 별칭
# from 패키지명 import 모듈명 as 별칭
# -> 사용법 : 별칭.변수명

import skn.my_math as ms

print(ms.get_circle_area(4))
print(ms.pi)
print(ms.x)
print('mymath.__z ', ms.__z)

'''
import * 을 이용해서 가져오는 것보다 
import 모듈명, import 모듈명 as 별칭 이 더 권장된다

왜?
변수명, 함수명 충돌 방지 + 가독성 증가(어떤 모듛의 변수/함수인지 구분)

'''

# __name__ : 현재 모듈의 이름 반환
print('__name__:', __name__)

# 현재 모듈을 import 해서 사용하는 경우 하위코드를 실행하지 마시오
if __name__ == '__main__':
    pass # 아무것도 하지 마라


