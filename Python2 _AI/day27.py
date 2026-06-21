
students = []


def add_student():
    name = input("请输入姓名： ")
    for student in students:
        if student["name"] == name:
            print("该学生已存在 他的信息是：")
            print(student)
            print("是否添加同名学生")
            Num = input("确认? 1为确认 其他取消")
            if Num == "1":
                name = input("请输入加标注的姓名： ")
                age = int(input("请输入年纪： "))
                score = int(input("请输入学生分数： "))
                student = {
                        "name":name,
                        "age":age,
                        "score":score
                            }
                students.append(student)
                print("      添加成功!      ")
            else:
                print("已取消")
            return
    age = int(input("请输入年纪： "))
    score = int(input("请输入学生分数： "))
    student = {
            "name":name,
            "age":age,
            "score":score
               }
    students.append(student)
    print("      添加成功!      ")


def show_students():
        if len(students) == 0:
            print("当前无学生信息 请添加")
            return
        for student in students:
            name = student["name"]
            age = student["age"]
            score = student["score"]
            print(f"姓名:{name},年纪:{age},分数:{score}")

def search_student():
    name = input("请输入姓名： ")
    for student in students:
        age = student["age"]
        score = student["score"]
        if student["name"] == name:
            print(f"姓名:{name},年纪:{age},分数:{score}")
            return
    print("      未找到该学生!      ")

def modify_student():
    name = input("请输入姓名： ")
    for student in students:
        if student["name"] == name:
            print("原成绩：",student["score"])
            new_score = input("请输入新成绩： ")
            student["score"] = new_score
            print("      修改成功!      ")
            return
        print("      未找到该学生!      ")
     
def delete_student():
    name = input("请输入姓名： ")
    for student in students:
        if  student["name"] == name:
            print("找到学生:")
            print(student)
            num = input("确认删除？(1确认,其他取消):")
            if num == "1":
                students.remove(student)
                print("      删除成功!      ")
            else:
                print("好的 取消删除操作")
            return
    print("      未找到该学生!      ")

def save_students():
    file = open("students.txt","w",encoding="utf-8")
    for student in students:
        text = f'{student["name"]},{student["age"]},{student["score"]}\n'
        file.write(text)
    file.close()
    print("      保存成功！      ")

def load_students():
    students.clear()
    file = open("students.txt","r",encoding="utf-8")
    lines = file.readlines()
    for line in lines:
        data = line.split(",")
        student = {
            "name":data[0],
            "age":int(data[1]),
            "score":int(data[2])
        }
        students.append(student)
    file.close()
    # print("读取成功！")
    
# save_students()
# load_students()
"""show_students()
add_student()
search_student()
modify_student()
delete_student()"""
load_students()


while True:


    print("1 添加学生")
    print("2 查看学生")
    print("3 查询学生")
    print("4 修改成绩")
    print("5 删除学生")
    print("6 保存数据")
    print("7 读取数据")
    print("0 退出系统")

    choice = input("请输入功能：")
    if choice == "1":
        add_student()
        print("\n\n")
    elif choice == "2":
        show_students()
        print("\n\n")
    elif choice == "3":
        search_student()
        print("\n\n")
    elif choice == "4":
        modify_student()
        print("\n\n")
    elif choice == "5":
        delete_student()
        print("\n\n")
    elif choice == "6":
        save_students()
        print("\n\n")
    elif choice == "7":
        load_students()
        print("\n\n")
    elif choice == "0":
        save_students()
        print("系统已退出")
        print("\n\n")
        break
    else:
        print("系统错误")
        print("\n\n")