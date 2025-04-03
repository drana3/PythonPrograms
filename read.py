# importing the module
import json

# reading the data from the file
with open("dictionary.txt") as f:
    data = f.read()

print("Data type before reconstruction : ", type(data))

# reconstructing the data as a dictionary
js = json.loads(data)

print("Data type after reconstruction : ", type(js))
print(js)


with open("test.txt") as f:
    data = f.read()

js = json.loads(data)
