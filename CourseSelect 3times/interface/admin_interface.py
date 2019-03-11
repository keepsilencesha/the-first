from db import modles


def register_interface(name, password):
    obj_path = modles.Admin.select(name)
    if not obj_path:

        modles.Admin(name, password)
        return True, '注册成功'
    else:
        return False, '管理员已存在'


def create_school_interface(admin_name, school_name, address):
    school_path = modles.School.select(school_name)
    if school_path:
        return False, '学校已存在'
    else:
        obj_path = modles.Admin.select(admin_name)
        obj_path.create_school(school_name, address)
        return True, '创建学校成功'


def create_teacher_interface(admin_name, name, password='123'):
    course_path = modles.Teacher.select(name)
    if course_path:
        return False, '老师已存在'
    else:
        obj_path = modles.Admin.select(admin_name)
        obj_path.create_teacher(name, password)
        return True, '创建老师成功'


def create_course_interface(admin_name, course_name,school_name):
    course_path = modles.Course.select(course_name)
    if course_path:
        return False, '课程已存在'
    else:
        obj_path = modles.Admin.select(admin_name)
        obj_path.create_course(course_name)

        school_obj=modles.School.select(school_name)
        school_obj.add_course(course_name)
        return True, '创建课程成功'
