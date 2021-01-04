# #   while 구문에 else 사용 
# i = 0
# while i < 5 :
#     print("%s번 반복문장을 실행"%(i))
#     i += 1 
# else :
#     print("조건식이 거짓인 경우에 실행")
# print("메인프로그램코드 실행")              # 이게 없는것과 잇는것의 차이?

# while에 무한반복
# : while 구문이 항상 참이되게 설정한 후에 반복문 내에 제어를 위한 명령어를 사용하여 제어 
# 사용 언어 : break(반복구문 종료할때=for에도 사용), continue(조건식으로 이동)
#
# 형식)
# while True :
#   종속문장1(반복문)
#   종속문장2
#   ...
#(메인프로그램 코드실행)
# 이경우에 무한 반복하기 떄문에 프로그램이 while구문을 나올 수 없다.
# 때문에 제어를 통해서 반복구문을 중지시켜야 한다. 이때 break를 사용 
#
#       ＊ break )
# while True :
#   종속문장1 
#   break
#   종속문장2                         # = 증발 
#(메인프로그램 코드 실행)
#
# 프로그램의 흐름 : while의 조건식 =-> 종속문장1 => break(반복문 종료)
#                  => 메인프로그램 코드 실행 (break를 만나면 그자리에서 작동중지하고 나감 )
#
#       ＊ continue : while 구문에서 반복문을 종료하지 않고, 반복 중에 continue를 만나면, 반복문의 조건식으로 이동, 다시 반복 ... 
# while True :
#   종속문장1 :       < ┐
#   continue            ┘
#   종속문장2 :
# (메인프로그램 코드 실행) 
#
#   프로그램의 흐름 : while의 조건식 -> 종속문장1 => continue -> while의 조건식 -> 종속문장1 -> continue -> 조건식 -> 종속문장1 -> 반복....

# 예제 ) break 와 continue의 사용 예제
# # break ) 
# while True:
#     a = int(input("정수 입력(0입력시 프로그램 종료) : "))
#     if a ==0 : 
#         break
#     print("입력값 출력 : ",a)

# # continue )                # 주의 : continue만쓰면 무한반복해서 멈추어 줘야함
# a = 0
# while a < 5:
#     a += 1
#     if a == 3 :
#         continue
#     print("a = {}".format(a))

# 문제 ) 쌀100통이 저장되어 있는 창고에 암수 1쌍의 2마리 쥐가 있습니다
# 쥐한마리가 하루 20g씩 먹고 있습니다
# 10 일마다 쥐의수가 2배씩 늘어난다면 며칠만에 쌀이 사라지고 쥐는 몇마릴까 
# 쌀 한통은 1000g  \
# 결과는 - 80일 , 512마리 
# 쥐 = 2
# 밥 = 100*1000
# 날짜 = 1
# while 밥 > 0 :              # 정수를 맞추어야함
#     밥 -= 쥐 * 20           
#     if 날짜%10 ==0:         # 10일의 배수는 나누면 됨
#         쥐 *= 2
#     if 밥 <= 0 :    
#         break
#     날짜 += 1               # 브레이크 없으면 여기 날짜 +1이 마지막에 붙어서 힘듬 
# print("결과 = %s , 쥐 숫자 = %s" %(날짜,쥐)) 

# 문제 2)    turtle.을 이용해서 다각형 그리는 코드를 반복문으로 사용하여  3~ 12각형 까지의 값을 나오게


# import turtle                               #내가한건 while이용 = 실패 , 
# a = int(input("3~12각형 숫자 입력 :"))    
# b = 30  #변의길이
# c = (360/a)  # 각도
# if a >=3 and a<=12 :                        #for를 이용해서 a숫자 입력만큼 종속문장을 이용해라 
#     for idx in range (a) :              # for다음 의미없는 변수명의 사용 여부??
#         turtle.forward(b)
#         turtle.left(c)
#     turtle.mainloop()
# else :
#     print("그릴수 없습니다")


