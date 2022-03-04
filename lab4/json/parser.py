import json

n = open('sampledata.json').read()
data = json.loads(n)

print(
    "================================================================================" "\n"
"DN                                                 Description           Speed    MTU" "\n"
"-------------------------------------------------- --------------------  ------  ------ ")

imdata = data["imdata"]
for i in imdata:
        dn = i["l1PhysIf"]["attributes"]["dn"]
        description = i["l1PhysIf"]["attributes"]["descr"]
        speed = i["l1PhysIf"]["attributes"]["speed"]
        mtu = i["l1PhysIf"]["attributes"]["mtu"]
        print("{0:50} {1:20} {2:7} {3:6}".format(dn,description,speed,mtu))