# 딕셔너리 (dictionary - 사전 = 시퀸스자료) 
# 1, list의 비슷한 자료형. (리스트는 멤버에 접근할때 첨자(index)를 사용, 딕셔너리는 멤버에 접근할때는 첨자를' key를 사용함 )
# 2. 딕셔너리는 key가 가리키는 곳에 값(value-데이터가 존재)
# 3. 딕셔너리를 정의할 떄는 "{}"를 사용한다
# 4. 특정슬롯에 대헤 참조할 때는 key-value를 입력하거나, dictionary 안에 있는 요소를 참조할때에는 "[]" 사용한다 


# 형식 )
# 변수명 = {} # 비어있는 사전형 자료를 선언
# 변수명 = {key1:value1 , key2:value2, key3:value3}      - 기본요소 : 키와 값을 콜론을 이용하며 중괄호 사용 키와 value는 쌍으로 이루어져있음
# 
# dict()를 이용하여 선언하는 경우 ) 
# 변수명 = dict([(k1,v1),(k1,v1),(k1,v1)])              - 튜플형태로 묶어서 키와 값을 한번에 넘겨줌
# 
#  접근방식 )
# dic = {key:value}                                                                             # 변수명 = { 키 : val }
# dic[key] = value 
# print(dic[key])                                                                                  # 출력 결과 = value
# # a = dict([('b',1)])
# print(a['b'],type(a))

# 예제) 딕셔너리에 대한 정의 및 접근
# dic = {'a':1, 'b':2, 'c':3}                                                                         # a,b,c에 각 1,2,3의 값을 넣음
# print(dic['c'])                                                                                     # 리스트와 튜플같이 인덱스 값 앞에 변수명 즉 key를 넣어주면됨
# dic['c'] = 5 * dic['b']                                                                             # dic['c'] = 5*2 
# print(dic['c'])

# 예제) 딕셔너리에 for구문을 사용하는 경우
# for x in [1,2,3,4,5] :                                                                              # 리스트나 튜플은 값을 그대로 변수에 넣음
#     print(x)

# for k in dic:                                                                                       # key값들을 새로운 변수에 넣음
#     print(k)                                                                                        # key값이 출력
#     print(k,dic[k])                                                                                 # key와 value 값 출력


# 예제3 ) 딕셔너리와 리스트를 같이 사용하는 경우 , 딕셔너리 안에 리스트가 있는 경우
# dl = {'음료':['탄산','과일','우유','물'],
#         '식사':['김밥','라면','돈까스','비빔밥','볶음밥']}
# for key in dl  :                                                                                    # 음료와 식사라는 키값이 key에 들어감
#     print(dl[key])
#     for i in dl[key]:                                                                               # 딕셔너리 안에 있는 key안에있는 리스트의 값인 탄산, 과일 등등을 가져온다 
#         print(i,end=" ")
#     print()
#     for j in range(len(dl[key])):                                                                              # = range(len(dl[key])) = 길이값 4 같은얘기
#         print(dl[key][j],end=" ")
#     print()

# 예제4 ) 리스트안에 딕셔너리를 멤버로 가지고 있는경우
# id = [{'name':'길동','age':20,'blood':'b'}, 
#      {'name':'병원','age':24,'blood':'a'}]
# for dic in id :
#     print(dic['name'],dic['age'],dic['blood'])
#     print()
# for i in range(len(id)):
#     print(id[i]['name'],id[i]['age'],id[i]['blood'])


# 예제 5 )딕셔너리 안에 딕셔너리가 있는경우
# dic = {'길동':{'age':20,'blood':'b'}
#       ,'방원':{'age':24,'blood':'a'}}
# for name in dic:
#     print(name,dic[name]['age'],dic[name]['blood'])                                                     # name이라는 딕셔너리를 불러오고, 딕셔너리 안에있는 age값과 blood값을 각각 불러옴


