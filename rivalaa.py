class Bangun_Ruang:
    __vendor_message = "Segitiga"
    name    ="" #deklarasi variabel
    alas    =""
    tinggi  =""
    luas    =""

    def __init__(self, name):
        self.name = name

    def get_vendor_message(self):
        print(self.__vendor_message)

    def set_alas(self, alas):
        self.alas = alas

    def set_tinggi(self, tinggi):
        self.tinggi = tinggi

    def set_luas(self,luas ):
        self.luas = luas

segi = Bangun_Ruang("Objek Segitiga Pertama")
segi1 = Bangun_Ruang("Objek Segitiga Kedua")
segi2 = Bangun_Ruang("Objek Segitiga Ketiga")

segi.set_alas(7)
segi1.set_alas(8)
segi2.set_alas(9)

segi.set_tinggi(10)
segi1.set_tinggi(5)
segi2.set_tinggi(12)

segi.luas = 0.5 * segi.alas * segi.tinggi
segi1.luas = 0.5 * segi1.alas * segi1.tinggi
segi2.luas = 0.5 * segi2.alas * segi2.tinggi

segi.get_vendor_message()

print("%s\nAlas Segitiga adalah : %d \nTinggi Segitiga adalah : %d \nLuas Segitiga adalah : %s\n" % (segi.name, segi.alas, segi.tinggi,segi.luas))
print("%s\nAlas Segitiga adalah : %d \nTinggi Segitiga adalah : %d \nLuas Segitiga adalah : %s\n" % (segi1.name, segi1.alas, segi1.tinggi,segi1.luas))
print("%s\nAlas Segitiga adalah : %d \nTinggi Segitiga adalah : %d \nLuas Segitiga adalah : %s\n" % (segi2.name, segi2.alas, segi2.tinggi,segi2.luas))
