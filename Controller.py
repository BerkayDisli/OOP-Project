from anaekran import Model
from View import View
import json
class Controller:
 def baslat():
  while True:
    View.viewbaslat()
    print("Lütfen yapmak istediğiniz işlemi seçin : ")
    giris=input()
    if giris not in ["0","1","2","3","4","5"]:
        print("Hatalı giriş !!!")
    elif giris == "0":
        print("Çıkış seçildi")
        exit(0)
    elif giris == "1":
        return Controller.kisiekleme()
    elif giris == "2":
        return Controller.kisiarama()
    elif giris == "3":
        return Controller.kisiguncelle()
    elif giris == "4":
        return Controller.kisisilme()
    elif giris == "5":
        return Controller.kisilistele()

    else :
        print("yanlış bir giris yaptınız ")
 def kisisayisi():
    kisisayi=Model.kisisayisi()
    return View.viewkisisayisi(kisisayi)

 def kisiguncelle():
    print("Lütfen güncellemek istediğiniz kimlik no'yu girin")
    kimlikno=input()
    x = input("Kimlik numarasını girdiğiniz kişinin hangi verisini güncellemek istiyorsunuz?"
              "\n1- Adı "
              "\n2- Soyadı "
              "\n3- Baba Adı"
              "\n4- Anne Adı"
              "\n5- Doğum Yeri"
              "\n6- Medeni Durumu"
              "\n7- Kan Grubu"
              "\n8- Kütük Şehiri"
              "\n9- Kütük İlçesi"
              "\n10- İkametgah Şehri"
              "\n11- İkametgah İlçesi")
    guncellenenveri=input("Değiştirmek istediğiniz bilgiyi girin")
    if kimlikno in Model.kimlikliste():
        if int(x) in range(1,12):
            a=Model()
            a.kisiguncelle(kimlikno,x,guncellenenveri)

            return View.viewkisiguncelle(kimlikno,guncellenenveri)
        else:
            print("Güncellemek istediğiniz veri girişini yanlış seçtiniz")
    else:
        print("Belirtilen kimlik no nüfus sistemimizde bulunmamaktadır")


 def kisiekleme():
    ad = input("Kaydı yapılacak yeni kişinin adı? ")
    soyad = input("Kaydı yapılacak yeni kişinin soyadı? ")
    babaad = input("Kaydı yapılacak yeni kişinin baba adı? ")
    annead = input("Kaydı yapılacak yeni kişinin anne adı? ")
    dogumyer = input("Kaydı yapılacak yeni kişinin doğum yeri? ")
    medenidurum = input("Kaydı yapılacak yeni kişinin medeni durumu? (Bekar/Evli) ")
    kangrup = input("Kaydı yapılacak yeni kişinin adı? (örn. A rH +) ")
    kutukil = input("Kaydı yapılacak yeni kişinin kütük şehri? ")
    kutukilc = input("Kaydı yapılacak yeni kişinin kütük ilçesi? ")
    ikametil = input("Kaydı yapılacak yeni kişinin ikametgah ettiği şehir? ")
    ikametilc = input("Kaydı yapılacak yeni kişinin ikametgah ettiği ilçe? ")
    Kisiekle=Model()
    Kisiekle.kayitgir(ad, soyad, babaad, annead, dogumyer, medenidurum, kangrup, kutukil, kutukilc, ikametil, ikametilc)
    return View.viewkisiekle(ad,soyad)
 def kisiarama():
    kimlikno = input("Görmek istediğiniz kişinin kimlik numarasını giriniz. >> ")
    kisiara=Model.arama(kimlikno)
    return View.viewkisiarama(kimlikno)

 def kisilistele():
    kisilisteleme=Model.databaselisteleme()
    return View.viewkisilistele(kisilisteleme)


 def kisisilme():
    kimlikno=input("Silmek istediğiniz kişinin kimlik no'sunu girin")
    print("Silmek istediğiniz kişinin bilgileri : ")
    Model.arama(kimlikno)
    kisisil=Model()
    kisisil.kisisilme(kimlikno)
    return View.viewkisisil(kimlikno)

while True:
    Controller.baslat()