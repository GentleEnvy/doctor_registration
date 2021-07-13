import jinja2
loader = jinja2.FileSystemLoader('./adminnp.html')
env = jinja2.Environment(loader=loader)
name_of_user=''
login=''
password=''
type_of_user=''
tbody = jinja2.Template("{{name_of_user}}"
                    "{{login}}"
                    "{{password}}"
                    "{{type_of_user}}")

print(tbody.render( name_of_user=name_of_user, login=login, password=password, type_of_user=type_of_user ))
