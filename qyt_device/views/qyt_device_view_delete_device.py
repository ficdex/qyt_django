from qyt_device.views.qyt_device_view_show_device import show_device
from qyt_device.models import Devicedb


def delete_device(request, device_id):
    try:
        # 获取对应ID的设备
        m = Devicedb.objects.get(id=device_id)
        # 从数据库中删除设备条目
        m.delete()
        return show_device(request, successmessage="设备删除成功")
    except Devicedb.DoesNotExist:
        return show_device(request, errormessage="设备未找到!或者已经被删除!")
