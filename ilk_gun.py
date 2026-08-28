rehber = {}

while True:
    isim = input("isim gir: ")
    numara = input("numara gir: ")

    rehber[isim] = numara

    devam = input("Devam etmek istiyormusun? (e/h): ")

    if devam == "h":
        break

print("Rehber:", rehber)


aranan = input("Aramak istediğin isim: ")
if aranan in rehber:
    print("Numara:", rehber[aranan])
else:
    print("Kişi bulunamadı")

silinecek = input("Silmek istediğin isim: ")

if silinecek in rehber:
    del rehber[silinecek]
    print("Silindi")
else:
    print("Kişi bulunamadı")

print("Güncel rehber:", rehber)

    
                                                                                                                                                               


                          