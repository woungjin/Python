'''
# count(value) : 특정값의 개수를 출력
lst = [1,2,4,8,4,7,0,5,3,4]
su = lst.count(6)
print(lst)
print("6의 값을 가진 멤버의 개수 : ",su)

# index(value) : 특정값의 인덱스 값을 반환
lst = [1,2,4,8,4,7,0,5,3,4]
idx = lst.index(6)
print("0의 값의 인덱스 위치 값은 : ",idx)
# index()는 값이 존재하지 않는 경우 ValueError

# reverse() 
lst = [1,2,4,8,4,7,0,5,3,4]
print("사용전:",lst)
lst.reverse()
print("사용후:",lst)

# sort() : 리스트를 정렬하는 함수
#        오름차순(reverse=False)-기본,내림차순(reverse=True) 
lst = [1,2,4,8,4,7,0,5,3,4]
lst.sort()
print("lst를 오름차순 정렬 : ",lst)
lst.sort(reverse=True)
print("lst를 내림차순 정렬 : ",lst)

# sort() 사용시 주의사항
# 1. 숫자 형식 또는 문자 형식은 분리해야 정렬이 된다. 
#    (숫자는 숫자끼리, 문자는 문자끼리 정렬해야 한다.)
# 2. 정수와 실수는 같은 숫자이기 때문에 정령이 가능
# 3. 정렬된 리스트를 새롭게 만들고 싶은 경우, (sorted())
#    lst1 = [1,2,4,8,4,7,0,5,3,4] 
#    lst2 = sorted(lst1)
#    lst3 = sorted("I am a student".split())
#       # ['I','a','am','student']
#    lst4 = sorted("I am a student".split(),key=str.lower)
#       # ['a','am','I','student'] 
lst1 = [1,2,4,8,4,7,0,5,3,4]
lst2 = sorted(lst1)
print(lst2)
lst3 = sorted("I am a student".split())
print(lst3)
lst4 = sorted("I am a student".split(),key=str.lower)
print(lst4)

# ** split() 문자열을 분리하는 함수
# : "()" 안에 아무것도 없으면, 공백(스페이스,탭,엔터 등)을 기준으로
#  문자열을 나눠서 저장(리스트). 만약 split(';')을 사용하면, ';'를 
#  기준으로 문자열을 나누겠다는 의미가 됨.  

# Copy 기능
#  - shallow copy : 서로 다른 변수가 같은 위치에 있는 
#                  데이터를 가리키는 경우
#  - deep copy : 두개의 변수가 별도의 공간을 가리키게 복사하는 경우 

# (예시) shallow copy
lst1 = [1,2,3,4,5]
lst2 = lst1         # lst2에게 lst1이 가리키는 값의 주소를 복사
print('lst1의 값: ',lst1,'lst1의 주소 : ',id(lst1))
# id()는 변수나 함수의 주소 값을 반환하는 함수
print('lst2의 값: ',lst2,'lst2의 주소 : ',id(lst2))
lst1[1]='a'     # [1,'a',3,4,5]
print(lst1)
print(lst2)

# (예시) deep copy
lst1 = [1,2,3,4,5]
lst2 = list(lst1)
lst1[1] = 'a'
print('lst1의 값: ',lst1,'lst1의 주소 : ',id(lst1))
print('lst2의 값: ',lst2,'lst2의 주소 : ',id(lst2))

# 해당 복사 기능을 사용하기 위한 모듈 : copy
import copy

lst1 = [1,2,3,4,5]
lst2 = copy.deepcopy(lst1)  # deepcopy 함수를 사용
lst3 = lst1                 # shallow copy => 데이터의 주소를 복사
print(lst1,lst2)
print(id(lst1),'\t',id(lst2),'\t',id(lst3))
lst2[0] = 10
print(lst1,lst2)


[ Quiz 1 ] : 리스트 초기값 [ 30, 20, 10 ] 설정 후 
아래와 같이 출력 되도록 코드를 작성하세요.
    현재 리스트 : [30, 20, 10]

append(40) 후의 리스트 : [30, 20, 10, 40]
pop() 으로 추출한 값 : 40
pop() 후의 리스트 : [30, 20, 10]
sort() 후의 리스트 : [10, 20, 30]
reverse() 후의 리스트 : [30, 20, 10]

lst1 = [30,20,10]
print("현재 리스트 : ",lst1)
lst1.append(40)
print("append(40) 후의 리스트 : ",lst1)
su = lst1.pop()
print("pop() 으로 추출한 값 : ",su)
print("pop() 후의 리스트 : ",lst1)
lst1.sort()
print("sort() 후 리스트 : ",lst1)
lst1.reverse()
print("reverse() 후 리스트 : ",lst1)

# [ Quiz 2 ] : 리스트 초기값 [ 30, 20, 10 ] 설정 후 
# 아래와 같이 출력 되도록 코드를 작성하세요.

현재 리스트 : [30, 20, 10]
10 값의 위치 : 2
insert(2,200) 후의 리스트 : [30, 20, 200, 10]
remove(200) 후의 리스트 : [30, 20, 10]
extend( [ 555 , 666 , 555 ] ) 후의 리스트 : [30, 20, 10, 555, 666, 555]
555 값의 개수 : 2  

lst2 = [30,20,10]
print("현재 리스트 : ",lst2)
idx = lst2.index(10)
print("10 값의 위치 : ",idx)
lst2.insert(2,200)
print("insert(2,200) 후의 리스트 : ",lst2)
lst2.remove(200)
print("remove(200) 후의 리스트 : ",lst2)
lst2.extend( [ 555 , 666 , 555 ] )
print("extend( [ 555 , 666 , 555 ] ) 후의 리스트 : ",lst2)
su = lst2.count(555)
print("555 값의 개수 : ",su)

# 2차(원) 리스트
# : 리스트 안에 멤버 중 리스트가 존재하는 경우 사용되는 방식
#   리스트 안에 리스트 멤버에 대한 참조 

#예제1. 2차 리스트 변수 값 참조
aa = [  [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12] ] 
    #aa의 멤버의 개수는 3개 : [1,2,3,4],[5,6,7,8],[9,10,11,12]
print(aa)
for x in range(3): # 리스트 aa의 멤버의 개수만큼 반복
    for y in range(4): #리스트 aa의 멤버의 리스트 멤버의 개수 반복
        print(aa[x][y],end='\t')
    print()

#예제2. 2차 리스트 생성 및 출력
ls_1 = []; ls_2=[]; value = 1
for i in range(3): 

    for y in range(4):
        ls_1.append(value)
        value +=1
    ls_2.append(ls_1)   #i = 0, ls_2 =[[1,2,3,4]]
                        #i = 1, ls_2 =[[1,2,3,4],[5,6,7,8]]
                        #i = 2, ls_2 =[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    ls_1 = []           # ls_1의 멤버의 값을 정리
print(ls_2)     # ls_2 =[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
for i in range(3):
    for y in range(4):
        print(ls_2[i][y],end='\t')
    print()
'''
# 문제1] numbers = [10,20,30,40,50,60,70]
# 위 리스트의 모든 값을 더한 결과를 출력하세요. (sum() 사용하지 말고..)
numbers = [10,20,30,40,50,60,70]
Sum = 0
for x in numbers:
    Sum += x
print(Sum)

# 문제2] 1 ~ 45 까지 임의의 중복 없이 6개 생성하여 출력 (리스트 사용)
from random import random
lotto = []
cnt = 0
while True:
    rand = int(random()*45)+1
    if rand not in lotto:
        lotto.append(rand)
        cnt += 1
        if cnt == 6:
            break
lotto.sort()
print("1 ~ 45까지 중복 없는 임의 값 6개 : ",lotto)



# 문제3] lst_sec =[['홍길동','남',36],['김수양','여',32],
#       ['박담수','남',28]]
#     위 2차 리스트 자료를 다음과 같은 형식으로 출력
#    
#     이름 : 홍길동
#     성별 : 남
#     나이 : 36 

lst_sec = [['홍길동','남',36],['김수양','여',32],['박담수','남','28']]
for y in range(3):
    for i in range(3):
        print("이름 : ",lst_sec[y][i])
        


# 문제4] 구구단을 출력하는 코드를 작성하되, 2차 리스트에 결과값을
#     저장하고 출력할 수 있도록 하시오.  