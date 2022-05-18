# kamus= sbuah struktru data yg bisa menyimpan data dalam bentuk key atau value nlai

user = {
    "nama": "Agung Setiawan",
    "age": 30,
    "is_admin": True
}

# name = user["nama"]
# age  = user["age"]
# is_admin = user["is_admin"]

# print(name)
# print(age)
# print(is_admin)

user["Username"] = "Nursam Halal"
user["name"] = "Syammm"

temp = user.get("Username", "syam")
temp = user.get("name")

print(temp)