# 딕셔너리에서 사용하는 함수
# -update(key[,value])  : 사전형 자료의 key값을 추가                                                     # key값을 빈값으로 만들어놓고 나중에 추가할수 있음
# -fromkeys(iter,[value]) : iter자리에 리스트,튜플의 값을 딕셔너리의 'key'로 집어넣어 사용하는 딕셔너리를 생성함  # ,[value] 값은 넣어도 되고 안넣어도 됨
# -get(key[,value])     : 사전형의 키를 사용하여 값을 얻어오는 함수 
# -keys()               : 사전형의 모든 키를 받아옴(반환)
# -values()             : 사전형의 모든 값을 받아옴(반환)
# -items()              : 사전형의 모든 "key : value"의 쌍을 튜플로 반환시킴                                # 튜플은 값을 변형할수 없는 특징을 이용함
# -pop(key)             : 사전형 key를 통해서 반환한 후에 삭제                                              # 리스트와 비슷하지만 딕셔너리는 삭제할 key값을 넣어주어야함
# -popitem()            : 사전형 자료에 마지막 "key : value" 쌍을 튜플로 반환 후 삭제
# -clear()              : 사전형의 모든 "key:value" 값을 삭제하여 빈 사전형 자료로 만듬 


# update()      : 딕셔너리에 추가하는 함수
# dic = {'a':1 , 'b':2, 'c':3}
# dic.update({'d':4})                                                                                     # 딕셔너리 안에 업데이트로 새로운 딕셔너리 즉 키와 값을 넣어주는형태
# print(dic['a'])
# print(dic['d'])
# print(dic)


# fromkeys(iter,[value])
# k = ['a','b','c','d']
# dic1 = {}.fromkeys(k)                                                                                       # 비어있는 딕셔너리형태에다가 키 값만 집어넣음  = {'a':none, 'b':none, 'c':none}
# dic2 = {}.fromkeys(k,1)                                                                                     # key값을 넣어주면 한번에 처리하게됨 = {'a':1 , 'b':1 , 'c':1}
# print(dic1)
# print(dic2)

# get(key,[value])                                                                                          # [,value] 값이 없으면 = none 이라고 값이 뜸  
# dic = {'a':1 , 'b':2 , 'c':3}                                                                               # 만약 없는 key 값을 가져올떄 value 값을 입력하면 value 값이 뜨게됨 
# value = dic.get('b')
# print(value)
# print(dic.get('d'))
# print(dic.get('d','not exist key'))                                                                         # value 값을 넣엇기에 아무것도 없다면 출력하게됨  = 'not exist key'를 출력하게됨 
# print(dic.get('c','not exist key'))                                                                         # c 는 값이 있기에 3 이 출력됨 키값의 우선권을 가지고 출력하고 만약에 없다면 지정한 value 값으로 넣게됨

# keys()                                                                                                #(키값을 변수에 저장)
# dic = {'a':1,'b':2,'c':3}
# for key in dic.keys():                                                                                      # 본래 키값을 변수에 저장하는형태인데 dic.keys라고 하면 key값인 a,b,c를 저장하게됨 
#     print(key,end=" ")
# print()
# print(dic.keys())



# keys()
dic = {'a':1 , 'b':2 , 'c':3 }
for key in dic.keys():
    print(key,end=' ')          # a b c
print()
print(dic.keys())               # dict_keys(['a', 'b', 'c'])

# # values()  
# dic = {'a':1 , 'b':2 , 'c':3}
# for values in dic.values():                                                                                 #  values 변수에 1,2,3인 value 값을 저장하게됨 
#     print(values,end= " ")
# print()
# print(dic.values())                                                                                         # dict_values([1,2,3])

# # items()                                                                                                    key = a , value =1 
# dic = {'a':1, 'b':2,'c':3}                                                                                  # (a,1),('b',2),('c',3)                   
# for key,value in dic.items():                                                                               # key에는 key 값이 들어가고  value 값에는 1,2,3 이 들어가는 언패킹이 일어남
#     print("%s:%s" %(key,value),end=" ")
# print()


# # pop(key)
# dic = {'a':1 ,'b':2 ,'c':3}                                                                             
# value = dic.pop('b')                                                                                        # pop() 값을 넣어주어야 함
# print(dic)                                                                                                  # = 2 
# print(value)

