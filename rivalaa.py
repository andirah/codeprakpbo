class Bangun_Ruang:
    __vendor_message = "ini adalah segitiga"
    name   = "" #deklarasi variabel
    alas   = ""
    tinggi = ""
    luas   = ""

    def __init__(self, name): #method konstruktor
        print ("Ini adalah konstruktor")
        self.name = name
    def get_vendor_message(self): # method biasa
        print(self.__vendor_message)

    def set_alas (self,alas):
        self.alas = alas

    def set_tinggi (self,tinggi):
        self.tinggi = tinggi

    def set_luas (self,luas):
        self.luas = luas

segi = Bangun_Ruang("segitiga pertama")

segi.set_alas(7)
segi.set_tinggi(8)

segi.luas = 0.5 * segi.alas * segi.tinggi

segi.get_vendor_message()
print("%s\n alas segitiga adalah : %d \n Tinggi segitiga adalah : %d \n Luas segitiganya adalah : %s\n" % (segi.name,segi.alas,segi.tinggi,segi.luas))

