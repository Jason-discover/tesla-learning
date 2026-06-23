# class Student:
#     pass
# stu1 = Student()
# print(stu1)

"""class Student:
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
stu1 = Student("张三",18,90)
print(stu1.name)
print(stu1.age)
print(stu1.score)"""

"""class Student:
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score"""
    
"""    def show_info(self):

        print(
            self.name,
            self.age,
            self.score
        )
stu1 = Student("张三",18,90)
stu1.show_info()
"""
"""class Student:
    def __init__(self,name,age,score):
        
        self.name = name,
        self.age = age,
        self.score = score

    def update_score(self,new_score):

        self.score = new_score
stu1=Student("张三",18,90)
stu1.update_score(95)
print(stu1.score)"""

class student:
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
    def show_info(self):
        print(
            f"姓名：{self.name}"
        )
        print(
            f"年龄：{self.age}"
        )
        print(
            f"分数：{self.score}"
        )
    def update_score(self,new_score):
        self.score = new_score

stu1 = student(
    "张三",
    18,
    90
)
stu1.show_info()
stu1.update_score(100)
stu1.show_info()