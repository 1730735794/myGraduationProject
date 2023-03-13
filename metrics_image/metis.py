# -*- coding: UTF-8 -*-

from time_series_detector import detect     
from utils.alertmanager import send_alert
from utils.prometheus import get_prometheus_data
from utils.config import Setup
from datetime import datetime
from utils.config import Config
import json, time

def MetisJob(min):
    while True:
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        # 360 data of the same time a week ago
        results = get_prometheus_data("((1-node_memory_MemFree_bytes/node_memory_MemTotal_bytes)*100)[6m1s:1s] offset 6d23h47m")
        dataC = ','.join(str(int(float(x[1]))) for x in results[0]['values'])

        # 360 data of before the same time a day ago
        results = get_prometheus_data("((1-node_memory_MemFree_bytes/node_memory_MemTotal_bytes)*100)[6m1s:1s] offset 6d23h47m")
        dataB = ','.join(str(int(float(x[1]))) for x in results[0]['values'])

        # 180 data before current time
        results = get_prometheus_data("((1-node_memory_MemFree_bytes/node_memory_MemTotal_bytes)*100)[3m1s:1s]")
        dataA = ','.join(str(int(float(x[1]))) for x in results[0]['values'])
        detect_obj = detect.Detect()
        data = {}
        data['window'] = 180
        data['dataA'] = dataA
        data['dataB'] = dataB
        data['dataC'] = dataC
        res = detect_obj.value_predict(data)
        if res[1]['ret'] == 0:
            summary = "Abnormal memory usage"
            description = "Metrics' result is " + str(res[1])
            print(" [Send Alert]\n")
            send_alert(summary, description)
        else:
            print(" [OK]\n")
        time.sleep(min * 60)

 
if __name__ == '__main__':
    try:
        with open("./config.json",'r') as f:
            config = json.loads(f.read())
        Setup(config['prometheus'], config['alertmanager'], config['min'])
    except Exception as err:
        print(err)
        exit(1)

    MetisJob(Config.min)