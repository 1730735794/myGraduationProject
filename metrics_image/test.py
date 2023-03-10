from time_series_detector import detect

import json
import requests
import csv
import time
import sys
import getopt
PROMETHEUS = 'http://124.221.127.211:30000/'
interval = 1

def get_prometheus_data(expr):
    url = PROMETHEUS + '/api/v1/query?query=' + expr
    try:
        return json.loads(requests.get(url=url).content.decode('utf8', 'ignore'))['data']['result']
    except Exception as e:
        print(e)
        return {}

def get_interval(argv):
    try:
        opts, args = getopt.getopt(argv,"hi:")
    except getopt.GetoptError:
        print 'test.py -i <detect interval>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <detect interval>'
            sys.exit()
        elif opt in ("-i"):
            try:
                global interval
                interval = int(arg)
            except: 
                print("please input a integer interval!" + arg + " is invalid!")
                exit(1)

if __name__ == '__main__':
    get_interval(sys.argv[1:])
    print(interval)
    while True:
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
        print(detect_obj.value_predict(data))
        time.sleep(interval)
        
# ALERT_URL = "http://alert-catcher.hf.free4inno.com/alerts"

# def send_alert(alert_json):
#     data = alert_json
#     headers = {'Content-Type': 'application/json'}
#     responses = requests.post(url=ALERT_URL, headers=headers, data=data)