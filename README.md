# Object-Oriented-Hospital-Appointment-Management-System
Nesne Tabanlı Programlama(OOP) ilkeleri ile geliştirilmiş Python tabanlı hastane randevu yönetim sistemi
​Bu proje, Kastamonu Üniversitesi Tosya Meslek Yüksekokulu Programlama II dersi dönem sonu ödevi kapsamında geliştirilmiştir. 
Proje Özeti ve Amacı
Bu proje, bir hastanedeki doktor kayıtlarını yönetmek ve hastaların bu doktorlardan randevu almasını sağlamak amacıyla geliştirilmiştir. Konsol tabanlı bir arayüz (CLI) üzerinden çalışan sistem, girilen bilgileri bir SQLite veritabanında saklayarak program kapansa dahi verilerin kaybolmamasını sağlar.
2. Kullanılan Teknolojiler ve Kavramlar
Projede modern yazılım geliştirme süreçlerinde kullanılan şu temel yapılar yer almaktadır:
Python: Ana programlama dili.
SQLite3: Hafif, dosya tabanlı ve kurulum gerektirmeyen ilişkisel veritabanı motoru.
Nesne Yönelimli Programlama (OOP):
Kalıtım (Inheritance): Kisi sınıfının özelliklerinin Doktor ve Hasta sınıflarına aktarılması.
Kapsülleme (Encapsulation): __tc gibi hassas verilerin dışarıdan doğrudan erişime kapatılması.
Soyutlama (Abstraction): Karmaşık veritabanı işlemlerinin metodlar arkasına gizlenerek basitleştirilmesi.
SQL (JOIN): İki farklı tablodaki verilerin (Doktorlar ve Randevular) ilişkilendirilerek tek bir liste halinde sunulması.
3. Modüllerin İncelenmesi
A. kullanici.py (Veri Modeli)
Bu modül, sistemdeki aktörleri (insanları) temsil eder.
Kisi Sınıfı: Tüm insanların ortak özelliği olan ad, soyad ve TC bilgisini tutar. TC bilgisi __ ön ekiyle korunarak sınıf dışından müdahale engellenmiştir.
Doktor ve Hasta Sınıfları: Kisi sınıfından türetilmiştir. super().__init__ kullanımı sayesinde ortak özellikler tekrar yazılmadan miras alınmış, üzerine uzmanlık veya şikayet gibi spesifik alanlar eklenmiştir.
B. veritabani.py (Veri Katmanı)
Veritabanı bağlantısı ve SQL sorgularının yönetildiği bölümdür.
tablolari_kur: Program ilk çalıştığında hastane.db dosyasını ve gerekli tabloları otomatik oluşturur.
randevulari_getir: Burada kullanılan JOIN yapısı kritiktir; sadece doktor ID'sini değil, o ID'ye karşılık gelen doktorun ismini de getirerek kullanıcıya anlamlı bir liste sunar.
C. main.py (Yönetim Katmanı)
Kullanıcının etkileşime girdiği ana merkezdir. Bir while döngüsü içinde sonsuz bir menü sunar ve kullanıcı "Çıkış" diyene kadar programı aktif tutar.
4. Proje Nasıl Çalıştırılır?
Projenin düzgün çalışması için her üç dosyanın da aynı klasör içerisinde bulunması gerekir:
1.Terminali/CMD'yi Açın: Proje dosyalarının olduğu dizine gidin.
2.Programı Başlatın: Şu komutu çalıştırın:
python main.py
3.İşlem Sırası: * Önce 1 tuşuna basarak bir doktor kaydedin (Veritabanında doktor yoksa randevu oluşturulamaz).
Ardından 2 tuşuna basarak hasta bilgilerini ve ilgili doktorun ID numarasını girerek randevu oluşturun.
Son olarak 3 tuşu ile tüm randevuları listeleyin.
