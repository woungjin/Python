'''
x, y, z = 1, 1.0, '1'   # x = 1 ; y = 1.0 , z = '1'
print(x);print(y);print(z)

print(type(x))          # <class 'int'>
print(type(y))          # <class 'float'>
print(type(z))          # <class 'str'>
print('')               # Null문자
print(x+y,type(x+y))    # 2.0 <class 'float'>
print(x*y,type(x*y))    # 1.0 <class 'float'>
#print(x+z)              # TypeError => 문자와 숫자는 연산X

# 변수의 자료형
# 1. 정수(int)  : 0, 양의정수, 음의정수로 구성된 숫자들 
# 2. 실수(float) : 정수를 포함한 소수점 이하의 값을 표시하는 숫자들
# 3. 문자열(str) : 따옴표("" or '')를 사용하여 표시되는 문자들
# 4. bool형 : 참과 거짓으로 표현되는 자료형.  
# =====================프로그램 언어의 기본 자료형================
#    ==> 시퀸스 자료형 <==
# 5. 리스트(List) : 정수, 실수, 문자열과 같은 여러 자료형을 나열한 집한
#                  (값들의 집합)
# 6. 튜플(Tuple) : 정수, 실수, 문자열과 같은 여러 자료형을 나열한 집합
#                  (리스트와 거의 흡사. 단, 요소(멤버)의 값을 변경X)
# 7. 사전(Dictionary) : 정수, 실수, 문자열과 같은 여러 자료형을 나열한 집합
#                  (키(key)와 값(value)의 쌍으로 존재하는 자료)  

# 자료형 변환 함수(형변환 함수) **중요함**
# bool() : 부울형 자료로 변환(True or False)
# int() : 정수형 자료로 변환
# float() : 실수형 자료료 변환
# str() : 문자형 자료로 변환
# list() : 리스트형 자료로 변환
# tuple() : 튜플형 자료로 변환
# dict() : 딕셔너리(사전)형 자료로 변환
# set() : 집합 자료로 변환

# bool() 함수의 사용사례
print(bool(1))      # True
print(bool(0))      # False
print(bool(-1))     # True
print(bool(''))     # False
print(bool(' '))    # True
print(bool('a'))    # True
print(bool([]))     # False
print(bool([-1]))   # True

#int() => 실수, 숫자문자를 정수로 변환
print(int(1.0))     # 1
print(int(1.1))     # 1
print(int('1'))     # 1 (str(x))
#print(int('1.0'))   # ValueError

#float() => 숫자, 숫자문자를 실수로 변환
print(float(1))     # 1.0
print(float('1'))   # 1.0
print(float('1.0')) # 1.0

#str()  => 받은 값을 그대로 문자열로 변환
print(str(1))       # 1
print(str(0))       # 0
print(str(-1))      # -1
print(str(True))    # True
print(str([]))      # []
print(str([1]))     # [1]

# list() => 리스트 자료형으로 변환
print(list('12345'))        # ['1','2','3','4','5']
print(list((1,2,3,4,5)))    # [1,2,3,4,5]

# tuple() => 튜플 자료형으로 변환
print(tuple('12345'))       # ('1','2','3','4','5')
print(tuple([1,2,3,4,5]))   # (1,2,3,4,5)

# dict() => 딕셔너리 자료형으로 변환
print(dict( ( ('a',1),('b',2) ) ))  # {'a':1,'b':2}

# set() => 요소의 순서를 임의 결정됨.
print(set('12345'))
print(set([1,2,3,4,5]))
   
# 예제1  변수선언
var1 = 1
var2 , var3 = 2, 3
var4 = var5 = 4
print(var1);print(var2);print(var3);print(var4);print(var5)

# 예제2 변수의 연산
su1 = 100
su2 = 200
Sum = su1 + su2
print(Sum)      # 300
Sum2 = str(su1) + str(su2)
print(Sum2)     # 100200  이유는 문자열의 더하는 붙여쓰기

# 문제1] : "num1(10) + num2(20) = 30" 라고 출력하세요. 
# 단, 10,20,30은 변수를 사용하여 출력하세요. 

num1 = 10
num2 = 20
result = num1 + num2
print("num1({}) + num2({}) = {}".format(num1,num2,result))

# 문제2] num1 = 7 , num2 = 5 를 선언
# 위의 값을 가지고 연산 결과(+,-,*,/)를 각각 변수에 저장한 후 출력
# (위에 변수 선언 및 연산 결과는 변수에 저장) 
num1,num2 = 7,5
Sum = num1+num2
Sub = num1-num2
Mul = num1*num2
Div = num1/num2
print("더하기 결과 : ",Sum)
print("빼기 결과 : ",Sub)
print("곱하기 결과 : ",Mul)
print("나누기 결과 : ",Div)


# 문제3] 다음과 같이 출력되게 코딩합니다. 
# 단, 변수를 사용해야 합니다!!!!!
#  1) "python 100점!!!"
str1 = "python 100점!!!"
print(str1)

#  2) "나는 오늘 행복합니다.!!!"
str2 = "나는 오늘 행복합니다.!!!"
print(str2)

#  3) python, C언어, JAVA 3과목의 점수를 각 변수에 저장(점수는 맘대로)
#   저장된 값을 사용하여 합계와 평균을 구하는 프로그램을 작성하세요. 
#   (평균은 소수점 2자리까지) 
Python, C언어, Java = 100, 100, 90
합계 = Python + C언어 + Java
평균 = 합계/3
print("Python-{}점\nC언어-{}점\nJava-{}점\n합계:{}, 평균:{:.2f}"\
    .format(Python,C언어,Java,합계,평균))

# 문제4] su = 100, num='100' , flt=1.111 이라는 변수는 선언
# 이것들을 이용해서 다음과 같이 출력되게 코딩해보세요. 
# 
#  출력결과
#  200
#  101.111
#  100100 
su , num, flt = 100 , '100' , 1.111
pr1 = su + int(num)
pr2 = su + flt
pr3 = num + str(su)
print(pr1);print(pr2);print(pr3)

# input()
# -print와 반대 개념으로 문자/숫자를 입력받는 함수
# -사용자로부터 데이터를 입력 받아 변수에 저장할 수 있음.
# -값을 입력받아 숫자 연산처리해야 하는 경우, 반드시 형변환이 필요함.
#  (이유, input()의 반환값 type은 'str'이기 때문) 

print(input())
print(input("여기에는 너가 출력하고픈 내용을 입력해 : "))


# 예제1) 두 수를 입력받아 합을 출력하는 예제
num1 = input("첫번째 정수 입력 : ")
num2 = input("두번째 정수 입력 : ")
print(type(num1),type(num2))
num3 = num1 + num2
print("형변환전 계산 : ",num3)
num3 = int(num1) + int(num2)
print("형변환후 계산 : ",num3)

# 예제2) 입력 값 두개를 받아서 출력하는 예제(데이터 타입)
su1 = int(input("정수 입력 : "))
su2 = float(input("실수 입력 : "))
print("su1 = {}".format(type(su1)))
print("su2 = {}".format(type(su2)))

# 예제3) 두 정수를 입력받아 사칙연산 결과를 출력하는 예제
num1 = int(input("첫번째 정수 입력 : "))
num2 = int(input("두번째 정수 입력 : "))
print("num1 + num2 = ",num1+num2)
print("num1 - num2 = ",num1-num2)
print("num1 * num2 = ",num1*num2)
print("num1 / num2 = ",num1/num2)
'''
# int()의 확장 사용
print(int('0xa',16))
print(int('0b1010',2))
print(int('a',16))
print(int('1010',2))
