# try:
#     age = int(input("please enter your age: "))
# except:
#     print("wrong")

"""try:
    num1 = int(input("please enter num1: "))
    num2 = int(input("please enter num2: "))

    result = num1 / num2
    print(result)
except ValueError:
    print("please enter num!")
except ZeroDivisionError:
    print("除数can not zero!")

else:
    print("result is: ",result)

finally:
    print("process end")"""

# with open("test.txt","r",encoding="utf-8") as f:
#     content = f.read()
#     print(content)

# with open("test.txt","r",encoding="utf-8") as f:
#     lines = f.readlines()
    

# for line in lines:
#     print(line.strip())

"""with open("student.txt","w",encoding="utf-8") as f:
    f.write("hello")

with open("student.txt","a",encoding="utf-8") as f:
    f.write(" jack")

with open("student.txt","r",encoding="utf-8") as f:
    content = f.read()
    print(content)"""

# try:
#     num1 = int(input("please enter num1: "))
#     num2 = int(input("please enter num2: "))
#     result = num1 / num2
#     print(result)
# except ValueError:
#     print("num is wrong!")
# except ZeroDivisionError:
#     print("除数不能为0!")
# else:
#     print("result is: ",result)
# finally:
#     print("process end!")

"""def calculate():
    try:
        num1 = int(input("please enter num1: "))
        num2 = int(input("please enter num2: "))
        print(num1 / num2)
    except ValueError:
        print("wrong")
    except ZeroDivisionError:
        print("除数不为0")

calculate()"""

"""while True:
    try:
        age = int(input("请输入年纪： "))
        print("enter success!")
        break
    except:
        print("wrong enter please enter again!")"""

"""try:
    with open("student.txt","r",encoding="utf-8") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
        print("tile is none")"""
students = []

def save_students():
    try:
        with open(
            "student.txt",
            "w",
            encoding="utf-8"
        )as f:
            f.write(str(students))
    except Exception as e:
        print("保存失败！")
        print(e)

def load_students():
    global students
    try:
        with open(
            "student.txt",
            "r",
            encoding="utf-8"
        )as f:
            content = f.read()
            students = eval(content)
            print("读取成功")
    except FileExistsError:
        print("文件不存在")
    except Exception as e:
        print("读取失败")
        print(e)