# # 문제3 ) 1~ 100 까지의 합을 구하는 코드를 작성
# # 
# sum = 0
# for x in range (1,101,):                      # 반복횟수가 정해져있을땐 for 모를떈 while
#     sum += x
# print(sum)
# # 문제 4) 1부터 1씩 증가하는 값에 대헤 누적합을 구할때 10000큰 누적합 값에 대헤 마지막에 더해진 값이 얼마인지 구하시오
# x = 1           # 1~10000
# sum = 0         # 누적합
# while True :
#     sum += x
#     if sum >=10000:
#         break    
#     x += 1
# print(x,"는 10000되기 전에 더한 누적합")

# # 문제 5) 1 부터 100 사이의 소수를 출력하고 개수를 구하여라 1제외하고 (소수는 자신을 제외하고 나누어지지 않는 수)
# count = 0
# for x in range(2,101):                   
#     flag = True                                 # 소수 여부 판단
#     for y in range(2,x):                        # 소수 판단
#         if x%y ==0 :                            # x의 값이 나누어지면 소수가 아니이기에 배수관계로
#             flag = False                        # 소수 아닌건 브레이크 건다
#             break
#     if flag :                            
#         print(x,end =' ')
#         count +=1 
# print()
# print(count,"개의 소수가 존재합니다")

# 문제) 
# for i in range(5):                      # 0,1,2,3,4
#     for j in range(0,i+1,1):            # 0, 01 012 0123 01234  #개수
#         print("*",end='')
#     print()

# for i in range(5):
#     for j in range(6,i+1,-1):
#         print("*",end='')
#     print()

# for i in range(6):
#     for j in range(1,i+1,1):
#         print("*",end='')
#     print()

# for i in range(5):
#     j = 3                   # 빈공간이 4개 이기에 4번 즉 0,1,2,3 을 반복하게끔
#     while j >= i :          # for j in rnage(3,i,-1)
#         print(end=" ")
#         j -=1
#     j=0
#     while j <= i:
#         print("*",end="")
#         j += 1 
#     print()

# for i in range(5):
#     j= 0 
#     while j < i :
#         print(end=" ")
#         j += 1 
#     j= 4
#     while j >=i :
#         print("*",end="")
#         j -= 1
#     print()

# 문제 )
# sp = 여백 , st 별개수 ,ln 홀수의 줄수 ,flag 조건반전을 위한 

import os
num =1 
while num :                                             # 해당 내용을 반복하기 위해서 
    os.system('cls')                                # . 을 넣어서 뒤의 시스템을 불러온다 
    ln = int(input('홀수를 입력하세요 :'))
    sp = ln//2; st=1; flag = True                     # // = 나눈 몫의 값 즉 ex) 5//2 = 2의 빈칸만큼
    for i in range(ln) :                                 # 중요한 부분으로 상위부분 
        for j in range(sp): print(end=" ")                    # 첫부분에 공백을 찍기위해 앞에 sp 공백만큼 주고 뒤에 print(end=" ")로 공백을 준다
        for j in range(st): print("*",end="")                   # 띄어쓰기는 이해되는데 별의개수는 왜 ㄴ늘어나는거지
        print()
        if i == (ln//2): flag = False                           # flag는 bool형 값을통해 특정 조건 즉 역피라미드 를 가기위해 처음에 True에서 False로 조건을 바꾸겟다
        if flag : sp -=1; st +=2                                # 트루일떄 sp 여백을 줄이고 st 별을 2개씩 늘린다
        else : sp += 1; st -=2 
    num = int(input("0,종료 1,계속 "))
print("프로그램종료")


# import os               # 여러가지 모듈을 가져온다 os가 예 ) system() = > 시스템에 cmd 명령어를 사용가능 
                        # system ('cls') => 터미널 창의 내용을 깨끗하게 정리
                        # system ('pause') => 일시 정지
                        