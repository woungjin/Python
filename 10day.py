'''
# 문제6] 다음과 같은 모형으로 출력되게 하세요. 
# (단, 파이썬 서식을 사용안함. )
6-1         6-2         6-3         6-4
*           *****           *       *****
**          ****           **        ****
***         ***           ***         ***
****        **           ****          **
*****       *           *****           *

# 6-1
for i in range(5): #[0,1,2,3,4]
    for j in range(0,i+1,1):#[0],[0,1],[0,1,2],[0,1,2,3],[0,1,2,3,4]
        print("*",end='')
    print()
print('\n')
# 6-2
for i in range(5): #[0,1,2,3,4]
    for j in range(0,5-i,1):#[0,1,2,3,4],[0,1,2,3],[0,1,2],[0,1],[0]
        print("*",end='')
    print()
print('\n')
# 6-3
for i in range(5):
    j = 3
    while j >= i:   
        print(end=' ')  #print(" ",end='')
        j -= 1
    j=0
    while j <= i:
        print("*",end='')
        j += 1
    print()
print('\n')

# 6-4
for i in range(5):
    j = 0
    while j < i:   
        print(end=' ')  #print(" ",end='')
        j += 1
    j = 4
    while j >= i:
        print("*",end='')
        j -= 1
    print()
print('\n')


6-5 출력 줄수를 입력하면 다음과 같이 출력 입력 줄은 홀수이여야만 함. 

홀수 줄수를 입력: 7
   *
  ***
 *****
*******
 *****
  ***
   *


import os  # system() => 시스템 CMD명령어를 사용할 수 있음.
           # system('cls') => 터미널 창의 내용을 정리(clear)
           # system('pause') => 일시 정지 
# sp(여백), st(별개수),ln(줄수),flag(조건반전을 위한)
i,j = 0,0; num = 1
while num:
    os.system('cls') 
    ln = int(input('홀수 줄수를 입력 : '))
    sp = ln//2; st = 1 ; flag = True
    for i in range(ln):
        for j in range(sp): print(end=' ')      # 공백출력
        for j in range(st): print('*',end='')   # 별 출력
        print()
        if i == (ln//2): flag=False
        if flag : sp -= 1; st += 2
        else : sp += 1; st -= 2 
    num = int(input("0.종료 1.계속 >>> "))
print("프로그램 종료")

# 램덤 함수
#  : 임의의 값을 출력하는 함수. 이 때 생성되는 값을 "난수"라고 한다.
# 
# 램덤함수를 사용하기 위한 모듈
#  : random 모듈
# 
# 모듈 사용방법 : import [모듈/패키지]
# 1) import random             # random 모듈을 로딩(불러옴)
#   or
# 2) from random import random # random 모듈에 있는 random함수를 불러움
#   

from random import random   # from random => 랜덤 모듈에서 
                            # import random => random함수를 호출
print(random())             # 0.0 ~ 1.0 미만의 값을 출력(float형)
print(random()*10)          # 0.0 ~ 10.0 미만의 값을 출력(float형)
print(int(random()*10))     # 0 ~ 10 미만의 값을 출력(int형)
print(int(random()*10)+1)   # 1 ~ 10까지의 값을 출력(int형)

# 예제] 1 ~ 45까지의 임의의 값 6개 출력
from random import random

for x in range(6):
    print(int(random()*45)+1)

# 문제1] 1 ~ 100까지 랜덤 값 6개를 출력하는 코드 작성
from random import random

for x in range(6):
    print(int(random()*100)+1,end=' ')
print()

# 문제2] 1 ~ 100까지 랜덤 값을 반복하여 출력하되, 출력 값이 50이 
#     출력되는 순간 반복을 종료하는 코드를 작성하세요.  
from random import random

while True:
    su = int(random()*100)+1
    print(su,end=' ')
    if su == 50:
        break
print()

# 문제3] 1 ~ 15까지 랜덤 값을 중복 없이 3개 생성하여 출력하는 코드 작성
num1, num2, num3 = 0, 0, 0
while True:
    su = int(random()*15)+1
    if num1 != su:
        num1 = su
        break
while True:
    su = int(random()*15)+1
    if num1 != su and num2 != su:
        num2 = su
        break
while True:
    su = int(random()*15)+1
    if num1 != su and num2 != su and num3 != su:
        num3 = su
        break
print("{} {} {}".format(num1,num2,num3))

# random 모듈 내에 있는 다른 형태의 random함수들...
#  - randint() : 임의의 값을 int형값으로 출력하는 함수
# 
#  사용방법
#   randint(a,b)
#    a : 시작값, b: 마지막 값
#   예제) 1 ~ 6 까지의 임의의 값을 출력하는 코드
#   from random import random,randint
#                   # random모듈에 있는 random(),randint()호출
#   print(randint(1,6))

#예제2] 1 ~ 6 , 100 ~ 200 사이의 임의 값 출력(randint()사용)
from random import random,randint

print(randint(1,6))         # 1 ~ 6까지 
print(randint(100,200))     # 100 ~ 200까지

# - randrange() : 범위 내에 임의값을 출력
#  
#  (예시1)
#   randrange(5,10)     => 5 ~ 10미만의 값을 출력
#  (예시2)
#   randrange(5,10,2)   => 5,7,9 중에 하나가 출력(2씩 증가된 값 중에) 
from random import random,randint,randrange

print(randrange(10))        # 0 ~ 10미만 
print(randrange(5,10))      # 5 ~ 10미만
print(randrange(5,10,2))    # 5 ~ 10미만, 2씩 증가값 중

# random모듈 내에 choice()
# : 이 함수의 특징은 리스트와 같은 형태의 자료 중 일부를 램덤하게 추출
# 
# (예시)
# dice = [1,2,3,4,5,6]
# choice(dice) # dice 리스트 내에 있는 멤버중 하나를 추출해서 출력
# 
import random           # 모듈을 볼러오면, 모듈명.함수()
dice = [1,2,3,4,5,6]
x = random.choice(dice)
print(x)

# or
from random import choice  # random모듈 내에 choice()만 호출
dice = [1,2,3,4,5,6]
x = choice(dice)
print(x)
'''
# 문제4] 1 ~ 99 까지 랜덤 값 중에 짝수면 True, 홀수면 False 출력하는
# 프로그램 코딩
from random import random

print("출력 결과: ",end='')
rand = int(random()*99)+1
if rand % 2 == 0:
    print("True({})".format(rand))
else: 
    print("False({})".format(rand))
