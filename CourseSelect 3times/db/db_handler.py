from conf import setting
import os, pickle


def save(self):
    dir_path = os.path.join(setting.BEAS_DB, self.__class__.__name__.lower())
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    obj_path = os.path.join(dir_path, self.name)
    with open(obj_path, 'wb')as f:
        pickle.dump(self, f)
        f.flush()


def select(dir_name, name):
    dir_path = os.path.join(setting.BEAS_DB, dir_name)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    obj_path = os.path.join(dir_path, name)
    if os.path.exists(obj_path):
        with open(obj_path, 'rb')as f:
            return pickle.load(f)
    else:
        return None
