

#변수 : 값을 저장하는 메모리상의 공간
# 변수명 = 값  으로 선언

a = 10 # a라고 명명한 메모리에 10(literal)을 대입
b = 'str'

print('a =', a)
print('b =', b)

#대입 연산자(=)
# 등호 오른쪽 항의 값을 왼쪽 변수에 대입

num = 10
print('num =',num)
print(type(num))
str = 'str'
print(str)
print(type(str))

num = '100'
print('num =',num)
print(type(num))


# 변수 명명규칙
# 1. 의미있는 이름 사용
# 2. snake_case 사용
#   대문자 사용 가능하고, 대소문자 구분됨
# 3. 한글 변수명도 가능
# --
# 4. 변수명은 숫자로 시작하면 안됨('_'로 시작은 가능)
# 5. 언더바 외에 특수문자 사용 불가
# 6. 예약어 변수명으로 사용 불가(ex>for, while, if, else, elif 등 )

# *private 변수 선언 시 _로 시작

team_name = "오지라퍼스"
print(team_name)    # 오지라퍼스

Team_name = "Ohgiraffers"
print(team_name)    # 오지라퍼스
print(Team_name)    # Ohgiraffers

밥조 = "1조"
print(밥조)

# python 예약어 종류 확인
import keyword
print(keyword.kwlist)
