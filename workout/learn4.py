inst = {
    "minh" : 32,
    "thao": 18,
    "long" : 20,
    "minh": 44
}

inst_name = list(filter(lambda key: inst[key] > 20, inst.keys()))
print(inst_name)
#print(inst["minh"])