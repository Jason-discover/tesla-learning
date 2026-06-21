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
        if name in students:
            print("该学生已存在")
        else:
            score = int(input("请输入成绩： "))
            students[name] = score    
            print("添加成功")
        
def search_student():
    name = input("请输入姓名： ")
    if name in students:
        print(name, "成绩： ",students[name])
    else:
        print("没有找到该学生")

def delete_student():
    name = input("请输入要删除的学生： ")
    if name in students:
        del students[name]
        print("删除成功")
    else:
        print("学生不存在")

def update_score():
    name = input("请输入姓名： ")
    if name in students:
        score = int(input("请输入新成绩： "))
        students[name] = score
        print("修改成功")
    else:
        print("学生不存在")


def menu():
    print("======学生管理系统======")
    print("1.查看全部学生")
    print("2.添加学生")
    print("3.查看优秀学生")
    print("4.查询学生")
    print("5.修改成绩")
    print("6.删除学生")
    print("7.退出系统")

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
        search_student()
    elif choice == "5":
        update_score()
    elif choice == "6":
        delete_student()
    elif choice == "7":
        print("系统已退出")
        break
    else:
        print("输入错误,请重新输入")
    
    





