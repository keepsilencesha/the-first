from interface import admin_interface, common_interface
from lib import common

admin_info = {
    'name': None
}


def register():
    print('管理员注册')
    while True:
        name = input('请输入用户名(返回请按q)：').strip()
        if name == 'q': break
        password = input('请输入密码：').strip()
        conf_password = input('请确认密码：').strip()
        if password == conf_password:
            flag, msg = admin_interface.register_interface(name, password)
            if flag:
                print(msg)
                break
            else:
                print(msg)


def login():
    print('登录')
    while True:
        name = input('请输入用户名').strip()
        password = input('请输入密码').strip()
        flag, msg = common_interface.login_interface('admin', name, password)
        if flag:
            admin_info['name'] = name
            print(msg)
            break
        else:
            print(msg)


@common.login_interface('admin')
def create_school():
    print('创建学校')
    while True:
        name = input('请输入学校名称：').strip()
        address = input('请输入学校地址').strip()
        flag, msg = admin_interface.create_school_interface(admin_info['name'], name, address)
        if flag:
            print(msg)
            break
        else:
            print(msg)


@common.login_interface('admin')
def create_teacher():
    print('创建老师')
    while True:
        name = input('请输入老师名称：').strip()

        flag, msg = admin_interface.create_teacher_interface(admin_info['name'], name)
        if flag:
            print(msg)
            break
        else:
            print(msg)


@common.login_interface('admin')
def create_course():
    print('创建课程')
    while True:
        school_list = common_interface.get_all_school_interface()
        if school_list:
            for i, school in enumerate(school_list):
                print('%s:%s' % (i, school))
            choice = input('请选择学校').strip()
            if choice.isdigit():
                choice = int(choice)
                if choice >= len(school_list): continue

                name = input('请输入课程名称：').strip()

                flag, msg = admin_interface.create_course_interface(admin_info['name'], name,school_list[choice])
                if flag:
                    print(msg)
                    break
                else:
                    print(msg)


service = {

    '1': register,
    '2': login,
    '3': create_school,
    '4': create_teacher,
    '5': create_course
}


def run():
    while True:
        print('选课系统')
        print('''
        0、退出
        1、注册
        2、登录
        3、创建学校
        4、创建老师
        5、创建课程

        ''')
        choice = input('请选择：').strip()
        if choice == '0':
            admin_info['name']=None
            break
        if choice in service:
            service[choice]()
