from db import modles


def student_register_interface(student_name, password):
    student_obj = modles.Student.select(student_name)
    if student_obj:
        return False, '该学生已存在'
    else:
        modles.Student(student_name, password)
        return True, '注册成功'


def student_choose_school_interface(student_name, school_name):
    student_obj = modles.Student.select(student_name)
    school = student_obj.get_school()
    if not school:

        student_obj.choose_school(school_name)
        return True, '选择成功'
    else:
        return False, '您已选择'


def student_get_all_school_course(student_name):
    obj = modles.Student.select(student_name)

    if not obj.school_name:
        return False, '你还没有选择学校'
    school_obj = modles.School.select(obj.school_name)
    if school_obj.course_list:
        return True, school_obj.course_list
    else:
        return False, '该学校暂时没有课程'


def student_choose_course(student_name, course_name):
    student_obj = modles.Student.select(student_name)
    if course_name in student_obj.course_list:
        return False, '你已经选过这个课程'
    else:
        student_obj.add_course(course_name)
        course_obj = modles.Course.select(course_name)
        course_obj.add_student(student_name)
        return True, '选课成功'


def student_check_course(student_name):
    student_obj = modles.Student.select(student_name)
    if student_obj.course:
        return student_obj.course
