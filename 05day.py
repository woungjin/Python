'''
# [입력 함수=문제1]
# 학생 이름과 국어,영어,수학 점수를 입력받아 출력하세요. 
# (입력예제)
# 학생 이름 : 덕우
# 국어 점수 : 90
# 영어 점수 : 90
# 수학 점수 : 100
# 
# (출력예제)
# ==================== 학생 정보 ===================
# 이름      국어    영어    수학     합계     평균
# 덕우       90      90     100      280     93.33 
name = input("학생 이름 : ")
kor = int(input("국어 점수 : "))
eng = int(input("영어 점수 : "))
mat = int(input("수학 점수 : "))
Sum = kor + eng + mat
avg = Sum/3
print("="*20," 학생 정보 ","="*20)
print("{}\t{}\t{}\t{}\t{}\t{}"\
    .format("이름","국어","영어","수학","합계","평균"))
print("{}\t{}\t{}\t{}\t{}\t{:.2f}"\
    .format(name,kor,eng,mat,Sum,avg))


# [문제2]
# 사용자로부터 이름, 키, 체중을 입력받아 비만도를 구해서 출력하는 프로그램 작성
#   비만도 계산 식 : 비만도(%) = 현재 체중 / 표준 체중 * 100
#   표준 체중 계산 식 : 표준체중 = (현재키 - 100) * 0.9
# 
# (출력 예시) : 홍길도 님의 비만도는 112.15% 입니다. 
name = input("이름을 입력하세요 : ")
kie = float(input("{} 님의 키를 입력하세요 : ".format(name)))
wei = float(input("{} 님의 몸무게를 입력하세요 : ".format(name)))
std = (kie - 100) * 0.9
fat = wei / std *100
print("{} 님의 비만도는 {:.2f}%입니다.".format(name,fat))

# turtle 모듈 사용하기
#  : 그림 또는 표를 만드는 모듈
# 
# (사용방법)
# import turtle  (=> turtle 모듈을 불러와요!!!)
#  => 모듈 안에는 특정 기능을 사용할 수 있는 함수들이 들어 있어요!!
# 
#  turtle에서 사용하는 함수들....
#  - forward(distance) : distance만큼 앞으로 이동(선을 출력)
#  - backward(distance) : distance 만큼 뒤로 이동(선을 출력)
#  - left(angle) : angle만큼 좌회전
#  - right(angle) : angle만큼 우회전
#  - goto(x,y) : 그름의 포인터를 좌표(x,y축만큼)로 이동
#  - color(color) : 지정한 color로 색을 설정
#  - width(width) : 지정한 두께(width)만큰 선 두께를 설정
#  - bgcolor(color) : 지정된 색으로 배경을 설정
#  - speed(int) : 지정된 int(0 ~ 10)값으로 애니메이션 속도를 조절
#  - penup() : 화면에 선을 그리지 않게 설정
#  - pendown() : 화면에 선을 그릴 수 있게 설정
#  - mainloop() : 프로그램이 종료되지 않고 유지될 수 있게 함.  
import turtle

turtle.speed(1)
turtle.color("red")
turtle.forward(100)
turtle.left(120)
turtle.color("blue")
turtle.forward(100)
turtle.left(120)
turtle.color("yellow")
turtle.forward(100)
turtle.left(120)
turtle.mainloop()

# 문제1] input() 사용하여 정삼각형을 그리는 코드
import turtle
su = int(input("한변의 길이 입력 : "))
turtle.forward(su)
turtle.left(360/3)
turtle.forward(su)
turtle.left(360/3)
turtle.forward(su)
turtle.left(360/3)
turtle.mainloop()

# 문제2] input() 가로 세로 길이 입력은 사각형 그리는 코드
import turtle
ga = int(input("가로 길이 입력 : "))
se = int(input("세로 길이 입력 : "))
turtle.forward(ga)
turtle.left(360/4)
turtle.forward(se)
turtle.left(360/4)
turtle.forward(ga)
turtle.left(360/4)
turtle.forward(se)
turtle.left(360/4)
turtle.mainloop()

# 문제3] input() 사용하여 정육각형을 그리는 코들
import turtle
su3 = int(input("한변의 길이 : "))
turtle.forward(su3)
turtle.left(360/6)
turtle.forward(su3)
turtle.left(360/6)
turtle.forward(su3)
turtle.left(360/6)
turtle.forward(su3)
turtle.left(360/6)
turtle.forward(su3)
turtle.left(360/6)
turtle.forward(su3)
turtle.left(360/6)
turtle.mainloop()

# 연산자
#  : 프로그램에서 특정한 계산을 위해서 사용하는 기호들...
# 
# (1) 산술 연산자
#  '+' : 두 피연산자의 더한 결과를 반환
#  '-' : 두 피연산자의 빼기 결과를 반환
#  '*' : 두 피연산자의 곱하기 결과를 반환
#  '/' : 두 피연산자의 나누기 결과를 반환
#  '//': 두 피연산자의 나누기 결과를 반환(정수 나누기 => 몫을 반환)
#  '%' : 두 피연산자의 나누기 결과의 나머지 값 반환
#  '**': 좌측 피연산자를 우측 피연산자의 값으로 거듭제곱 처리 후 값 반환
   
# 예제1] 3과 2를 가지고 다음과 같이 연산식 계산
print("{} + {} = {}".format(3,2,3+2))       # 3 + 2 = 5
print("{} - {} = {}".format(3,2,3-2))       # 3 - 2 = 1
print("{} * {} = {}".format(3,2,3*2))       # 3 * 2 = 6
print("{} / {} = {}".format(3,2,3/2))       # 3 / 2 = 1.5
print("{} // {} = {}".format(3,2,3//2))     # 3 //2 = 1(몫)
print("{} % {} = {}".format(3,2,3%2))       # 3 % 2 = 1(나머지) **
print("{} ** {} = {}".format(3,2,3**2))     # 3 ** 2 = 9

# (2)비교 연산자
#  : 두 피연산자의 값을 비교하여 "참(True)" 또는 "거짓(False)"를 판별
# 
# "==" : 두 피연산자의 값을 비교, 동일하면 "참", 다르면 "거짓"
# "!=" : 두 피연산자의 값을 비교, 동일하지 않으면 "참", 동일하면 "거짓"
# "<"  : 두 피연산자의 값을 비교, 왼쪽이 작다면 "참", 크면 "거짓"
# ">"  : 두 피연산자의 값으 비교, 왼쪽이 크다면 "참", 작으면 "거짓"
# "<=" : 두 피연산자의 값을 비교, 왼쪽이 작거나 같다면 "참", 크면 "거짓"
# ">=" : 두 피연산자의 값을 비교, 왼쪽이 크거나 같다면 "참", 작으면 "거짓"
print(3==2)     # 거짓(False)
print(3!=2)     # 참(True)
print(3>2)      # 참(True)
print(3<2)      # 거짓(False)
print(3>=2)     # 참(True)
print(3<=2)     # 거짓(False)

# (3) 논리연산자
#  : 두 피연사나의 값을 비교, "참" 또는 "거짓"인지를 판별
# "and" : 논리곱. 두 피연산자가 모두 참인 경우, "참" 
#        두 피연산자중 하나라도 "거짓"있으면 "거짓"
# "or" :  논리합. 두 피연산자가 둘중에 하나도 참이면 "참",
#        둘다 "거짓"이면 "거짓"
# "not" : 부정. 오른쪽 피연산자의 값이 "참"이면 "거짓"
#        오른쪽 피연산자 값이 "거짓"이면 "참" 

# AND : 논리곱
print((1==1) and (1==1))    # 참
print((1==1) and (1==0))    # 거짓
print((1==0) and (1==1))    # 거짓 *short cut 연산 : and연산은 부정을 우선함
print((1==0) and (1==0))    # 거짓  

# OR : 논리합
print((1==1) or (1==1))     # 참
print((1==1) or (1==0))     # 참
print((1==0) or (1==1))     # 참
print((1==0) or (1==0))     # 거짓

# NOT : 부정
print(not(1==1))            # 거짓
print(not(1==0))            # 참

# (4) 멤버연산자
#  : 피연산자 내에 멤버의 존재에 대한 질의
#  "in"  : 왼쪽 피연산자가 오른쪽 멤버 중에 일치하는 값이 존재하면,
#          "참", 그렇지 않으면 "거짓"
#  "not in" : 왼쪽 피연산자가 오른쪽 멤버 중에 일치하는 값이 존재하면,
#          "거짓", 그렇지 않으면 "참"

# in
print(1 in (1,2,3)) # 참
print(5 in [1,2,3]) # 거짓

# not in
print(1 not in (1,2,3)) # 거짓
print(5 not in [1,2,3]) # 참

# (5) 식별 연산자
#  : 두개의 피연산자를 비교하여 객체 값이 동일한지 아닌지를 구분
#  "is"  : 두 피연산자의 식별 값을 비교하여 , 동일한 객체이면 "참"
#         그렇지 않으면 "거짓"
#  "is not" : 두 피연산자의 식별 값을 비교하여, 동일한 객체이면 "거짓"
#         그렇지 않으면 "참" 

# is
print(type(1) is int)   # 참
print(type(1) is str)   # 거짓
# is not
print(type('1') is not int)     #참
print(type('1') is not str)     #거짓
'''