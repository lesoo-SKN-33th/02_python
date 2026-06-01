# 논리형 변수 Boolean

a = True
b = False
print(a, type(a))
print(b, type(b))

# 비교연산
print(10 < 9)
print(10 > 9)
print(10 <= 9)
print(10 == 9)
print(10 != 9)


print("1 > 0.5:", 1 > 0.5)      #t
print("1 < 0.5:", 1 < 0.5)      #f
print("1 >= 0.5:", 1 >= 0.5)    #t
print("1 <= 0.5:", 1 <= 0.5)    #f
print("1 == 1:", 1 == 1)        #t
print("1 != 1:", 1 != 1)        #f


#논리 부정 연산(not)
print(not True)
print(not not True)
print(not not not True)

print(not False)

# and 연산 (소문자)
# A and B -> A가 참, B도 참일때 참
# T and T == T
# T and F == F
# F and T == F
# F and F == F

print('--- and ---')
print(100 > 0 and 1 == 1) # T
print(30 > 20 and 123 != 123) # F
print(3 <= -3 and 12 > 12) # F
print(9 >= 9 / 9 * 9 and 12 != 12 + 1) # T

a = 9 >= 9 / 9 * 9
b = 12 != 12 + 1
print( a and b )


# or 연산
# A 또는 B가 참이면 참
# T and T == T
# T and F == T
# F and T == T
# F and F == F

print('--- or ---')
print(100 > 0 or 1 == 1) # T
print(10 * 10 == 100 or 1 != 1) # T
print(100 == 0 or 10 == 10) # T
print(10 + 20 * 5 == 100 or 30 /10 + 5 == 2) # F


# 합/불합 (T/F)
# 60 이상 합 else 불합

print("---합/불합---")

# int()함수 : str -> int 로 변환
score = int(input('점수를 입력하세요 : '))
print(score)
print(type(score))

result = score >= 60
# print(result)
# print('합격여부 : ',score >= 60)


print('합격여부 : ', '합격' if result == True else '불합격')











