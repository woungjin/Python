



# 7, count(value) : 특정값의 개수를 출력                              # 리스트내의 특정멤버의 개수를 출력
# lst = [1,2,4,8,4,7,0,5,3,4]                                        # pop과는 다르게 리스트 내의 모든 숫자를 찾아냄
# su = lst.count(4)                                                  # 내가 찾고싶은 문자에대한 변수를 지정 pop과 비슷
# print(list)
# print("4의 값을 가진 멤버의 개수 : ", su)






# 8,  index(value) : 특정값의 인덱스 값을 반환 
# lst = [1,2,4,8,4,7,0,5,3,4]                                        # 특정 리스트 내의 멤버가 아닌 멤버의 위치를 찾아냄
# idx = lst.index(4)                                                 # 내가 찾고싶은 멤버를 넣으면 위치를 나타냄
# print("4의 값의 인덱스 위치 값은 ", idx)
# index()는 값이 존재하지 않은 경우 ValueError                     






# 9, reverse()                                                        # 함수의 순서 위치를 바꿈
# lst = [1,2,4,8,4,7,0,5,3,4]                     
# print("사용전 : ",lst)
# lst.reverse()                                                      # 역으로 순서를 바꿈 
# print("사용후: ",lst)







# 10, sort() : 리스트를 정렬하는 함수 (숫자뿐만 아니라 다른것도 가능)
#            오름차순(reverse=False) - 아무것도 표시하지 않으면 이게 기본 설정
#            내림차순(reverse=Tre)  - 내림차순할려면 True 써주어야함
# lst = [1,2,4,8,4,7,0,5,3,4]  
# lst.sort()                                                         # 아무것도 안적으면 오름차순
# print("lst를 오름차순 정렬 : ",lst)
# lst.sort(reverse=True)                                             # reverse()이것만 쓰면 그냥 역순이라면 sort를 포함해서 사용하면 정렬을 해줌 
# print("lst를 내림차순 정렬 : ",lst)

# sort() 사용시 주의사항
# 1, 숫자 형식 OR 문자 형식은 분리해야 정렬이 된다.                 # 정수와 실수는 숫자이기에 분리할필요X   =  (숫자=숫자),(문자=문자)
# lst1 = [3,2,1,4,5,6,7]
# lst2 = sorted(lst1)
# lst3 = sorted("I am a student".split())                           # split() = 문자열을 분리 I am a student라는 4개의 멤버를 가진 리스트를 만들어줌 (대소문자 구분해줌)
#           ['I','a','am','student'] 
# lst4 = sorted("I am a student".split(),key=str.lower)             # 정렬기준을 바꿈 (a ~ z 까지의 순서대로 정렬해줌, 대소문자 구분x)
#           ['a','am','I','student']
# lst1 = [3,2,1,4,5,6,7]
# lst2 = sorted(lst1)                                                 # sorted = 새롭게 정렬해서 변수에 만들어준다
# print(lst2)
# lst3 = sorted("I am a student".split())
# print(lst3) 
# lst4 = sorted("I am a student".split(),key=str.lower)
# print(lst4)
# lst6 = [1,5,2]
# lst7 = sorted(lst6)                                                 # 한번에 쉽게 정렬할수 있음
# print(lst7)


#  split()  :  문자열을 분리하는 함수
#     "()" 안에 아무것도 없으면 공백(Tab,엔터)를 기준으로 문자열을 나눠서 list로 저장 
#          만약 split(";")을 사용하면, ";"을 기준으로 문자열을 나누겠다는 의미가 됨 






# copy 기능     
# 1, shallow copy  : 변수는 새로운 공간에 값을 넣어주지만 이 shallow copy는 원본주소를 그대로 가져옴 하나이자 두개 두개이자 하나
# 2, deep copy     : 새로운 공간에 값을 만들어서 변수에 넣어줘서 별도의 공간에 복사해줌
# 예시 ) shallow copy                                                 # 복사햇는데 같음
# lst1 = [1,2,3,4,5]
# lst2 = lst1                                                         # shallow copy 가 일어남(파이썬 특징) , lst2에게 lst1이 가진 값의 주소를 복사해줌
# print("lst1의 값 : " , lst1, 'lst1의 주소 :',id(lst1))              # id() 함수 : 변수나 함수의 주소 값을 반환하는 함수 (해당 값의 주소를 나타냄)
# print("lst2의 값 : " , lst2, "lst2의 주소 :",id(lst2))              # 두개의 변수가 가리키는 주소의 값이 같다 = 실제값을 넘긴게 아닌 주소를 넘김(=shallow copy)
# lst1[1] = 'a' # [1,'a',3,4,5]                                       # 하나를 변경해주면
# print(lst1)                                                         # 값이 둘다 바뀜
# print(lst2)

