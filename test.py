a = 43
b = "23"

print(type(a*b))

l1 = [1, 2, 3]
l2 = [3, 4, 5]

l1.extend(l2)
combined = list(set(l1))

print(combined)


def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]


word1 = "Bike"

print(reverse(word1))

print(word1)
