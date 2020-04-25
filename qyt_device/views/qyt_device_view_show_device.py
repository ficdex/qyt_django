from django.shortcuts import render
from qyt_device.models import Devicedb


def show_device(request, successmessage=None, errormessage=None):
    # 查询整个数据库的信息 object.all()
    result = Devicedb.objects.all()
    # 最终得到设备清单devices_list,清单内部是每一个设备信息的字典
    devices_list = []
    for x in result:
        # 产生学员信息的字典
        device_dict = {'id_delete': "/delete_device/" + str(x.id),
                       'id': x.id,
                       'name': x.name,
                       'ip': x.ip,
                       'snmp_ro_community': x.snmp_ro_community,
                       'snmp_rw_community': x.snmp_rw_community,
                       'ssh_username': x.ssh_username,
                       'ssh_password': x.ssh_password,
                       'enable_password': x.enable_password,
                       'type': x.type.name,
                       'create_datetime': x.create_datetime,
                       }

        # 提取学员详细信息,并写入字典
        devices_list.append(device_dict)
    return render(request, 'qyt_device_show_device.html', {'devices_list': devices_list,
                                                            'successmessage': successmessage,
                                                            'errormessage': errormessage,
                                                            })
