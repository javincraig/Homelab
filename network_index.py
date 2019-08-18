app_list = ['Switch Template', 'Router Template', 'Core Template', 'UPS Template']
app_list.append('Exit')
exit_number = -1

print('      Template Choices')
print('=============================')

for index, app in enumerate(app_list):
    print(f"{index}: {app}")
    exit_number = exit_number + 1

print('=============================')
app_number = input('Enter the application number: ')

if app_number == '0':
    from app1 import app1
if app_number == '1':
    from app2 import app2
if app_number == '2':
    from app3 import app3
if app_number == '3':
    from app4 import app4
else:
    exit('EXITING NOW')

