from db import modles
from conf import setting
from lib import common
import os


def login_interface(type_user, name, password):
    if type_user == 'admin':
        obj = modles.Admin.select(name)
    elif type_user == 'teacher':
        obj = modles.Teacher.select(name)
    elif type_user == 'student':
        obj = modles.Student.select(name)

    else:
        return False, '没有用户类型'
    if obj:
        if obj.password == password:
            return True, '登陆成功'
        else:
            return False, '密码错误'
    else:
        return False, '用户名不存在'


def get_all_school_interface():
    obj_path = os.path.join(setting.BEAS_DB, 'school')
    return common.get_all_dir_obj(obj_path)
