'''
# ASCII 코드
#  미국의 표준 문자 코드로 7bit(0 ~ 127)로 하나의 문자를 표현
# ASCII 코드는 통신상 기본 문자 코드로 사용되고 있음.
# 
# (특징)
# 1. 프린트 가능한 문자는 총 95개, 나머지 33는 프린트 불가능한 문자
#   프린트 가능문자는 0x20(32)(space)부터 시작 0x7E(126)까지
# 2. 숫자는 0x30(0) ~ 0x39(9)까지 10개의 코드
# 3. 영문 대문자는 0x41(65)='A'에서 부터 0x5A(90)='Z'
# 4. 영문 소문자는 0x61(97)='a'에서 부터 0x7A(122)='z'
# 5. ASCII코드는 문자이나 숫자(정수)로 표현이 가능한 코드
# 
# 숫자를 문자(ASCII)로 변경하는 함수 : chr()
# : chr()은 "()"엔에 ASCII코드를 입력하면 문자로 출력함. 

print(chr(0x41))  # 'A'
print(chr(65))

# 문제5] 'A' ~ 'Z'까지의 임의 문자 3자를 출력하는 코드를 작성하세요!!

from random import random,randint

for x in range(3):
    ch = int(random()*26)+65  # 65 ~ 90 => ch = randint(65,90)
    print(chr(ch),end='')
print()


# LIST #################################
# list 자료형이란? 
#   -데이터 목록을 다루는 자료형
#   -리스트 정의할 때는 "[]"를 사용함.
#   -리스트 안에는 어떤 종류의 자료형이든 상관없이 저장 가능.
# 
# list 자료형의 기본 사용
# 
#  (정의-선언)
#  변수명 = []          # 비어 있는 리스트를 생성
#  변수명 = [value1,value2,value3, .... ]
# 
#  (list()를 이용한 리스트 생성)
#  변수명 = list()          # 비어 있는 리스트를 생성
#  변수명 = list("Hello")   # ['H','e','l','l','o'] 문자를 가지는 리스트
#  변수명 = list(range(5))  # [0,1,2,3,4] 정수 값을 가지는 리스트

# 예제1
lst = [1,2,3,4,5,6,7,8]
print(lst,type(lst))

# 리스트의 특정 값을 참조하는 방법 : indexing
# 인덱싱은 "index"값을 사용하여 특정 멤버를 참조
# index값은 리스트의 멤버의 순서번호로 시작은 0부터...  
lst = [1,2,3,4,5,6,7,8]
#index 0 1 2 3 4 5 6 7 
print(lst[0])   # 1 출력
print(lst[6])   # 7 출력

# 인덱싱을 이용한 list값 변경
lst[0] = lst[5]     # lst[0] = 6(=> lst[5]의 값)
print(lst[0])       # 6
print(lst)          # [6,2,3,4,5,6,7,8]

# 리스트 자료의 길이 : len() => 요소[멤버]의 개수를 반환하는 함수
print("lst의 길이 : ",len(lst)) #lst안에 있는 요소[멤버]의 개수를 반환

# 리스트 자료형의 결합1(병합)
lst2 = [9,10]
print(lst+lst2)     # [6,2,3,4,5,6,7,8,9,10]
lst3 = lst + lst2   # lst3 = [6,2,3,4,5,6,7,8,9,10]
print(lst3)

# 리스트 자료형의 결합2(확장)
lst = lst + lst2
print(lst)          # [6,2,3,4,5,6,7,8,9,10]

# 리스트 자료형의 반복
print(lst2*3)       # [9,10,9,10,9,10]

# max(), min()
# lst = [6,2,3,4,5,6,7,8,9,10]
print(max(lst))
print(min(lst))
print(sum(lst))

# 예제2] 변수를 선언 3개의 정수를 입력받아 출력하는 코딩
# 출력 결과 >>"합계 = xx" <"합계"라는 문자열도 변수 처리>

# list사용X
a = int(input("첫번째 정수 입력 : "))
b = int(input("두번째 정수 입력 : "))
c = int(input("세번째 정수 입력 : "))
d ="합계"
Sum = a + b + c
print("{} = {}".format(d,Sum))

# list사용
lst = [0,0,0,"합계"]
lst[0] = int(input("첫번째 정수 입력 : "))
lst[1] = int(input("두번째 정수 입력 : "))
lst[2] = int(input("세번째 정수 입력 : "))
Sum = lst[0] + lst[1] + lst[2] 
print("{} = {}".format(lst[3],Sum))

# LIST 인덱싱
# : index값을 이용한 참조
# 
#       lst = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 양의 인덱스 :  0  1  2  3  4  5  6  7  8  9 
# 음의 인덱스 :-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
# 

# 예제3, List의 인덱스
lst = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# (+)   0  1  2  3  4  5  6  7  8  9
# (-) -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
print('lst[]',lst)
print('lst[-1]',lst[-1])    # 10
print('lst[-2]',lst[-2])    # 9
print('lst[-3]',lst[-3])    # 8

# slicing방식을 이용한 시퀸스 객체(자료) 접근
# slicing이란? 리스트와 같은 시퀸스 자료 값들의 범위로 접근하기 위해서
#       사용하는 방법으로 시퀸스 객체(자료)의 일부분을 잘라서 새롭게
#       생성하는 것을 의미함. 
# 
#   (형식)
#   변수명[시작인덱스:끝인덱스]
#   변수명[시작인덱스:끝인덱스:증감값]
# 
#   예] lst = [ 1, 2, 3, 4, 5, 6]
#      index    0  1  2  3  4  5
#       (-)    -6 -5 -4 -3 -2 -1 
# 
#    lst[0:3] = [1,2,3] , lst[0:3:2] = [1,3]

# 예제4) slicing을 이용한 리스트에 대한 접근
lst = [ 1, 2, 3, 4, 5, 6]
# index 0  1  2  3  4  5
# (-)  -6 -5 -4 -3 -2 -1
print(lst[0:3])     # [1,2,3]
print(lst[0:3:2])   # [1,3]
print(lst[5:0:-3])  # [6,3]

# slicing의 인덱스 값 생략
print(lst[:3])      # [1,2,3]
print(lst[3:])      # [4,5,6]

# slicing 후에 새로운 리스트 생성
slc = lst[3:6]      # [4,5,6]
print(slc)
slc2 = lst[1:5:3]   # [2,5]
print(slc2)
slc3 = lst[5::-1]   # [6,5,4,3,2,1]
print(slc3)
slc4 = lst[-3:-1]   # [4,5]
print(slc4)
'''
# 리스트 함수들.... 
# : 리스트 자료형에 대한 처리를 하는 함수들... 
# 1)append(value) : 리스트 끝에 값을 추가(멤버를 추가)
# 2)extend(iter(스퀸스자료-리스트)) : 리스트 끝에 list,tuple, dict의
#              값을 하나씩 추가.
# 3)insert(idx,value) : 인덱스(idx)에 있는 위치에 특정값을 추가하는 함수 
# 4)pop([idx]) : 인덱스를 지정하지 않으면, 마지막 인덱스 값을 반환후 삭제
#              인덱스를 지정하면, 해당 인덱스 값을 반환후 삭제
# 5)remove(value) : 특정 값을 찾아서 삭제하는 함수 
# 6)clear() : 리스트의 모든 멤버를 삭제하고, 빈 리스트를 반환 
# 7)count(value) : 리스트 내에 특정 값의 개수를 반환하는 함수
# 8)index(value) : 리스트 내에 특정 값의 인덱스값을 반환하는 함수
# 9)reverse() : 리스트 맴버의 순서를 역으로 뒤집어 나열하는 함수
# 10)sort([reverse=False]) : 리스트의 값을 오름차순(False), 
#                         내림차순(True)으로 정렬해주는 함수   

