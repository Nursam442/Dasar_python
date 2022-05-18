name = "Nursam Halal"

if len(name) > 3:
    print("Welcome")
else: 
    print("Nama Terlalu pendek")

print("==============================")

name = "al"

if len(name) > 3 or True:
    print("Welcome")
else: 
    print("Nama Terlalu pendek")


print("==============================")


name = "al"
by_pass_validation = False

if len(name) > 3 or by_pass_validation:
    print("Welcome")
else: 
    print("Nama Terlalu pendek")