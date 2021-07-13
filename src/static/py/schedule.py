import jinja2
loader = jinja2.FileSystemLoader('./schedule.html')
env = jinja2.Environment(loader=loader)
date = ''
status1 = ''
status2 = ''
status3 = ''
status4 = ''
status5 = ''
status6 = ''
status7 = ''
status8 = ''
t = jinja2.Template("{{date}}"
                    "{{status1}}"
                    "{{status2}}"
                    "{{status3}}"
                    "{{status4}}"
                    "{{status5}}"
                    "{{status6}}"
                    "{{status7}}"
                    "{{status8}}")

print(t.render( date=date, status1=status1,status2=status2,status3=status3,status4=status4,
                status5=status5,status6=status6,status7=status7,status8=status8, ))
