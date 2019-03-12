from netmiko import ConnectHandler
from getpass import getpass

# ---------------Gather information---------------------
# credentials gathering
username = input('What is the username? [admin]: ') or 'admin'
password = getpass(prompt='Password: ', stream=None)

# List of switch IP addresses
switch_list = ['192.168.0.5']

for device in switch_list:
    cisco_switch = {
        'device_type': 'cisco_ios',
        'ip': device,
        'username': username,
        'password': password}
    connection = ConnectHandler(**cisco_switch)
    hostname_output = connection.send_command('show run | include hostname')
    # access_list_output = connection.send_command('show ip access-list')
    print('--------------------------------------------')
    print('The hostname is: ' + hostname_output[9:])
    # for line in access_list_output.splitlines():
    #     print(line)
done = input('press enter: ')
