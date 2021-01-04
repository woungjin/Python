#           ※for 문
#  : 가장 대표적인 반복구문 중 하나로 주어진 조건에 따른 회차 만큼 반복
#    (형식)
#       for 변수명 in range(반복횟수):
#       for의 종속문장1
#       for의 종속문장2
#       ...(반복할 내용)
# (메인프로그램 실행 코드)
#
#  ※ range () : 파이썬의 내장함수로 정해진 범위에 연속된 값을 만들어 내는 함수 
#   range 사용법 
#   1) range(종료값) = 마지막 값 (기본값은 0 부터)
#       : 0부터 종료값 이전까지의 값의 범위
#       ex) range(7) => [0,1,2,3,4,5,6]  - 0 부터 종료값 이전까지이 값을 나타냄
#   2) range(시작값, 종료값)
#       : 시작값부터 종료값 이전까지의 값의 범위
#       ex) range(5,10) => [5,6,7,8,9]
#   3) range(시작값, 종료값, 증감값(or감소))
#       : 시작값부터 종료값 이전까지의 증가값의 범위에 있는 내용
#       ex) range(1~10,2) => [1,3,5,7,9]
# print(list(range(10)))
# print(list(range(5,10)))
# print(list(range(1,10,2)))
# print(list(range(10,5.4,-2))) 

# 예제1 
i = 0
for a in range(10):
    print(a,end='')      # in = 조건문으로 참이면 반복함 # end=' ' (print는 마지막에  \n을 가지고 실행하는데 그거대신에 ' ' 띄어쓰기됨)
    i += 1                      # print ()의 end 인자값 설정 : 기본 (\n)
print("반복횟수 : ", i)                          # end='(문자)' print()의 마지막에 사용할 문자

# # 예제2)
# for x in range(5,10) :
#     print(x,end=' ')
# print()                 # 이부분의 print는 위에 for구문에서 \n 줄바꿈을 바꾸었기 때문에 줄바꿈을 넣어준것 

# # 예제3) 
# for x in range(1,10,2):
#     print(x,end=' ') 
# print(i)

# # 예제4)
# for x in range(10,0,-2) :
#     print(x,end=' ')
# print()

# # 예제5) 문자열을 이용한 for구문 
# for x in 'string':          # string라는 문자열 한번에 반복되는것이 아닌 각 스펠링마다 s,t,r,i,n,g 각각 반복한다  즉 반복회수는 6번
#     print(x,end='')
# print()

# # # 예제6) 연속된 자료(list,tuple ..) 의 for 구문
# i = 0
# for x in [1,4,78,'test','a',1.90,0.5,100]: 
#     print(x,end=' ')
#     i += 1
# print("반복횟수(멤버의 갯수) :", i)

# # 예제7) 이중 for 구문 : for구문을 중점해서 사용하는 예시
# sum1 = 0
# sum2 = 0
# for x in range(10):
#     print("상위for문이 %s일때" %( x ))
#     for y in range(10):
#         sum2 += 1  # 하위 for문의 반복 횟수
#         print("하위 for문의 값이 {}".format(y))
#     sum1 += 1      # 상위 for문의 반복 횟수
# print("상위 for문의 반복 횟수 :",sum1) # 상위 for문에서 한번돌때 하위for문을 다 돌린다 
# print("하위 for문의 반복 횟수 :",sum2)

# 중첩 for구문은 상위의 for구문이 한번 실행할때 
# 하위 for구문(상위 for문의 종속문장)은 자신에게 주어진 반복회차 만큼 실행하는 동작을 하게된다
# 실행하는 동작을 하게 됨, 즉. 상위 for문이 1회 반복할때에 하위 for문은 10회 반복하는 것 
# 
# # 형식
# for x in range(반복횟수):
#   for y in range(반복횟수):
#       하위 for문의 종속문장1
#       하위 for문의 종속문장2
#       ...
#   종속문장3(상위for문)
#   (메인 실행 코드)


# for문 문제 1) 중첩 for문을 이용하여 구구단 표를 작성 
# for x in range (2,10):
#     print("%s단 출력" %x)
#     for y in range (1,10):
#         print("%s x %s = %s" %(x,y,x*y))

# # 문제2)  중첩 for문을 이용하여 다음과 같이 구구단 표를 출력
# for x in range(2,10):
#     for y in range(2,10) :
#         print("%s x %s = %s"%(y,x,x*y),end=' ')
#     print()

# # 문제 3) for 구문
# for x in range(0,5) :
#     for y in range(1) :
#         print("상위 for문이 %s 일때, 하위 for문 : %s %s %s %s %s " %(x,x*y,x,x*2,x*3,x*4))

# for x in range(0,5) :
#     print("상위 for 문이 %s 일때. 하위for문 : " %(x), end=' ')
#     for y in range(5) :
#         print(x*y,end =' ')
#     print()


# 문제 4 ) 서식x 이중for문
# for x in range(5) :
#     for y in range(1,6) :
#         print(y+x*5, end='\t')
#     print() 

# # sum1 = 0
# for x in range(5):
#     for y in range(5):
#         sum1 += 1 
#         print("{}".format(sum1),end='\t')
#     print()

# for x in range(5,0,-1):             # 5단위씩 끊어서 하니까 5를 기준으로 해주어야 함 
#     for y in range(5):
#         print(x*5-y, end=' \t ')
#     print()

# for x in range(5) :
#     for y in range(5) :
#         print("%s" %((x+y)%5+1) ,end='\t')
#     print()


# ※ while 구문
#   : 조건문이 참인 경우에 반복하는 반복문
# 
# (형식)
# while (조건식):
#   종속문장1(while)
#   종속문장2(while)
#   ... 반복할 내용
# 메인프로그램 실행 코드

# \예)
# while x <10 :
#   종속문장1
#   종속문장2
#       x +=1   # -> 조건식에 변화를 주는 값
#   메인프로그램 코드 실행


# 예제 while 구문을 이용한 반복 (짝수의 합, 홀수의 합)
# i = 1
# odd,even = 0,0
# while i <= 10 :
#     if i % 2 ==0:
#         even += i
#     else :
#         odd += i
#     i +=1            #조건식에 변화 부여 (무한반복을 할수있으니 변화를 부여해주어야 함!)
# print("짝수의 합 :  {}, 홀수의 합 {}".format(even,odd))