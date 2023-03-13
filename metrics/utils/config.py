class Config:
    ALERT_URL = '' #"http://alert-catcher.hf.free4inno.com/alerts"
    PROMETHEUS = '' #'http://124.221.127.211:30000'
    min = 1

def Setup(prometheus_url, alertmanager_url, min):
    Config.ALERT_URL = str(alertmanager_url)
    Config.PROMETHEUS = str(prometheus_url)
    Config.min = min
    print(Config.PROMETHEUS, Config.ALERT_URL, min)