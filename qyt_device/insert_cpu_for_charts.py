import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qyt_django.settings')
django.setup()
from qyt_device.models import Devicecpu, Devicedb
from random import randint
from time import sleep
from datetime import datetime

Devicecpu.objects.all().delete()

for i in range(50):
    record_time = datetime.now()
    for d in Devicedb.objects.all():
        cpu = randint(1, 100)
        c = Devicecpu(device=d, cpu_usage=cpu, record_datetime=record_time)
        c.save()
    sleep(1)