# main.py
from kullanici import Doktor, Hasta
from veritabani import HastaneDB
import sys

def menu():
    db = HastaneDB()
    
    while True:
        print("\n--- HASTANE RANDEVU SİSTEMİ ---")
        print("1. Doktor Kaydı\n2. Randevu Oluştur\n3. Randevuları Listele\n4. Çıkış")
        secim = input("İşlem seçiniz: ")

        if secim == "1":
            ad = input("Doktor Adı: ")
            soyad = input("Doktor Soyadı: ")
            uzmanlik = input("Uzmanlık Alanı: ")
            yeni_dr = Doktor(ad, soyad, "111111", uzmanlik)
            db.doktor_ekle(yeni_dr)
            print("Doktor sisteme eklendi.")

        elif secim == "2":
            h_ad = input("Hasta Ad Soyad: ")
            d_id = int(input("Doktor ID: "))
            db.randevu_al(h_ad, d_id)
            print("Randevu başarıyla oluşturuldu.")

        elif secim == "3":
            liste = db.randevulari_getir()
            print("\nRANDEVU LİSTESİ:")
            for r in liste:
                print(f"No: {r[0]} | Hasta: {r[1]} | Doktor: {r[2]}")

        elif secim == "4":
            print("Çıkılıyor...")
            sys.exit()

# Görseldeki kritik yapı
if __name__ == "__main__":
    menu()