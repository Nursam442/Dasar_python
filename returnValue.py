from operator import length_hint


def halo_user(name, level):
    print(f"Halo {name} - {level}")
    print("selamat Belajar python")
    return 100

# print("start")
# halo_user("Nursam", 2)
# halo_user(10, "Nursam")
# halo_user(level=10, name="Nursam") # keyword argument
# # calculate_total_cost(total_price=1000000, shipping_cost=50000, discount=50000)

# print("Finish")

# length = len([1, 2, 3])
# print(length)

temp = halo_user("Agung", 10)
print(temp)