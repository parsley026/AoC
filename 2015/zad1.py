with open('zad1', 'r') as file:
    data = file.read().strip()

# final floor
result1 = data.count('(') - data.count(')')
print(result1)

# first position reaching basement
result2 = 0
for i, char in enumerate(data, start=1):
    result2 += 1 if char == '(' else -1
    if result2 == -1:
        print(i)
        break