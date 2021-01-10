'''
# 파이썬의 문자열
# : 파이썬에서 사용되어지는 문자열 처리
# 
#  (특징)
#  1) 인덱싱을 이용한 참조
st = 'python string'
#     0123456789...(index값)
print(st[5])    # n
print(st[3])    # h
#  2) 슬라이싱을 이용한 참조
print(st[0:6])  # python
print(st[7:])   # string
#  3) 문자열의 반복문(for)
st = "python for"
for x in st:
    print(x,end=' ')
print()

# 문자열 함수
# -find(str) : 문자열에서 특정 문자열을 찾아 해당 문자의 index값을 반환
# -count(str) : 문자열에서 특정 문자열을 찾아 해당 문자의 개수를 반환
# -lower() : 문자열에서 영문자를 소문자로 변경하여 반환
# -upper() : 문자열에서 영문자를 대문자로 변경하여 반환
# -strip() : 문자열에서 양쪽 공백 또는 문자를 제거
# -lstrip() : 문자열에서 왼쪽 공백 또는 문자를 제거
# -rstrip() : 문자열에서 오른쪽 공백 또는 문자를 제거
# -replace(old,new) : 문자열에서 왼쪽(old) 문자열을 찾아, 
#       오른쪽(new)문자열로 변경
# -split(str) : 문자열을 특정 문자를 기준으로 분리(저장은 list에...) 

# find(str) 
st = 'python string'
print(st.find('string'))    # 7
# find(str,시작인덱스,끝인덱스)
print(st.find('t'))         # 2
print(st.find('t',2+1))     # 8
# find()가 값을 찾지 못한 경우 : -1
print(st.find('a'))         # -1

# count(str) 
st = 'python string'
print(st.count('t'))        # 2
# count(str,시작인덱스,끝인덱스)
print(st.count('t',6))      # 

# lower() 대문자 => 소문자
st = 'PYTHON STRING'
print(st.lower())           # python string
st = st.lower()
print(st)

# upper() 소문자 => 대문자
st = 'python string'
st = st.upper()
print(st)                   # PYTHON STRING

# strip() : 인자 값이 없는 경우 공백제거, 
#         인자값으로 받은 문자 해당 문자제거
st = '    python string    '
print("[{}]".format(st))    #[    python string    ]
st = st.strip()
print("[{}]".format(st))    #[python string]

# lstrip()
st = '    python string    '
print("[{}]".format(st))    #[    python string    ]
st = st.lstrip()
print("[{}]".format(st))    #[python string    ]

# rstrip()
st = '    python string    '
print("[{}]".format(st))    #[    python string    ]
st = st.lstrip()
print("[{}]".format(st))    #[    python string]

# replace(old,new)
st = 'python string'
st1 = st.replace('string','문자열')
print(st1)                  # python 문자열('string'=>'문자열')

# split(str) : 문자열을 'str'에 있는 문자를 기준 분리(=> 리스트에 저장)
st = 'python string'
st1 = st.split()
print(st1)                  # ['python','string']

##(중요)## : split()을 이용한 입력문자 값 분리
values = input("입력 : ").split(' ')    # 입력값 => I am a student
print(values,type(values))
a,b,c,d = values        # unpacking
print(a,b,c,d)

# 예제1) 문자열 연산 처리(결합 및 반복)
A = 'Have a'
B = ' nice Day!'
C = A + B
print(C)
print(B*3)
A += B
print(A)

# 예제2) 문자열에 영문 대소문자 변경
str1 = 'Python is Easy. Programming 참 쉽죠?... 아..닌가???!!!'
print(str1)
print(str1.lower())
print(str1.upper())
# swapcase() : 영문 대문자를 소문자로, 소문자는 대문자로 변경하는 함수
print(str1.swapcase())
# title() : 영문 단어의 시작을 대문자로 변경
str2 = str1.lower()
print(str2)
print(str2.title())

# 문제1. 아래의 문장 주어진 조건에 맞게 변경
# "NevEr-eVer 100gIVe Up" [변경전]
# "Never-Ever 100Give Up" [변경후]
st = "NevEr-eVer 100gIVe Up"
st1 = st.title()
print(st1)
# Have a nice day 문자열에서 다음 알아오기 
# 'a', 'day', 'dak'의 갯수 알아오기
st2 = "Have a nice day"
a = st2.count('a')
b = st2.count('day')
c = st2.count('dak')
print(a);print(b);print(c)
# 문제2. "It is a fun python class" 문자열의 길이,
# 문자 'a'의 개수, 's'의 개수를 출력하는 코딩 (함수 쓰지마세요... )
st2 = "It is a fun python class"
cnt = cnt_a = cnt_s =0
for i in st2:
    cnt+=1
    if i =='a':
        cnt_a += 1
    elif i == 's':
        cnt_s += 1
print("문자열의 길이 : ",cnt)
print("문장 \'a\'의 개수 : ",cnt_a)
print("문장 \'s\'의 개수 : ",cnt_s)
# 함수사용
print('문자열의 길이 : ',len(st2))
print('문장 \'a\'의 개수 : ',st2.count('a'))
print('문장 \'s\'의 개수 : ',st2.count('s'))

# 문제3. "Have a nice day" 문자열을 가지고 다음을 처리하세요.
#  - 각각 find와 index를 사용하여 "day"문자의 위치를 찾으세요.
#  - 각각 find와 index를 사용하여 "kkk"문자의 위치를 찾으세요. 
#  - find를 사용하여 첫번째, 두번째, 세번째, 네번째 'a'의 위치를 
#   출력하세요.
st3 = "Have a nice day"
print("find(\'day\') : ",st3.find('day'))
print("index(\'day\') : ",st3.index('day'))
print("find(\'kkk\') : ",st3.find('kkk'))
#print("index(\'kkk\') : ",st3.index('kkk'))

idx = st3.find('a')
print("find : 첫번째 \'a\'의 위치 : ",idx)
idx = st3.find('a',idx+1)
print("find : 두번째 \'a\'의 위치 : ",idx)
idx = st3.find('a',idx+1)
print("find : 세번째 \'a\'의 위치 : ",idx)
idx = st3.find('a',idx+1)
print("find : 네번째 \'a\'의 위치 : ",idx)

#[ Quiz ] : List를 정의 하여 첨자 위치 저장
#a의 총 개수와 첨자의 위치를 출력 하시오
#st = 'Have a nice day Have a nice day Have a nice day'
#결과 
#a 개수 : 9
#첨자 : [1, 5, 13, 17, 21, 29, 33, 37, 45]
st = 'Have a nice day Have a nice day Have a nice day'
idx = 0
cnt_a = 0
ls = []
while True:
    idx = st.find('a',idx)
    if idx != -1:
        ls.append(idx)
        idx += 1
        cnt_a+=1
    else:
        break
print("a 개수 : ",cnt_a)   # cnt_a => count('a')
print("첨자 : ",ls)

# strip() 
st1 = "파이썬파"
print(st1.strip('파'))      # 이썬
print(st1.lstrip('파'))     # 이썬파
print(st1.rstrip('파'))     # 파이썬

st2 = "---파이썬---"
print(st2.strip('-'))       # 파이썬
print(st2.lstrip('-'))      # 파이썬---
print(st2.rstrip('-'))      # ---파이썬

# replace()
st ="2019-12-20"
#    0123456789 (인덱스)
print(st)
print(st.replace('2019','2020'))
print(st[0:4])  # 2019
print(st.replace(st[0:4],'2022'))
'''
# split(str) : 특정 문자를 기준으로 문자열 나누는 함수(저장 => 리스트)
st = "Never Ever Give Up" 
a =st.split()  #공백 기준으로 나누겠다. 
print(st)
print(a,type(a))

