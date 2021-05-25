from models import *
from pony.orm import db_session, select


class TeacherManager:
    @staticmethod
    @db_session
    def create_teacher(login,name,manager):
        t = Teacher(login=login,name=name,manager=manager)
        return t

    @staticmethod
    @db_session
    def update_teacher(t,login,name,manager, **kwargs):
        t.login=login
        t.name=name
        t.manager=manager
        return t

    @staticmethod
    def get_teacher(id_teacher=None):
        if id_teacher:
            return Teacher.get(id=id_teacher)
        return None

    @staticmethod
    def get_teachers():
        return list(select(teacher for teacher in Teacher))

    # POZOR - napred musi byt staticmethod a teprve pote dekorator db_session
    # kdyz je to opacne, hlasi to pri volani: TypeError: 'staticmethod' object is not callable
    @staticmethod
    @db_session
    def delete_teacher(id_teacher):
        return Teacher.get(id=id_teacher).delete()
        #return delete(Teacher.get(id=id_teacher))    # toto nefunguje! (error) TypeError: The first positional argument must be generator expression or its text source. Got: Teacher[15]


class StudentManager:
    @staticmethod
    @db_session
    def create_one(login,firstname,surname):
        return Student(login=login,firstname=firstname,surname=surname)

    @staticmethod
    @db_session
    def update_one(s,login,firstname,surname,classroom=None, **kwargs):
        s.login=login
        s.firstname=firstname
        s.surname=surname
        if classroom:
            s.classroom=classroom
        return s

    @staticmethod
    def get_one(id_item=None):
        if id_item:
            return Student.get(id=id_item)
        return None

    @staticmethod
    def get_all():
        return list(select(s for s in Student))

    @staticmethod
    @db_session
    def delete(id):
        return Student.get(id=id).delete()

    @staticmethod
    @db_session
    def choice_all_names():
        #return [("a","ahoj"),("c","cau")]
        return list(select( (s.id, f"{s.login} {s.firstname} {s.surname}") for s in Student))




class ProjectManager:
    @staticmethod
    @db_session
    def create_project(title,supervisor,class_exp,school_year,type_state,**kwargs):
        return Project(title=title,supervisor=supervisor,class_exp=class_exp,school_year=school_year,type_state=type_state,**kwargs)
