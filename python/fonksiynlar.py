# fonksiyon def ile tanımlanır

# def fonksiyon_adi():

# bir veya daha fazla parametre alır

# def fonksiyon_adi(parametre1, parametre2, parametre3):

# defualt değer içerebilir

# def fonksiyon_adi(parametre1, parametre2, parametre3 = 5):

def hello1():
    return "Merhaba "


hello1()


def hello(name):
    print("Hello " + name)


hello("Volkan")


def hello(name="Volkan"):
    print("Hello " + name)


hello()
name2 = "volkan"


def hello():
    print(f'Merhaba {name2}')


hello()


def isim():
    print(f'{hello1()}{name2}')


isim()

# Kendi kendini çağıran fonkisyon


products = [
    ["iphone", 1000, 2],
    ["samsung", 2000, 3],
    ["xiaomi", 3000, 4],
    ["leptop", 5000, 5]
]


def print_items(items):
    for item in items:
        if not type(item) == list:
            print(item)
        else:
            print(item)

print_items(products)

# arg ve kwargs kullanımı

def user_info(user_name, password, *args,**kwargs):
      print(user_name, password, args)
      print(kwargs)

user_info("admin", "12345", first_name="volkan",last_name="çalışkan")