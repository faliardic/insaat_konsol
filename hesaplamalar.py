
#1
def atalet_momenti():
    print("atalet momenti hesabı")
      
#2
def beton_metraji():    
    print("beton metrajı")
    

#3
def donati_metraj():
    print("donatı metrajı")
    

#4
def donati_tahvil():  
    print("donatı tahvili")
    

#5  
def spektrum():   
    print("deprem spektrum hesabı")
    

    
def hesaplamalar_menu():
    while True:
        print("***hesaplamalar***")
        print("1 - atalet momenti hesabı")
        print("2 - beton metrajı")
        print("3 - donatı metrajı")
        print("4 - donatı tahvili")
        print("5 - deprem spektrum hesabı")
        print("0 - ana menü")
        secim = input()
        if secim == "1":
            atalet_momenti()
        elif secim == "2":
            beton_metraji()
        elif secim == "3":
            donati_metraj()
        elif secim == "4":
            donati_tahvil()
        elif secim == "5":
            spektrum()
        elif secim == "0":
            break
        else:
            print("Hatalı giriş")
            

