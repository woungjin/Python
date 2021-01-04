# x, y, z =1, 1.0, '1'             # 데이터 형태는 다름
# print(x);print(y);print(z)       # ; = 한줄에 여러개의 명령어 사용시, 

# print(type(x))                   # int                  type = 값을 형태로 출력함 = 자료형 10진수로 출력
# print(type(y))                   # float
# print(type(z))                   # str
# print('')                        # = 비어있는 문자 = null
# print(x+y,type(x+y))             # = 정수 + 실수 = 실수 
# print(x*y,type(x*y))             
# print(x+z)                       # = typeerror : 문자와 숫는 연산 x 

 
# =====================================프로그램 언어의 기본 자료형==================================================
#       ＊ 변수의 자료형
#        -> 1, 정수(int)   : 0, 양의 정수, 음의정수로 구성된 숫자들
#        -> 2, 실수(floot) : 정수를 포함한 소수점 이하의 값을 표시하는 숫자들
#        -> 3, 문자열(str) : 따옴표(""or'')를 사용하여 표시되는 문자들
#        -> 4, bool자료형  : 참과 거짓으로 표현되는 자료형(c언어에는 없음)
#                   ------------------------시퀸스 자료형 (=이어서만들어진 자료형) --------------------------
#        -> 5, 리스트(list): 정수, 실수, 문자열과 같은 여러 자료형을 나열한 집합 (결과 값들의 집합) = 괄호 안의 요소를 변경 O
#        -> 6, 튜플(tuple) : 정수, 실수, 문자열과 같은 여러 자료형을 나열한 집합 (리스트와 거의 흡사, 단,요소(멤버)의 값을 변경 X)
#        -> 7, 사전(dictionary) : 정수, 실수, 문자열과 같은 여러 자료형을 나열한 집합 (키(key), 값(value)의 쌍으로 존재하는 자료) ex) 키 = 사전의 색인, 값 = 내용



#       ＊ 자료형 변환 함수(형변환 함수) = 명시적 형변환(지정해서 변환) ★ 중요 ★
#        -> 1, bool() : 부울형 자료로 변환 ( True or false) → 함수는 () 붙어있음
#        -> 2, int()  : 정수형 자료로 변환 ( 가장 많이 사용함 )
#        -> 3, float(): 실수형 자료로 변환 
#        -> 4, str()  : 문자형 자료로 변환 
#        -> 5, list() : 리스트형 자료로 변환  ( 클래스 생성자 )
#        -> 6, tuple(): 튜플형 자료로 변환 (함수안에 괄호가 또 붙음 tuple([])
#        -> 7, dict() : 사전형 자료로 변환 (키와 값의 형태를 필요로 함으로 집어넣줘야함)
#        -> 8, set()  : 집합 자료로 변환(많이 안쓰임)
#

# # bool() 함수의 사용사례  : 값을 표시할게 있으면 Ture , 없으면 false
# print(bool(1))              # True (대,소문자 구분함)
# print(bool(0))              # false
# print(bool(-1))             # True
# print(bool(''))             # false (null문자 = 아무것도 없음)
# print(bool(' '))            # True
# print(bool('a'))            # True
# print(bool([])              # False
# print(bool([-1]))           # True

# # int() => 실수, '숫자'문자를 정수로 변환해주는 함수
# print(int(1.0))             # 실수부분을 정수로 변환
# print(int(1.1))             # 소수점 이하부분 생략 
# print(int('1'))             # str X, 정수 O
# # print(int('1.0'))         # ValueError : str -> 실수 -> 정수 (int는 넣은만큼 변경하기에 두번 넣어야 가능, 한번에 x)

# # float() => 숫자, '숫자'문자를 실수로 변환
# print(float(1))             # 정수 -> 실수 
# print(float('1'))           # 문자 -> 실수
# print(float('1.0'))         

# # str() => 받은값을 그대로 문자열로 출력
# print(str(1))                 # '1'
# print(str(0))
# print(str(-1))
# print(str(True))
# print(str([]))
# print(str([1]))
# print(str(type))

# # list() => list 자료형으로 변환 (()) - 대괄호 사용
# print(list('12345'))
# print(list((1,2,3,4,5)))

# # tuple() => tuple 자료형으로 변환 ([]) 소괄호 사용
# print(tuple('12345'))
# print(tuple([1,2,3,4,5]))

# dict() => 딕셔너리 자료형으로 변환
# print(dict((('a',1),('b',2))))                   # dict() = iterable = 연속된 자료형 , 키 = '키' 붙여줘야함

# set() : 집합 함수 - 요소의 문서를 임의로 결정함, 값들을 뭉쳐서 모아놓는 함수 
# print(set('12345'))              # 값은 집어넣지만 순서는 정해지있지 않음 = 집합 쓸일 이 거의 x 
# print(set([1,2,3,4,5]))

