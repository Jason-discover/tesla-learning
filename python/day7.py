# age = int(input("please enter your age: "))


# if age >=60 or age <18:
#     print("You have discount.")

# age = int(input("please enter your age: "))
# money = int(input("please enter your money: "))
# if age <0 :
#     print("Invalid age!")
# elif age <18:
#     print("you have discount!")
# elif money >= 100:
#     print("Welcome!")
# else:
#     print("sorry you can not buy ticket")

age = int(input("please enter your age: "))
money = int(input("please enter your money: "))
if age < 0:
    print("Invalid")
elif age <=12:
    print("Free")
elif age <=17:
    print("Half price")
# if money >= 100 and age >=18:
#     print("Buy successfully!")
# if money <100 and age >=18:
#     print("Not enough money")
elif money >=100:
    print("Buy successfully!")
else :
    print("Not enough money!")
"""代码走到这里的时候 age已经>=18了 因此只需执行money大于100的情况即可
18岁之后 钱大于100即购买成功 钱少于100则钱不够"""