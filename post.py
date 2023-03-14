import requests
from datetime import datetime

startTime = datetime.now()
res = requests.post('https://ssdteam.ru', {'hehehe': 'hehehehehehe'})
endTime = datetime.now()
print('Time: ' + str(endTime - startTime))
print(res)