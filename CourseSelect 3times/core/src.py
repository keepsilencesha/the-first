from core import admin, student, teacher

service = {

    '1': admin.run,
    '2': teacher.run,
    '3': student.run
}


def run():
    while True:
        print('选课系统')
        print('''
        0.退出
        1.管理员
        2.老师
        3.学生
        
        
        ''')
        choice = input('请选择登陆角色：').strip()
        if choice == '0': break
        if choice in service:
            service[choice]()
