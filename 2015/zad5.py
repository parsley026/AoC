with open('zad5', 'r') as file:
    lines = file.read().split('\n')

result1 = 0
result2 = 0

vowels = ['a', 'e', 'i', 'o', 'u']
invalid_substrings = ['ab', 'cd', 'pq', 'xy']

for line in lines:
    if any(sub in line for sub in invalid_substrings):
        continue

    vowelCount = sum(1 for char in line if char in vowels)

    flag1 = False
    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            flag1 = True
            break

    if vowelCount >= 3 and flag1 == True:
        result1 += 1

print(result1)

for line in lines:
    flag1 = False
    for i in range(len(line) - 1):
        for j in range(len(line) - 1):
            if i != j and i - 1 != j and i + 1 != j and line[i:(i + 2)] == line[j:(j + 2)]:
                flag1 = True
                break

    flag2 = False
    for i in range(len(line) - 2):
        if line[i] == line[i + 2]:
            flag2 = True
            break

    if flag1 == True and flag2 == True:
        result2 += 1

print(result2)

