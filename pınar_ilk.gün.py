
import random

tutulan_sayi = random.randint(1, 10)
hak = 3

while True:
tahmin} = int(input("Tahmin et: "))

if tahmin == tutulan_sayi:
print("BİLDİN")
break
elif tahmin > tutulan_sayi:
print("DAHA KÜÇÜK BİR SAYI")
hak = hak - 1
print("Kalan hak:", hak)
else:
print("DAHA BÜYÜK BİR SAYI")
hak = hak - 1
print("Kalan hak:", hak)

if hak == 0:
print("Hakkın bitti, sayı:", tutulan_sayi)
break