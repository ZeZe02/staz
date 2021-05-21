from pony.orm import db_session, select

from models import Teacher


class TeacherManager:
    @staticmethod
    @db_session
    def create_teacher(fname, lname, login):
        fullname = f'{fname} {lname}'
        t = Teacher(name=fullname, login=login)
        return t

    @staticmethod
    def get_teacher(teacher_id):
        return Teacher.get(id=teacher_id)

    @staticmethod
    def get_teachers():
        return list(select(teacher for teacher in Teacher))