# 예시 ) deep copy                                                    # 복사해서 별개로 둠
# lst1 = [1,2,3,4,5]
# lst2 = list(lst1)                                                     # 변수안에 list(변수)를 두면 별개의 복사본을 만듦
# lst1[1] = 'a'
# print("lst1의 값 : " , lst1, 'lst1의 주소 :',id(lst1))                # 주소 또한 다르게 나옴
# print("lst2의 값 : " , lst2, "lst2의 주소 :",id(lst2))   

# 해당 복사 기능을 사용하기 위한 모듈 : copy 
# import copy
# lst1 = [1,2,3,4,5]
# lst2 = copy.deepcopy(lst1)                                            # deep copy = 
# lst3 = lst1                                                           # shallow copy = 데이터의 주소를 복사
# print(lst1,lst2)
# print(id(lst1), "\t", id(lst2), "\t" , id(lst3))


# 문제 1  ) 리스트 초기값 [30,20,10] 설정 후
# print("문제1")
# list = [30,20,10]
# print("현재 리스트 \t\t\t : ",list)
# list.append(40)
# print("append로 추가한 값 \t\t : ",list)
# a = list.pop(3)
# print("pop 으로 출력한 값 \t\t : ",a)
# print("pop 후의 리스트  \t\t : " ,list)
# list.sort()
# print("sort 후의 리스트 = 오름차순\t :",list)
# list.reverse()
# print("reverse 후의 리스트 = 역순 \t :",list)

# print("\n문제 2 ")
# lst = [30,20,10]
# print("10 값의 위치 \t\t\t : ",list.index(10))
# list.insert(2,200)
# print("insert 후의 리스트 \t\t :",list)
# list.remove(200)
# print("remove 후의 값 \t\t\t :",list)
# list.extend([555,666,555])
# print("extend 후의 값 \t\t\t :",list)
# print("555 값의 개수 \t\t\t :" ,list.count(555))
# print(list






# 2차(원) 리스트
#  : 리스트 안에 멤버 중 리스트가 존재하는 경우 데이터 처리하는데 사용하는 방식(표형태)
#    리스트 안에  리스트 멤버에 대한 참조
#
# #  예제 )  2차 리스트 변수 값 참조 
# aa = [ [1,2,3,4],                                                                       # aa의 멤버의 개수는 3개 [1,2,3,4], [5,6,7,8] , [9,10,11,12] = 총 3개의 멤버를 가짐 
#        [5,6,7,8],
#        [9,10,11,12] ]
# print(aa)                                
# for x in range(3) :                                                                     # 리스트 aa의 멤버의 개수만큼 반복  [1,2,3,4], [5,6,7,8] , [9,10,11,12]
#     for y in range(4) :                                                                 # 리스트 aa의 멤버의 리스트 멤버의 개수만큼 반복  (1,2,3,4) = 4개 
#         print(aa[x][y],end='\t')                                                        # aa의 멤버의 리스트를 각각 출력하는 방법 ([x][y]의 값의 의미는 index의 값의 위치들이 0,123 1,123 2,123들어간다 )

# bb = [[0,1,2],[1,2,3]]
print(bb)
for a in range(2):
    for b in range(3):
        print(bb[a][b])

# 예제 2) 2차 리스트 생성 및 출력
# ls_1 = []; ls_2=[] ; value = 1                                                          # 만들어진걸 사용이 아니라 값을 넣어서 만든다
# for i in range(3):                                      
#     for y in range(4):  
#         ls_1.append(value)
#         value +=1   
#     ls_2.append(ls_1)                                                                   # i = 0일떄 ls_2 = [[1,2,3,4]]
#                                                                                         # i = 1일때 ls_2 = [[5,6,7,8]]
#     ls_1 = []                                                                           # ls_1의 멤버의 값을 정리 첫번째 반복이 될떄 1,2,3,4를 가지고 2번째 멤버에 들어가니 한번 반복이 끝날때 멤버를 비워주어야 한다
# print(ls_2)                                                                                
# for i in range(3):
#     for y in range(4):
#         print(ls_2[i][y])

# 문제 ) 
# a = [10,20,30,40,50,60,70]
# sum = 0
# for x in a :
#     sum += x
# print(sum)

# # print(b)
# #  문제 )2

# from random import random                                                                   
# a = []                                                                                       # 리스트에 넣을 빈칸 변수를 만들어준다
# c = 0                                                                                        # 6번 반복하면 끝나게끔 횟수를 지정  
# while True :
#     rand = int(random()*45+1)                                                               # 1~45까지의 랜덤 에서 뽑아냄
#     if rand != a :                                                                           # 만약 a리스트에 rand 숫자가 없다면 
#         a.append(rand)                                                                        # a리스트에 rand를 추가해라
#         c += 1                                                                               # c는 6번 되면 끝나게 지정해준다
#         if c == 6 :                                                                          # 6번 되면 break
#             break
# a.sort()
# print("1~45까지의 중복 없는 6개 : ", a)