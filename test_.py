import json


x = [{
    "name" : "John",
    "age" : 45,
    "color": "Blue"
},
{
    "name" : "Doe",
    "age" : 56,
    "color": "Red" 
}]

"""
testSav = open("save.json", "w")

json.dump(x, testSav, indent=4, sort_keys=False)

testSav.close()


loadedjson = open("save.json", encoding="utf-8")
file = loadedjson.read()
x = json.loads(file)
for i in x:
    print(i.items())

"""
#Dumping the Pyhton object to a json file stored in a variable y
y = json.dumps(x)

#loadiing the variable y which contains serialize json file
j = json.loads(y)
print(j[0])
print(type(y))

