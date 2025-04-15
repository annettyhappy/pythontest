#리스트 데이터 추가

# numbers=[1,2,3,4,5]
# numbers.append(6)
# print(numbers)
# numbers.insert(2,7)
# print(numbers)

#리스트 데이터 삭제
# numbers=[1,2,3,4,4,5]
# del numbers[2]
# print(numbers)
# numbers.pop(1)
# print(numbers)
# numbers.pop()
# print(numbers)
# numbers.remove(4)
# print(numbers)

#리스트의 정렬
# numbers=[7,3,28,10,9]
# numbers.sort()
# print(numbers)
# numbers=[7,3,28,10,9]
# numbers.sort(reverse=True)
# print(numbers)

#특정 데이터 인덱스 찾기
# numbers=[3,1,3,6,1]
# print(numbers.index(1))
# print(numbers.index(9))

#특정 데이터 갯수 찾기
# numbers=[3,1,3,6,1]
# print(numbers.count(1))

#리스트 뒤집기
# numbers=[3,1,3,6,1]
# numbers.reverse()
# print(numbers)

#연습문제1
# li=[]
# n=0
# while n <5:
#     item = input("물건? ")
#     li.append(item)
#     print(li)
#     n+=1

#연습문제2
# numbers=[1,2,3,4,5]
# numbers.pop()
# print(numbers)
# numbers=[1,2,3,4,5]
# if len(numbers)/2 ==0:
#     numbers.pop((len(numbers)//2)+1)
# else:
#     numbers.pop((len(numbers)//2))
# print(numbers)
#
# #연습문제3
# li=['배낭','나침반','텐트','무전기','나침반','배낭']
# for i in range(len(li)):
#     m = li.count(li[i])
#     if m>1:
#         print(li[i])


#연습문제4
# li=[]
# n=0
# while n<10:
#     score=int(input("성적? "))
#     li.append(score)
#     n+=1
# li.sort()
# print(li)
# li.reverse()
# print(li[0:3])

#연습문제5??
# li=[6,2,3,4,1,6,5]
# li2=[6,2,3,4,1,6,5]
# li2.sort()
# print(li.index(li2[0]))
# print(li.index(li2[-1]))
# li[4]=li[0]
# print(li)




#도전문제1(리스트 정렬 삽입)
# li=[]
# n=0
# while n<10:
#     number=int(input("숫자? "))
#     li.append(number)
#     li.sort()
#     print(li)
#     n+=1

#도전문제2(리스트 최대값 삭제하기)
li=[10,293,29,293,50,60]
n = 0
for i in li:
    if n < i:
        n = i
while n in li:
    li.remove(n)
print(li)








#2차원 리스트
# numbers=[[0,1],[2,3],[4,5]]
# print(numbers[0])
# print(numbers[0][1])
# print(numbers[2][0])
# numbers[0][1]=6
# print(numbers)

#다차원리스트
# numbers=[[[0,0],[1,1]],[[3,3],[4,4]]]
# print(numbers[0][0][0])
# numbers[0][0][0]=5
# print(numbers[0][0])

#다차원 리스트함수
# numbers=[[0,1],[2,3]]
# numbers[1].append(4)
# print(numbers)

# numbers=[[0,1],[2,3]]
# numbers[1].pop()
# print(numbers)
# print(numbers[1].count(2))
# numbers[0].remove(0)
# print(numbers)

#연습문제1
# li1=[1,2,3]
# li2=[4,5,6]
# li3=[7,8,9]
# li4=[]
# li4.append(li1)
# li4.append(li2)
# li4.append(li3)
# print(li4)

# #연습문제2
# li=[[9,10,4],[4,6,7],[2,3,8]]
# n=0
# for i in li:
#     n+=i[0]
# print(n)


#연습문제3
# li=[[9,10,4],[4,6,7],[2,3,8]]
# for i in range(len(li)):
#     li[i].reverse()
# print(li)

#연습문제4
# li=[[9,10,4],[4,6,7],[2,3,8]]
# n=0
# for i in range(len(li)):
#     m=li[i]
#     for j in range(len(m)):
#         n+=m[j]
# print(n)



#연습문제5
# li=[[9,10,4],[4,6,7],[2,3,8]]
# n=0
# for i in range(len(li)):
#     m=li[i]
#     if i%2==0:
#         n+=m[0]
#         n+=m[2]
#     else:
#         n+=m[1]*2
# print(n)

#연습문제6
# li=[]
# numbers=[4,1,3,7,5,2,4,7,8]
# for i in range(3):
#     temp =[]
#     for j in range(3):
#         temp.append(numbers[i + (j * 3)])
#     li.append(temp)
# print(li)




#연습문제7
# li=[[9,10,4],[4,6,7],[2,3,8]]
# li2=[]
# m=len(li)
# n=len(li[0])
# li2.append(m)
# li2.append(n)
# print(li2)

#연습문제8
# li=[[9,10,4],[4,6,7],[2,3,8]]
# n=0
# for i in range(len(li)):
#     m=li[i]
#     n+=m[1]
# print(n)

#연습문제9
li=[]
numbers=[[9,10,4],[4,6,7],[2,3,8]]





#1번 문제
# li=[]
# number=int(input(" 입력:"))
# for i in range(number):
#     temp =[]
#     for j in range(i+1):
#         temp.append(j + 1)
#     li.append(temp)
#
# print(li)

#3번 문제
# li=[]
# for i in range(5):
#     temp=[]
#     for j in range(5):
#         temp.append((i*5)+(j+1))
#     li.append(temp)
# print(li)


# answer=[]
# n=12345
# m=0
# for i in str(n):
#     while m==len(str(n)):
#         answer+=[i]
#         m+=1
# print(answer)

