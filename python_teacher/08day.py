'''
# 반복문(for, while)
#  for문은 횟수를 정해서 반복하고자 할 경우... 
#  while문은 조건을 정해서 반복하고자 할 경우...

# for문
#  : 가장 대표적인 반복구문 중 하나로 주어진 조건에 따른 회차 만큼 반복
# 
# (형식)
# for 변수명 in range(반복횟수):
#     for의 종속문장1
#     for의 종속문장2
#     ...(반복할 내용)
# (메인 프로그램 실행 코드)
# 
# range() : 파이썬의 내장함수로 정해진 범위의 연속된 값을 만들어 내는 함수
# 
# 사용법
# 1. range(종료값)
#  : 0부터 종료값 이전까지의 값의 범위
#  예] range(10) => [0,1,2,3,4,5,6,7,8,9]
# 2. range(시작값, 종료값)
#  : 시작값부터 종료값 이전까지의 값의 범위
#  예] range(5,10) => [5,6,7,8,9]
# 3. range(시작값, 종료값, 증감값)
#  : 시작값부터 종료값 이전까지의 증감값의 범위에 있는 내용
#  예] range(1,10,2) => [1,3,5,7,9] 
print(list(range(10)))      # [0,1,2,3,4,5,6,7,8,9]
print(list(range(5,10)))    # [5,6,7,8,9]
print(list(range(1,10,2)))  # [1, 3, 5, 7, 9]
print(list(range(10,0,-2))) # [10, 8, 6, 4, 2]

# 예제1]
i = 0
for x in range(10):
    print(x,end=' ') # print()의 end인자값 설정 : 기본("\n")
    i+= 1            # end='(문자)' => print()의 마지막 사용할 문자  
print("반복횟수 : ",i)

# 예제2]
for x in range(5,10):
    print(x,end=' ')
print()

# 예제3] 
for x in range(1,10,2):
    print(x,end=' ')
print()

# 예제4]
for x in range(10,0,-2):
    print(x,end=' ')
print()

# 예제5] 문자열을 이용한 for구문
for x in "string":
    print(x,end='')
print()

# 예제6] 연속된 자료(list, tuple .. )의 for구문
i = 0
for x in [1,4,78,'test','A',1.90,0.5,100]:
    print(x,end=' ')
    i += 1
print()
print("반복횟수(멤버의 갯수): ",i)


# 예제7] 이중 for구문 : for구문을 중첩해서 사용하는 예시
Sum1 = 0
Sum2 = 0
for x in range(10):
    print("상위 for문이 {}일때,".format(x))
    for y in range(10):
        Sum2 +=1        # 하위 for문의 반복 횟수
        print("하위 for문의 값이 {}일 경우.".format(y))
    Sum1 += 1           # 상위 for문의 반복 횟수
print("상위 for문의 반복 횟수 : ",Sum1)
print("하위 for문의 반복 횟수 : ",Sum2)

# 중첩 For구문은 상위 For구문이 한번 실행할 때에 
# 하위 For구문(상위 For문의 종속문장)은  자신에게 주어진 반복 횟수 만큼
# 실행하는 동작을 하게 됨. 즉, 위 예제에서 상위 for문아 1회 반복 할 때에
# 하위 for문은 10회 반복하는 것을 알 수 있음. 
# 
# (형식)
# for x in range(반복횟수):
#     for y in range(반복횟수):
#         하위for문의 종속문장1
#         하위for문의 종속문장2
#         ...
#     종속문장3(상위for문)
# (메인 실행 코드) 


# 문제1] 중첩 for문을 이용하여 구구단 표를 작성
# (출력 예시)
#   (2단 출력)
#   2 x 1 = 2  
#   2 x 2 = 4
#   2 x 3 = 6
#   2 x 4 = 8
#   ... 
for x in range(2,10):  # [2,3,4,5,6,7,8,9]
    print("({}단 출력)".format(x))
    for y in range(1,10): #[1,2,3,4,5,6,7,8,9]
        print("{} x {} = {:<3}".format(x,y,x*y))
    print()

#문제2] 중첩 for문을 이용하여 다음과 같이 구구단 표를 출력
# 2 x 1 = 2   3 x 1 = 3   4 x 1 = 4   5 x 1 = 5   6 x 1 = 6   ...
# 2 x 2 = 4   3 x 2 = 6   4 x 2 = 8   5 x 2 = 10  6 x 2 = 12  ...
# 2 x 3 = 6   3 x 3 = 9   4 x 3 = 12  5 x 3 = 15  6 x 3 = 18  ...
# ....        ...         ...         ...         ...         
# 
for x in range(1,10):
    for y in range(2,10):
        print("{} x {} = {:<3}".format(y,x,x*y),end=' ')
    print()

# 문제3) 다음과 같이 출력되게 For구문을 작성하세요.... !!!!
# 상위 For문이 0일때, 하위 For문 : 0 0 0 0 0   
# 상위 For문이 1일때, 하위 For문 : 0 1 2 3 4   
# 상위 For문이 2일때, 하위 For문 : 0 2 4 6 8   
# 상위 For문이 3일때, 하위 For문 : 0 3 6 9 12  
# 상위 For문이 4일때, 하위 For문 : 0 4 8 12 16 
for x in range(5):
    print("상위 For문이 {}일때, 하위 For문 : ".format(x),end=' ')
    for y in range(5):
        print(x*y,end=' ')
    print()
'''
# 문제 4) 이중 For문을 사용하여 다음과 같이 출력되게 만들어 보세요. 
#  1) 1   2   3   4   5
#     6   7   8   9   10
#     11  12  13  14  15
#     16  17  18  19  20
#     21  22  23  24  25 
for x in range(5):          #[0,1,2,3,4]
    for y in range(1,6):    #[1,2,3,4,5]
        print(y+x*5,end='\t')
    print()
print('\n')
#or
Sum = 0
for x in range(5):
    for y in range(5):
        Sum += 1
        print("{}".format(Sum),end='\t')
    print()
print('\n')    
#  2) 25  24  23  22  21
#     20  19  18  17  16
#     15  14  13  12  11
#     10   9   8   7   6
#      5   4   3   2   1 

for x in range(5,0,-1):     #[5,4,3,2,1]
    for y in range(5):      #[0,1,2,3,4]
        print(x*5-y,end='\t')
    print()
print('\n')

#  3)  1   2   3   4   5
#      2   3   4   5   1
#      3   4   5   1   2
#      4   5   1   2   3
#      5   1   2   3   4 
for x in range(5):
    for y in range(5):
        print("{}".format((x+y)%5+1),end='\t')
    print()

# while 구문
#  : 조건문이 참인 경우에 반복하는 반복문
# 
# (형식)
# while (조건식):
#     종속문장1(while)
#     종속문장2(while)
#     ... (반복할 내용)
# (메인 프로그램 실행 코드) 

# 예]
# while x < 10:
#    종속문장1
#    종속문장2
#    x += 1  # => 조건식에 변화를 주는 값(***)
# (메인 프로그램 실행 코드)
#   

# 예제] while 구문을 이용한 반복(짝수의 합, 홀수의 합)
i = 1
odd,even = 0,0
while i <= 10:
    if i % 2 ==0:
        even += i
    else:
        odd += i
    i += 1  #조건식에 변화값 부여
print("짝수의 합 : {}, 홀수의 합 : {}".format(even,odd))
    