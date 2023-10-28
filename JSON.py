import json

data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    },
    "gender": "male"
}'''

# Devuelve un diccionario
info = json.loads(data)
print('Name:', info["email"]["hide"])