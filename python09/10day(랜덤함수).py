#               ※ 랜덤 함수 - 컴퓨터는 완전한 랜덤은없고 입력한 값의 확률적인 값을 계산함
# : 임의의 값을 출력하는 함수 , 이 떄 생성되는 값을 " 난수 " 라고한다

# 랜덤함수를 사용하기 위한 모듈
# : random 모듈

# 모듈 사용 방법 : import [모듈/패키지]
# 1) import random                  - 랜덤 모듈을 로딩.즉 불러옴
#   or
# 2) from random(모듈) import random(함수)      - random 모듈에 있는 random 함수를 불러온다
#  

# from random import random                       # from random 여기 모듈로 부터 import random 함수를 불러오겠다 

# print(random())                                 # 시간값을 통해 랜덤하게 출력된다 0.0 ~ 1.0 미만의 값을 출력 하는데 실수(float)로 출력 함 
# print(random()*10)                              # 0.0 ~ 10.0 미만의 값을 출력 - 10 은 절대 안나옴 이유 : "랜덤함수는 %값을 이용하기에 몫이 0~9밖에 안나옴"


# # 0 ~ 10 미만의 값 정수를 출력할때
# print(int(random()*10))

# # 1 ~ 10 까지의 값을 출력
# print(int(random()*10+1))                       # %연산값에 +1 해주면 0은 안나오고 10나온다

# 예제 ) 1 ~ 45 까지의 임의의 값 6개 출력
# from random import random
# for x in range(6):
#     print(int(random()*45)+1)


# 문제 1 ] 1 ~ 100 까지 랜덤 값 6개를 출력 하는 코드 작성
# from random import random
# for a in range(6):
#     print(int(random()*100)+1)

# 문제 2 ) 1 ~ 100 까지 랜덤 값을 반복하여 출력하되, 출력 값이 50이 출력 되는 순간 반복을 종료하는 코드를 작성
# from random import random 
# while True :
#     su = int(random()*100+1)                       # 내가한건 su ==print(int(random()*100)+1) 이걸 프린트랑은 다르게 넣어서 출ㄹ력에 넣는다
#     print(su,end=" ")
#     if su == 50 :
#         break

# # # 문제3) 1 ~15 까지 랜덤 값을 중복 없이 3개 생성하여 출력하는 코드 작성
# from random import random
# num1 , num2 , num3 = 0,0,0
# while True :
#     su = int(random()*15+1)                 # ??궁금 random()이 함수안에 값을 변수라던가 넣을수는 없는건가 무조건 %값으로 0~9가 출력되는건가? 다른 randint나 randrange는 괄호에 값을 넣는데;;
#     if num1 != su:
#         num1 = su
#         break
# while True :
#     su = int(random()*15+1)
#     if num1 != su and num2 != su:                # != 같지 않다면     중복없이니까 앞에나온 num1 의 값이 중복이 안되게끔 해주어야 함
#          num2 =su 
#          break
# while True:
#     su = int(random()*15+1)
#     if num1 != su and num2 != su and num3 != su:
#         num3 = su 
#         break
# print("%s %s %s" %(num1,num2,num3))

# random 모듈내에 있는 다른 형태의 random함수들
# - randit() : 임의 의 값을 int값으로 출력하는 함수  = random()*10+1 이랑 같다
# 사용 방법 )
# randint(a,b)                                      # 두개의 값을 받는데 시작값과 종료값을 받는다    자신을포함한 b의 값까지 나오게 됨 +1 필요없음
# 예제) 1 ~6 까지의 임의의 값을 출력하는 코드
# from random import randint 
# print(randint(1,6))

# 예제 2) 1 ~ 6 . 100 ~ 200 사이의 임의 값 출력
# from random import random,randint
# print(randint(1,6))                                 # 1~ 6
# print(randint(100,200))                             # 100~ 200

# - randrange() : 범위 내의 임의값을 출력
# 예시 1) 
# randrange(5,10)  -> 5 ~10 "미만"의 값을 출력 , int값으로 나옴             # range는 미만의 값을 출력 
# 예시 2)
# randrange(5,10,2) -> 5,7,9 중에 하나가 랜덤하게 출력됨
# from random import random,randint,randrange
# for a in range(6):
#     print(randrange(1,45))
# print(randrange(10))

# random 모듈 내에 choice()
#  : 이 함수의 특징은 리스트와 같은 형태의 자료 중 일부를 랜덤하게 추출  (리스트 = 정수든 실수든 집합안에서 임의값을 출력하는 choice())
# 
# 예시 )
# dice = [1,2,3,4,5]
# # choice(dice)                      # dice 멤버중 랜덤하게 출력
# import random 
# dice = [1,2,3,4,5]
# x = random.choice(dice)
# print(x)

# # or                                        # 위의 import random은 import의 랜덤의 모든 함수를 불러오는데 from random import choice 를 사용하면 사용의 크기가 달라 좁은 범위에서 사용이가능하다
# from random import choice               # import 모듈 내에 choice()만 호출 한다
# dice = [1,2,3,4,5]                      # 최적화라는게 이렇게 작은범위를 사용하는건가?? 궁금
# x = choice(dice)
# print(x)

# 문제 4) 1~ 99 까지 랜덤 값중에 짝수면 True, 홀수면 False 출력하는 
# 프로그램 코딩 
from random import random,randrange
for a in range(1):                
    su = (randrange(1,100)) 
    print(su)                    # 주의 - range는 마지막값의 미만을 출력함 
    if su%2 ==0 :
        print("True")
    else :
        print("False")


