# Aralık belirterek for döngüsü ile çalışmak range

for item in range(1, 100):
    if item % 5 == 0:
        print(item)

# Liste içindeki verileri tek tek işlemek

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for item in liste:
    print(item)

# Liste içindeki verileri tek tek işlemek

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for item in enumerate(liste):
    print(item)
    print(item[0], item[1])


# list unpacking

user_info = ["admin", "12345"]

user_detail = ["admin", "123450", "volkancaliskan14@gmail.com", "mail@master"]

products = [
    ["iphone", 1000, 2],
    ["samsung", 2000, 3],
    ["xiaomi", 3000, 4],
    ["leptop", 5000, 5]
]

users = ["Ahmet", "Volkan", "Ayşe", "Nazım", "Hüseyin"]


for user in users:
    print(user)

for user in enumerate(users):
    print(user)

for user in enumerate(users, 1):
    print(user)

for product in products:
    print(product)

for product in products:
    print(product[0], product[1], product[2])

for product in products:
    print(f"Ürün adı: {product[0]} Fiyatı: {product[1]} Adedi: {product[2]}")

for product in enumerate(products):
    print(product)

for product in enumerate(products, 1):
    print(product)
