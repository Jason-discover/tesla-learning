# age = int(input("How old are you?"))

# if age >=18:
#     print("You are an adult.")
# else:
#     print("Child")
# age = int(input("please enter your age: "))
# if age >=18:
#     print("You can drive")
# else:
#     print("you cannot drive")
# number = int(input("please enter number: "))
# if number> 0:
#     print("psoitive")
# else:
#     print("not positive")
age = int(input("please enter your age: "))
if age <=0:
    print("Invalid age")
elif age >=60:
    print("Senior")
elif age >=18:
    print("Adult")
elif age >=13:
    print("Teenager")
else:
    print("Child")