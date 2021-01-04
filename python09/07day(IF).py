#       ※다중 if 구문 (다수의 조건을 구문하고 싶을때 사용)
# : if 조건문이 참이 아니면, 다른 if구문 (elif) 조건문을 비교,
# 이것도 참이 아니, 최종적으로는 else 구문에 있는 종속문장을 실행함
# #elif의 조건의 개수에 대한 제한은 없음.
#
# (형식)
# if(조건식) :
#   if종속문장1
#   if종속문장2
# elif (조건식):
#   elif종속문장1
#   elif종속문장2
# ....
# else:
#   else종속문장1
#   else종속문장2
#(메인프로그램 코드 실행)


#       ※중복 if 구문
# : if 구문 안에  또 다른 if구문을 만든 형태
# 첫번쨰 if 가  참인 경우 두번쨰 if구문의 조건을 본다
# else 에 if를 중복하는 경우 else 조건에 부합 될 경우에 if문을 확인 (else에도 if구문 사용가능)
#
# (형식)
# if (조건식):
#   if종속문장1(첫번째if)
#   if (조건식2):
#       종속문장1(두번째if) # 들여쓰기로 차이를 둠 
#   종속문장2(첫번째 if)
# (메인프로그램 코드 실행)
#


#       예제1) 두 수를 입력받아 큰 수가 짝수이면 출력하는 예제, 짝수 홀수 구문
# num1 = int(input("첫번쨰 정수 입력 : "))
# num2 = int(input("두번째 정수 입력 : "))
# if num1 > num2 :
#     if num1%2==0:
#         print("num1(%s)는 큰 수이면서 짝수이다" %(num1))
#     else:
#         print("num1(%s)는 큰 수이면서 홀수이다." %(num1))
# elif num2>num1:
#     if num2%2==0:
#         print("num2({})는 큰 수이면서 짝수이다.".format(num2))
#     else:
#         print("num2({})는 큰 수이면서 홀수이다.".format(num2))
# else:
#     print("num1({})와  num2({})는 같다".format(num1,num2))


#     #   ＊문제  1 )           #강사님꺼 참조바람
# 이름 = (input("이름 입력 : "))
# 키 = float(input("키 입력 : "))
# 현재체중 = float(input("체중 입력 : "))
# 표준체중 = float(키 - 100)*0.9
# 비만도 = float(현재체중/표준체중*100)
# if 비만도 < 100 :                         # elif를 대신써서 해도되는데 그냥 if를 쓰면 안되는건가? 차이가 머지
#     print("%s님의 비만도는 %.1f 로 저체중 입니다"%(이름,비만도))
# if 비만도 >= 100 and 비만도 <110 :
#     print("%s님의 비만도는 %.1f 로 정상 입니다"%(이름,비만도))
# if 비만도 > 110 and 비만도 < 120 :
#     print("%s님의 비만도는 %.1f 로 과체중 입니다"%(이름,비만도))
# if 비만도 > 130 :
#     print("%s님의 비만도는 %.1f 로 고도비만 입니다"%(이름,비만도))

# # 문제 2 )
# import turtle
# num2 = int(input("3~10 까지 정수 입력 : "))
# a = (30)
# b = (360/num2)
# if num2 >= 3 and num2 <=10:
#     if num2 ==3 :
#         turtle.forward(a)
#         turtle.left(b)
#         turtle.forward(a)
#         turtle.left(b)
#         turtle.forward(a)
#         turtle.mainloop()
#     if num2 ==4 :
#         turtle.forward(a)
#         turtle.left(b)
#         turtle.forward(a)
#         turtle.left(b)
#         turtle.forward(a)
#         turtle.left(b)
#         turtle.forward(a)  
#         turtle.mainloop()       # 반복 해서 다음껏도 작성          
# else : 
#     print("그럴 수 없습니다")



# #       문제3)
# year = int(input("년도를 입력해주세요 : "))
# if year % 4==0:             #배수는 나누면 0이된다
#     if year % 100 ==0:
#         if year % 400 ==0 :
#             print(year,"년도는 윤년입니다.")
#         else:
#             print(year,'년도는 평년입니다')
#     else:
#         print(year,"년도는 윤년입니다")
# else :
#     print(year,"년도는 평년입니다")


#       문제4 )
# 이름 = input("이름을 입력하세요 : ")
# 학번 = input("학번을 입력하세요 :")
# a = int(input("A 점수 입력 : "))
# b = int(input("B 점수 입력 : "))
# c = int(input("C 점수 입력 : "))
# sum1 = int(a+b+c)
# 평균 = sum1/3
# if 평균 >= 90 :
#     leve1 = 'A'
# elif 평균 >=80:         # 다중이프 구문은 순차적으로 내려오기에 90점을 이미 패스했기에 그냥 이렇게 써도 됨
#     level = 'B'
# elif 평균 >=70:
#     level = 'c'
# elif 평균 >= 60:
#     level = 'D'
# else :
#     level = 'F'
# print("%s,%s님의 평균 점수%.1f은 %s입니다" %(이름,학번,sum1,level))

#       문제 5
# money = 0
# 개수 = int(input("커피의 개수를 입력해 주세요 : "))
# if 개수 > 10 :
#     money = money + 20000 + (개수 - 10) * 1500
# elif 개수 >=0 and 개수 <= 10 :
#     money = 2000*개수
# else:
#     print("개수를 잘못 입력하였습니다")
# print("커피의 %s개는 %s원 입니다"%(개수,money))


#   문제 6              # 가장 작은 범위부터 순서대로 넣으면 편리
num6 = int(input("정수 입력 : "))
if num6 ==0:
    print("0은 3의 배수도 4의 배수도 아닙니다")
elif num6 %3==0 and num6 %4==0:
    print("3의 배수 이면서 4의 배수 입니다.")
elif num6 %3==0:
    print("3의 배수 입니다")
elif num6 %4==0:
    print("4의 배수 입니다")
else :
    print("3의 배수도 4의 배수도 아닙니다")

    # 궁금 :  if 종속문장에 print 를 넣는것과 마지막에 들여쓰기 없이 print를 넣는 것의 차이 
     #: 아마 각각의 if구문에서 값을 뽑아낼땐 각각 입력하고
     #한번에 그걸 집어넣을땐 종속문장에 안쓰고 전체를 가져올떄 쓰는거

# 반복문 (for, while)
# for문은 횟수를 정해서 반복하고자 할 경우      (반복의 횟수를 정해서 하고싶을떄)
# while 문은 조건을 정해서 반복하고자 할경우    (조건에만 맞을때까지 반복할때)