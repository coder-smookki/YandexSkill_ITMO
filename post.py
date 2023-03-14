import requests
from datetime import datetime
import threading

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def asd():
    startTime = datetime.now()
    res = requests.post('https://ssdteam.ru:2083', {'hehehe': 'hehehehehehe'})
    endTime = datetime.now()
    print('Time: ' + str(endTime - startTime))
    print(res)

set_interval(asd, 0.5)



