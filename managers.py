from models import *
from pony.orm import db_session, select, delete


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
    def choice_all_names():
        return [("a","ahoj"),("c","cau")]
        return list(select( tuple(s.id, f"{s.login} {s.firstname} {s.surname}") for s in Student))




class ProjectManager:
    @staticmethod
    @db_session
    def create_project(title,supervisor,class_exp,school_year,type_state,**kwargs):

        return Project(title=title,supervisor=supervisor,class_exp=class_exp,school_year=school_year,type_state=type_state,**kwargs)

    # @staticmethod
    # def get_project(id_project=None):
    #     if id_project:
    #         return Teacher.get(id=id_teacher)
    #     return None
    #
    # @staticmethod
    # def get_projects():
    #     return list(select(record for record in Project))




