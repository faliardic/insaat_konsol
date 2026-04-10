print("Proje geliştirilmeye başlandı")

from hesaplamalar import hesaplamalar_menu
from statik_rehber import statik_rehber_menu
from oyunlar import oyunlar_menu

def main():
    while True:
        print("1 - Hesaplamalar")
        print("2 - Statik rehber")
        print("3 - Oyunlar")
        print("0 - Çıkış")
        secim = input()
        
        if secim == "1":
            hesaplamalar_menu()
        elif secim == "2":
            statik_rehber_menu()
        elif secim == "3":
            oyunlar_menu()
        elif secim == "0":
            print("Kapatılıyor")
            break
        else:
            print("Hatalı giriş")
            
main()

