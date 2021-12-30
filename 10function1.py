'''
함수
    형식]def 함수명(매개변수1, 매개변수2)
        실행주
        return 결과1, 결과2
        
    return문은 생략할 수 있따.
    또한 2개 이상의 결과를 콤바로 구분하여 반환할 수 있고,
    반환 값은 튜플로 받을 수 있다.
'''
def menu():
    print('메뉴 중 숫자를 선택하세요')
    print('1.덧셈 2.뺄셈 3.곱셈 3.나눗셈')
    print('5.종료')
    return input('번호선택: ')

def add(a, b):
    print(a, "+", b, "=", a+b)
def sub(a, b):
    print(a, "-", b, "=", a-b)
def mul(a, b):
    print(a, "*", b, "=", a*b)
def div(a, b):
    print(a, "/", b, "=", a/b)

#loop가 1일때 지속적으로 수행가능한 반복문을 생성(무한루프)
loop=1
choice=0 
while loop==1:
    choice=int(menu()) #메뉴 출력 및 번호입력
    if choice==1:
        add(int(input("덧셈 a= ")), int(input("b=")))
    elif choice==2:
        sub(int(input("뺄셈 a= ")), int(input("b=")))
    elif choice==3:
        mul(int(input("곱셈 a= ")), int(input("b=")))
    elif choice==2:
        div(int(input("나눗셈 a= ")), int(input("b=")))
    elif choice==5: #사용자가 5를 입력하면 while탈출
        loop=0
print("연산종료!")

def min_max(num):
    sum=0
    for val in num:
        sum+=val
    return sum, min(num), max(num)

numbers = (8,7,6,8,4,9,5)
sumval, minval, maxval, = min_max(numbers)
print("튜플의 합, 최대값, 최소값: ", sumval, minval, maxval)   

    