from time import sleep

users = {
    "user_name": [
        "Admin"
    ],
    "user_password": [
        "114514"
    ]
}

def init_front_register():
    print("           ·欢迎使用本系统·                  ")
    print("=          1.登入系统                       =")
    print("=          2.注册账户                       =")
    print("=          3.退出系统                       =")

def init_after_register():
    print("           ·请选择功能·                          ")
    print("=          1.修改账户信息                       =")
    print("=          2.查看账户信息                       =")
    print("=          3.清空账户信息                       =")
    print("=          4.注销该账户                         =")
    print("=          5.退出账户                           =")

def register():
    print("请设置用户名：", end='')
    user_name = input()
    print("请设置用户密码：", end='')
    user_password = input()
    new_user = User(user_name, user_password)
    users["user_name"].append(new_user.get_user_name())
    users["user_password"].append(new_user.get_user_password())

def login():
    print("请输入用户名：", end='')
    user_name = input()
    print("请输入用户密码：", end='')
    user_password = input()
    if (user_name in users["user_name"]) and (user_password in users["user_password"]):
        print("登入账户成功!")
    else:
        print("账户名或密码错误!")


def exit_system():
    print("已退出系统")
    sleep(0.5)
    print("已退出系统")





class User:
    def __init__(self, user_name, user_password):
        self.user_name = user_name
        self.user_password = user_password
    def get_user_name(self):
        return self.user_name
    def get_user_password(self):
        return self.user_password
    def set_user_name(self, new_user_name):
        self.user_name = new_user_name
    def set_user_password(self, new_user_password):
        self.user_password = new_user_password
    def console_user_info(self):
        print(f"User name:{self.user_name}, User password:{self.user_password}")

while True:
    init_front_register()
    cmd = input(">>> ")
    match cmd:
        case '1':
            login()
        case '2':
            register()
        case '3':
            exit_system()
            break