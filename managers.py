from pony.orm import db_session, select

from models import Teacher


class TeacherManager:
    @staticmethod
    @db_session
    def create_teacher(first_name, last_name, login, manager, **kwargs):
        fullname = f'{first_name} {last_name}'
        t = Teacher(name=fullname, login=login, manager=manager)
        return t

    @staticmethod
    def get_teacher(teacher_id):
        return Teacher.get(id=teacher_id)

    @staticmethod
    def get_all_teachers():
        return list(select(teacher for teacher in Teacher))