# # popitem()                                                                                                 # popitem은 맨 끝에있는 것만 빼내고 저장해서 사용하는거고 items는 모든값을 튜플로 빼내는 일을 함 
# dic = {'a':1, 'b':2, 'c':3 }
# tu1 = dic.popitem()
# print(dic)                                                                                                  # {'a':1, 'b':2}
# print(tu1)                                                                                                  # {'c':3}

# # clear()
# print(dic)
# dic.clear()
# print(dic)





# < 문제 >
# 1, 이름, 전화번호, 이메일 주소를 키로 사용하는 사전 자료를 생성하시오 
# 2, 리스트형 변수에 1번 문제와 같은 사전 자료가 여러개 생성될수 있게 하시오 (입력값을 받아서 자료를 생성) 딕셔너리 내부에 여러개의 딕셔너리가 생성되게끔 입력값을 받아서 자료를 내도록

# 3, 2번에서 입력한 자료가 출력될수 있도록 하시오 
#   이름 : 홍길동
#   전화번호 : 010-xxxx-xxxx
# #   이메일 : xxxx@xxx.com
                                                                          
# dic = {'이름':'홍길동','전화번호':'010-1234-5678',"이메일":'abcd@never.com'}                                    # 1번 딕셔너리 만드는법
# import os
# ld = []                                                                                                        # 리스트안에 딕셔너리를 만드는 방법을 사용
# while True :
#     dic2 = {}
#     dic2.update({'이름':input("이름을 입력하세요 : ")})                                                           # KEY 와 value 값 넣음 , input을 value 값 안에 넣을수있다
#     dic2.update({'전화번호':input("전화번호를 입력하세요 : ")})                                                     # update는 키와 값을 입력하는데 값의 부분에 input을 넣어 값을 넣게끔한다
#     dic2.update({'이메일':input("이메일을 입력하세요")})
#     ld.append(dic2)                                                                                                # 여러가지 입력값을 받은 dic2를 append를 통해 {}딕셔너리 자체를 통으로 리스트안에 넣음
#     if (input('계속 하시겠습니까?(y/n')) == 'n':                                                                      # n 이면 멈추어라
#         break
#     os.system('cls')                                                                                              # n이 아니면 깔끔하게 정리하고 반복재생
#     print(ld) 
# for d in ld:                                                                                                       # ld는 총 이름, 전화번호, 이메일 3번 반복하게됨
#     print('이름 : %s' %(dic2['이름']))                                                                             # dic2의 전화번호 value값을 불러옴
#     print('전화번호: %s' %(dic2['전화번호']))
#     print('이메일 : %s' %(dic2['이메일']))




# 1, 다음과 같은 메뉴와 가격긍ㄹ key와 value로 사용하여 
# 사전형 자료를 만들어 보자 변수명은 menu
# 칼국수 = 6000원 비빔밥 5500 돼지국밥 7000
# 돈까스 7000 김밥 2000 라면 2500
# 2, 1번에서 만든 자료 menu 변수에서 가격이 6000원 미만에 해당하는 메뉴와 가격을 출력하는 코드를 작성 
menu = {'칼국수':6000, '비빔밥':5500,'돼지국밥':7000,'돈까스':7000, '김밥':2000,'라면':2500}
b = 0
for k in menu:                                                                                                      # key 값이 들어감
    if menu[k] < 6000  :                                                                                            # menu 의 key 값의 value 값들이 6000 보다 작을때
        print("%s : %s 원" %(k,menu[k]))
add_menu = input("메뉴를 입력하세요: ")
add_value = int(input("가격을 입력하세요 : "))                                                                      # 가격은 int로 
if add_menu in menu:                                                                                               # 추가할 메뉴가 기존 메뉴에 있는지
    menu[add_menu] = add_value
else :
    menu.update({add_menu:add_value})                                                                              # 추가할 메뉴가 없다면 메뉴랑 값을 넣어라
print(menu)

sel = input("메뉴를 출력하시겠습니까? y/n : ")
if sel =='y' or se1 != 'n' :
    for key in menu :
        print(key,menu[key])
    print()


    # for values in dic.values():                                                                                 #  values 변수에 1,2,3인 value 값을 저장하게됨 
#     print(values,end= " ")