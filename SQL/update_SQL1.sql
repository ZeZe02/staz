create table Project_dg_tmp
(
	id INTEGER
		primary key autoincrement,
	title TEXT not null,
	supervisor INTEGER not null
		references Teacher
			on delete cascade,
	student INTEGER
		references Student
			on delete set null,
	class_exp TEXT not null,
	school_year INTEGER not null,
	date_to DATETIME,
	classroom INTEGER
		references Classroom,
	grade_text TEXT not null,
	grade_final INTEGER
		references Type_grade
			on delete cascade,
	url1 TEXT not null,
	url2 TEXT not null,
	file_pdf INTEGER
		references File,
	file_attachment INTEGER
		references File,
	anotation TEXT not null,
	type_state INTEGER not null
		references Type_state
			on delete cascade
);

insert into Project_dg_tmp(id, title, supervisor, student, class_exp, school_year, date_to, classroom, grade_text, grade_final, url1, url2, file_pdf, file_attachment, anotation, type_state) select id, title, supervisor, student, class_exp, school_year, date_to, classroom, grade_text, grade_final, url1, url2, file_pdf, file_attachment, anotation, type_state from Project;

drop table Project;

alter table Project_dg_tmp rename to Project;

create index idx_project__classroom
	on Project (classroom);

create index idx_project__file_attachment
	on Project (file_attachment);

create index idx_project__file_pdf
	on Project (file_pdf);

create index idx_project__grade_final
	on Project (grade_final);

create index idx_project__student
	on Project (student);

create index idx_project__supervisor
	on Project (supervisor);

create index idx_project__type_state
	on Project (type_state);

