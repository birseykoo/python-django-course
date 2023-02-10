first_name = input("Adınızı Giriniz: ")
last_name = input("Soyadınızı Giriniz: ")
year_of_birth = input("Yaşınızı Giriniz: ")

character_length = f'İsim Soyisim Karakter uzunluğu: {len(first_name+last_name)}'
full_name = f'{first_name[0]}. {last_name[0]}'.upper()
age_after_five_years = f'Şimdiki Yaşınız: {year_of_birth}\nBeş Yıl sonra {int(year_of_birth)+5} yaşında olacaksınız'
age_of_majority = f'Yaşınız: {year_of_birth}\n18 Yaşından Büyüksünüz' if int(year_of_birth) > 18 else f'Yaşınız: {year_of_birth}\n18 Yaşından Küçüksünüz'


print(character_length)
print(full_name)
print(age_after_five_years)
print(age_of_majority)
