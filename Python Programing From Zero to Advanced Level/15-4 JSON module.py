import json
from platform import python_version

person={"name":"Ali","last_name":"Veli","languages":["python","C"],}
print(person["name"])
# json sting to dic
person_string='{"name":"Ali","languages":["python","C"]}'
print(json.loads(person_string)) # loads json dict çevirir
print((json.loads(person_string))["languages"])

with open("person.json") as f:
    data=json.load(f) # load json dosyasýný okur
    print(data["name"])
    print(data["languages"])

# dict to json string
print(type(json.dumps(person)))
with open ("person.json", "a") as f:
    json.dump(person,f) # dump kayýt iþlemi yapar

print(json.dumps(person,indent=4,sort_keys=True)) #dumps kayýt edilebilir json formata dönüþtürür