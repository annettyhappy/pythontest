#연습문제1
# price=int(input("Total Price? " ))
# money=int(input("Money? " ))
# print("*"*7," Receipt ","*"*7)
# print("Total Price: ",price)
# print("Money: ",money)
# tax=price*0.1
# print("Tax: ",tax)
# print("Change: ",money-(price+tax))

#연습문제2
# r=int(input("Radius? "))
# vol=4/3*(3.14*(r**3))
# print("Sphere Volume: ",vol)

#연습문제3
# f=float(input("Temperature(F): "))
# c=5/9*(f-32)
# print("F: ",f," => ","C: ",c)

#연습문제4
# l=int(input("Length(Km): "))
# m=(1/1.609)*l
# print("km: ",l,"=>","mile: ",m)

#연습문제5
# width=int(input("넓이: "))
# length=int(input("길이: "))
# ext=width*length
# print("면적: ",ext)

#연습문제6
# m=int(input("M? "))
# n=(m//4)+1
# print("필요한 생수통은 "+str(n)+"개 입니다.")


# #Boolean
# a = True
# print(a)
# b = False
# print(b)

#compare
# checker = (1==2)
# print(checker)
# a = 20
# b = 15
# c = (a==b)
# print(a,"==",b,":",c)
# c = (a!=b)
# print(a,"!=",b,":",c)
# c=(a>b)
# print(a,">",b,":",c)
# c=(a<b)
# print(a,"<",b,":",c)
# c=(a>=b)
# print(a,">=",b,":",c)
# c=(a<=b)
# print(a,"<=",b,":",c)

#logic
# a=True
# b=False
# print(a and b)
# x=2==3
# y=4>=5
# print(x or y)
# a=5!=1
# b=4<3
# print(a or b)
# c=3==3
# print(not c)

#logic2
# a=True
# b=False
# c=True
# print(a and b or c)
#
# a=True
# b=False
# c=True
# print(a or (b and c))

#연습문제1
# number = int(input("숫자? "))
# print("짝수? ",number/2==0)

#연습문제2
# kor = int(input("국어 점수: "))
# math = int(input("수학 점수: "))
# eng = int(input("영어 점수: "))
# ave = float((kor+math+eng)/3)
# print("평균 점수: ",ave)
# print("합격 여부: ",ave >=40)

#연습문제3
# rand=int(input("숫자: "))
# print("한 자리 수?",rand<10)

#연습문제4
# ques=input("숫자? ")
# print("-"*4," 출력 결과 ","-"*4)
# print("이번 랜덤 숫자는: ",number," 입니다.")
# print("결과: ",ques==number)

#연습문제5

#연습문제6
# num_1 = int(input("숫자: "))
# print("결과: ",num_1%3  ==0 or num_1%5==0)
# num_2 = int(input("숫자: "))
# print("결과: ",num_2%3 ==0 or num_2%5==0)

#문자열
# a="Hello"
# b="Tony"
# times =5
# print(a+b)
# print(a*times)

#연습문제1
# snake="pithon"
# n_snake=snake[0:1]+"y"+snake[2:]
# print(n_snake)

#연습문제2
b="bloc"

# new_b=b+"k"
# print(new_b)

#연습문제3
# h="Hello"
# new_h="h"+h[1:]
# print(new_h)

#연습문제4
# words = "I want to take a picture"
# print("picture" in words)

#연습문제5
# words = "I love adventure"
# print(len(words))
# print(words[-2:])

# 연습문제6
# word_1 = input("단어? ")
# print(len(word_1)%5==0)
# word_2 = input("단어? ")
# print(len(word_2)%5==0)

#연습문제1
# li=[1,2,3,4,5]
# li[4]=20
# print(li)
# print(li[2])

#연습문제2
# numbers=list(input("리스트입력 "))
# print(numbers)
# loc=len(numbers)//2
# print(numbers[loc])

#연습문제3
# li=[11,22,33,44,55]
# print(li[0:5:2])
# print(li[1:4])
# print(li[1:4:2])

#연습문제4
# li=[50,60,70,80,90,100]
# print(100 in li)
# print(200 in li)
# li[0]=200
# print(li)
# print(200 in li)
# print(50 in li)
# print(30 not in li)
# print(50 not in li)

#연습문제5
# list1=list(input("리스트 "))
# list2=list(input("리스트 "))
# print(list1+list2)

#연습문제6
# numbers=[1]
# print(numbers*10)

#연습문제7
# li=[0,0,0]
# kor= int(input())
# li[0] = kor
# math=int(input())
# li[1] = math
# eng=int(input())
# li[2] = eng
# print(li)
# print("하위권? ",0 in li or (li[0]+li[1]+li[2])/3<50)
# kor= int(input())
# li[0] = kor
# math=int(input())
# li[1] = math
# eng=int(input())
# li[2] = eng
# print(li)
# print("하위권? ",0 in li or (li[0]+li[1]+li[2])/3<50)

#연습문제8
# height=[160,165,170,155,-1]
# print(-1 in height)



