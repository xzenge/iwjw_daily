from datetime import datetime

now = datetime.now().strftime('%Y%m%d')
tag = '工作日报{0}-史翔'.format(now)
print(tag)