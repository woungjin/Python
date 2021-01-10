'''
# 딕셔너리(Dictionary - 사전)
#  1. List와 비슷한 자료형. List는 멤버(요소)에 접근할 때에 첨자(index)를
#   사용. 하지만, 딕셔너리는 멤버(요소)에 접근할 때에 첨자를 "key"를 사용
#  2. 딕셔너리는 key가 가리키는 곳에 값(value-데이타)가 존재
#  3. 딕셔너리를 정의할 때는 "{}"를 사용한다. 
#  5. 특정 슬롯을 대해 참조할 때는 key-value를 입력하거나, Dictionary안에
#    있는 요소를 참조할 때에는 "[]"를 사용한다. 
# 
#  (형식)
#  변수명 = {}  # 비어 있는 사전형 자료를 선언
#  변수명 = {key1:value1 , key2:value2, key3:value3, ... } 
# 
#  dict()를 이용하여 선언하는 경우
#  변수명 = dict([(k1,v1),(k2,v2),(k3,v3), ....])
# 
#  (접근방식)
#  dic = { key: value}
#  dic[key] = value
#  print(dic[key])      출력결과 : "value" 

# 예제1] 딕셔너리에 대한 정의 및 접근
dic = {'a':1, 'b':2, 'c':3}
print(dic['c'])     # 3
dic['c'] = 5 * dic['b']   # dic['c'] = 5 * 2
print(dic['c'])     # 10

# 예제2] 딕셔너리에 for문을 사용하는 경우 
for k in dic:       # key를 변수에 대입.....
    print(k)        # key값이 출력
    print(k,dic[k]) # key와 value 값이 같이 출력

# 예제3] 딕셔너리와 리스트를 같이 사용하는 경우 
dl = {'음료':['탄산','과일','우유','물'],
      '식사':['김밥','라면','돈까스','비빕밥','복음밥']}
for key in dl:
    print(dl[key])
    for i in dl[key]:
        print(i,end=' ')
    print()
    for j in range(len(dl[key])):   #dl[key] 멤버를 가리킴
        print(dl[key][j],end=' ')
    print()

# 예제4] 리스트 안에 딕셔너리가 있는 경우 
ld = [{'name':'길동','age':20,'blood':'b'},
      {'name':'방원','age':24,'blood':'a'}]
for dic in ld:
    print(dic['name'],dic['age'],dic['blood'])
print()
for i in range(len(ld)):
    print(ld[i]['name'],ld[i]['age'],ld[i]['blood'])    
print()

# 예제5] 딕셔너리 안에 딕셔너리가 있는 경우 
dd = {'길동':{'age':20,'blood':'b'},
      '방원':{'age':24,'blood':'a'}}
for name in dd:
    print(name,dd[name]['age'],dd[name]['blood'])

# 딕셔너리에서 사용하는 함수
#  -update(key[,value]) : 사전형 자료에 값을 추가(key)
#  -fromkeys(iter,value) : iter에 리스트,튜플의 값을 딕셔너리의 'key'로
#                        사용하는 딕셔너리를 생성하여 반환
#  -get(key[,value]) : 사전형의 키를 사용하여 값을 얻어오는 함수
#  -keys() : 사전형의 모든 키를 받아옴(반환)
#  -values() : 사전형의 모든 값을 받아옴(반환)
#  -items() : 사전형의 모든 "키(key):값(value)"의 쌍을 튜플(**)로 반환
#  -pop(key) : 사전형 키를 통해서 값을 반환한 후에 삭제
#  -popitem() : 사전형 자료의 마지막 "key:value" 쌍을 튜플(**)로 
#             반환 후 삭제 
#  -clear() : 사전형의 모든 "key:value"을 삭제하여 빈 사전형 자료로 만듬


# update() - 딕셔너리에 추가하는 함수 
dic = {'a':1 , 'b':2 , 'c':3 }
dic.update({'d':4})             # {'d':4}를 추가
print(dic['a'])                 # 1
print(dic['d'])                 # 4
print(dic)                      # {'a':1 , 'b':2 , 'c':3 , 'd':4 }

# fromkeys(iter[,value])
k = ['a','b','c','d']
dic1 = {}.fromkeys(k)           # {'a':none , 'b':none , 'c':none , 'd': none}
dic2 = {}.fromkeys(k,1)         # {'a':1 , 'b':1 , 'c':1 , 'd':1}
print(dic1)
print(dic2)

# get(key[,vlaue])
dic = {'a':1 , 'b':2 , 'c':3 }
value = dic.get('b')                # value = 2
print(value)                        # 2
print(dic.get('d'))                 # none
print(dic.get('d','Not exist key')) # Not exist key
print(dic.get('c','Not exist key')) # 3

# keys()
dic = {'a':1 , 'b':2 , 'c':3 }
for key in dic.keys():
    print(key,end=' ')          # a b c
print()
print(dic.keys())               # dict_keys(['a', 'b', 'c'])

# values()
dic = {'a':1 , 'b':2 , 'c':3 }
for values in dic.values():
    print(values,end=' ')       # 1 2 3
print()
print(dic.values())             # dict_values([1, 2, 3])

# items()
dic = {'a':1 , 'b':2 , 'c':3 }
for key,value in dic.items():  #unpacking
    print("{}:{}".format(key,value),end='\t')   # a:1   b:2   c:3
print()
print(dic.items())

# pop(key)
dic = {'a':1 , 'b':2 , 'c':3 }
value = dic.pop('b')                # value = 2
print(dic)                      # {'a':1 , 'c':3 }
print(value)                    # 2

# popitem() # 인자값이 없음. => 딕셔너리의 마지막 값을 반환(튜플로... )
dic = {'a':1 , 'b':2 , 'c':3 }
tu1 = dic.popitem()
print(dic)                      # {'a':1 , 'b':2 }
print(tu1)                      # ('c',3)

# clear()
print(dic)                      # {'a':1 , 'b':2 }
dic.clear()
print(dic)                      # {}


<<문제>>
1. 이름, 전화번호, 이메일 주소를 키로 사용하는 사전 자료를 생성하시오

dic = {'이름':'홍길동','전화번호':'010-1234-5678','이메일':'hong@gildong.com'}

2. 리스트형 변수에 1번 문제와 같은 사전 자료가 여러개 생성될 수 있게
  하시오.(입력값을 받아서 자료를 생성)

import os
ld = []
while True:
    dic2 = {}
    dic2.update({'이름':input("이름을 입력하세요 : ")})
    dic2.update({'전화번호':input("전화번호 입력하세요 : ")})
    dic2.update({'이메일':input("이메일을 입력하세요 : ")})
    ld.append(dic2)
    if (input('계속하시겠습니까?(y/n):'))=='n':
        break
    os.system('cls')
    #print(ld)

3. 2번에서 입력한 자료가 출력될 수 있도록 하시오. 
   (출력예시)
   이름 : 홍길동
   전화번호 : 010-xxxx-xxxx
   이메일 : xxxx@xxx.com


for dic in ld:
    print('이름 : {}'.format(dic['이름']))
    print('전화번호 : {}'.format(dic['전화번호']))
    print('이메일 : {}'.format(dic['이메일']))
    print()

'''
# <<아래의 내용을 토대로 프로그램을 작성해보세요.>>
# 1. 다음과 같은 메뉴와 가격을 key와 value로 사용하여
# 사전형 자료를 만들어보세요(변수명은 menu)
#  칼국수(6000원), 비빕밥(5500원), 돼지국밥(7000원),
#  돈까스(7000원), 깁밥(2000원), 라면(2500원) 
menu = {'칼국수':6000,'비빕밥':5500,'돼지국밥':7000,
'돈까스':7000,'김밥':2000,'라면':2500}
# 2. 위에서 만든 사전형 자료 menu 변수에서 가격이 6000원 미만에
# 해당하는 메뉴와 가격을 출력하는 코드를 작성하세요. 
for key in menu:
    if menu[key] < 6000:
        print("{} : {}원".format(key,menu[key]))
# 3. 사용자 입력으로 메뉴와 가격을 입력 받아  menu 변수에 자료를
# 추가 할 수 있도록 하시오.(동일한 메뉴는 가격만 변경)
add_menu = input("메뉴를 입력하세요 : ")
add_value = int(input("가격을 입력하세요 : "))
if add_menu in menu:
    menu[add_menu] = add_value
else:
    menu.update({add_menu:add_value})
#print(menu)

# 4. 메뉴를 자동으로 선택하여 출력하게 만들어 보세요. 
sel = input("메뉴를 출력하겠습니까?(y(기본)/n) :")
if sel == 'y' or sel != 'n':
    for key in menu:
        print(key,menu[key])
    print()