# append(value) : 리스트 끝에 값을 추가
lst1 = [1,2,3,4,5]
lst1.append('a')
print(lst1)
lst1.append([9,10])
print(lst1)         # [1,2,3,4,5,'a',[9,10]]
print(lst1[-1])     # [9,10]

# extend(iter) : 리스트 뒤에 추가할 list,tuple,dict자료 멤버들을 추가
lst1 = [1,2,3,4,5,6,7,8]
lst1.extend(['a','b','c','d','e','f'])
print(lst1)     # [1,2,3,4,5,6,7,8,'a','b','c','d','e','f']

# insert(idx,value)
lst1 = [1,2,3,4,5]
# idx:  0 1 2 3 4
lst1.insert(3,'a')  # [1,2,3,'a',4,5]
print(lst1)

# pop()
lst1 = [1,2,3,4,5]
a = lst1.pop()      # a = lst.pop()[=>5], a= 5
print(a)            # 5
print(lst1)         # [1,2,3,4]
b = lst1.pop(2)     # b = lst.pop(2)[=>3], b=3
print(b)            # 3
print(lst1)         # [1,2,4]

# remove(value) : value에 있는 내용을 검색 후 삭제
lst1 = [1,2,3,4,5,2,4,5,6,3,2,6]
lst1.remove(2)      # 첫번째 2삭제
print(lst1)
lst1.remove(2)      # 두번째 2삭제
print(lst1)
lst1.remove(2)      # 세번째 2삭제
print(lst1)
#lst1.remove(2)      # 네번째??? 
                    #ValueError: list.remove(x): x not in list

# clear()
lst1 = [1,2,3,4,5]
lst1.clear()
print(lst1)         # []



