counts = {}

for die1 in range(1, 7):
    for die2 in range(1, 7):
        total = die1 + die2
        if total in counts:
            counts[total] = counts[total] + 1
        else:
            counts[total] = 1

print(counts)