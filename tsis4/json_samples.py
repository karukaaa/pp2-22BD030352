import json

with open('sample-data.json', 'r') as read_file:
    data = json.load(read_file)


for a in range(3):
    for i, k in data["imdata"][a]["l1PhysIf"]["attributes"].items():
        if i == "dn":
            print(k, end=" ")
        if i == "mtu":
            print(k, end=" ")
        if i == "speed":
            print(k, "\n")


