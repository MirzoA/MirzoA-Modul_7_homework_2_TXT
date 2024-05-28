my_file = 'My_soul.txt'
with open(my_file, mode='r', encoding='utf-8') as file:
    for line in file:
        print(line)
print(file.closed)