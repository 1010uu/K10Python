'''
format() 함수 사용하기
    : 문자열 포매팅(String formatting)은 서식문자보다 좀 더 간단히
    문자열을 표현할 수 있다. {}안에 포매팅을 지정하고 format()함수로 
    값을 삽입한다.
'''

#문자열을 직접 대입
str1='name : {0}'.format('홍길동')
print(str1)

#변수를 대입
age=55
str2='age : {0}'.format(age)
print(str2)

#변수명을 통한 대입
str3='name:{name}, age:{age}'.format(name='홍길동', age=33)
print(str3)

#인덱스나 변수명이 없으면 순서대로 매칭된다.
str4='이름:{}, 나이:{}'.format('이순신', 44)
print(str4)

#인덱스를 이용하면 순서를 변경하는 것도 가능하다.
str5='나이:{1}, 이름:{0}'.format('이성계', 55)
print(str5)

#인덱스를 중복 사용하여 출력할 수 있다.
str6='항목1:{0}, 항목2:{1}, 항목3:{0}'.format('서울', '부산')
print(str6)

#정수 n자리 표현 : {인덱스:자리수 및 서식문자}
str7='정수3자리: {0:03d},{1:03d}'.format(12345,12) #출력결과:12345, 012
print(str7) #자리의 남는 부분은 0으로 채운다.

'''
    파이썬은 문장의 끝에 세미콜론을 사용하지 않으므로 코드를 줄바꿈 해야 한다면
    문장의 끝에 \(역슬러쉬)를 붙여서 연결되는 코드임을 명시해야 한다.
'''
str8='소수점 아래 2자리: {0:0.2f}, 소수점 아래 5자리: {1:0.5f}'.format(123.1234567,3.14)
print(str8) #소수의 남는 부분을 0으로 채운다. #출력결과:3.14000

#드문 경우이긴 하나 {}자체를 출력해야 할 때는 중괄호를 겹쳐서 기술한다.
str9='{{ {0} }}'.format('Python 중괄호 표현')
print('str9=', str9)

#세자리마다 콤마를 찍을 때 사용
str10=1592000
print(format(str10, ','))