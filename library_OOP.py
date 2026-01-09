class Book():
    # OOP Konsepti: Constructor (__init__) - Nesne başlatma
    def __init__(self, ad, yazar, sayfa, yil):
        self.ad = ad
        self.yazar = yazar
        self.sayfa = sayfa
        self.yil = yil
        # OOP Konsepti: Encapsulation (Kapsülleme) - Durum bilgisini gizleme
        self.__durum = "Mevcut" 
        
    # OOP Konsepti: Getter Metodu (Erişim)
    def get_durum(self):
        return self.__durum 
        
    # OOP Konsepti: Setter Metodu (Kontrollü Güncelleme)
    def set_durum(self, yenidurum):
        # Durum güncelleme için basit doğrulama (validation)
        if yenidurum in ["Mevcut", "Ödünç Verildi"]:
            self.__durum = yenidurum
        else:
            print("Geçersiz durum") 
            
    # OOP Konsepti: Polymorphism (Çok Biçimlilik) için temel gösterim metodu
    def bilgi_goster(self):
        print(f"{self.ad} - {self.yazar} ({self.get_durum()})")
        
    # OOP Konsepti: __str__ Metodu - Nesne print edildiğinde okunur format sağlar
    def __str__(self):
        return f"{self.ad} - {self.yazar} ({self.yil})"

class User():
    # OOP Konsepti: Constructor - Kullanıcı nesnesini başlatma
    def __init__(self, isim, user_id):
        self.isim = isim
        self.user_id = user_id
        
    def bilgi_goster(self):
        print(f"Kullanıcı ID: {self.user_id}, İsim: {self.isim}")

# OOP Konsepti: Inheritance (Kalıtım) - Member, User'dan miras alır
class Member(User):
    # Constructor
    def __init__(self, isim, user_id):
        # Base class (User) constructor'ını çağırma
        super().__init__(isim, user_id)
        self.odunc_alinanlar = [] # Üzerindeki kitap listesi
        
    # OOP Konsepti: Polymorphism (Çok Biçimlilik) - bilgi_goster metodunu override etme
    def bilgi_goster(self):
        print(f"Üye: {self.isim} (ID: {self.user_id})")
        # Üzerindeki kitapları listeleme mantığı
        if len(self.odunc_alinanlar) > 0:
            print("Üzerindeki Kitaplar:") 
            for kitap in self.odunc_alinanlar:
                print(f"        - {kitap.ad}")
        else:
            print("Üzerinde hiç kitap yok.")
            
    # Kitap ödünç alma işlemi
    def kitap_al(self, kitap_obj):
        self.odunc_alinanlar.append(kitap_obj)
        
    # Kitap iade etme işlemi
    def kitap_ver(self, kitap_obj):
        if kitap_obj in self.odunc_alinanlar:
            self.odunc_alinanlar.remove(kitap_obj)

# OOP Konsepti: Class (Sınıf) - Ana Kütüphane Yöneticisi
class Library():
    def __init__(self, kutuphane_adi):
        self.kutuphane_adi = kutuphane_adi
        # Tüm kitap ve üye nesneleri bu listelerde tutulur
        self.kitaplar = []
        self.uyeler = [] 
        
    # Yeni Book nesnesini listeye ekler
    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap)
        print(f"{kitap.ad} eklendi.")
        
    # Yeni Member nesnesini listeye ekler
    def uye_ekle(self, uye): 
        self.uyeler.append(uye)
        print(f"{uye.isim} üye oldu.")
        
    # Üye arama metodu
    def uye_bul(self, user_id): 
        for uye in self.uyeler:
            # ID karşılaştırması (string'e çevirerek esneklik sağlar)
            if str(uye.user_id) == str(user_id): 
                return uye
        return None # Üye bulunamazsa None döndürür
        
    # Tüm kitapları listeler
    def listele(self):
        print(f"\n{self.kutuphane_adi} Kitapları:")
        # __str__ metodu k nesnesi üzerinde otomatik çalışır
        for k in self.kitaplar: print(f"- {k} [{k.get_durum()}]")
        
    # Ödünç verme mantığı
    def odunc_ver(self, kitap_adi, uye):
        for k in self.kitaplar:
            # Kitap adı ve durum kontrolü (Encapsulation: get_durum ile durum sorgulanır)
            if k.ad == kitap_adi and k.get_durum() == "Mevcut":
                k.set_durum("Ödünç Verildi") # Durum güncellenir (Setter metodu)
                uye.kitap_al(k) 
                print("Kitap verildi.")
                return
        print("Kitap verilemedi (Yok veya başkasında).")
        
    # İade alma mantığı
    def iade_al(self, kitap_adi, uye):
        for k in self.kitaplar:
            if k.ad == kitap_adi:
                k.set_durum("Mevcut")
                uye.kitap_ver(k)
                print("İade alındı.")
                return

# Ana Uygulama Sınıfı
class Uygulama():
    # Uygulama başladığında Library nesnesini başlatır
    def __init__(self):
        # OOP Konsepti: Object (Nesne) - Library nesnesi oluşturulur
        self.kutuphane = Library("BAUN Kutuphanesi")
        
    # Programın ana döngüsü 
    def calistir(self):
        while True:
            secim = input("\n1:Kitap Ekle 2:Üye Ekle 3:Listele 4:Ödünç Ver 5:İade Al 6:Çıkış\nSeçim: ")
            
            # Kitap Ekleme: Tek satırda nesne oluşturma ve metot çağırma
            if secim == '1':
                self.kutuphane.kitap_ekle(Book(input("Ad: "), input("Yazar: "), input("Sayfa: "), input("Yıl: ")))
            
            # Üye Ekleme: Tek satırda nesne oluşturma
            elif secim == '2':
                self.kutuphane.uye_ekle(Member(input("İsim: "), input("ID: ")))
            
            elif secim == '3':
                self.kutuphane.listele()
                
            # Ödünç Verme İşlemi
            elif secim == '4': 
                uye = self.kutuphane.uye_bul(input("Üye ID: ")) 
                if uye: self.kutuphane.odunc_ver(input("Kitap Adı: "), uye) 
                else: print("Üye bulunamadı!")
                
            # İade Alma İşlemi
            elif secim == '5': 
                uye = self.kutuphane.uye_bul(input("Üye ID: "))
                if uye: self.kutuphane.iade_al(input("Kitap Adı: "), uye)
                else: print("Üye bulunamadı!")
                
            elif secim == '6':
                print("Uygulama kapatılıyor...")
                break

# Programın Çalışma Bloğu
if __name__ == "__main__":
    # OOP Konsepti: Object (Nesne) - Uygulama nesnesi oluşturulur
    app = Uygulama()
    app.calistir() # Uygulama başlatılır