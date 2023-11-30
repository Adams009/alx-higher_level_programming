#!/usr/bin/python3

with open("variable_load_5.py", "r") as file:
    code = compile(file.read(), "variable_load_5.py", 'exec')

namespace = {}
exec(code, namespace)

print(namespace['a'])

if __name__ == "__main__":
    pass
