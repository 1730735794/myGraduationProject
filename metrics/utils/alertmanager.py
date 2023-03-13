# -*- coding: UTF-8 -*-

import json
import datetime
import random
import string
import requests
from utils.config import Config


def create_string_number(n):
    """生成一串指定位数的字符+数组混合的字符串"""
    m = random.randint(1, n)
    a = "".join([str(random.randint(0, 9)) for _ in range(m)])
    b = "".join([random.choice(string.ascii_letters) for _ in range(n - m)])
    return ''.join(random.sample(list(a + b), n))

def create_alert_json(summary, description):
    now = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    contain_dict_list = []
    annotations_dict = {
        "summary": summary,
        "description": description
    }
    contain_dict = {
        "fingerprint": create_string_number(16),
        "startsAt": now,
        "annotations": annotations_dict,
        "endsAt":  "0001-01-01T00:00:00Z",
        "labels": {
            "job": "ops_components"
        }
    }
    contain_dict_list.append(contain_dict)
    pre_json = {"alerts": contain_dict_list}
    alert_json = json.dumps(pre_json)
    return alert_json

def send_alert(summary, description):
    data = create_alert_json(summary, description)
    headers = {'Content-Type': 'application/json'}
    responses = requests.post(Config.ALERT_URL, headers=headers, data=data)
    print("Send new alert: \n" + data)
    print("Response: \n" + str(responses))