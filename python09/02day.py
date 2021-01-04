
print("Hello Python")
# 주석 처리 
# 1. 한줄 주석 : "#"
# 2. 여러줄 주석 : '''(시작) ~(주석 내용) '''(끝)
# 주석을 사용하는 이유 :
#  프로그램에 대한 comment를 달기 위해서 
#  왜 이 코드를 작성했는지 언제,누가 작성을 했는지
#  동작은 어떻게 되는 것인지를 기술해준 것.   

'''
# 한줄 주석 예시
print("Hello Python1")
# print("Hello Python2")
print("Hello Python3")

# 여러줄 주석 예시
'''
print("Hello Python4")
print("Hello Python5")
print("Hello Python6")
print("Hello Python7")
'''
print("Hello Python8")

# 파이썬의 특성
# 1. 가독성 : 프로그램 코드 간결하고, 가독성 높다. 
#          코드블럭을 들여쓰기로 구분합니다.(*)
#  코드 블럭이란? 동작인 영역에서 동작하는 코드 모음
#
# 2. 풍부한 라이브러리 : 매우 광범위 라이브러리를 가짐.
#       외부 라이브러리가 매우 풍부해서 확장 가능함.  
#       라이브러리란? 다양한 동작을 하는 함수들...
# 
# 3. 접착성 : 쉽게 라이브러리를 추가할 수 있고, 파이썬에
#       C로 구현된 부분을 사용할 수 있고, C에서 파이썬을 
#       사용할 수 있다.(예)
# 
# 4. 무료 : 파이썬은 파이썬 재단에서 관리, 거의 무료와 같음
# 
# 5. 유니코드를 지원 : 파이썬에서는 문자열을 모두 유니코드로
#       사용함. 
#       유니코드란? 문자를 표현하는 값을 의미함. 모든 나라의
#          문자를 표현할 수 있게 함.
#
# 6. 동적 타이핑 : 런타임 시에 타입을 체크하는 동적타이핑을
#       지원함. 즉, 메모리 관리를 자동으로 처리함.   

# 파이썬을 사용하는 프로젝트
#  BitTorrent, MoinMoin, Scons, Trac, Yum
#  CherryPy, Django
#  GIMP, Maya, Paint Shop Pro
#  Youtube.com, Google Groups, Google Maps, Gmail
 
# 파이썬 2.x 와 파이썬 3.x의 차이점
# 
# 1) print가 함수로 변경됨. 
#  2.x style :
#    >>> print "welcome to", "python3k"
#    welcome to python3k
# 
#  3.0 style :
#    >>> print("welcome to", "python3k")
#    welcome to python3k 
# 
# 2) long 자료형이 없어지고, int형으로 통일
#   2.x style :
#    >>> type(2**31)
#    <type 'long'> 
#    >>> sys.maxint
#    2147483647
#
#  3.0 style :
#    >>> type(2**31)
#    <class 'int'>
#    >>> type(2**40)
#    <class 'int'>  

# 3)'int / int' 의 결과가 float으로 처리.
#  2.x style : 
#    >>> 3/2
#    1
#
#  3.x style : 
#    >>> 3/2
#    1.5
#    >>> type(2/2)
#    <class 'float'>
   
   
# 4) String, Unicode 체계 변경.
#  2.x style :
#    >>> type('가')      
#    <type 'str'> 
#    >>> type(u'가')
#    <type 'unicode'>
#
#  3.0 style :
#    >>> type('가')
#    <class 'str'>
#    >>> type('가'.encode('cp949'))
#    <class 'bytes'> 

# ===================================
# 이스케이프 문자
#  : 특수한 의미를 가지고 있는 문자를 출력하기 위한 기능
#
#  - '\n' : 줄바꿈 문자(개행문자)
#  - '\r' : 해당 줄의 처음으로 커서를 이동.
#  - '\t' : 탭만큼 커서를 이동. 보통 탭은 8칸 간격.
#  - '\'' : ' 문자
#  - '\"' : " 문자
#  - '\\' : \ 문자 
print('오늘 아침 날씨 쌀쌀해요\n그래서 배고파요!!')

print('오늘 아침은 날씨가 춥데요')
print('내일')
print('오늘 아침은 날씨가 춥데요\r내일')

print('오늘도\t여러분을\t봐서\t기분이\t좋네요!!')

print('오늘 아침에 \'기분\'이 정말 좋았어요!!')
print('Have a \\nice\\ day!!')
'''
# 파이썬을 이용한 간단한 연산 처리
print(3+10)     # 13
print(10-3)     # 7
print(10*3)     # 30
print(10/3)     # 3.33333333
print("10더하기 20의 결과는 : ",10+20)
print("3 곱하기 9의 결과는 : ",3*9)

# 실습
print(' '*15,' #### 회비 정보 ####','\n','='*48,'\n',
    '이름\t\t나이\t전화번호\t회비\n',
    '='*50,'\n',
    '김동완\t\t38\t010-1111-1111\t\\20,000\n',
    '서지수\t\t24\t010-1234-5678\t\\30,000\n',
    '이지은\t\t25\t010-2525-2345\t\\50,000\n',
    '-'*50,'\n',
    '총합계\t\t\t\t\t\\100,000\n',
    '='*50
    )
# or
print("\n출력예제")
print("\t\t#### 회비 정보 ####")
print("==================================================")
print("이름\t\t나이\t전화번호\t회비")
print("="*50)
print("김동환\t\t38\t010-1111-1111\t \\20,000")
print("서지수\t\t24\t010-1234-5678\t \\30,000")
print("이지은\t\t25\t010-2525-2345\t \\50,000")
print("-"*50)
print("총합계\t\t\t\t\t\\100,000")
print("="*50)