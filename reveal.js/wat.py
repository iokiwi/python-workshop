a = 250
b = 250

for _ in range(10):
    if a is b:
        a += 1
        b += 1
        continue
    else:
        break

a = 250
b = 250

for _ in range(10):
    if a == b:
        a += 1
        b += 1
        continue
    else:
        break

# What is the value of a and b?
print(a, b)


a = 256
b = 256

a is b
