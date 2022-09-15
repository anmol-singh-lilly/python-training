s1 = set()
print(s1)

s1.add(1)
s1.add("anmol")
s1.add(1)
print(s1)


s2 = set({'bangalore', 'anmol', 10})
print(s2)

s3 = s1.union(s2)
print(s3)

s4 = s1.intersection(s2)
print(s4)