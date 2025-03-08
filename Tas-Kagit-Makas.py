from random import randint

puan = 0
while True:
    secenek = ["Taş", "Kağıt", "Makas,3"] or ["1", "2", "3"]
    bilgisayar = secenek[randint(0, 2)]
    kullanici = input("\n1.Taş mı? \n2.Kağıt mı? \n3.Makas mı? \nSeçiminizi Yapınız: ")
    if kullanici == bilgisayar:
        print("Berabere!")
    elif kullanici == "Taş" or kullanici == "1":
        if bilgisayar == "Kağıt":
            print("Bilgisayar kazandı!")
            puan = puan - 1
        else:
            print("Kullanıcı kazandı!")
            puan = puan + 1
    elif kullanici == "Kağıt" or kullanici == "2":
        if bilgisayar == "Makas":
            print("Bilgisayar kazandı!")
            puan = puan - 1
        else:
            print("Kullanıcı kazandı!")
            puan = puan + 1
    elif kullanici == "Makas" or kullanici == "3":
        if bilgisayar == "Taş":
            print("Bilgisayar kazandı!")
            puan = puan - 1
        else:
            print("Kullanıcı kazandı!")
            puan = puan + 1
    else:
        print("Geçersiz seçenek!")
    print("Puanınız: ", puan)