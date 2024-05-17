#Aşağıda ki örnekte 'Hesap Makinesi' adında bir sınıf oluşturduk ve içine toplama,çıkarma,çarpma,bölme,kare ve karekök fonksiyonlarını ekledik.

class Islemler:
    def __init__(self):
        self.sonuc = 0

    def toplama(self):
        while True:
            try:
                a = float(input("Toplanacak ilk sayıyı girin: "))
                b = float(input("Toplanacak ikinci sayıyı girin: "))
                self.sonuc = a + b
                break
            except ValueError:
                print("Hata: Geçersiz sayı girişi!")

    def cikarma(self):
        while True:
            try:
                a = float(input("Çıkarılacak sayıyı girin: "))
                b = float(input("Çıkarılacak diğer sayıyı girin: "))
                self.sonuc = a - b
                break
            except ValueError:
                print("Hata: Geçersiz sayı girişi!")

    def carpma(self):
        while True:
            try:
                a = float(input("Çarpılacak ilk sayıyı girin: "))
                b = float(input("Çarpılacak ikinci sayıyı girin: "))
                self.sonuc = a * b
                break
            except ValueError:
                print("Hata: Geçersiz sayı girişi!")

    def bolme(self):
        while True:
            try:
                a = float(input("Bölünecek sayıyı girin: "))
                b = float(input("Bölen sayıyı girin: "))
                if b == 0:
                    raise ZeroDivisionError("Sıfıra bölme hatası!")
                self.sonuc = a / b
                break
            except ValueError:
                print("Hata: Geçersiz sayı girişi!")
            except ZeroDivisionError as e:
                print("Hata:", e)

    def kare(self):
        while True:
            try:
                a = float(input("Karesi alınacak sayıyı girin: "))
                self.sonuc = a ** 2
                break
            except ValueError:
                print("Hata: Geçersiz sayı girişi!")

    def karekok(self):
        while True:
            try:
                x = float(input("Karekökü alınacak sayıyı girin: "))
                if a < 0:
                    raise ValueError("Negatif sayının karekökü alınamaz!")
                self.sonuc = a ** 0.5
                break
            except ValueError as e:
                print("Hata:", e)


# Kullanım örneği
# islemler = Islemler()
# islemler.bolme()
# print("Sonuç:", islemler.sonuc)

islemler2 = Islemler()
islemler2.toplama()
print("Sonuç:",islemler2.sonuc)
