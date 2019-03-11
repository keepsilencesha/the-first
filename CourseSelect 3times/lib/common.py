import os
def login_interface(type_user):
    from core import admin, student, teacher
    def anth(func):
        def warrper(*args, **kwargs):
            if type_user == 'admin':
                if not admin.admin_info['name']:
                    admin.login()
            else:
                return func(*args, **kwargs)

            if type_user == 'student':
                if not student.student_info['name']:
                    admin.login()
            else:
                return func(*args, **kwargs)
            if type_user == 'teacher':
                if not teacher.teacher_info['name']:
                    admin.login()
            else:
                return func(*args, **kwargs)

        return warrper

    return anth


def get_all_dir_obj(obj_path):

    if os.path.exists(obj_path):
        return os.listdir(obj_path)
    else:
        return None