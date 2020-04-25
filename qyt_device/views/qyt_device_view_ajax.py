from django.http import JsonResponse
from qyt_device.views.qyt_device_view_make_echarts_data import data_from_db
from qyt_device.models import Devicedb, Devicecpu
import random
import time
import datetime


def ajax_chart2(request):
    all_data = data_from_db(Devicedb.objects.all(), ['#00BFFF', '#FF3300'], ['line', 'bar'])
    return JsonResponse({'labelname': 'CPU利用率',
                         'legends': all_data[0],
                         'labels': all_data[1],
                         'datas': all_data[2]})


def ajax_pie3(request):
    pie3_label = '协议分布'
    pie3_protocol = ['HTTP', 'Telnet', 'SSH', 'ICMP']
    pie3_data = [{'value': random.randint(20, 100), 'name': p} for p in pie3_protocol]
    return JsonResponse({'labelname': pie3_label,
                         'labels': pie3_protocol,
                         'datas': pie3_data})


# 产生每一条线数据的函数
def line_data(name, time_data_list, color):
    return {
                'symbolSize': 0,  # 这个参数表示在图像上显示的原点大小，为0则不显示
                'symbol': 'circle',
                'name': name,
                'type': 'line',
                'smooth': True,
                'smoothMonotone': True,
                'data': time_data_list,
                'areaStyle': {
                    'color': color
                },
                'markPoint': {
                    'itemStyle': {
                      'color': color
                    },
                    'data': [
                        {'type': 'max', 'name': '最大值'},
                        {'type': 'min', 'name': '最小值'}
                    ]
                },
                'lineStyle': {
                    'color': color
                },
                'itemStyle': {
                    'color': color
                }
            }


def change_time(datetime_obj):
    return int(time.mktime(datetime_obj.timetuple())) * 1000


def echarts_final_line_ajax_cpu_usage(request):
    cpu_time_list = []
    cpu = Devicecpu.objects.filter(device__name='网关路由器')
    for x in cpu:
        cpu_time_list.append([x.record_datetime, x.cpu_usage])

    cpu_time_list_sorted = sorted(cpu_time_list, key=lambda x: x[0])
    cpu_time_list_converted = [[change_time(x[0]), x[1]] for x in cpu_time_list_sorted]

    cpu_datas = [line_data('R1 CPU利用率', cpu_time_list_converted, '#00BFFF')]

    return JsonResponse({'labelname': 'CPU利用率',
                         'legends': [x['name'] for x in cpu_datas],
                         'datas': cpu_datas,
                         'starttime': '2020-04-23'})


def echarts_final_line_ajax_if_speed_ajax(request):
    # 产生随机数据
    g1_up_time_speed_list = []
    g1_down_time_speed_list = []
    now_time = datetime.datetime.now()
    for i in range(100):
        g1_up_time_speed_list.append(
            [int(time.mktime((now_time + datetime.timedelta(minutes=i * 30)).timetuple())) * 1000,
             random.randint(40, 60)])
        g1_down_time_speed_list.append(
            [int(time.mktime((now_time + datetime.timedelta(minutes=i * 30)).timetuple())) * 1000,
             random.randint(30, 70)])
        i += 1


    speed_datas = [line_data('G1 up流量', g1_up_time_speed_list, '#00BFFF'),
                   line_data('G1 down流量', g1_down_time_speed_list, '#FF3300')]


    return JsonResponse({'labelname': '接口速率',
                         'legends': [x['name'] for x in speed_datas],
                         'datas': speed_datas,
                         'starttime': '2020-04-23'})