# 예제1
# var1 = 1                # 변수 선언
# var2, var3 = 2, 3
# var4 = var5 = 4
# print(var1);print(var2);print(var3);print(var4)print(var5)

# # 예제2 변수의 연산
# su1 = 100
# su2 = 200
# sum = su1 + su2
# print(sum)
# sum2 = str(su1) + str(su2)
# print(sum2)                 # str의 문자열 더하기는 붙여쓰기


# # 문제1 )  num1(10) + num2(20) = 30" 라고 출력 하세요         #서식문자 사용해서 값이 나오도록 함 
# # 단 10, 20,30은 변수를 사용하여 출력하기
# num1 = 10
# num2 = 20
# result = num1 + num2
# print("num1({}) + num2({}) = result{}".format(num1,num2,result))

# # 문제2 ) num1 = 7 ,  num2 = 5 를 선언                            #간단
# # 위의 값을 가지고 연산 결과(+.-.*./)를 각각 변수에 저장한 후 출력
# # (위에 변수 선언 및 연산 결과는 변수에 저장)

# num1, num2 = 7, 5
# sum = num1 + num2
# sub = num1 - num2
# mul = num1 * num2
# div = num1 / num2
# print("더하기결과 : ",sum)
# print("빼기 결과 : ",sub)
# print("곱하기 결과 :",mul)
# print("나누기 결과 :",div)



# # 문제3] 다음과 같이 출력되게 코딩하기                    #복잡
# # 단, 변수를 사용해야 함
# # 1) "python 100점!!!"
# # 2) "나는 오늘 행복합니다.!!!"
# # 3) "python, c언어, JAVA 3과목의 점수를 각변수에 저장(점수는 맘대로)"
# # 저장된값을 사용하여 합계와 평균을 구하는 프로그램을 작성하세요 
# # (평균은 소수점 2자리까지)

# str1 = "ptyhon 100점!!!"
# print(str1)
# str2 = "나는 오늘도 행복합니다"
# print(str2)
# python , c언어 , Java = 100, 100, 90
# 합계 = python + c언어 + Java
# 평균 = 합계/3
# print("python-{}점\n, c언어-{}점\n, Java-{}점\n : 합계:{}, 평균 :{})"
#         .format(python,c언어,Java,합계,"%.2f"%평균))


# x = 'python100점!!!'
# y = '\n나는 오늘 행복합니다.!!!'
# a = python = int(100)
# b = c언어 = int(70)
# c = JAVA = int(80)
# d = '%.2f'%(a+b+c/3)
# print(x,y)
# print(a+b+c,d)

# # 문제4 su = 100 num = 100 flt =1.111 변수 선언 이것들을 이용해서 다음과 같이 출력되게

# su, num, flt = 100 , '100' , 1.111
# pr1 = su + int(num)
# pr2 = su + flt
# pr3 = num + str(su)
# print(pr1);print(pr2);print(pr3)

# input()                       # cmd창에서 결과값을 나타낼수 있지만 숫자를 처리할려면 형변환 해줘야함  문자형은x 
# -print와 반대 개념으로 문자/숫자를 입력받는 함수
# - 사용자로부터 데이터를 입력 받아 변수에 저장할 수 있음
# - 값을 입력받아 숫자 연산처리해야 하는 경우, 반드시 형변환이 필요함.
# 이유 : intput()의 변환값 type은 'str'이기 떄문 (즉 문자형태로만 입력하기에 숫자로 변화해줘야함)

# print(input())
# print(input(1+2))

# # input 예제1) 두 수를 입력받아 합을 출력하는 예제
# num1 = input("첫번째 정수 입력 : ")
# num2 = input("두번째 정수 입력 : ")
# print(type(num1),type(num2))
# num3 = num1 + num2
# print("형번환전 계산 : ",num3)              # 문자열 연산처리되서 같이 나열됨
# num3 = int(num1) + int(num2)
# print("형변환후 계산 : ", num3)             # 정수로 숫자로 만들어서 연산이 됨 

# # input 예제3) 두 정수를 입력받아 같이 연산 결과르ㅜㄹ 출력하는 예제 
num1 = int(input("첫번째 정수 입력 : "))
num2 = int(input("두번째 정수 입력 : "))
print("num1 + num2 = ",num1+num2)
print("num1 - num2 = ",num1-num2)
print("num1 * num2 = ",num1*num2)
print("num1 / num2 = ",num1/num2)

# # int()의 확장 사용  > float 실수는 진수를 사용하지 않으니 int에서만 
# print(int('0o173',8))       # 기본은 10진수 출력이지만 뒤에 8진수 라고 확장해주면  값을 8진수로 출력
# print(int('0xa',16)) 
# print(int('0b1010',2))
# print(int('a',16))          # int() 괄호안의 뒤에 진수값을 입력하면 앞에 베이스를 진수형으로 나타내지 않아도 가능 