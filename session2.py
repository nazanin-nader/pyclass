# Primitive types
# Integer-valued variable
x = 5 # int
print(x)
print(2 * x)

# real-valued variable
y = 2.5  # float

print(y)

print(2//y)

# text-valued
s = "Nazanin Nader"  # string

print(s)

# Array-valued variable
array = ["Nazanin Nader", "Bahar Bazargan"]
print(array)

array.append("Nima Hamidi")
print(array)
array.extend(["Taghi", "Naghi"])
# array.append(["Taghi", "Naghi"])
print(array)

array.extend(["taghi"])
print(array)

# Dictionary
d = {"nima": 5, "nazanin": 6.5, "bahar": [2, 4, 3]}
print(d)

# End of primitive types

# conditionals
if y > 0:
    print(y)
else:
    print(-y)

y = -3.7

if y > 0:
    print(y)
else:
    print(-y)

# Loop
print("before for:")
for i in array:
    print(i)

print("printing keys of a dictionary:")
for k in d.keys():
    print(k)

print()
print("printing values of a dictionary:")
for v in d.values():
    print(v)

print()
print("printing items of a dictionary:")
for k in d.keys():
    print(k, ":", d[k])

print()
print("printing items of a dictionary(method2):")
for k, v in d.items():
    print(k, ":", v)
    
# Functions
