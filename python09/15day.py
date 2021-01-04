# 파이썬의 문자열
#  : 파이썬에서 사용되어지는 무자열 처리




# 특징
# 1) 인덱싱을 이용한 참조
# st = 'python string'
# #     0123456789.(index값)
# print(st[5])                                                            # n 
# print(st[3])                                                            # h
# # 2) 슬라이싱을 이용한 참조
# print(st[0:6])                                                          # python
# print(st[7:])                                                           # string
# # 3) 문자열의 반복문 (for)
# st = 'python for'
# for s in st:                                                            # 문자열의 하나씩 집어넣음
#     print(s,end=" ")
# print()






# 문자열함수
# find(str)
# - .find(str)    : 문자열에서 특정 문자열을 찾아 해당 문자의 index값을 반환 
# -count(str)   : 문자열에서 특정 문자열을 찾아 해당 문자의 개수를 반환
# -lower()      : 문자열에서 영문자를 소문자로 변경하여 변환
# -upper()      : 문자열에서 영문자를 대문자로 변경하여 변환
# -strip()      : 문자열에서 양쪽 공백 or 문자를 제거 
# -lstrip()     : 문자열에서 왼쪽 공백 or 문자를 제거
# -rstrip()     : 문자열에서 오른쪽 공백 or 문자를 제거
# -replace(old,new) : 문자열에서 왼쪽(old) 문자열을 찾아 , 오른쪽(new)문자열로 변경, 많이사용함
# -split(str)   : 문자열을 특정 문자를 기준으로 분리해서 저장함(list에 저장)








#    find(str) 
# st = 'python string'
# print(st.find('string'))                                                # 7
# # find(str.시작인덱스,끝인덱스)                                          #
# print(st.find('t'))                                                     # 2 (첫번째 것만 찾음)
# print(st.find('t'))                                                     # 한번더 해도 첫번째 것만 찾음
# print(st.find('t',2+1))                                                 # 2+1 = 자리수 3번째 뒤에부터 다시 찾아라
# # find()가 값을 찾지 못할 경우 : -1 
# print(st.find('a'))                                                     # 찾지 못하면 -1 뜸





# #   count(str)
# print(st.count('t'))                                                    # 천제 st의 문자배열중 't'의 개수를 찾아냄 : 2 
# # count(str,시작인덱스,끝인덱스 )
# print(st.count('t',5))                                                  # 5번째 위치부터 시작해서 't'를 찾고싶을때 







# # lower() 대문자 -> 소문자
# st = 'Python String'    
# print(st.lower())                                                       # 전체문장중 대문자를 소문자로 바꾸어줌 P -> p  , S -> s   (st자체에 문자배열을 바꾸어주진 못함, 출력만)
# st = st.lower()                                                         # 문자열 자체를 바꾸기 위해선 다시한번 변수에 지정을 해주어야 함 

# # upper() 소문자 -> 대문자
# st = 'pyton string' 
# st = st.upper()                                                         # st 자체에 함수를 적용해줘서 따로 변수에 저장해주어야 문자열 자체가 바뀜 
# print(st)                                                               # PYTHON STRING









# strip() : 인자값이 없는경우 공백제거 , 인자값으로 받은 문자가 있다면 해당문자를 양쪽에서 제거함
# st = '    python string    '
# print('[{}]'.format(st))      
# st = st.strip()                                                           # 공백제거 저장
# print('[{}]'.format(st))                                                  # 양쪽 공백제거 

# lstrip() : 
# st = '    python string    '
# print('[{}]'.format(st))
# st = st.lstrip()                                                          # 공백제거 저장
# print('[{}]'.format(st))                                                  # 왼쪽 공백제거 

# rstrip() : 
# st = '    python string    '
# print('[{}]'.format(st))
# st = st.rstrip()                                                          # 오른쪽 공백 제거 저장
# print("[{}]]".format(st))    










# replace(old,new)
# st = 'python string'
# st1 = st.replace('string','문자열')
# print(st1)                                                                # 파이썬의 문자열 (stirng - > 문자열)







# # split(str)    : 문자열을 'str'에 있는 문자를 기준 분리 (분리후 리스트에 저장)
# st ='python string'
# st1 =st.split()
# print(st1)                                                                # ['python','string']

# ##중요## : split(을 이용한 입력 문자 값 분리)
# values =  input("입력 : ").split(' ')                                        # 입력문자 str을 입력받아 split 기분으로 잘라내겟다  (입력값 =-> i am a student)
# print(values,type(values))
# a,b,c,d = values                                                             # unpacking
# print(a,b,c)










