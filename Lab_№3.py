import http.client
import json
conn = http.client.HTTPConnection("167.172.172.227:8000")
conn.request('GET', '/number/7',)
r1 = conn.getresponse().read().decode()
# метод .loads преобразует строку в формате JSON в объект Python
r1_json = json.loads(r1)
print(r1_json['number'])

conn.request('GET', '/number/?option=7',)
r2 = conn.getresponse().read().decode()
r2_json = json.loads(r2)
print(r2_json)
if r2_json["operation"] == "sum":
    res2 = r1_json["number"] + r2_json["number"]
elif r2_json["operation"] == "sub":
    res2 = r1_json["number"] - r2_json["number"]
elif r2_json["operation"] == "mul":
    res2 = r1_json["number"] * r2_json["number"]
elif r2_json["operation"] == "div":
    res2 = r1_json["number"] / r2_json["number"]
res2 = int(res2)
print(res2)

headers = {'Content-type': 'application/x-www-form-urlencoded'}
conn.request('POST', '/number/', 'option=7', headers)
r3 = conn.getresponse().read().decode()
r3_json = json.loads(r3)
print(r3)
if r3_json["operation"] == "sum":
    res3 = res2 + r3_json["number"]
elif r3_json["operation"] == "sub":
    res3 = res2 - r3_json["number"]
elif r3_json["operation"] == "mul":
    res3 = res2 * r3_json["number"]
elif r3_json["operation"] == "div":
    res3 = res2 / r3_json["number"]
res3 = int(res3)
print(res3)

headers = {'Content-type': 'application/json'}
conn.request('PUT', '/number/', '{"option":7}', headers)
r4 = conn.getresponse().read().decode()
r4_json = json.loads(r4)
print(r4_json)
if r4_json["operation"] == "sum":
    res4 = res3 + r4_json["number"]
elif r4_json["operation"] == "sub":
    res4 = res3 - r4_json["number"]
elif r4_json["operation"] == "mul":
    res4 = res3 * r4_json["number"]
elif r4_json["operation"] == "div":
    res4 = res3 / r4_json["number"]
res4 = int(res4)
print(res4)

conn.request('DELETE', '/number/', '{"option":7}',)
r5 = conn.getresponse().read().decode()
r5_json = json.loads(r5)
print(r5_json)
if r5_json["operation"] == "sum":
    res5 = res4 + r5_json["number"]
elif r5_json["operation"] == "sub":
    res5 = res4 - r5_json["number"]
elif r5_json["operation"] == "mul":
    res5 = res4 * r5_json["number"]
elif r5_json["operation"] == "div":
    res5 = res4 / r5_json["number"]
res5 = int(res5)
print(res5)






