import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qyt_django.settings')
django.setup()

from qyt_device.models import Devicetype, SNMPtype, DeviceSNMP, Devicedb, Devicecpu
from random import randint
import time

devicetypes = ['CSR1000v', 'Nexus9000', ]

snmptypes = ['cpu利用率', '内存使用', '内存空闲']

devicesnmps = [{'device_type': 'CSR1000v', 'snmp_type': 'cpu利用率', 'oid': '1.3.6.1.4.1.9.9.109.1.1.1.1.3.7', },
               {'device_type': 'CSR1000v', 'snmp_type': '内存使用', 'oid': '1.3.6.1.4.1.9.9.109.1.1.1.1.12.7', },
               {'device_type': 'CSR1000v', 'snmp_type': '内存空闲', 'oid': '1.3.6.1.4.1.9.9.109.1.1.1.1.13.7', },
               {'device_type': 'Nexus9000', 'snmp_type': 'cpu利用率', 'oid': '1.3.6.1.4.1.9.9.109.1.1.1.1.3.7', },
               {'device_type': 'Nexus9000', 'snmp_type': '内存使用', 'oid': '1.3.6.1.4.1.9.9.109.1.1.1.1.12.7', },
               {'device_type': 'Nexus9000', 'snmp_type': '内存空闲', 'oid': '1.3.6.1.4.1.9.9.109.1.1.1.1.13.7', },
               ]

devicedbs = [{'name': '网关路由器', 'ip': '1.1.1.1', 'type': 'CSR1000v', 'snmp_ro_community': 'public',
              'snmp_rw_community': 'private', 'ssh_username': 'admin', 'ssh_password': 'admin',
              'enable_password': 'cisco'},
             {'name': '核心交换机', 'ip': '2.2.2.2', 'type': 'Nexus9000', 'snmp_ro_community': 'public',
              'snmp_rw_community': 'private', 'ssh_username': 'admin', 'ssh_password': 'admin',
              'enable_password': 'cisco'}, ]

devicecpus = [{'device': '网关路由器', 'cpu_usage': '5.1', },
              {'device': '核心交换机', 'cpu_usage': '10.5', }, ]

for devicetype in devicetypes:
    d = Devicetype(name=devicetype)
    d.save()

for snmptype in snmptypes:
    d = SNMPtype(name=snmptype)
    d.save()

for devicesnmp in devicesnmps:
    d = DeviceSNMP(device_type=Devicetype.objects.get(name=devicesnmp.get('device_type')),
                   snmp_type=SNMPtype.objects.get(name=devicesnmp.get('snmp_type')),
                   oid=devicesnmp.get('oid'), )
    d.save()

for devicedb in devicedbs:
    d = Devicedb(name=devicedb.get('name'), ip=devicedb.get('ip'),
                 type=Devicetype.objects.get(name=devicedb.get('type')),
                 snmp_ro_community=devicedb.get('snmp_ro_community'),
                 snmp_rw_community=devicedb.get('snmp_rw_community'),
                 ssh_username=devicedb.get('ssh_username'),
                 ssh_password=devicedb.get('ssh_password'),
                 enable_password=devicedb.get('enable_password'), )
    d.save()

for devicecpu in devicecpus:
    d = Devicecpu(device=Devicedb.objects.get(name=devicecpu.get('device')),
                  cpu_usage=devicecpu.get('cpu_usage'), )
    d.save()

gw = Devicedb.objects.get(name='网关路由器')
print(gw)

for x in range(50):
    c = Devicecpu(device=gw, cpu_usage=randint(1, 100))
    c.save()
    time.sleep(1)

snmp_info = gw.type.devicesnmp.all()
for snmp in snmp_info:
    print(f'SNMP类型:{snmp.snmp_type.name:<20}| OID:{snmp.oid}')

cpu_info = gw.cpu_usage.all()
for cpu in cpu_info:
    print(f"CPU利用率:{cpu.cpu_usage:<5}| 记录时间:{cpu.record_datetime.strftime('%Y-%m-%d %H:%M:%S')} ")

