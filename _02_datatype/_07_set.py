# set(집합) : {} - 중복제거 배열
# 중복허용 x
# sequence type 아님(순서, index 없음)
# 순회(iterable)는 가능
# 집합 관련 메서드 제공됨

print('--- set ---')
st = {2, 4, 1, 3, 2, 3, 3,1,4,1,3,2,4,1,2,4,2,1,3,4,2,3,1,4}
print(st, type(st))
# print(st[0]) # 오류 발생
# TypeError: 'set' object is not subscriptable

print('--- list -> set 변경 (중복제거) ---')
lst = [2, 4, 1, 3, 2, 3, 3,1,4,1,3,2,4,1,2,4,2,1,3,4,2,3,1,4]
st2 = set(lst)
print(st2, type(st2))
lst2 = list(st2) # set -> list로 변환
print(lst2, type(lst2)) # [1, 2, 3, 4] <class 'list'>
print('lst2[2]:', lst2[2])

print('--- tuple -> set 변경 (중복제거) ---')
tpl = (2, 4, 1, 3, 2, 3, 3,1,4,1,3,2,4,1,2,4,2,1,3,4,2,3,1,4)
st3 = set(tpl)
print(st3, type(st3))
tpl2 = list(st3) # set -> list로 변환
print(tpl2, type(tpl2)) # [1, 2, 3, 4] <class 'list'>
print('tpl2[2]:', tpl2[2])

# 요소추가(add)
print('--- 요소추가(add) ---')
my_nums = {20, 30, 40}
my_nums.add(10)
my_nums.add(10)
my_nums.add(10)
print(my_nums, type(my_nums))

# 요소제거(remove)
print('--- 요소제거(remove) ---')
my_nums.remove(10)
print(my_nums, type(my_nums))

# 전체 제거(clear)
my_nums.clear()
print('clear 후 my_nums:', my_nums)

# set 순회
my_nums - {30, 50, 70, 90}
# my_nums에서 값을 하나 꺼내어 num 변수에 저장(반복)
for num in my_nums:
    print(num)


# 집합연산
print('--- set 집합연산 ---')
m = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
n = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}

print('합집합: ', m.union(n))
print('교집합: ', m.intersection(n))
print('차집합: ', m.difference(n)) # m-n
print('대칭차집합: ', m.symmetric_difference(n)) # 합집합 - 교집합