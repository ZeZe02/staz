from datetime import datetime
from pony.orm import PrimaryKey, Required, Optional, Database, Set, db_session


db = Database()
db.bind(provider="sqlite", filename="./database.sqlite", create_db=True)


class Teacher(db.Entity):
    id = PrimaryKey(int, auto=True)   #primární klíč
    projects = Set("Project")
    login = Optional(str)               #optional = volitelné
    name = Optional(str)
    manager = Optional(bool)

@db_session
def create_teacher(name, login, manager):
    t = Teacher(name=name, login=login, manager=manager)
    return t


class Project(db.Entity):
    id = PrimaryKey(int, auto=True)
    title = Required(str)               #required = povinné
    supervisor = Required(Teacher)
    student = Optional("Student")
    class_exp = Required(str)
    school_year = Required(int)
    date_to = Optional(datetime)
    classroom = Required("Classroom")
    grade_text = Optional(str)
    grade_list = Set("Project_criterion_grade")
    grade_final = Required("Type_grade")
    url1 = Optional(str)
    url2 = Optional(str)
    file_pdf = Required("File", reverse="project")
    file_attachment = Required("File", reverse="project_attachment")
    tags = Set("Tag")
    anotation = Optional(str)
    type_state = Required("Type_state")


class Student(db.Entity):
    id = PrimaryKey(int, auto=True)
    projects = Set(Project)
    login = Required(str)
    firstname = Required(str)
    surname = Required(str)
    classroom = Optional("Classroom")


class Classroom(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    students = Set(Student)
    project = Optional(Project)


class Type_grade(db.Entity):
    id = PrimaryKey(int, auto=True)
    order = Required(int)
    name = Required(str)
    identifier = Optional(str)
    project_criterion_grades = Set("Project_criterion_grade")
    projects = Set(Project)


class Type_difficulty(db.Entity):
    id = PrimaryKey(int, auto=True)
    order = Required(int)
    name = Required(str)
    identifier = Optional(str)
    project_criterion_grades = Set("Project_criterion_grade")


class Type_criterion(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    order = Required(int)
    identifier = Optional(str)
    project_criterion_grades = Set("Project_criterion_grade")
    is_grade = Optional(bool)


class Project_criterion_grade(db.Entity):
    id = PrimaryKey(int, auto=True)
    project = Required(Project)
    type_grade = Optional(Type_grade)
    type_criterion = Optional(Type_criterion)
    type_difficulty = Optional(Type_difficulty)


class File(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    path = Optional(str)
    project = Optional(Project, reverse="file_pdf")
    project_attachment = Optional(Project, reverse="file_attachment")


class Tag(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    projects = Set(Project)


class Type_state(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    projects = Set(Project)


db.generate_mapping(create_tables=True)