# 예제1 문자열 연산 처리(결합 및 반복)
# A = 'Have a'
# B = ' nice Day!'
# C = A + B
# print(C)
# print(B*3)  
# A += B
# print(A)


# # 예제 2) 문자열의 연산처리 ()
# str1 = 'Python is Easy. Programing 참 쉽죠?... 아...난가???!!!'
# print(str1)
# print(str1.lower())                                                             #영문자의 대문자만 소문자로 바뀌는게 확인됨
# print(str1.upper())                                                             # 한글은 적용 X
# # swapcase() : 영문 대문자를 소문자로 , 소문자 -> 대문자 
# print(str1.swapcase())                                                          # 소문자 대문자 다 바꿈 
# #title() : 영문 단어에 시작을 대문자로 변경해줌
# str2 = str1.lower()                                                             # 전부다 소문자로 만듬
# print(str2) 
# print(str2.title())                                                             # 문자열 맨앞 부분을 다 대문자로 바꿈



#   문제1 아래의 문장 주어진 조건에 맞게 변경
# "NevEr-eVer 100gIVe Up"                       # 변경전
# "Never-Ever 100Give Up"                       # 변경후

# a = "NevEr-eVer 100gIVe Up" 
# print(a)
# b = a.title()
# print(b)

# # Have a nice day 문자열 에서 다음 알아오기 
# # 'a', 'day', 'dar' 의 갯수 알아오기

# a = "Have a nice day"                               
# b = print(a.count('a'))             
# c = print(a.count('day'))
# d = print(a.count('dak'))                                                   # count는 못찾으면 0개수를 반영함



# # 문제 2 ."IT is a fun python class" 문자열이 길이.
# # 문자 'a'이 개수 's'의 개수를 출력하는 코딩 (count 사용하지 않고)

# a = "IT is a fun python class"
# # print(len(a))
# # print(a.count('a'))
# # print(a.count('s'))

# a = "IT is a fun python class"                                                      # for 구문사용  
# cnt = cnt_a = cnt_s = 0
# for i in a:                                                                         # a의 문자하나하나 반복할떄
#     cnt +=1                                                                         # cnt = 길이 = 개수를 늘린다 
#     if i =='a':                                                                     # i가 a의 반복이 될때 cnt_a 의 개수 즉 a의 개수를 늘리고
#         cnt_a +=1 
#     elif i =='s':                                                                   # s위랑 똑같이 s부문이 반복될떄 cnt_s의 개수를 늘린다 
#         cnt_s +=1
# print("문자열의 길이 : " , cnt)
# print("문장 'a'의 개수 : ", cnt_a)
# print("문장 's'의 개수 : ", cnt_s)


# # 문제3 . "Have a nice day" 문자열을 가지고 다음을 처리
# # - 각각 find와 index를 사용하여 "day" 문자의 위치를 찾으세요
# # - 각각 find와 index를 사용하여 "rrr" 문자의 위치를 찾으세요
# a = "Have a nice day"
# print("find(day) : ",a.find('day'))
# print("index(day) :",a.index('day'))
# print("find(rrr) : ",a.find('rrr'))
# # print("index(rrr) :",a.index('rrr'))                                                # substring not found 에러뜸 (문자열할떄는 find를 쓰는이유가 에러뜨면 아무것도 찾지 못하기에...)
# idx = a.find('a')
# print("첫번째 a의 위치 : ",idx)
# idx = a.find('a',idx+1)                                                               # idx+1 = 두번째 a의 위치 = 즉  index위치값 +1 해주면 그다음 부터 찾음
# print("두번째 a의 위치", idx)
# idx = a.find('a',idx+1)                                                               # idx+1 = 두번째 a의 위치 = 즉  index위치값 +1 해주면 그다음 부터 찾음
# print("두번째 a의 위치", idx)
# idx = a.find('a',idx+1)                                                               # idx+1 = 두번째 a의 위치 = 즉  index위치값 +1 해주면 그다음 부터 찾음
# print("두번째 a의 위치", idx)




