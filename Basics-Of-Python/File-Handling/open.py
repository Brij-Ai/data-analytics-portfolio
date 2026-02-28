from pathlib import Path

path = Path(r"C:\Users\Dell\Documents\One_DRIVE\OneDrive\Desktop\t.txt")

with path.open('r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')

file2 = open('xXx.txt','r', encoding='utf-8')

print(file2.read())

for line in file2:
    print(line);