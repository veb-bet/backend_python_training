import math
print(math.sqrt(16))  # Выведет: 4.0
from math import sqrt
print(sqrt(16))  # Выведет: 4.0
import mymodule
print(mymodule.greet("Alice"))  # Выведет: Hello, Alice!
import os
print(os.getcwd())  # Выведет текущую рабочую директорию
import sys
print(sys.version)  # Выведет версию Python
import datetime
current_time = datetime.datetime.now()
print(current_time)  # Выведет текущую дату и время
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

with open('example.txt', 'w') as file:
    file.write("Hello, World!")

with open('example.bin', 'rb') as file:
    content = file.read()
    print(content)

with open('example.bin', 'wb') as file:
    file.write(b'Hello, World!')
    
import json
data = {"name": "Alice", "age": 25}
with open('data.json', 'w') as file:
    json.dump(data, file)
import json
with open('data.json', 'r') as file:
    data = json.load(file)
print(data)

import csv
with open('data.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
import csv
data = [["Name", "Age"], ["Alice", 25], ["Bob", 30]]
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)