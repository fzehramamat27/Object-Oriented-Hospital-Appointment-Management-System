# kullanici.py
class Kisi:
    """Temel Sınıf: Kapsülleme ve Kalıtım örneği."""
    def __init__(self, ad, soyad, tc):
        self.ad = ad
        self.soyad = soyad
        self.__tc = tc  # Private: Kapsülleme (Encapsulation)

    def tam_ad(self):
        return f"{self.ad} {self.soyad}"

class Doktor(Kisi):
    """Kalıtım: Kisi sınıfından türetilmiştir."""
    def __init__(self, ad, soyad, tc, uzmanlik):
        super().__init__(ad, soyad, tc)
        self.uzmanlik = uzmanlik

class Hasta(Kisi):
    """Kalıtım: Kisi sınıfından türetilmiştir."""
    def __init__(self, ad, soyad, tc, sikayet):
        super().__init__(ad, soyad, tc)
        self.sikayet = sikayet