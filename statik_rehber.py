print("burada önemli statik kontrol adımları yer alacak")


def statik_rehber_menu():
    while True:
        print("***statik rehber***")
        print("1 - minimum eleman boyutları kontrolü")
        print("2 - temel insaati kontrolleri")
        print("3 - gövde donatısı kontrolü")
        print("4 - minimum kolon boyuna donatısı kontrolü")
        print("5 - kirişli plak döşeme kalınlığı kontrolü")
        print("0 - ana menü")
        secim = input()
        if secim == "1":
            min_eleman()
        elif secim == "2":
            temel()
        elif secim == "3":
            govde()
        elif secim == "4":
            kolon_min_boy()
        elif secim == "5":
            dos_kal()
        elif secim == "0":
            break
        else:
            "hatalı giriş"
                        

#1 
def min_eleman():
    print("deprem yönetmeliğine göre minimum eleman boyutları kontrolü")       
        
#2
def temel():    
    print("temel insaati kontrolleri")

#3
def govde():    
    print("gövde donatısı kontrolü")

#4
def kolon_min_boy():    
    print("minimum kolon boyuna donatı hesabı")

#5
def dos_kal():    
    print("kirişli plak döşeme kalınlığı kontrolü")

