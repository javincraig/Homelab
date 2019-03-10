networks = {}
more = 'YES'

# Yes/No input validation
yesnoans = ['Y', 'YE', 'YES', 'N', 'NO']
yesans = ['Y', 'YE', 'YES']
noans = ['N', 'NO']

# Gather vlan/network information
while more in yesans:
    vlan = input('What is the vlan ID?: ')
    while int(vlan) < 0 or int(vlan) > 4096:
        vlan = input('What is the vlan ID?: ')
    vlan_name = input('What is the name for vlan ' + str(vlan) + '?: ')
    while ' ' in vlan_name:
        vlan_name = input(
            'What is the name for vlan ' + str(vlan) + '?(this cannot contain spaces, use underscore if necessary): ')
    vlan_network = input('What is the network for vlan ' + str(vlan) + '?: ')
    vlan_mask = input('What is the network mask for vlan ' + str(vlan) + '?: ')
    vlan_gateway = input('What is the default gateway for vlan ' + str(vlan) + '?: ')
    networks[vlan] = vlan
    networks[vlan] = {}
    networks[vlan]['vlanid'] = vlan
    networks[vlan]['vlanname'] = vlan_name
    networks[vlan]['vlannetwork'] = vlan_network
    networks[vlan]['vlanmask'] = vlan_mask
    networks[vlan]['vlangateway'] = vlan_gateway
    more = input('Are there any more VLANs(YES/NO)?: ').upper()
    while more not in yesnoans:
        more = input('Are there any more VLANs(YES/NO)?: ').upper()

# gather switch management information
managementvlan = input('What is the switch management vlan?: ')
# validating that the vlan was gathered above
if managementvlan not in networks:
    print('Did you forget to add the management vlan!?')
    vlan = input('What is the management vlan ID?: ')
    while int(vlan) < 0 or int(vlan) > 4096:
        vlan = input('What is the vlan ID? (1-4096): ')
    vlan_name = input('What is the name for vlan ' + str(vlan) + '?: ')
    vlan_network = input('What is the network for vlan ' + str(vlan) + '?: ')
    vlan_mask = input('What is the network mask for vlan ' + str(vlan) + '?: ')
    vlan_gateway = input('What is the default gateway for vlan ' + str(vlan) + '?: ')
    networks[vlan] = vlan
    networks[vlan] = {}
    networks[vlan]['vlanid'] = vlan
    networks[vlan]['vlanname'] = vlan_name
    networks[vlan]['vlannetwork'] = vlan_network
    networks[vlan]['vlanmask'] = vlan_mask
    networks[vlan]['vlangateway'] = vlan_gateway
managementip = input('What is the management IP?: ')
switchhostname = input('What is the hostname for the switch?: ')
enable_secret = input('What is the enable secret password?[cisco]: ') or 'cisco'
user = input('What username would you like to create?[cisco]: ') or 'cisco'
user_password = input('What is the password?[cisco]: ') or 'cisco'
def esxi_conf(networks):
    esxi_switch_name = input('What is the virtual switch name? [LAN]: ') or 'LAN'
    vmnic = input('what is the virtual switch uplink? [vmnic1]: ').lower() or 'vmnic1'
    print('')
    print('-------------------------ESXI CLI Cconfiguration---------------------------------')
    print('esxcli network vswitch standard add --vswitch-name=' + esxi_switch_name)
    print('esxcli network vswitch standard set --cdp-status=both --vswitch-name=' + esxi_switch_name)
    print('esxcli network vswitch standard uplink add --uplink-name=' + vmnic + ' --vswitch-name='+ esxi_switch_name)
    # Portgroup list
    for net in networks:
        print('esxcli network vswitch standard portgroup add --portgroup-name=' + networks[net]['vlanname'] + ' --vswitch-name=' + esxi_switch_name)
        print('esxcli network vswitch standard portgroup set -p ' + networks[net]['vlanname'] + ' --vlan-id ' + networks[net]['vlanid'])

def cisco_switch_conf(networks):
    print('')
    print('Copy and paste the following on to your switch from the console port')
    print('')
    print('vtp domain ' + switchhostname)
    print('''
vtp mode transparent
spanning-tree mode rapid-pvst
spanning-tree portfast default
spanning-tree portfast bpduguard default
line con 0
login local
line vty 0 15
login local
crypto keygen gen rsa mod 2048
ssh version 2
''')
    print('enable secret ' + enable_secret)
    print('user ' + user + ' priv 15 secret ' + user_password)
    print('')
    for net in networks:
        print('vlan ' + net)
        print('  name ' + networks[net]['vlanname'])
    print('interface vlan ' + managementvlan)
    print('  ip address ' + managementip + ' ' + networks[managementvlan]['vlanmask'])
    print('  no shut')
    print('exit')
    print('ip default gateway ' + networks[managementvlan]['vlangateway'])

# Trigger the above definition
cisco_switch_conf(networks)
esxi_conf(networks)