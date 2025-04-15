#튜플 다루기
# t1=(1,2,3,4)
# print(t1[0])
# print(t1[3])
# print(t1[1:])
# t1=(1,2)
# t2=(3,4)
# print(t1+t2)
# print(t2*3)
# print(len(t1))

#세트 입력
# s1=set([1,2,3])
# print(s1)
# s2=set("Hello")
# print(s2)

#교집합, 합집합, 차집합 구하기
# s1=set([1,2,3,4,5,6])
# s2=set([4,5,6,7,8,9])
# print(s1&s2)
# print(s1.intersection(s2))
# print(s1 | s2)
# print(s1.union(s2))
# print(s1-s2)
# print(s2-s1)
# print(s1.difference(s2))
# print(s2.difference(s1))

#세트 관련 함수
# s1=set([1,2,3])
# s1.add(4)
# print(s1)
# s1=set([1,2,3])
# s1.update([4,5,6])
# print(s1)
# s1=set([1,2,3])
# s1.remove(2)
# print(s1)

#연습문제1
# s1=(1,2,3,4,5,6,7,8,9,10)
# print(s1)

#연습문제2
# s1=(1,2)
# s2=(3,4)
# s3=(5,6)
# li=[]
# li.append(s1)
# li.append(s2)
# li.append(s3)
# print(li)

#연습문제3
# li=[(1,2),(3,4),(5,6)]
# li[0]=(7,8)
# print(li)

#연습문제4

# n=0
# s1=set([])
# while n<5:
#     number = int(input("숫자? "))
#     s1.add(number)
#     n+=1
# print(s1)

#연습문제5
# s1=set([])
# s2=set([])
# s1.update(['a','b','c'])
# s2.update(['c','d','e'])
# print(s1)
# print(s2)
# print(s1.intersection(s2))
# print(s1.union(s2))
# print(s2-s1)

#연습문제6
# s1=set([10,82,100])
# print(s1)
# s1.update([40,50,82])
# print(s1)
# s1.remove(82)
# print(s1)

