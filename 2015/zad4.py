import hashlib

with open('zad4', 'r') as file:
    data = file.read()

result1 = ''
result2 = ''

i = 1
while True:
    hash_value = hashlib.md5((data + str(i)).encode()).hexdigest()

    # 5 zeros
    if not result1 and hash_value[:5] == '00000':
        result1 = (data + str(i))

    # 6 zeros
    if not result2 and hash_value[:6] == '000000':
        result2 = (data + str(i))

    if result1 and result2:
        break

    i += 1

print(result1)
print(result2)