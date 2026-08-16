def dot_product(v1, v2):
    products = []
    for i in range(len(v1)):
        products.append(v1[i] * v2[i])
    return sum(products)




visit1 = [45, 90, 20]
visit2 = [45, 92, 10]

scaled = []
changes = []
total = []
product = []

for i in range(len(visit1)):
    diff = visit1[i] - visit2[i]
    add = visit1[i] + visit2[i]

    changes.append(diff)
    scaled.append(visit1[i] * 2)
    total.append(add)
    product.append(visit1[i] * visit2[i])



print(changes)
print(scaled)
print(total)
print(product)
print(dot_product(visit1, visit2))
