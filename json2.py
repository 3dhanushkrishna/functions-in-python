import json as j
data = {"name":"dhanush","status":"student"}
jsondata = j.dumps(data)
myjsondata = j.loads(jsondata)
print(myjsondata["status"])