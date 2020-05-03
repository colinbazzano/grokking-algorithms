a = 43
b = "23"

print(type(a*b))

l1 = [1, 2, 3]
l2 = [3, 4, 5]

l1.extend(l2)
combined = list(set(l1))

print(combined)
