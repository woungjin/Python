'''
# while 구문에 else 사용
i = 0
while i < 5:
    print("{}번 반복문장을 실행".format(i))
    i += 1
else:
    print("조건식이 거짓인 경우에 실행")
print("메인 프로그램 실행 코드")

# while의 무한 반복 
# :while 구문이 항상 참이되게 설정한 후에 반복문 내에 제어를 위한 명령어를
# 사용. break(반복 종료), continue(조건식으로 이동)
# 
# (형식)
# while True:
#     종속문장1(반복문)
#     종속문장2
#     ...
# (메인 프로그램 코드 실행)
#  이 경우에 무한 반복하기 때문에 프로그램이 while구문을 나올 수 없다.
# 때문에 제어를 통해서 반복 구문을 중지시켜야 한다. 이때 break를 사용
# 
# (break 예)
# while True:
#     종속문장1
#     break
#     종속문장2
# (메인 프로그램 코드 실행)  
# 
# 프로그램의 흐름 : while의 조건식 => 종속문장1 => break(반복문 종료)
#               => 메인 프로그램 코드 실행
# 
#  - continue : while 구문에서 반복문을 종료하지 않고, 반복 중에 continue
#             를 만나면, 반복문의 조건식으로 이동. 다시 반복... 
# 
# (continue)
# while True:
#     종속문장1
#     continue
#     종속문장2
# (메인 프로그램 코드 실행)
# 
# 프로그램의 흐름 : while의 조건식 => 종속문장1 => continue(조건식으로 이동)
#               => while의 조건식 => 종속문장1 => continue => 조건식
#               => 종속문장1 => continue ...  

#예제1] break와 continue 사용 예제
#(break)
while True:
    a = int(input("정수 입력(0입력시 프로그램 종료) : "))
    if a == 0:
        break
    print("입력값 출력 : ",a)

#(continue)
a = 0
while a < 5:
    a += 1
    if a == 3:
        continue
    print("a = {}".format(a))

# 문제 1] 
# 쌀 100통이 저장되어 있는 창고에 암수 1쌍의 쥐가 있습니다. 
# 쥐 한 마리가 하루 20g씩 쌀을 먹고 있습니다. 
# 10일 마다 쥐의 수가 2배씩 증가하고 있다면, 
# 며칠 만에 창고의 쌀이 모두 쥐의 먹이가 될까? 
# 또, 이때에 쥐는 총 몇마리가 되어 있을까? 
# (쌀 한통는 1kg, 쥐는 쌀은 먹은 후 2배로 증가하는 조건)
# [결과] : 80일, 512마리
#
rice = 100*1000
mice = 2
day = 1
while rice > 0:
    rice -= mice * 20   # rice = rice - (mice*20)
    if day%10==0:
        mice *= 2       # mice = mice * 2
    if rice <= 0:
        break
    day +=1
print("{}일만에 쥐는 {} 마리가 됨.".format(day,mice))

# 문제2] turtle을 통해서 만든 다각형 그리는 코드를 반복문으로 사용하여 
#     작성 (3 ~ 12까지의 값을 입력 받아서 하시오)
# 
import turtle
nu = int(input("3 ~ 12까지의 정수 입력 : "))
if nu >=3 and nu <= 12:
    for idx in range(nu):
        turtle.forward(100)
        turtle.left(360/nu)
    turtle.mainloop()
else:
    print("그릴수 없습니다.")
# 문제3] 1 ~ 100까지의 합을 구하는 코드를 작성
# 
Sum = 0
for x in range(1,101): # [1,2,3,4,5,6,7,8 ...98,99,100]
    Sum += x   # Sum = Sum + x
print(Sum)

# 문제4] 1부터 1씩 증가하는 값에 대해 누적합을 구할 때 10,000보다 
#     큰 누적합 값에 대해 마지막에 더해진 값이 얼마인지 구하시오
x = 1
Sum = 0
while True:
    Sum += x
    if Sum > 10000:
        break
    x += 1
print(x,"는 10000 되기 전에 더한 누적합!!")
# 문제5] 1부터 100 사이의 소수(prime number)를 출력하고 개수를 구하시오
count = 0
for x in range(2,101): #[2,3,4,5,...,98,99,100]
    flag = True     # 소수여부 판단, True= 소수, False = 소수 X
    for y in range(2,x):    # 소수 판단... 
        if x%y == 0:        # 이게 참이면 소수가 아님. 
            flag = False
            break
    if flag:
        print(x,end=" ")  #소수 출력
        count += 1
print() # 소수출력 후 줄바꿈
print(count,"개의 소수가 존재함!!!")


# 문제6] 다음과 같은 모형으로 출력되게 하세요. 
# (단, 파이썬 서식을 사용안함. )
6-1         6-2         6-3         6-4
*           *****           *       *****
**          ****           **        ****
***         ***           ***         ***
****        **           ****          **
*****       *           *****           *
'''
#6-1
for i in range(5):           #[0,1,2,3,4]
    for j in range(0,i+1,1): #[0],[0,1],[0,1,2],[0,1,2,3],[0,1,2,3,4]
        print("*",end='')
    print()
'''
6-5 출력 줄수를 입력하면 다음과 같이 출력 입력 줄은 홀수이여야만 함. 

홀수 줄수를 입력: 7
   *
  ***
 *****
*******
 *****
  ***
   *
'''