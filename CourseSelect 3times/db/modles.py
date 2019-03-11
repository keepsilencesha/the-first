from db import db_handler
from conf import setting
import os


class BaseClass:
    def save(self):
        db_handler.save(self)

    @classmethod
    def select(cls, name):
        return db_handler.select(cls.__name__.lower(), name)


class Admin(BaseClass):
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.save()

    def create_school(self, school_name, address):
        School(school_name, address)

    def create_teacher(self, name, password):
        Teacher(name, password)

    def create_course(self, name):
        Course(name)


class Teacher(BaseClass):
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.course_list = []
        self.save()

    def add_course(self, course_name):
        self.course_list.append(course_name)
        self.save()

    def modify_score(self, student, course_name, score):
        student.score[course_name] = score
        student.save()


class School(BaseClass):
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.course_list = []
        self.save()

    def add_course(self, course_name):
        self.course_list.append(course_name)
        self.save()


class Student(BaseClass):
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.school_name = None
        self.course_list = []
        self.score = {}
        self.save()

    def choose_school(self, school_name):
        self.school_name = school_name
        self.save()

    def get_school(self):
        return self.school_name

    def add_course(self, course_name):
        self.course_list.append(course_name)
        self.save()


class Course(BaseClass):
    def __init__(self, course_name):
        self.name = course_name
        self.student_list = []
        self.save()

    def add_student(self, student_name):
        self.student_list.append(student_name)
        self.save()
