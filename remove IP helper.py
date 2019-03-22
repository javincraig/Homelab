device_list = ['192.168.0.1']
ip_helper = ['10.0.0.1']
for device in device_list:
    show_run = 'show_run'
    if ('ip helper address ' + ip_helper) in show_run:
        show_ip_int = 'show ip interface brief'
        svi = []
        for line in show_ip_int.splitlines():
            if 'vlan' in line:
                svi.append('interface ' + line[8:])

        for vlan in svi:



