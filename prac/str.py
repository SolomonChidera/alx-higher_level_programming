per = {'name': 'Dera', 'age': 19}
print("Hello, {name}. you are {age}".format(name=per['name'], age=per['age']))
print("Hello, {name}. you are {age}".format(**per))
