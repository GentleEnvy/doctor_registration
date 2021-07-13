import jinja2
loader = jinja2.FileSystemLoader('./index.html')
env = jinja2.Environment(loader=loader)
type_of_user=''
index = jinja2.Template("{{type_of_user}}")
print(index.render( type_of_user=type_of_user ))