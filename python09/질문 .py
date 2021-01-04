num =1
while num : 
    ln = int(input("홀수를 입력하세요"))        
    sp = ln//2; st=1; flag = True               # 1, sp = ln//2 에서 2의 값이 나온 이유가 무엇인가요? 
    for i in range(ln):                         
        for j in range(sp) : print(end=" ")       
        for j in range(st) : print("*",end="")  # 2, 위에 for j in range (sp) 와 for j in range(st)에서 변수 "j:는 같아야 하는건가요?
        print()
        if i == (ln//2): flag = False           # 3, 여기서 i의 조건이 (i == ln//2) 가 되는 이유가 무엇인가요?
        if flag : sp -=1; st +=2                # 4, 여기 부분은 처음에 st = "*"의 개수가 증갈할때 2개씩 별의 개수를 늘리는 이유가 맞나요?
        else : sp += 1; st -=2                  # 5, else가 있는 이유가 무엇인가요??
    num = int(input("0,종료,1계속"))
print("프로그램종료")                          # 너무어렵습니다....ㅜ

        


# print(random())                                 # 6, 랜덤 함수에서 random() 괄호 안에는 %값으로  0~9 까지의 숫자만 나온다고 하셧는데 그럼 저희가 괄호안에는 어떠한것도 넣을수 없는건가요?


# import random                                   # 7, 랜덤 모듈 내에 있는 많은 함수중에 choice 라는 특정 함수를 불러와서 사용하는게 맞나요?? 
# dice = [1,2,3,4,5]
# x = random.choice(dice)
# print(x)
# or                                              # 8,from random import choice 를 사용하면 import random내에 choice를 사용하는것보다 사용의 크기가 작다고 하셧었는데 그러면, 게임내의 최적화 개념이랑 비슷하게 생각해도 되는건가요?
# from random import choice                       
# dice = [1,2,3,4,5]                              
# x = choice(dice)
# print(x)







#     #   각 주석에 위치해있는 문장마다 질문이 있습니다!
# # 1, 

# # 2,

# # 3,

# # 4,

# # 5, 

# # 6, 

# # 7, 

# # 8, 