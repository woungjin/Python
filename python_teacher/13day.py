'''
# 문제3] lst_sec =[['홍길동','남',36],['김수양','여',32],
#       ['박담수','남',28]]
#     위 2차 리스트 자료를 다음과 같은 형식으로 출력
#    
#     이름 : 홍길동
#     성별 : 남
#     나이 : 36 
lst_sec =[['홍길동','남',36],['김수양','여',32],['박담수','남',28]]
for i in range(len(lst_sec)):
    for j in range(1):
        print("이름 : {}".format(lst_sec[i][j]))
        j += 1
        print("성별 : {}".format(lst_sec[i][j]))
        j += 1
        print("나이 : {}".format(lst_sec[i][j]))
    print()

#or
for val in lst_sec:
    print("이름 : {}".format(val[0]))
    print("성별 : {}".format(val[1]))
    print("나이 : {}".format(val[2]))
    print()


# 문제4] 구구단을 출력하는 코드를 작성하되, 2차 리스트에 결과값을
#     저장하고 출력할 수 있도록 하시오. 
gugu = []
for x in range(2,10):       # [2,3,4,5,6,7,8,9]
    gugu.append([])         # gugu 빈 리스트를 멤버로 추가
    for y in range(1,10):   # [1,2,3,4,5,6,7,8,9]
        gugu[x-2].append(x*y)
print(gugu)
for x in range(2,10):
    for y in range(1,10):
        print("{} x {} = {:<3}".format(x,y,gugu[x-2][y-1]),end='')
    print()
            

#(실습)
#위에서 학습한 내용을 토대로 다음과 같은 내용을 프로그램하세요.
#  
#  아래와 같은 메뉴를 만들고, 친구 이름을 관리하는 코드를 작성
#  (리스트를 사용해서 작성하세요) 
 
 -------------------------
 1. 친구 리스트 출력          #등록한 친구 목록 보기
 2. 친구 추가                #친구 등록하기(정보는 문제3번 참조)            
 3. 친구 삭제                #등록 친구 삭제
 4. 이름 변경                #이름 변경
 0. 종료                     #프로그램 종료
 메뉴를 선택하세요 : 2
 이름을 입력하시오 : 홍길동
 -------------------------

import os       #  system() 호출하기 위해서

fr = []
idx = 0
while True:
    os.system('cls')
    print("-"*30)
    print(" 1. 친구 리스트 출력")
    print(" 2. 친구 추가")
    print(" 3. 친구 삭제")
    print(" 4. 이름 변경")
    print(" 0. 종료")
    print("-"*30)
    sel = input("메뉴를 선택하세요 : ")
    if sel == '1':          # 리스트 출력
        print(fr)
        os.system('pause')      # 일시정지
    elif sel == '2':        # 리스트에 멤버 추가
        name = input("이름을 입력하세요 : ")
        fr.append(name)
        os.system('pause')
    elif sel == '3':        # 리스트에 멤버 삭제
        name = input("삭제할 이름을 입력하세요 : ")
        if name in fr:
            fr.remove(name)
        else
            print("삭제할 친구가 없습니다.")
        os.system('pause')
    elif sel == '4':    # 이름 변경
        name = input("변경 대상 이름을 입력하세요: ")
        if name in fr:
            idx = fr.index(name)
        else:
            print('대상 이름이 없습니다')
            os.system('pause')
            continue
        mod_name = input("변경할 이름을 입력하세요 : ")
        fr[idx] = mod_name
        os.system('pause')    
    elif sel == '0':    #종료
        print("프로그램을 종료합니다....")
        break
    else:
        print("메뉴 선택 오류입니다.")
        print("입력값은 0 ~ 4번 중에 선택해주세요")
        os.system('pause')

# 튜플(tuple)
# : 리스트와 비슷한 자료형으로 튜플 안에 다양한 형태의 값을 사용가능
#  (형식)
#  튜플변수명 = (value1, value2, value3 ....)
# 
# 리스트와 튜플의 차이점
#  1. 리스트는 "[]"를 사용하지만, 튜플은 "()"를 사용한다. 
#  2. 리스트는 그 값을 생성, 삭제, 수정이 가능하지만,
#     튜플은 그 값을 바꿀 수 없음(중요)
#  3. 튜플은 멤버(요소)의 값이 1개인 경우 반드시 뒤에 ","를 붙여야 한다.
#     예] tu = (10,)
#  4. 튜플은 가장 외각에 있는 "()"는 생략이 가능함. 
#     예] tu1 = 10,20,30 , tu2 = 10, , tu3 = (10,20),(30,40) 

# 튜플의 인덱싱
#  : 튜플도 리스트와 같이 인덱싱을 통해서 값에 접근
# 
#  예]
#  양의 인덱싱(+)    0  1  2  3  4  5  6  7  8  9
#  음의 인덱싱(-)  -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
#      튜플       ( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# 튜플의 슬라이싱(slicing)
# : 튜플의 특정 범위의 값에 접근하기 위한 방법으로 리스트와 동일하게 사용

# 예제1) 튜플의 정의 및 사용
tu = (1,2,3,4,5)
print(tu,type(tu))
print(tu[0])            # 1
print(tu[1])            # 2
print(tu[-1])           # 5
print(tu[0:3])          # (1,2,3)
print(tu[3:])           # (4,5)

tu1 = '문자열',100,123.456
print(tu1,type(tu1))    # ('문자열',100,123.456) <class 'tuple'>
tu2 = (10)
print(tu2,type(tu2))    # 10 <class 'int'>
tu3 = (10,)
print(tu3,type(tu3))    # (10,) <class 'tuple'>
tu4 = 10,
print(tu4,type(tu4))    # (10,) <class 'tuple'>

# 예제2) 튜플의 특정 - 변경불가
tu = (1,2,3,4,5)
#tu[0] = 10              # TypeError : 튜플은 값을 변경할 수 없음

# 튜플의 결합1(병합)
a = 1,2,3
b = 4,5,6
c = a + b
print(c,type(c))        # (1,2,3,4,5,6) <class 'tuple'>

# 튜플의 결합(확장)
tu1 = 10,20,30
tu2 = 40,50,60
tu1 = tu1 + tu2
print(tu1,type(tu1))    # (10,20,30,40,50,60) <class 'tuple'>

# 튜플을 리스트로 변경
lst = list(tu1)
print(lst,type(lst))    # [10,20,30,40,50,60] <class 'list'>
# 리스트를 튜플로 변경
tu = tuple(lst)
print(tu,type(tu))      # (10, 20, 30, 40, 50, 60) <class 'tuple'>


# packing과 unpacking 
# : 튜플을 하나의 튜플로 묶어서 사용하는 것을 packing
#  반대로 묶여진 튜플을 나눠서 사용하는 것을 unpacking
#
#  예] (1,2) , (3,4)
#  packing => pack = ((1,2),(3,4))
#  unpacking => a, b = pack     # a, b = (1,2),(3,4)
#   a = (1,2) , b = (3,4)

print('packing')
tup1 = (1,2),(3,4)  #((1,2),(3,4))
print(tup1)
print(tup1[0]);print(tup1[1])

print('unpacking')
pack = 1,2,'패킹'    # packing
a,b,c = pack         # unpacking
print(a,b,c)

lst = [1,2,3]
a,b,c = lst
print(a,b,c)

# 튜플의 함수
# : 튜플의 경우 요소의 값을 변경할 수 없다. 때문에 변경관련된 함수X
#  -index(value) : 튜플의 값의 해당하는 멤버의 인덱스 값을 반환
#  -count(value) : 튜플에 있는 값의 개수를 반환

# 예제4)
tu = (100,200,'함수',100,'개수')
print(tu.index(200))
print(tu.count(100))


# [ Tuple 종합 문제 ]
1. 여러 개의 값을 튜플로 패킹시킨 후 저장되어 있는 값을 빼내어 리스트로 저장 
  출력 하시오. (5개 값 저장)
( Tuple의 값을 리스트에 저장하시오. 단, Len함수를 이용)
  1)튜플 생성 2)튜플 => 리스트에 저장 3) 리스트에 내용을 출력

tu = (100,'파이썬',3.14,'11_43',1101)
lst = []
for i in range(len(tu)):
    lst.append(tu[i])
print(lst)



2.아래와 같이 출력 시키시오
----------------------------------------------------
     (Tuple)          (List)
    회사정보     :   삼성전자
    제품명       :    Galaxy
    가격정보     :    100원
    출시일       :    미정
----------------------------------------------------
'''
tu = '회사정보','제품명','가격정보','출시일'
lst = ['삼성전자','Galaxy','100원','미정']
print("-"*40)
print("     (Tuple)\t\t(List)")
for i in range(len(tu)):
    print("    {:5}\t:\t{}".format(tu[i],lst[i]))
print("-"*40)
'''
3. 위에서 출력 한 내용을 업데이트 하시오. 
[ 단, Index, Insert, Remove 함수를 전부 사용할 것 ]
가 격 : 100 -> 110
출시일 : 미정 -> 이번 달 말

'''
tu = '회사정보','제품명','가격정보','출시일'
lst = ['삼성전자','Galaxy','100원','미정']
a = lst.index('100원')
b = lst.index('미정')
lst.remove('100원')
lst.remove('미정')
lst.insert(a,'110원')
lst.insert(b,'이번 달 말')
print("-"*40)
print("     (Tuple)\t\t(List)")
for i in range(len(tu)):
    print("    {:5}\t:\t{}".format(tu[i],lst[i]))
print("-"*40)