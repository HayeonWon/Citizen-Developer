
def func(param):
    print(param)
    print('여기는 함수!!')

print('hello world') # 디버깅하면 breakpoint에서 멈춤
func('안녕') # f10 누르면 다음 줄 실행 # debugging 상태에서 f11누르면 함수 안으로 들어감
print('hello world')

# 값이 계속 변하는 경우엔 watch 창에 등록해놓으면 편함
# 주피터 노트북 처럼 변하는 값 바로 출력하는 게 DEBUG CONSOLE -> 아래 줄에 값 입력하면 바로 보여줌
# 디버깅을 통해 문제가 되는 코드를 찾고 해결할 수 있음. 디버깅을 잘 하는 게 중요.
# 들여쓰기는 앞서 나온 코드의 영향성을 결정함. tab을 누르면 자동으로 4칸 들여쓰기
# 창 아래 Select Indentation을 통해 들여쓰기 설정 바꿀 수 있음. 기본은 4칸으로 설정됨.
# 코드가 복잡해져도 유지보수 용이하게 잘 정리하자
# call stack을 사용하여

##### 메모리란?
# a=10일 때, a가 10을 가리킨다. a가 10을 바인딩한다. 라고 얘기해야 정확함 (a가 10을 가진다x)

def f1(a):
    return a + 20

def f0(a):
    a = 20
    b = f1(a)
    return b

a = 10
b = f0(a)
print(b)

# 예제
def f(a):
    a = 100

a = 10
f(a)
print(a) # 100이 아닌, 10 출력
         # f(a)의 a는 지역변수로, 함수가 종료되면 메모리에서 삭제됨

##### 클래스
class 삼성차:
    pass

a = 삼성차()
b = 삼성차()

a.차종 = "SM5"
b.차종 = "QM6"

print(a.차종)


##### 클래스와 메서드
def 환영인사():
    print("안녕하세요")
    print("반갑습니다")
def 격한인사(이름):
    print("오!!! 방가방가")
    print("나는" + 이름 + "이야!")
환영인사()
환영인사()
격한인사("어피치") # 이렇게 하면 너무 길어짐

# 클래스를 사용해보자
# 클래스 안에 포함된 함수의 인수에 객체를 반드시 넣어줘야 줘야함
class 인사:
    def 환영인사(객체): # 인사라는 클래스에 포함된 함수(들여쓰기 필수)
        print("안녕하세요")
        print("반갑습니다")
    def 격한인사(객체, 이름):
        print("오!!! 방가방가")
        print("나는" + 이름 + "이야!")

a = 인사()
인사.환영인사(a)
인사.격한인사(a,"어피치")

# 연습문제 1 - 클래스로 표현
class 학생:
    pass

a = 학생()
b = 학생()

a.이름 = "어피치"
b.이름 = "라이언"

# 연습문제 1 - 메서드로 표현
class 학생:
    def 이름입력(obj, 실제이름):
        obj.이름 = 실제이름
        obj.나이 = 17 # obj 객체의 나이 변수 안에 17 값 바인딩

a = 학생()
학생.이름입력(a, '어피치') #어피치를 obj가 가리키는 이름 변수 안에 바인딩하라는 명령

b = 학생()
학생.이름입력(b, '라이언') #obj는 b와 같은 메모리를 갖게 되고, b 안의 이름이라는 공간에 "라이언"을 넣게 됨

print(a.이름, a.나이)

# 연습문제 2 - 나열하기
def 입금하기(잔고, 입금액):
    return 잔고 + 입금액
이름_a = '어피치'
잔고_a = 1000
잔고_a = 입금하기(잔고_a, 100)

이름_b = '라이언'
잔고_b = 1000
잔고_b = 입금하기(잔고_b, 100)

# 연습문제 2 - 클래스
class 계좌:
    def 개설하기(객체, 이름, 입금액):
        객체.이름 = 이름
        객체.입금액 = 입금액

    def 입금하기(객체, 이름, 입금액):
        객체.이름 = 이름
        객체.잔고 = 객체.잔고 + 입금액

    def 출력하기(객체):
        print("-" * 20)
        print(f"{객체.이름}님 잔고는 {객체.잔고} 원 입니다") # f string 사용하는 것 권요
        print("-" * 20)

a = 계좌()
계좌.개설하기(a, '라이언', 1000)
계좌.입금하기(a, 100)

b = 계좌()
계좌.개설하기(b, '어피치', 1000)
계좌.입금하기(b, 100)

##### 클래스 생성자
# 연습문제 - 사람 클래스 정의
class 사람:
    def __init__(self, 이름, 생년월일, 성별):
        self.이름 = 이름
        self.년 = 생년월일[:4]
        self.월 = 생년월일[4:6]
        self.일 = 생년월일[6:]
        self.성별 = 성별
    def 정보출력(self):
        print(f"{self.년}년")
        print(f"({self.성별}) {self.이름}")

첫째 = 사람("유종훈", "19860302", "남")
첫째.정보출력()


# 예제1 - 나열 함수
def f(a):
    a = 100

a = 10
f(a)
print(a) # 100이 아닌, 10 출력
         # f(a)의 a는 지역변수로, 함수가 종료되면 메모리에서 삭제됨

# 예제1 - 메서드 사용
class 사람:
    def f(self):
        self.alive = 1

def test(a):
    a.f()

a = 사람()
test(a)
a.alive # a = 1 출력


# 예제2
class 자동차:
    def __init__(self, brand):
        self.brand = brand

c0 = 자동차('삼성')
c1 = 자동차('현대')

print(c0.brand, c1.brand) # (1) 그냥 print 하기

def 비교하기(c0, c1): # (2) 함수 사용하기
    # c0와 c1은 자동차 객체입니다.
    # 두 객체를 입력받아 정보를 비교/출력합니다.
    print(c0.brand, c1.brand)
비교하기(c0, c1)

class 바퀴: # (3) 바퀴 class도 추가해보기
    def __init__(self, brand):
        self.brand = brand
class 자동차:
    def __init__(self, brand):
        self.brand = brand
        self.front = 바퀴('한국')
        self.rear = 바퀴('미국')

c0 = 자동차('삼성')
c1 = 자동차('현대')

print(c0.brand)
print(c0.front.brand) # c0.front만 하면 바퀴('한국')이 출력되므로 바퀴('한국').brand를 출력하는 것.


##### 클래스 상속
# (1) 에러O
class 보병:
    def __init__(self):
        self.speed = 5
        self.size = 3

class 마린:
    def __init__(self):
        self.attack = 3

a = 마린()
print(a.attack) # 마린의 attack은 출력되나
print(a.speed) # speed는 없으므로 error남

#(2) 에러X
class 마린(보병):
    def __init__(self):
        super().__init__()
        self.speed = 3
    
a = 마린()
print(a.speed)

#









