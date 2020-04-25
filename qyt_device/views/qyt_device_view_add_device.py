from django.shortcuts import render
from qyt_device.models import Devicedb, Devicetype
from qyt_device.forms.qyt_device_form_add_device import AddDeviceForm
from django.http import HttpResponseRedirect

def add_device(request,):
    if request.method == 'POST':
        # 没有登录
        # if not request.user.is_authenticated:
        #     return HttpResponseRedirect('/accounts/login?next=/add_device')
        # # 登录但是没有权限
        # elif not request.session.get('device_permission') and request.user.is_authenticated:
        #     return render(request, 'qyt_device_deny.html', {'errormessage': '你无权访问此页面'})
        form = AddDeviceForm(request.POST)
        if form.is_valid():
            try:
                d1 = Devicedb(name=request.POST.get('name'),
                              ip=request.POST.get('ip'),
                              description=request.POST.get('description'),
                              type=Devicetype.objects.get(id=request.POST.get('type')),
                              snmp_ro_community=request.POST.get('snmp_ro_community'),
                              snmp_rw_community=request.POST.get('snmp_rw_community'),
                              ssh_username=request.POST.get('ssh_username'),
                              ssh_password=request.POST.get('ssh_password'),
                              enable_password=request.POST.get('enable_password'))
                d1.save()
            except Devicetype.DoesNotExist:
                return render(request, 'qyt_device_add_device.html', {'form': form,
                                                                      'errormessage': '设备类型没有找到'})

            form = AddDeviceForm()
            return render(request, 'qyt_device_add_device.html', {'form': form,
                                                                  'successmessage': '设备添加成功'})

        else:  # 如果Form校验失败,返回客户在Form中输入的内容和报错信息
            # 如果检查到错误,会添加错误内容到form内,例如:<ul class="errorlist"><li>IP地址已经存在</li></ul>
            return render(request, 'qyt_device_add_device.html', {'form': form})
    else:  # 如果不是POST,就是GET,表示为初始访问, 显示表单内容给客户
        # 没有登录
        # if not request.user.is_authenticated:
        #     return HttpResponseRedirect('/accounts/login?next=/add_device')
        # # 登录但是没有权限
        # elif not request.session.get('device_permission') and request.user.is_authenticated:
        #     return render(request, 'qyt_device_deny.html', {'errormessage': '你无权访问此页面'})
        form = AddDeviceForm()
        return render(request, 'qyt_device_add_device.html', {'form': form})
