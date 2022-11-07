#dis is isis haar projectje
from datetime import datetime
now = datetime.now()

timestamp = datetime.timestamp(now)
timestamp = timestamp + 3600
dt_object = datetime.fromtimestamp(timestamp)
print(dt_object)
print("timestamp =", timestamp)