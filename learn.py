def check_temp(temp):
    if temp <0:
        return "freezing"
    elif temp <=15:
        return "cold"
    else:
        return "warm"

results = []
results.append(check_temp(-4))
results.append(check_temp(5))
results.append(check_temp(34))
print(len(results))

for index, item in enumerate(results):
    print(index, item)