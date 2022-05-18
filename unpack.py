numbers = (1, 2, 3)

# x = numbers[0]
# y = numbers[1]
# z = numbers[2]

x, y, z = numbers
print(z)

x, _, _ = numbers
print(x)


x, *y = numbers
print(x)
print(y)