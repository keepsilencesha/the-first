from interface import student_interface, common_interface
from lib import common

student_info = {'name': None}


def register():
    print('注册学生')
    while True:
        name = input('请输入姓名:').strip()
        password = input('请输入密码').strip()
        conf_password = input('请确认密码').strip()
        if password == conf_password:
            flag, msg = student_interface.student_register_interface(name, password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('俩次密码不一致，请重新输入')


def login():
    print('登录')
    while True:
        name = input('请输入用户名').strip()
        password = input('请输入密码').strip()
        flag, msg = common_interface.login_interface('student', name, password)
        if flag:
            student_info['name'] = name
            print(msg)
            break
        else:
            print(msg)


@common.login_interface('student')
def choose_school():
    print('选择学校')
    while True:
        school_list = common_interface.get_all_school_interface()
        if school_list:
            for i, school in enumerate(school_list):
                print('%s:%s' % (i, school))
            choice = input('请选择学校').strip()
            if choice.isdigit():
                choice = int(choice)
                if choice >= len(school_list): continue
                flag, msg = student_interface.student_choose_school_interface(student_info['name'], school_list[choice])
                if flag:
                    print(msg)
                    break
                else:
                    print(msg)
                    break
        else:
            print('暂时没有学校')


@common.login_interface('student')
def choose_course():
    print('选择课程')
    flag, course_list = student_interface.student_get_all_school_course(student_info['name'])
    if flag:
        for i, course in enumerate(course_list):
            print('%s:%s' % (i, course))
            choice = input('请选择课程').strip()
            if choice.isdigit():
                choice = int(choice)
                if choice >= len(course_list): continue
                flag, msg = student_interface.student_choose_course(student_info['name'], course_list[choice])
                if flag:
                    print(msg)
                    break
                else:
                    print(msg)
    else:
        print(course_list)


@common.login_interface('student')
def check_score():
    course = student_interface.student_check_course(student_info['name'])
    print(course)


service = {

    '1': register,
    '2': login,
    '3': choose_school,
    '4': choose_course,
    '5': check_score
}


def run():
    while True:
        print('选课系统')
        print('''
        0、退出
        1、注册
        2、登录
        3、选择校区
        4、选择课程
        5、查看成绩

        ''')
        choice = input('请选择：').strip()
        if choice == '0':
            student_info['name'] = None
            break
        if choice in service:
            service[choice]()
