import json as j
data = '{"name":"dhanush","status":"student"}'
myjsondata = j.loads(data)
print(myjsondata["status"])