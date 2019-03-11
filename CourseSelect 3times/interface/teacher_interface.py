from conf import setting
from lib import common
from db import modles
import os


def get_all_course_interface():
    dir_obj = os.path.join(setting.BEAS_DB, 'course')
    if os.path.exists(dir_obj):
        return common.get_all_dir_obj(dir_obj)
    return None


def choose_course_interface(teacher_name, course_name):
    obj = modles.Teacher.select(teacher_name)
    if course_name in obj.course_list:
        return False, '你已选过该课程'
    else:
        obj.add_course(course_name)
        return True, '选择成功'

def check_course_interface(teacher_name):
    obj=modles.Teacher.select(teacher_name)
    return obj.course_list

def check_course_student(course_name):
    obj=modles.Course.select(course_name)
    return obj.student_list

def modify_score_interface(teacher_name,student_name,course_name,score):
    teacher_obj=modles.Teacher.select(teacher_name)
    student_obj=modles.Student.select(student_name)
    teacher_obj.modify_socre(student_obj,course_name,score)
    return True
