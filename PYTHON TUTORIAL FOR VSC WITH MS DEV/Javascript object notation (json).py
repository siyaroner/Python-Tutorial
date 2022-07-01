""" Many wev services return data as JSON
JSON is a standard data format that an be intimidating at first glance

Using a linting too to format JSON makes it easier to read

JSON  contains key pairs
"key":"value"

To retrieve the value from a "key":"value" request the key name
"""
# you can create "key":"value" json objects from a dictionary
#create a dictionary object
import json
person_dict= {"first":"Muhammed(as)","last":"Emin"}
#add additional key pairs as needed to dictionary
person_dict["City"]="Mekke"
#Convert dictionary to json object
person_json=json.dumps(person_dict)
print(person_json)

""" Nest dictionaries to create JSON in the format {"key":{"subkey0":"subvalue0","subkey1":"subvalue1",... }}
"""
person_dict= {"first":"Muhammed(as)","last":"Emin"}
#create staff dictionary which assigns a person to a role
staff_dict={}
staff_dict["Program Manager"]=person_dict
#Convert dictionary to json object
staff_json=json.dumps(staff_dict)
print(staff_json)
""" Add lists to the dictionary to create JSON in the format {"key":["listvalue0","listvalue1","listvalue2",... ]}
"""
person_dict= {"first":"Muhammed(as)","last":"Emin"}
#create a list object of programming languages
languages_list=["CSharp","Python","javascript"]
#Add list to dictionary
person_dict["languages"]=languages_list
# Convert dictionary to JSON objects
person_json=json.dumps(person_dict)
print(person_json)