# 문제 ( : 리스트를 정의 하여 첨자 위치를 저장하고 )
# a의 총 개수와 첨자의 위치를 출력 하시오 
# st = "Have a nice day Have a nice day have a nice day"
# 결과 
# a 의 개수 : 9
# 첨자 : [1, 5, 13 , 17 ,21 ,29 , 33 ,37 ,45]
# st = "Have a nice day Have a nice day have a nice day"
# idx = 0
# cnt_a = 0
# list = []                                                               # 인덱스 값이 나올 장소
# while True :
#     idx = st.find('a',idx)                                              # 찾을 a의 개수가 idx가 0 번째 시작할때
#     if idx != -1:                                                       # -1이 아니라면 리스트에 idx즉 자리수를 저장해라 
#         list.append(idx)
#         idx += 1
#         cnt_a +=1 
#     else :                                                              # -1이라면 중지
#         break
# print("a의 개수 ",cnt_a)                                                # cnt_a = count('a')
# print("첨자 : ",list)
        



        # strip ()

# st1 = "파이썬파"
# print(st1.strip("파"))                                  # 이썬
# print(st1.lstrip('파'))                                 # 이썬파
# print(st1.rstrip('파'))                                 # 파이썬


# st2 = "---파이썬---"
# print(st2.strip('-'))                                   # 파이썬
# print(st2.lstrip('-'))                                  # 파이썬---
# print(st2.rstrip('-'))                                  # ---파이썬

        # replace(old,new) 
# st = "2019-12-20"
# #     0123456789
# print(st)
# print(st.replace('2019','2020'))                        # 저장하지않고 그대로 
# print(st[0:4])
# print(st.replace(st[0:4],'2022'))                       # old 값을 슬라이스로 해서 처리할수있다 




#         # split(str)    : 특정문자를 기준으로 문자를 나눔
# st = "Never Ever Give Up"
# a =st.split()                                           # 띄어쓰기 공백 다 포함 여기서는 아무것도 없으면 () 띄어쓰기 기준으로됨
# print(st)
# print(a,type(a))

# st2 = "하나:둘:셋"                                      # 이것들을 각각 나누고 싶을때
# st3 = "1,2,3"   
# b = st2.split(':')                                      # :콜론을 기준으로 나눔
# c = st3.split(',')                                      # , 를 기준으로 나눔
# print(b)
# print(c)


# st4 ="하나둘셋넷"
# d = st4.split()                                         # 뭉쳐있는건 나눌수 없음 하나의 문자로 됨
# print(d,type(d))                                        # 스플릿은 분할후 무조건 리스트에 저장

# # splitlines() : 계행('\n')을 기준으로 문자열을 나눈 함수 (이전까지는 한줄 문자 여기는 여러줄 문자)
# st = """Never Ever Give Up
# Never Ever Give Up
# Never Ever Give Up
# Never Ever Give Up
# never Ever Give up
# """                                                     # """ ~ """  : 여러줄 주석할때 사용하지만 문자열을 여러줄로 표기할떄도 사용 
# print(st)
# a = st.split()                                          # 각각 띄어쓰기마다 저장하게됨 never, ever , , , ,
# print(a,type(a))

# b = st.splitlines()                                          # 각 \n 줄마다 문자로 나눔 never ever give up,
# print(b,type(b))



# join() : 지정한 "문자열"을 기준으로 문자열을 결합   리스트 아님x
# st = '123'
# print(st.join('%%'))                # %%를 st의 123에 합치는 작업을 함
# print('%'.join(st))                 #  1%2%3

# lst1 = ["","123","456"]
# print(lst1)
# print("".join(lst1))                # 공백을 기준으로 공백을 결합시킴 123456 -> """"123"456  출력결과는 리스트가 아니라 문자열 로 출력됨

# lst2 = ["","안녕","반가워","또만나!"]
# print("\n".join(lst2))

# lst3 = input("입력 : ").split()     # I am a student split은 분리    join결합
# print("join전 : " ,lst3)
# print("join한 결과 : "," ".join(lst3))

# 문제 1 (input()) 함수로 이름과 나이 값을 입력 받을때 한번에 입력받아 처리하고 출력하는 결과           # 강사님꺼 확인하기(중요) 언패킹을 사용

name,age = 



# 문제 2 input() 함수로 입력 받은 수의 더하기 빼기 곱하기 나누기의 간닪나 수식을 처리할 수 있도록 코드를 작성하시오 
        # ex ) 5+5 입력시에 결과를 출력 = 10                    # 입력값을 받을떄 문자열이 되니 int로 형변환해주어야함 
                                                #  5+5라는 예시를 보여주고 if elif로 +,-,*,/기가 있으면 더할땐 언패킹한 값을 더해서 나오게
                                                # 뺄셈일땐 언패킹한 값을 빼주는데 처음 input 에서 문자로 받으니 변수는 int로 묶어서 처리해주어야함