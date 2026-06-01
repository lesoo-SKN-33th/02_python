# list : [] - mutable 가변
# tuple : () - immutable 불변한 list
# 데이터 안전 유지, 함수에서 여러 값 반환 시 사용
# sequence type (indexing, slicing, iterable)
# 주로 함수 반환 값, 안전한 데이터 집합 생성 시 사용


print('--- tuple ---')
t1 = () #비어있는 tuple
t2 = (10) # (int)10과 동일
t3 = (10, ) # tuple type으로 인식
t4 = (10, 20) # tuple
t5 = 10, 20 # tuple

print(t1, type(t1))
print(t2, type(t2))
print(t3, type(t3))
print(t4, type(t4))
print(t5, type(t5))


# tuple indexing, 읽기 전용(수정 불가)
tpl = ('a','b','c','d')
print(tpl[0], tpl[1], tpl[2], tpl[3])

# tpl[0] = 'A' # print 시 오류 발생, 수정 불가
# TypeError: 'tuple' object does not support item assignment
# print(tpl[0], tpl[1], tpl[2], tpl[3])

# tuple slicing(list와 동일)
print('--- tuple slicing ---')
print(tpl[:2]) # ('a', 'b')
print(tpl[1::2]) # ('b', 'd')

# tuple unpacking(list와 동일)
print('--- tuple unpacking ---')
a, b, c, d = tpl
print(a, b, c, d)

e, *f = tpl
print(e, f)

g, *h, i = tpl
print(g, h, i)


# tuple 을 이용한 변수값 할당
print('--- tuple 을 이용한 변수값 할당 ---')
num1, num2 = (100, 200) # 괄호 생략된 tuple
print('num1: ',num1)
print('num2: ',num2)


print('--- tuple을 이용한 값 교환(swap) ---')
num1, num2 = num2, num1
print('num1:',num1)
print('num2:',num2)
