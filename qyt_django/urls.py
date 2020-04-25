"""qyt_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

# 首页
from views.index import index

# 设备管理
from qyt_device.views.qyt_device_view_add_device import add_device  # 添加设备
from qyt_device.views.qyt_device_view_show_device import show_device  # 查看设备
from qyt_device.views.qyt_device_view_delete_device import delete_device  # 删除设备

# 图表
from qyt_device.views.qyt_device_view_multi_echarts import multi_echarts  # 多图Echarts
from qyt_device.views.qyt_device_view_echarts_final_line_cpu_usage import echarts_final_line_cpu_usage
from qyt_device.views.qyt_device_view_echarts_final_line_if_speed import echarts_final_line_if_speed
#
# # AJAX
from qyt_device.views.qyt_device_view_ajax import ajax_chart2  # ajax提供chart2数据
from qyt_device.views.qyt_device_view_ajax import ajax_pie3  # ajax提供pie3数据
from qyt_device.views.qyt_device_view_ajax import echarts_final_line_ajax_cpu_usage  # ajax提供终极线性图(CPU利用率)数据
from qyt_device.views.qyt_device_view_ajax import echarts_final_line_ajax_if_speed_ajax  # ajax提供终极线性图(接口速率)数据
#
# # 登录登出
# from views.djg_login import djg_login  # 登录
# from views.djg_login import djg_logout  # 登出

urlpatterns = [
    path('admin/', admin.site.urls),
    # 首页
    path('', index),
    # 设备管理
    path('add_device', add_device),  # 添加设备
    path('show_device', show_device),  # 查看设备
    path('delete_device/<int:device_id>', delete_device),  # 删除设备
    # 图表
    path('multi_echarts', multi_echarts),  # 多图Echarts
    path('echarts_final_line_cpu_usage', echarts_final_line_cpu_usage),  # ajax提供终极线形图(CPU利用率)数据
    path('echarts_final_line_if_speed', echarts_final_line_if_speed),  # ajax提供终极线形图(接口速率)数据
    # # AJAX
    path('ajax/chart2', ajax_chart2),  # ajax提供chart2数据
    path('ajax/pie3', ajax_pie3),  # ajax提供pie3数据
    path('ajax/echarts_final_line_ajax_cpu_usage', echarts_final_line_ajax_cpu_usage),  # ajax提供终极线性图(CPU利用率)数据
    path('ajax/echarts_final_line_ajax_if_speed_ajax', echarts_final_line_ajax_if_speed_ajax),  # ajax提供终极线性图(接口速率)数据
    # # 登录登出
    # path('accounts/login/', djg_login),
    # path('accounts/logout/', djg_logout),
    # # 文件管理
    # path('files_mgmt/', include(('files_mgmt.urls', 'files_mgmt'), namespace='files_mgmt')),
]

