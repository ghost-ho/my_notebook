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



# 用户列表
USERs = {}
def LOGIN(USER_NAME:str, USER_PASSWORD:str, USER_AGE:int) -> dict:
    USER = {
        "USER_NAME": USER_NAME,
        "USER_AGE": USER_AGE,
        "USER_PASSWORD": USER_PASSWORD
    }
    USERs.update(USER)

def EXIT(command:str) -> bool:
    if command == "8":
        return False
    else:
        return True