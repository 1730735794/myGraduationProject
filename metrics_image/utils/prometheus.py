import json
import requests
from utils.config import Config

def get_prometheus_data(expr):
    url = Config.PROMETHEUS + '/api/v1/query?query=' + expr
    try:
        return json.loads(requests.get(url=url).content.decode('utf8', 'ignore'))['data']['result']
    except Exception as e:
        print(e)
        return {}


if __name__ == '__main__':
    results = get_prometheus_data("1- sum(increase(node_cpu_seconds_total{mode='idle'}[50m])) by (instance)/sum(increase(node_cpu_seconds_total[50m])) by (instance)")
    for result in results:
        print(' {metric}: {value[1]}'.format(**result))