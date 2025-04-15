# num = 4/0

# l = [1,2,3]
# print(l[3])

# try:
#     num = 4/0
# except:
#     print("Error!")

# try:
#     num = 4/0
# except ZeroDivisionError:
#     print("Division by zero")

# try:
#     num = 4/0
# except ZeroDivisionError as e:
#     print(e)

# try:
#     num = 4/0
#     l = [1,2,3]
#     print(l[4])
# except ZeroDivisionError as e1:
#     print(e1)
# except IndexError as yftdetr:
#     print(yftdetr)

class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다"

def say_nick(nick):
    if nick =='바보':
        raise MyError()
    print(nick)



try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)

./새폴더/test
../새폴더/test