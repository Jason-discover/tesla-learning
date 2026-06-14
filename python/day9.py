# password = 123456
# while True:
#     int_password = int(input("Please enter you password: "))
#     if int_password == password:
#         print("Login success")
#         break
#     else:
#         print("Wrong")
"""password = 123456
count = 0
while True:
    int_password = int(input("Please enter your password: "))
    if int_password != password:
        print("Wrong")
        count += 1
    else :
        print("Login success")
        break
    if count >= 4:
        print("Account Locked")
        break"""

password = 123456
count = 3
print("You have 3 chances")
while True:
    int_password = int(input("Please enter your password: "))
    if int_password != password:
        count -= 1
        if count > 1 :
            print(f"Wrong! {count} chances left")
        else :
            print(f"Wrong! {count} chance left")
    else :
        print("Login success")
        break
    if count == 0:
        print("Account locked")
        break
