patient = {
    "name" : "ahmed",
    "age" : 45,
    "city": "lahore",
    "diagnosis" : "diabetes"
}

print(patient["name"])

patient["age"] = 46
patient["status"] = "active"

for key, value in patient.items():
    print(key, value)