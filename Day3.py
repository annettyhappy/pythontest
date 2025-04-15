#if문
# name=input("모험가의 이름은?")
# if name == "Tony":
#     print("내 이름은 Tony 입니다.")

#elif문
# name=input("모험가의 이름은?")
# if name == "Tony":
#     print("내 이름은 Tony 입니다")
# elif name == "Jeffrey":
#     print("내 이름은 Jeffrey 입니다.")

#else문
# name = input("모험가의 이름은?")
# if name == "Tony":
#     print("내 이름은 Tony 입니다.")
# elif name == "Jeffrey":
#     print("내 이름은 Jeffrey 입니다.")
# else:
#     print("나는 다른 이름을 가졌다.")

# #여러 개의 elif
# destination = input("모험의 목적지?")
# if destination == "Seoul":
#     print("서울로 가자.")
# elif destination == "New York":
#     print("뉴욕으로 가자.")
# elif destination == "London":
#     print("런던으로 가자.")
# else:
#     print("다른 곳으로 가자.")

#if문과 elif 문의 차이
# fruit = "apple"
# if fruit == "apple":
#     print("이것은 사과입니다.")
# elif fruit == "apple":
#     print("이것은 사과입니다.")

# fruit = "apple"
# if fruit == "apple":
#     print("이것은 사과입니다.")
# if fruit == "apple":
#     print("이것은 사과입니다.")

#빈칸 띄우기
# name = "Tony"
# if name == "Tony":
#     print("나의 이름은 Tony 입니다")
# print("이 문장은 if와 상관없이 실행됩니다.")

#중첩 if문
# name = "Tony"
# age = 17
# if name == "Tony":
#     if age > 15:
#         print("나는 토니이고, 나이는 15살 이상입니다.")

# #연습문제1
# price=int(input("물건가격? "))
# if price > 5000:
#     print("비싸네")
# elif price<=2999:
#     print("안비싸네")
# else :
#     print("싸네")

# # #연습문제2
# number=int(input("숫자? "))
# if number%2==0:
#     print("짝수")
# elif number%2==1:
#     print("홀수")

# # #연습문제3
# number = int(input("숫자? "))
# if number > 0:
#     print(number)
# elif number <0:
#     print(number*-1)

# # #연습문제4
# num=int(input("분자? "))
# den=int(input("분모? "))
# if den == 0:
#     print("나눌 수 없습니다")
# else:
#     print(float(num/den))

# # 연습문제5
# num1=int(input("숫자1? "))
# num2=int(input("숫자2? "))
# num3=int(input("숫자3? "))
# if num1>num2 and num1>num3:
#     print("최대값 ",num1)
# elif num2>num1 and num2>num3:
#     print("최대값 ",num2)
# elif num3>num1 and num3>num2:
#     print("최대값 ",num3)
# if num1 < num2 and num1 < num3:
#     print("최소값 ", num1)
# elif num2 < num1 and num2 < num3:
#     print("최소값 ", num2)
# elif num3 > num1 and num3 > num2:
#     print("최소값 ", num3)

# #연습문제6
# year = int(input("Year? "))
# if year%4==0 and year%100!=0:
#     print("윤년 O")
# elif year%400==0:
#     print("윤년 O")
# else:
#     print("윤년 X")



#while 반복문
# age = 10
# while age <20:
#     print(age)
#     age+=1
# print("Stop")

#if문과 같이 쓰기
# year = 2004
# while year <2022:
#     if year ==2020:
#         print("2020 년은 코로나 때문에 최악이야!")
#     else:
#         print(year,"년 좋아")

#코드 무한 반복하기
# while True:
#     print("HI")

#break
# count=0
# while True:
#     count=int(input("전세계 국가 수를 맞춰보세요."))
#     if count == 195:
#         print("정답!")
#         break
#
# count=0
# while count != 195:
#     count=int(input("전세계 국가 수를 맞춰보세요."))
# print("정답!")

