kutuphane = []

def kitapEkle():
    #Kullanıcıdan alınan verilerle listeye ekleme yapar.
    print("Kitap Ekle: ")
    ad = input("Kitap Adı: ")
    yazar = input("Yazar: ")    
    sayfa = input("Sayfa Sayısı: ")
    yil = input("Basım Yılı: ")
    yeni_kitap = [ad, yazar, sayfa, yil, "Mevcut"]
    kutuphane.append(yeni_kitap)
    print(f"{ad} listeye eklendi.")

def kitapSil():
    #İsmi girilen kitabı listeden kalıcı olarak siler.
    print("Kitap Sil: ")
    if len(kutuphane) == 0:
        print("Kütüphane şu an boş! Silinecek herhangi bir kitap yok.")
        return
    aranan = input("Silinecek kitabın adı: ")
    bulundu = False
    for kitap in kutuphane:
        if kitap[0].lower() == aranan.lower():
            kutuphane.remove(kitap)
            print(f"{kitap[0]} silindi.")
            bulundu = True
            break

    if not bulundu:
        print("Kitap bulunamadı.")

def Listeleme():
    #Kitapları listeler.
    print("Kitap Listesi: ")
    if len(kutuphane) == 0:
        print("Kutuphane bos")
        return
    print(f"{'Kitap Adı':<30} {'Yazar':<20} {'Sayfa':<7} {'Yıl':<7} {'Durum':<15}")
    print("-" * 60) 
    for kitap in kutuphane:
        # Okunabilirliği artırmak için değişkenlere atama
        ad = kitap[0]
        yazar = kitap[1]
        sayfa = kitap[2] 
        yil = kitap[3]
        durum = kitap[4]
        print(f"{ad:<30} {yazar:<20} {sayfa:<7} {yil:<7} {durum:<15}")
    print("-" * 60)

def oduncVer():
    #Kitabın durumunu 'Odunc Verildi' olarak günceller.
    print("Ödünç Ver")
    aranan = input("Verilecek kitabın adı: ")

    bulundu = False
    for kitap in kutuphane:
        if kitap[0].lower() == aranan.lower():
            bulundu = True

            if kitap[4] == "Mevcut":
                kitap[4] = "Odunc Verildi"
                print(f"{kitap[0]} ödünç verildi.")
            else:
                print(f"{kitap[0]} başkasına verilmiş!") 
            break
    if not bulundu:
        print("Kitap bulunamadı.")
    
def iadeAl():
    #Kitap durumunu tekrar 'Mevcut' yapar.
    print("Kitap İade Alma")
    aranan = input("İade alınacak kitabın adı: ")

    bulundu = False
    for kitap in kutuphane:
        if kitap[0].lower() == aranan.lower():
            bulundu = True
            if kitap[4] == "Odunc Verildi":
                kitap[4] = "Mevcut"
                print(f"{kitap[0]} iade alındı.")
            else:
                print(f"{kitap[0]} zaten kütüphanede görünüyor.")
            break
            
    if not bulundu:
        print("Kitap bulunamadı.")

def menu():
    #Kullanıcı seçimine göre ilgili fonksiyonu çağırır.
    while True:
        print("\n 1:Ekle | 2:Sil | 3:Listele | 4:Ödünç Ver | 5:İade Al | 6:Çıkış ")
        secim = input("Seçim: ")
        
        if secim == '1': kitapEkle()
        elif secim == '2': kitapSil()
        elif secim == '3': Listeleme()
        elif secim == '4': oduncVer()
        elif secim == '5': iadeAl()
        elif secim == '6': break
        else: print("Hatalı seçim.")

# Programın başlangıç noktası
if __name__ == "__main__":
    menu()