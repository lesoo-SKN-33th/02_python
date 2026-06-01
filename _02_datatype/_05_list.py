# sequence type(시퀀스 자료형)
# str, list, tuple
# 저자된 값의 순서가 유지됨
# 인덱싱과 슬라이싱 가능
# 순회(iterable) 가능

# list
# 여러 값(literal)을 묶어서 관리 (컨테이너 자료형)
# 특징 : 동적으로 list 크기 변할 수 있다(수정 가능)

print('-- list ---')
lst = [1, 2, 3, 4, 5]
print('list:',lst)
print('len(lst):',len(lst))
print('lst[0]:',lst[0])
print('lst[1]:',lst[1])
print('lst[4]:',lst[4])


# list 저장 요소 추가/수정/삭제
# list는 동적으로 크기 변경이 가능한 mutable 자료형이다
# mutable : list, set, dict
# immutable : int, float, bool, str, tuple > 수정 시 버리고 다시 만듦

print('--- list mutable check ---')
print('lst: ', lst)
print('추가 전 id :,', id(lst))
before_id = id(lst)

# list.append(값) : list 끝에 값 추가
print('--- list append ---')
lst.append(999)
print('append 후 lst: ', lst)
print('append 후 id :,', id(lst))

print('append 전후 같은 list(id)인가?', before_id == id(lst))


# list.insert(idx, 값) : idx에 값 삽입
# 지정된 idx부터 뒤에있는 모든 list 값의 idx가 1씩 증가(밀림)

print('--- list insert ---')
lst.insert(1, 1.5)
lst.insert(0, 0)
print('lst[2]:', lst[2], type(lst[2])) # 1.5, float
print('lst[2]:', lst[0], type(lst[0])) # 0, int
print('insert 후 lst: ', lst)
print('insert 후 id :,', id(lst))

print('append 전후, insert 전후 같은 list(id)인가?', before_id == id(lst))

# list update(수정)
# list[index] = 값 (변수에 값 대입해서 변경)
print('--- list update ---')
lst[0] = -10
print('update 후 lst: ', lst)
print('update 후 id :,', id(lst))

print('update 전후 같은 list(id)인가?', before_id == id(lst))


# 특정 인덱스 값 제거
# list.pop(index)
# 제거된 index 뒤 요소들을 한칸씩 당김
print('--- list.pop() ---')
lst.pop(2)
print('pop 후 lst: ', lst)
print('pop 후 id :,', id(lst))

print('pop 전후 같은 list(id)인가?', before_id == id(lst))


# 2차원 list
students = [
    ['홍길동', 30],
    ['이순신', 80],
    ['세종대왕', 100]
]

print('students:', students)
print(students[0][0])
print(students[1])
print(len(students))
print(len(students[0]))

# str.split(구분자)
# str을 구분자를 기준으로 나눠서 list형태로 반환
# csv(Comma Separated Value)
print('--- str.split() ---')
data = '홍길동,20,서울시,서초구'
data_ = data.split(',')
print('data:',data_,type(data_))

name = data_[0]
age = data_[1]
addr1 = data_[2]
addr2 = data_[3]

print(name, age, addr1, addr2)

# list 슬라이싱 (str 슬라이싱과 방법 동일)
print('--- list slicing ---')
texts = ['hello', '안녕', '곤니찌와', 'hi']

# ['hello', '안녕']
print(texts[:2])

# ['안녕', '곤니찌와']
print(texts[1:3])

# ['hello', '곤니찌와']
print(texts[::2])
print(texts[0::2])
print(texts[:4:2])
print(texts[:3:2])
print(texts[0:3:2])
print(texts[0:4:2])

# ['곤니찌와', 'hi']
print(texts[2:4])


# slicing을 이용한 값 변경
print(texts)
print(texts[:2])
texts[:2] = ['aaa', 'bbb']
print(texts)
texts[1:3:1] = ['⭐', '🫶'] # step이 1이 아니면 오류 발생
print(texts)
texts[3:4] = ['eee', 'fff'] # 한 idx에 두개 배열 대입하면 list의 길이 증가
print(texts)


# list 끼리 더하기 연산
print('--- list 더하기 연산 ---')
a = [10, 20]
b = [30, 40]
a = a + b
print(a) # [10, 20, 30, 40]

b = b + a
print(b) # [30, 40, 10, 20, 30, 40]


# list 순회(순차 접근, 순차 반복)
# iterable(반복가능) 특징을 가지는 자료형만 가능

print('--- list 순회 ---')
lst = ['a', 'b', 'c']

# list 요소 순회
for v in lst:
    print(v)

# list 인덱스, 요소 순회
for index, v in enumerate(lst):
    print(f'lst[{index}]: {v}')



# list api
# list.count(값) : list 내에 같은 값이 몇개 있는지 count
print('--- list.count(값) ---')
fruits = ['apple', 'banana', 'cherry', 'apple', 'melon', 'orange']
print('count apple: ',fruits.count('apple'))
print('count banana: ',fruits.count('banana'))
print('count kiwi: ',fruits.count('kiwi'))

# sort : 정렬하다
# list.sort() : 원본 리스트 내에서 정렬(in-place)
# 원본 데이터가 변경(원본데이터 손실)
# sorted(list) : 정렬된 새 리스트 return(not-in-place)
# 원본 데이터 별도 유지

print('--- list.sort() ---')
nums = [100, 30, 50, 70]
print(nums)
nums.sort()
print('오름차순 정렬된 nums: ', nums)
nums.sort(reverse=True) # 내림차순 정렬
print('내림차순 정렬된 nums: ', nums)

#key 속성 -> 정렬 기준 함수
print('--- key 속성 -> 정렬 기준 함수 ---')
fruits.append('kiwi')
fruits.append('watermelon')
print('fruits: ',fruits)

# len 함수를 정렬 기준으로 설정
fruits.sort(key=len)
print('sorted by len : ', fruits)

# 커스텀 정렬기준함수
def my_sort(elem):
    return len(elem), elem # tuple로 우선순위 지정

fruits.sort(key=my_sort)
print(fruits)


print('--- sorted(list) ---')
nums = [9, 2, 4, 7, 1]
print(nums)
nums2 = sorted(nums)
print('nums: ', nums)
print('nums2:',nums2)

# list unpacking(묶음 풀기)
# list == 변수의 묶음
numbers = [10, 20, 30]
a, b, c = numbers
print(f'{a}, {b}, {c}')

# d = 0번 인덱스 요소(10)
# *e = 1,2 인덱스 요소[20, 30]
# -> 나머지를 list형태로 반환
d, *e = numbers
print(f'{d}, {e}')


numbers = [10, 20, 30, 40, 50]
a, *b, c = numbers
print(f'{a}, {b}, {c}')