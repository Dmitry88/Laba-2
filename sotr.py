ivan = {
    "name": "ivan",
    "age": 34,
    "children": [{
        "name": "vasja",
        "age": 17,
        }, {
        "name": "petja",
        "age": 13,
        }],
    }

darja = {
    "name": "darja",
    "age": 41,
    "children": [{
        "name": "kirill",
        "age": 21,
        }, {
        "name": "pavel",
        "age": 19,
        }],
    }

emps = [ivan, darja]

for i in emps:
    for ages in i.get('children'):
        if ages.get('age') >= 18:
            print (i.get("name"))
        break
        
