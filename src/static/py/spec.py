import jinja2
loader = jinja2.FileSystemLoader('./specialists.html')
env = jinja2.Environment(loader=loader)
doctor.surname = ''
doctor.name = ''
doctor.midname = ''
doctor.speciality = ''
doctor.qual=''
t = jinja2.Template("{{doctor.surname}}"
                    "{{doctor.name}}"
                    "{{doctor.midname}}"
                    "{{doctor.specialty}}"
                    "{{doctor.qual}}")

print(t.render( doctor.surname= doctor.surname, doctor.name=doctor.name, doctor.midname=doctor.midname, doctor.speciality=doctor.speciality,doctor.qual=doctor.qual ))
