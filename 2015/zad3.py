with open('zad3', 'r') as file:
    data = file.read()

result1 = 0
result2 = 0

# single santa

x = 0
y = 0

coordinates = [(0, 0)]

for char in data:
    if char == '^':
        x += 1
    elif char == '>':
        y += 1
    elif char == 'v':
        x -= 1
    elif char == '<':
        y -= 1

    coordinates.append((x, y))

result1 = len(set(coordinates))
print(result1)


# double santa

x = [0, 0]
y = [0, 0]

coordinates = [[(0, 0)], [(0, 0)]]
agent = 0

for char in data:
    if char == '^':
        x[agent] += 1
    elif char == '>':
        y[agent] += 1
    elif char == 'v':
        x[agent] -= 1
    elif char == '<':
        y[agent] -= 1

    coordinates[agent].append((x[agent], y[agent]))

    if agent == 0:
        agent = 1
    else:
        agent = 0

result2 = len(set(coordinates[0] + coordinates[1]))
print(result2)


