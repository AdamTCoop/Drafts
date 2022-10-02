with open('names.txt', 'r') as read_file:
    for line in read_file.read().splitlines():
        print(line)
print()

nowa_pozycja = 'Luke'
with open('names.txt', 'a') as write_file:
        write_file.write(nowa_pozycja)

print()

with open('names.txt', 'r') as read_file:
    for line in read_file.read().splitlines():
        print(line)