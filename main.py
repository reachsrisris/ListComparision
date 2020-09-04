a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# Solution 1
print(set(a) & set(b))

#solution 2
print(set(a).intersection(b))

#Solution 3
print([x for x in a if x in b])

#print(all(i == j for i, j in zip(a, b)) )
