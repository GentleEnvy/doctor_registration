import jinja2
loader = jinja2.FileSystemLoader('./adminnp.html')
env = jinja2.Environment(loader=loader)
type_of_user=''
specialty=''
qual=''
theader = jinja2.Template("{{type_of_user}}"
                          "{{specialty}}"
                          "{{qual}}")
print(theader.render( type_of_user=type_of_user, specialty=specialty, qual=qual ))

name_of_user=''
login=''
password=''
tbody = jinja2.Template("{{name_of_user}}"
                    "{{login}}"
                    "{{password}}"
                    "{{type_of_user}}"
                    "{{doctor.specialty}}"
                    "{{doctor.qual}}" )

print(tbody.render( name_of_user=name_of_user, login=login, password=password, type_of_user=type_of_user, specialty=specialty, qual=qual ))
