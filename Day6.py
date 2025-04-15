#딕셔너리
# phonebook={
#     "Tony": "01051420000",
#     "Jeffrey": "01044441111"
# }
# print(phonebook)
# phonebook["Nick"] = "01055552222"
# print(phonebook)
# del phonebook["Nick"]
# print(phonebook)
# phonebook.pop("Tony")
# print(phonebook)

#딕셔너리 데이터 추출
# grade = {"pey":10,"julliet":99}
# print(grade["pey"])
# print(grade["julliet"])

#키 리스트, 값 리스트
# phonebook={
#     "Tony": "01051420000",
#     "Jeffrey": "01044441111",
#     "Nick":"01055552222"
# }
# print(list(phonebook.keys()))
# print(list(phonebook.values()))

# #딕셔너리 멤버십
# phonebook={
#     "Tony": "01051420000",
#     "Jeffrey": "01044441111",
# }
# print("Tony" in phonebook)
# print("Nick" in phonebook)

#연습문제1
# people={"홍길동": 30,
#         "이순신": 45,
#         "강감찬": 32,
#         "이몽룡": 37}
# print(people)


#연습문제2
# menu={'아메리카노': 1900,
#       '카페모카': 3300,
#       '에스프레소': 1900,
#       '카페라떼': 2500,
#       '카푸치노': 2500,
#       '바닐라라떼': 2900}
#
# while True:
#     order = input("메뉴를 입력하세요: ")
#     if order in menu.keys():
#         print(menu[order],"원 입니다.")
#     else:
#         print("종료합니다.")

#연습문제3
# menu={'아메리카노': 1900,
#       '카페모카': 3300,
#       '에스프레소': 1900,
#       '카페라떼': 2500,
#       '카푸치노': 2500,
#       '바닐라라떼': 2900}
# print(list(menu.keys()))



#연습문제4
# number=int(input("숫자? "))
# dic={}
# for i in range(number):
#     dic[i+1] = (i+1)**2
# print(dic)

#연습문제5
# name=['Bob', 'Jeffrey', 'Tony', 'Casandra', 'Alex', 'Sophie', 'Tony', 'Sola', 'Merry', 'Bob']
# dic={}
# for i in name:
#     dic[i]=name.count(i)
# print(dic)

#연습문제6
# people={'Bob':2, 'Jeffrey':1, 'Tony':2, 'Casandra':1, 'Alex':1, 'Sophie':1, 'Sola':1, 'Merry':1}
# number=list(people.values())
# n=0
# for i in range(len(number)):
#     n+=number[i]
# print(n)

#5번문제
# icecream = {
#     "메로나": 600,
#     "돼지바": 700,
#     "브라보": 1800,
#     "월드콘": 1500,
#     "투게더":4500
# }
# price=list(icecream.values())
# n=0
# for i in price:
#     n+=i
# print(n)

#6번문제
coffee = {
    "아메리카노": 1900,
    "카페모카": 3300,
    "에스프레소": 1900,
    "카페라떼": 2500,
    "카푸치노": 2500,
    "바닐라라떼": 2900
}
n = 0
for i in coffee:
    if n < coffee[i]:
        n = coffee[i]




#7번 문제
# products = {
#     "지도":7000,
#     "나침반":3000,
#     "망원경":10000,
#     "물통":4000,
#     "껌":1000
# }
#
# for i in products:
#     products[i]*=1.1
# print(products)



#8번문제

products = {
    "지도":4,
    "나침반":2,
    "망원경":1,
    "물통":2,
    "껌":1
}

while True:
    item = input("물건의 이름은? ")
    if item not in products:
        break
    products[item] -= 1
    print(products[item])
    if products[item]==0:
        products.pop(item)
        print(products)
