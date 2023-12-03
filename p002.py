sequence = [1, 1]
sum = 0

while not sequence[-1] >= 4000000:
    if sequence[-1] and sequence[-2]:
        sequence.append(sequence[-1] + sequence[-2])

sequence.pop()
for x in sequence:
    if x % 2 == 0:
        sum += x

print(sum)
