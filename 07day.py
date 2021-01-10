'''
# 다중 if구문
#  : if 조건문이 참이 아니면, 다른 if구문(elif) 조건문을 비교,
#  이것도 참이 아니면, 최종적으로 else구문에 있는 종속문장을 실행
#  %elif의 조건의 개수에 대한 제한은 없음.(메뉴, 등급, 동등한 위치의 비교)
#  
# (형식)
# if (조건식):
#     if종속문장1
#     if종속문장2
# elif (조건식):
#     elif종속문장1
#     elif종속문장2
# ....
# else:
#     else종속문장1
#     else종속문장2
# (메인 프로그램 코드 실행)
# 
# 중복 if구문
#  : if구문 안에 또 다른 if구문을 만든 형태
#   첫번째 if가 참인 경우 두번째 if구문의 조건을 본다.
#   else에 if를 중복하는 경우는 else조건에 부합 될 경우에 if문을 확인
# 
# (형식)
# if (조건식1):
#     종속문장1(첫번째 if)
#     if (조건식2):
#         종속문장1(두번째 if)
#     종속문장2(첫번째 if)
# (메인 프로그램 코드 실행) 

# 예제1] 두 수를 입력받아 큰수가 짝수이면 출력하는 예제
num1 = int(input("첫번째 정수 입력: "))
num2 = int(input("두번째 정수 입력: "))
if num1>num2:
    if num1%2==0:
        print("num1({})는 큰 수이면서 짝수이다.".format(num1))
    else:
        print("num1({})는 큰 수이면서 홀수이다.".format(num1))
elif num2>num1:
    if num2%2==0:
        print("num2({})는 큰 수이면서 짝수이다.".format(num2))
    else:
        print("num2({})는 큰 수이면서 홀수이다.".format(num2))
else:
    print("num1({})와 num2({})는 같다".format(num1,num2))

# 문제1
name = input("이름을 입력하세요 : ")
kie = float(input("{}님의 키를 입력하세요: ".format(name)))
wie = float(input("{}님의 몸무게를 입력하세요: ".format(name)))
std = (kie - 100) *0.9  # 표준체중
fat = wie/std * 100 # %로 출력
if fat < 100:
    level = "저체중"
elif fat >= 100 and fat < 110:
    level = "정상"
elif fat >= 110 and fat < 120:
    level = "과체중"
elif fat >= 120 and fat < 130:
    level = "비만"
else:
    level = "고도비만"
print("{}님의 비만도는 {:.2f}% 로 {} 입니다.".format(name,fat,level))


# 문제2
import turtle
num2 = int(input("3 ~ 10까지 정수 입력 : "))
if num2 >= 3 and num2 <= 10:
    if num2 == 3:
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.mainloop()
    if num2 == 4:
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.mainloop()
    if num2 == 5:
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.mainloop()
    if num2 == 6:
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.mainloop()
    if num2 == 7:
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.mainloop()
    if num2 == 8:
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.mainloop()
    if num2 == 9:
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.mainloop()
    if num2 == 10:
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.forward(100)
        turtle.left(360/num2)
        turtle.mainloop()
    #... 10까지... 
else:
    print("그릴 수 없습니다.")

# 문제3
year = int(input("년도를 입력하세요 : "))
if year % 4 == 0:
    if year % 100==0:
        if year % 400==0:
            print(year,"년도는 윤년입니다.")
        else:
            print(year,"년도는 평년입니다.")
    else:
        print(year,"년도는 윤년입니다.")
else:
    print(year,"년도는 평년입니다.")

# 문제4]
# - 이름, 학번, 3과목의 성적을 입력 받아 합계와 평균을 구하고, 
#   평균이 90이상이면 'A', 80 이상'B', 70이상 'C', 60이상 'D',
#   60미만이면 'F' 를 출력하시오
name = input("이름 입력 : ")
st = int(input("학번 입력 : "))
ko = int(input("국어 점수 : "))
en = int(input("영어 점수 : "))
ma = int(input("수학 점수 : "))
Sum = ko + en + ma
avg = Sum/3
if avg >= 90:
    level = 'A'
elif avg >= 80:
    level = 'B'
elif avg >= 70:
    level = 'C'
elif avg >= 60:
    level = 'D'
else:
    level = 'F'
print("{}학생의 합계:{} , 평균:{:.2f}으로 성적은 {} 입니다."\
    .format(name,Sum,avg,level))
'''
# 문제5
# -커피의 개당 가격은 2000원이다. 10개를 초과하면 초과하는 
#   양에 대해서만 개당 1500원씩 받는다. 
#   커피의 개수를 입력 받아 금액을 출력하시오.
money = 0
cup = int(input("주문할 커피의 개수를 입력 : "))
if cup > 10:    # 10개 초과 분량 계산
    money = money + 20000 + (cup - 10 ) * 1500
    #money += 20000 + (cup - 10) * 1500
elif cup > 0 and cup <= 10: # 10개 이하 분량 계산
    money = 2000*cup
else:
    print("잘못입력 했습니다.")
print("총 금액은 {}원 입니다.".format(money))


# 문제6
# - 정수를 입력받아 아래와 같이 출력하시오.
#   3의배수이면서,4의배수 입니다 
#   3의배수 입니다
#   4의배수 입니다 
#   3의배수도,4의배수도 아닙니다 
#   0은3의 배수도 4의 배수도 아닙니다.
num6 = int(input("정수 입력: "))
if num6 ==0:
    print("0은3의 배수도 4의 배수도 아닙니다.")
elif num6 %3 ==0 and num6 %4 ==0:
    print("3의배수이면서,4의배수 입니다.")
elif num6 %3 ==0:
    print("3의배수 입니다.")
elif num6 %4 ==0:
    print("4의배수 입니다.")
else:
    print("3의 배수도, 4의 배수도 아닙니다.")


# 반복문(for, while)
#  for문은 횟수를 정해서 반복하고자 할 경우... 
#  while문은 조건을 정해서 반복하고자 할 경우...  




