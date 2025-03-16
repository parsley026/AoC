with open('zad2', 'r') as file:
    lines = file.read().strip().split('\n')

result1 = 0
result2 = 0

for line in lines:
    vals = list(map(int, line.split('x')))

    # surface area calculation
    l, w, h = vals
    area = 2 * (l * w + w * h + h * l)
    min_side_area = min(l * w, w * h, h * l)
    result1 += area + min_side_area

    # ribbon calculation
    sorted_sides = sorted(vals)
    perimeter = 2 * (sorted_sides[0] + sorted_sides[1])
    volume = l * w * h
    result2 += perimeter + volume

print(result1)
print(result2)