from anaekran import Model
import pprint

class View:
 def viewbaslat():
    print("Nüfus Yönetim Sistemi'ne Hoş Geldiniz")
    print(
        "\n Yeni kayıt oluşturmak için : 1 "
        "\n Kimlik No'ya göre kişi aratmak ve bilgilerini bastırmak için : 2"
        "\n Kimlik no'sunu girdiğiniz bir kişiyi güncellemek için : 3"
        "\n Kimlik no'sunu girdiğiniz bir kişiyi silmek için : 4"
        "\n Tüm veritabanındaki kişileri listelemek için : 5 giriniz"
        "\n Çıkış yapmak için : 0 giriniz"
    )
    print("Nüfus Yönetim Sistemimizdeki toplam kisi sayimiz : {}".format(Model.kisisayisi()))
 def viewkisisayisi(kisisayisi):
    print("Kişi sayısı : {} ".format(kisisayisi))


 def viewkisiguncelle(kimlik,guncelveri):
    print(" {} kimlik numaralı kişinin yeni verisi {} ile değiştirildi".format(kimlik,guncelveri))
    print("Bilgileri : ")
    Model.arama(str(kimlik))

 def viewkisiekle(ad,soyad):
    print("{} {} Nüfus Yönetim sistemine eklenmiştir".format(ad,soyad))
    print("Bilgileri : ")
    kimlikno=str(Model.kisisayisi())
    Model.arama(kimlikno)

 def viewkisiarama(kisiara):
    print(" {} kimlik numaralı kişinin bilgileri bastırıldı".format(kisiara))

 def viewkisilistele(kisilistele):
    print("Kisiler listeleniyor : ")
    pprint.pprint(kisilistele)


 def viewkisisil(kimlikno):
    print("{} kimlik numaralı kişi başarıyla silinmiştir".format(kimlikno))



