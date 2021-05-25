from models import *
from pony.orm import db_session, select

class TeacherManager():
    @staticmethod
    @db_session
    def create_teacher(name, login, manager):
        t = Teacher(name=name, login=login, manager=manager)
        return t

    @staticmethod
    @db_session
    def delete_teacher(id):
        return Teacher.get(id=id).delete()

    @staticmethod
    @db_session
    def update_teacher(t, login, name, manager):
        t.login=login
        t.login=name
        t.login=manager
        return t

    @staticmethod
    def get_teacher(id):
        return Teacher.get(id=id)


    @staticmethod
    def GetTeachers():
        return list(select(teacher for teacher in Teacher))

