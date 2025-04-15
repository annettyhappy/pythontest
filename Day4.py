#함수의 정의
# def print_hello():
#     print("Hello")
# print_hello()

#함수의 인자
# def print_hello(name):
#     print("Hello! ",name)
# print_hello("Tony")

#함수의 출력
# def add(x,y):
#     return x+y
# result=add(3,5)
# print(result)

#변수 유효 범위
# x = "this is x"
# def word():
#     w="Hello"
# print(w)
# print(x)
# word()

#변수 유효 범위
# def print_name(name):
#     print(name)
# name="Tony"
# print_name(name)

# def who_love(n1,n2):
#     print("I love",n1,"and",n2)
# n1="Tony"
# n2="Jeffrey"
# who_love(n2,n1)

#연습문제1
# name = input("이름을 입력하세요: ")
# def greeting(a):
#     print("Hi, I am", a)
# greeting(name)

#연습문제2
# def get_length(a):
#     return len(a)
# result=get_length([1,2,3])
# print(result)

#연습문제3
# mi=int(input("거리(mi)를 입력하세요: "))
# def mile_to_km(a):
#     return a*1.66
# result=mile_to_km(mi)
# print(result," km")

#연습문제4
# kg=int(input("몸무게(kg)를 입력하세요: "))
# m=float(input("키(m)를 입력하세요: "))
# def get_bmi(a,b):
#     return a/(b**2)
# result=get_bmi(kg,m)
# print(result)

#연습문제5
# ind=int(input("몇 번째 인덱스에 있는지 찾을 숫자를 입력하세요: "))
# li=[10,30,50,40,2]
# def get_index(a):
#     n=0
#     for i in li:
#         n+=1
#         if i == a:
#             break
#     return n-1
# result=get_index(ind)
# print(result)


#연습문제6
# li=[14,15,18,20]
# li2=[23,52,7,73,65,43]
# def get_sum(a):
#     n = 0
#     for i in range(len(a)):
#         n += a[i]
#     return n
# print(get_sum(li))
# print(get_sum(li2))

#게임 만들기
# print("="*20)
# print("10번안에 1에서 100사이의 숫자 맞추기 게임")
# print("="*20)
# def game():
#     import random
#     number2 = random.randint(1,100)
#     n=1
#     while True:
#         number = int(input("숫자를 입력 하세요: "))
#         if number == number2 :
#             print("게임에서 이겼습니다.")
#             return
#         else:
#             if number>number2:
#                 print(str(n)+"번 시도, 이 숫자보다 작습니다")
#             else:
#                 print(str(n) + "번 시도, 이 숫자보다 큽니다")
#             n+=1
#             if n>10:
#                 print(str(n-1)+"번의 기회를 모두 사용하였습니다.")
#                 print("게임에서 졌습니다.")
#                 break
#
#
# while True:
#     game()
#     jud = input("게임을 재시작 하겠습니까? (y/n)")
#     if jud == "n":
#         break



#가위 바위 보 게임
# print("="*20)
# print("가위 바위 보 3승 대결!")
# print("="*20)
# def game():
#     import random
#     number2 = random.randint(1,3)
#     n=1
#     m=0
#     c=0
#     while True:
#         number = int(input("1.가위 2.바위 3.보 중 하나를 선택하세요(숫자만 입력가능): "))
#         while number not in [1,2,3]:
#             print("잘못 눌렀습니다.")
#             number = int(input("1.가위 2.바위 3.보 중 하나를 선택하세요(숫자만 입력가능): "))
#         if number == number2 :
#             print("비김!")
#             print("나:"+str(m)+"승 | "+"컴퓨터: "+str(c)+"승")
#         else:
#             if number>number2:
#                 print("나 승리!")
#                 m+=1
#                 print("나:"+ str(m)+"승"+" | "+"컴퓨터: "+str(c)+"승")
#             else:
#                 print("컴퓨터 승리!")
#                 c+=1
#                 print("나:" + str(m)+"승"+" | "+"컴퓨터: "+str(c)+"승")
#         n+=1
#         if m==3 or c==3:
#             if m > n:
#                 print("*"*20+"나의 승리!"+"*"*5)
#                 break
#             else:
#                 print("*"*20+"컴퓨터의 승리!"+"*"*5)
#                 break
# while True:
#     game()
#     jud = input("게임을 재시작 하겠습니까? (y/n)")
#     while jud != 'n' and jud != 'y':
#         #while jud not in ['n','y']:
#         print("y나 n만 입력하세요")
#         jud = input("게임을 재시작 하겠습니까? (y/n)")
#
#     if jud == "n":
#        break







