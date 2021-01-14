import json
import pprint
class Model:




    def kimlikliste():  # nüfus kayıtlarındaki kişilerin sadece kimlik numaralarını listeliyor
        Dosya = open("kisiler.json", "r", encoding="utf-8")
        veri = json.load(Dosya)
        Dosya.close()
        kimliklistesi = []
        for i in veri:
            kimliklistesi.append(i)
        return kimliklistesi

    def kisisayisi():  # program başlangıcında kişi sayısı isteniyor. bu fonk çalışacak
        Dosya = open("kisiler.json", "r", encoding="utf-8")
        veri = json.load(Dosya)
        Dosya.close()
        return len(veri)



    def kayitgir(self,adi,soyadi,babaadi,anneadi,dogumyeri,medenidurumu,kangrubu,kutuksehir,kutukilce,ikametgahsehir,ikametgahilce):  # menüdeki 1. komut




        k = Model.kisisayisi()
        yenikimlikno = k + 1
        datalar = Model.databaselisteleme()
        yenisozluk = {"adi": adi, "soyadi": soyadi, "babaadi": babaadi, "anneadi": anneadi, "dogumyeri": dogumyeri,
                      "medenidurumu": medenidurumu, "kangrubu": kangrubu, "kutuksehir": kutuksehir, "kutukilce": kutukilce,
                      "ikametgahsehir": ikametgahsehir, "ikametgahilce": ikametgahilce}
        datalar[str(yenikimlikno)] = yenisozluk  # sözlükte yeni kayıt artık var, json dosyasına yazdırılmalı.
        Dosya = open("kisiler.json", "w", encoding="utf-8")
        json.dump(datalar, Dosya, ensure_ascii=False)  # dosyaya yazdırıldı
        Dosya.close()
        print("Yeni kayıt girildi ve kaydedildi! ")


    def databaselisteleme():  # menüdeki 5. komut
        Dosya = open("kisiler.json", "r", encoding="utf-8")
        veri = json.load(Dosya)
        Dosya.close()
        return veri
        # bu fonksiyonu kullanırken print yerine pprint.pprint kullanmak daha iyi bi görüntü sağlar!


    def arama(kimno):  # menüdeki 2. komut
        veridosyasi = Model.databaselisteleme()


        if kimno in Model.kimlikliste():
            return pprint.pprint(veridosyasi[kimno])
        else:
            print("Yanlış giriş yaptınız!")




    def kisisilme(self,kimlikno):  # menüdeki 4. komut
        Dosya = open("kisiler.json", "r", encoding="utf-8")
        veri = json.load(Dosya)
        Dosya.close()
        veri = dict(veri)
        try:

            veri.pop(kimlikno)
            Dosya = open("kisiler.json", "w", encoding="utf-8")
            json.dump(veri, Dosya, ensure_ascii=False)
            Dosya.close()
        except Exception:
            print("Yanlış giriş yaptınız!")

    def kisiguncelle(self,kimlikno,guncellenecekveritipi,guncellenenveri):  # menüdeki 3. komut
        Dosya = open("kisiler.json", "r", encoding="utf-8")
        veri = json.load(Dosya)
        Dosya.close()
        if kimlikno in Model.kimlikliste():  # girilen kimlik no kayıtlarda var mı?

            if int(guncellenecekveritipi) in range(1, 12):  # girilen sayı menüde var mı?
                if guncellenecekveritipi == "1":
                    elm = "adi"
                elif guncellenecekveritipi == "2":
                    elm = "soyadi"
                elif guncellenecekveritipi == "3":
                    elm = "babaadi"
                elif guncellenecekveritipi == "4":
                    elm = "anneadi"
                elif guncellenecekveritipi == "5":
                    elm = "dogumyeri"
                elif guncellenecekveritipi == "6":
                    elm = "medenidurumu"
                elif guncellenecekveritipi == "7":
                    elm = "kangrubu"
                elif guncellenecekveritipi == "8":
                    elm = "kutuksehir"
                elif guncellenecekveritipi == "9":
                    elm = "kutukilce"
                elif guncellenecekveritipi == "10":
                    elm = "ikametgahsehir"
                elif guncellenecekveritipi == "11":
                    elm = "ikametgahilce"

                # Sözlüğe ulaşmak için eleman seçildi

                a = veri[kimlikno][elm]
                print(f"Değiştirmek istediğiniz veri: {a}")
                veri[kimlikno][elm] = guncellenenveri
                Dosya = open("kisiler.json", "w", encoding="utf-8")
                json.dump(veri, Dosya, ensure_ascii=False)
                Dosya.close()

            else:
                print("Yanlış giriş yaptınız! ")
        else:
            print("Yanlış kimlik numarası girildi! ")

    # !!ÖNEMLİ!!  Kimlikno alan fonksiyonlara kimlik no verilirken, string olarak yani tırnak içinde verilmeli!!!

