# count = 1

# while count <= 5:
#     print("Hello")
#     count = count + 1
# number = 1
# while number <=10:
#     print(number)
#     number = number + 1
# password = int(input("please enter your password: "))
# while password == 123456:
#     print("Login success")
# else:
# #     print("wrong password")
# password = 123456
# while True:
#     input_password = int(input("please enter your password: "))
#     if input_password == password:
#         print("Login success")
#         break
#     else:
#         print("wrong password")
"""password = 123456
count = 1
while True:
    input_password = int(input("Please enter your password: "))
    if input_password != password:
        print("wrong password")
        count = count + 1
        if count == 4:
            break
    if input_password == password:
        print("Login success")
        break"""

password = 123456
count = 1
while True:
    input_password = int(input("Please enter your password: "))
    if input_password == 123456:
        print("Login success")
        break
    else:
        print("wrong password")
        count += 1
    if count == 4:
        print("Too many attempts")
        break