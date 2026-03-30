# 欢迎界面
def init():
    print(" 欢迎使用学生管理系统(v1.0)         ")
    print("====================================")
    print("=        1. 注册学生管理系统       =")
    print("=        2. 登录学生管理系统       =")
    print("=        3. 增加新的学生           =")
    print("=        4. 删除学籍记录           =")
    print("=        5. 修改学生信息           =")
    print("=        6. 查找学生信息           =")
    print("=        7. 关于本系统             =")
    print("=        8. 退出系统               =")
    print("====================================")


def Login(user_name:str, user_password:str, user_age:int, user_class:int, user_grade:int) -> dict:
    user = {}
    user["user_name"] = user_name
    user["user_password"] = user_password
    user["user_age"] = user_age
    user["user_class"] = user_class
    user["user_grade"] = user_grade

def Exit(command:str) -> bool:
    if command == "8":
        return False
    else:
        return True