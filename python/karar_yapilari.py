"""
age = input("Yaşı giriniz: ")
if age.isdigit():
    age = int(age)
    age += 1
print(age)
print(type(age15))
"""
"""
SYS_USER_NAME = "volkan"
user_name = input("Kullanıcı adı giriniz: ").lower()
# user_name = user_name.lower()
if SYS_USER_NAME == user_name:
    print("Kullanıcı adı doğru")
else:
    print("Kullanıcı adı yanlış")

print("...")
"""
"""
age = input("Yaşı giriniz: ")
if age.isdigit() and int(age) >= 18:
    print("Yaşınız 18'den büyük veye eşit")
else:
    print("Yaşınız 18'den küçük")
"""

# Notlarıalıyoruz
not1 = input("1. Notu giriniz: ")
not2 = input("2. Notu giriniz: ")
# veriler sayısal değilse uyarı veriyoruz
if not not1.isdigit() and not not2.isdigit():
    print("Lütfen sadece sayısal değer giriniz")
    # veriler sayısal ise int'e çeviriyoruz
else:
    not1 = int(not1)
    not2 = int(not2)
    # ortalama hesaplanıyor
    ortalama = (not1 + not2) / 2
    # ortalama 90'dan büyükse AA
    if ortalama >= 90:
        print("AA")
    # ortalama 85'den büyükse BA
    elif ortalama >= 85:
        print("BA")
    # ortalama 80'den büyükse BB
    elif ortalama >= 80:
        print("BB")
    # ortalama 75'den büyükse CB
    elif ortalama >= 75:
        print("CB")
    # ortalama 70'den büyükse CC
    elif ortalama >= 70:
        print("CC")
    # ortalama 65'den büyükse DC
    elif ortalama >= 65:
        print("DC")
    # ortalama 60'dan büyükse DD
    elif ortalama >= 60:
        print("DD")
    # ortalama 55'den büyükse FD
    elif ortalama >= 55:
        print("FD")
    # ortalama 55'den küçükse FF
    else:
        print("FF")