#continue
# i=0
# while i<100:
#     i+=1
#     if i%2==1:
#         continue
#     print(i)

#while안에 while 반복
# i=1
# j=1
# while i <4:
#     j=1
#     while j<4:
#         print(i,j)
#         j+=1
#     i+=1

#연습문제1
# i = 10
# while i > 0:
#     print(i)
#     import time
#     time.sleep(1)
#     i -=1


#연습문제2
# n = 1
# val=0
# while n <=10:
#     val+=int(input("입력 값 "+str(n)+":"))
#     n+=1
# print("평균값: ",val/n)


#연습문제3
# greet=int(input("입력: "))
# n=1
# while n<=greet:
#     print("Hello")
#     n+=1

# #연습문제4
# number=1
# while number<129:
#     print(number)
#     number*=2

#연습문제5
# mul=int(input("몇 단? "))
# n=1
# while n<10:
#     cal=n*mul
#     print(str(n)+" * "+str(mul)+ " = "+str(cal))
#     n+=1

#연습문제6
# count=int(input("숫자?"))
# while count%3 !=0:
#         print("계속")
#         count = int(input("숫자?"))
# print("그만")

# #연습문제7?
# num = 1
# den = 2
# cal = 0
# while num <100:
#     cal+=num/den
#     num+=1
#     den+=1
#     cal-=num/den
#     num+=1
#     den+=1
# print(cal)

#연습문제8
# ast="*"
# n=0
# while n<5:
#     n+=1
#     print(ast*n)

#연습문제9
# ast="*"
# n=6
# while n<7:
#     n-=1
#     print(ast*n)
#     if n <2:
#         break


#연습문제10
# n=1
# m=1
# while n<10:
#     m=1
#     while m<10:
#         cal=n*m
#         print(str(n)+" * "+str(m)+ " = "+str(cal))
#         m+=1
#     n+=1


#리스트 반복
# li = [1,2,3,4,5]
# for i in li:
#     print(i)

#인덱스 반복
# print(list(range(10)))
# print(list(range(1,11)))
# print(list(range(1,11,2)))

# for i in range(4):
#     print(i)
# for i in range(1,4):
#     print(i)
# for j in range(5,1,-2):
#     print(j)

#break,continue
# for i in range(1,10):
#     if i ==5:
#         break
#     print(i)
# for i in range(1,10):
#     if i==5:
#         continue
#     print(i)

#for 반복문과 리스트 인덱스
# li = [4,1,10,3,7]
# for i in range(len(li)):
#     print(li[i])
# for i in li:
#     print(i)

# #중첩 반복문
# for i in range(3):
#     for j in range(3):
#         print(i,",",j)

#연습문제1
# for i in range(2,101,2):
#     print(i)

#연습문제2
# greet=int(input("몇번? "))
# for i in range(greet):
#     print("Hello")

#연습문제3
# li = [5,10,388,72,83,1]
# print(li)
# n=0
# for i in li:
#     n+=i
#
# print("합: ",n)

#연습문제4
# li=[3,2,9,5]
# print("리스트 ",li)
# for i in range(len(li)):
#     li[i]=li[i]*3
# print("변경된 리스트 ",li)

#연습문제5
# mul=int(input("몇단? "))
# for i in range(1,10):
#     cal=i*mul
#     print(i," * ",mul," = ",cal)

#연습문제6
# for i in range(1,10):
#     for j in range(1,10):
#         cal=i*j
#         print(i," * ",j," = ",cal)

#연습문제7
# ast=['*','*','*','*','*']
# n=1
# for i in range(len(ast)):
#     ast[i]=ast[i]*n
#     n+=1
#     if n>6:
#          break
#     print(ast[i])

#연습문제8
# ast=['*','*','*','*','*']
# n=5
# for i in range(len(ast)):
#     ast[i]=ast[i]*n
#     n-=1
#     if n<0:
#          break
#     print(ast[i])

#연습문제9
li=[18,28,37,28,18]
for i in range(len(li)):
    print(li[4-i])