st2 = "하나:둘:셋"
st3 = "1,2,3"
b = st2.split(':')
c = st3.split(',')
print(b,type(b))
print(c,type(c))

st4 = "하나둘셋넷"
d = st4.split()
print(d,type(d))

# splitlines() : 개행('\n')을 기준으로 문자열을 나눈 함수
st = """Never Ever Give UP
Never Ever Give UP
Never Ever Give UP
Never Ever Give UP
Never Ever Give UP"""   #""" ~ """ :여러줄 문자열을 표기할 경우 사용
print(st)
a = st.splitlines()
print(a,type(a))

# join() : 지정한 문자열을 기준으로 문자열을 결합
st = '123'
print(st.join('%%'))    # %123%
print('%'.join(st))     # 1%2%3
lst1 = ["","123","456"]
print("".join(lst1))    # 123456 => """"123""456
lst2 = ["","안녕","반가워","또만나!"]
print("\n".join(lst2))
lst3 = input("입력 : ").split()     # I am a student
print("join전 split : ",lst3)
print("join한 결과 : "," ".join(lst3))

#Python 문자열 실습 문제
#문제1. input() 함수로 이름과 나이 값을 입력 받을 때 한번에 입력
#      받아 처리하고 출력하는 코드를 작성하시오. 

in_txt = input("이름과 나이를 입력[예) 홍길동 19]: ")
name,age = in_txt.split()   # name,age = ['홍길동','19']
print("이름 : {} , 나이 : {}".format(name,age))

#문제2. input() 함수로 입력 받은 수의 더하기,빼기,곱하기,나누기의 
#      간단한 수식을 처리할 수 있도록 코드를 작성하시오.
#      예) 5+5 입력시에 결과를 출력 10 

import os

while True:
    os.system('cls')
    calc = input("계산할 수식을 입력하세요[ex) 5+5 ]: ")
    if '+' in calc:
        num1,num2 = calc.split('+')
        num1 = int(num1)
        num2 = int(num2)
        print("계산 결과는 : ",num1+num2)
    elif '-' in calc:
        num1,num2 = calc.split('-')
        num1 = int(num1)
        num2 = int(num2)
        print("계산 결과는 : ",num1-num2)
    elif '*' in calc:
        num1,num2 = calc.split('*')
        num1 = int(num1)
        num2 = int(num2)
        print("계산 결과는 : ",num1*num2)
    elif '/' in calc:
        num1,num2 = calc.split('/')
        num1 = int(num1)
        num2 = int(num2)
        print("계산 결과는 : ",num1/num2)
    else:
        print("수식 입력이 잘못됐습니다.")
    sel = input("계속 하시겠습니까?(yes(default)/no)")
    if sel == 'no':
        break
print("프로그램 종료합니다.")
