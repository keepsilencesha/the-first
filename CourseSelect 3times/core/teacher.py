teacher_info={'name':None}

def login():
    pass


def check_course():
    pass


def choose_course():
    pass


def check_student():
    pass


def modify_score():
    pass


service = {

    '1': login,
    '2': check_course,
    '3': choose_course,
    '4': check_student,
    '5': modify_score
}


def run():
    while True:
        print('选课系统')
        print('''
        0、退出
        1、登录
        2、查看教授课程     
        3、选择教授课程     
        4、查看课程下学生   
        5、修改学生成绩 

        ''')
        choice = input('请选择：').strip()
        if choice == '0': break
        if choice in service:
            service[choice]()
