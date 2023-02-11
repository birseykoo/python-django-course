# Boş liste

liste = []

# İçinde bilgi olan lise

liste1 = [1, 2, 3, 4, 5]

# Liste hanig tür verileri kabul eder

liste2 = [1, 2, 3, 4, 5, "Volkan", "Kaya", 1.5, 2.5, True, False]

# Liste içine eleman ekleme

liste.append(1)

liste.append(2)

# Liste içindeki bilgiye erişmek

print(liste[0])

print(liste2[9])

print(len(liste2))

print(liste2[len(liste2) - 1]) # En son öğe

print(liste2[-1]) # En son öğe

# Bellir bir yere öğe eklemek

liste2.insert(10, "Volkan")
liste2.insert(len(liste2),"en son")

print(liste2)

# Bellir bir bölümü listelemek

print(liste2[0:3])

print(liste2[0:10:2])

print(liste2[3:])

# Listeyi ters çevir

print(liste2[::-1])

# STEP belirleyerek bilgileri al

print(liste2[::2])

# liteyi kopyalamak

liste3 = liste2.copy()

print(liste3)

# Listeyi birleştirmek

liste4 = liste2 + liste3

print(liste4)

# İç içe liste tanımlama

liste5 = [1, 2, 3, 4, 5, [6, 7, 8, 9, 10]]

print(liste5[5][2])

# Kaç öğe var

print(len(liste5))

# Öğe var mı

print(1 in liste5)

# Bir öğe kaç kez var

print(liste5.count(1))

# Öğe indexi

print(liste5.index(1))

# öğe adlarını sil remove

liste5.remove(1)

print(liste5)

# Son öğeyi çıkar

liste5.pop()

print(liste5)

# x indexli öğeyi çıkart

liste5.pop(0)

print(liste5)

# listeyi boşalt

liste5.clear()

# içindeki öğeleri topla

liste6 = [1, 2, 3, 4, 5]

print(sum(liste6))

# En küçük

print(min(liste6))

# En büyük

print(max(liste6))

# Ortalama

print(sum(liste6) / len(liste6))

# Listeyi sırala

liste6.sort()

print(liste6)


# İç içe listeler

liste7 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

print(liste7)

print(liste7[0])

print(liste7[0][1])

# İç içe listeleri sırala

liste7.sort()

print(liste7)

# İç içe listeleri ters çevir

liste7.reverse()

print(liste7)

# İç içe liste öğe silmek

liste7[1].pop(0)
liste7[0].pop(4)

print(liste7)

