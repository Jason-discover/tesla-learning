"""def is_spam(message):
    message = message.lower()
    if "free" in message or "buy" in message:
        return True
    else:
        return False

def main():
    messages = [
        "FREE money now!!!",
        "Hello how are you",
        "buy cheap iphone",
        "Let's go to school"
    ]
    spam_count = 0
    normal_count = 0
    for message in messages:
        if is_spam(message):
            print(message,"=> Rubbish")
            spam_count += 1
        else:
            print(message,"=> Normal")
            normal_count += 1  
    print("Rubbish",spam_count)
    print("Normal",normal_count)

main()"""

students = {
    "Tom":85,
    "Rose":92,
    "Jason":78,
    "Mary":95
}

def show_all():
    for name,score in students.items():
        print(name,score)
        
            


def show_good_students():
    for name,score in students.items():
        if score >= 90:
            print(name,score)
            


def add_student():
        name = input("请输入姓名：")
        score = int(input("请输入成绩： "))
        students[name] = score
        print("添加成功")
        


def menu():
    print("======学生管理系统======")
    print("1.查看全部学生")
    print("2.添加学生")
    print("3.查看优秀学生")
    print("4.退出系统")

while True:
    menu()

    choice = input("请输入功能编号：")

    if choice == "1":
        show_all()
    elif choice == "2":
        add_student()
    elif choice == "3":
        show_good_students()
    elif choice == "4":
        print("系统退出")
        break
    else:
        print("输入错误,请重新输入")
