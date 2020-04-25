import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qyt_django.settings')
django.setup()

from qyt_device.models import Devicecpu
from qyt_device.models import Devicedb
from datetime import datetime, timedelta


def make_echarts_data(line_name, datas_list, color, shape_type='line'):
    return_dict = {'name': line_name,  # 线的名字
                   'symbolSize': 0,  # 这个参数表示在图像上显示的原点大小，为0则不显示,
                   'data': datas_list,  # 数据的列表
                   # markPoint用于标记最大值和最小值
                   'markPoint': {
                                    'itemStyle': {
                                                    'color': color
                                                 },
                                    'data': [
                                                {'type': 'max', 'name': '最大值'},
                                                {'type': 'min', 'name': '最小值'}
                                            ]
                                },
                   # 平滑线
                   'smooth': True,
                   # 图类型
                   'type': shape_type,
                   # 线的颜色
                   'color': color}
    return return_dict


def data_from_db(devices_list, colors_list, types_list, last_hours=10):
    last_hours_before = datetime.now() - timedelta(hours=last_hours)
    times_list = []
    name_list = []
    datas_list = []
    for device in devices_list:
        name_list.append(device.name)
        last_hours_cpu = Devicecpu.objects.filter(device=device, record_datetime__gte=last_hours_before).order_by('record_datetime')
        device_datas_list = []
        if not times_list:
            for c in last_hours_cpu:
                times_list.append(c.record_datetime.strftime('%H:%M:%S'))
                device_datas_list.append(c.cpu_usage)
        else:
            for c in last_hours_cpu:
                device_datas_list.append(c.cpu_usage)
        datas_list.append(device_datas_list)

    echarts_data_list = []
    ziped_name_data_color_type = zip(name_list, datas_list, colors_list, types_list)
    for z in ziped_name_data_color_type:
        echarts_data_list.append(make_echarts_data(z[0], z[1], z[2], z[3]))
    return name_list, times_list, echarts_data_list


if __name__ == '__main__':
    # print(make_echarts_data('R1', [1, 2, 3], '#00BFFF'))
    print(data_from_db(Devicedb.objects.all(), ['#00BFFF', '#FF3300'], ['line', 'bar']))
