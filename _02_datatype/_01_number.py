# number(숫자형)
# 정수, 실수, 복소수

#type(변수명 | 값) 함수 : 변수 or 값의 type 확인

num = 10
print('num =',num)
print(type(num))

num = '100'
print('num =',num)
print(type(num))

num = 1.0
print('num =',num)
print(type(num))

num = -1
print('num =',num)
print(type(num))

price = 1_000_000_000
print(price, type(price))

#정수 최대값 (2^64)
import sys
print(sys.maxsize, type(sys.maxsize))

#2진법, 8진법, 16진법
a = 0b100 #2진수로 4
print(a, type(a))

b = 0o23 #8진수 19
print(b, type(b))

c = 0xff
print(c, type) # 16진수 255


#실수
f1 = 123.456
print(f1, type(f1))

f2 = -99.999
print(f2, type(f2))

f3 = 1.012345678901234567890
print(f3, type(f3)) # 소수점 아래 16자리까지만 표기

#복소수(complex) 허수 i를 j로 표기
d = 2j
print(d, type(d))

e = 3+4j
print(e, type(e))


#산술연산(+, -, *, /(소수점까지 나누기), //(몫), %(modulo, 나머지))
print('1+2=',1+2)
print('1-2=',1-2)
print('1*2=',1*2)
print('1/2=',1/2) # 나누어 떨어질때까지의 몫 # float으로 return
print('1//2=',1//2)
print('1%2=',1%2)

t1 = 5/4
t2 = 5//4
t3 = 4/2
print(t1, type(t1))
print(t2, type(t2))
print(t3, type(t3))

# 거듭제곱
print( 3**2)
print( 3**3)
print(2**63)




