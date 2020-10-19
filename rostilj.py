from datetime import date, time, datetime

#Counteri za pakete
paket1Counter = 0
paket2Counter = 0   

cevapcici500counter = 0
cevapcici1000counter = 0
cevapcici2000counter = 0  

piletina500counter = 0
piletina1000counter = 0    

kobasice400counter = 0
kobasice800counter = 0 

kotleti500counter = 0
kotleti1000counter = 0
paketi = {}        
ostatak = {}

#funkcija za izračun ostatka
def ostatakMesa(ostatak):
    
    global cevapcici500counter 
    global cevapcici1000counter 
    global cevapcici2000counter 

    global piletina500counter 
    global piletina1000counter   

    global kobasice400counter 
    global kobasice800counter 

    global kotleti500counter 
    global kotleti1000counter 
    
    while ostatak['Ćevapćići'] > 0:
        if (500 >= ostatak['Ćevapćići'] ):
            ostatak['Ćevapćići'] = ostatak['Ćevapćići'] - 500
            cevapcici500counter += 1
        elif (1000 >= ostatak['Ćevapćići']):
            ostatak['Ćevapćići'] = ostatak['Ćevapćići'] - 1000
            cevapcici1000counter += 1
        elif (1500 >= ostatak['Ćevapćići']):
            ostatak['Ćevapćići'] = ostatak['Ćevapćići'] - 1500
            cevapcici500counter += 1
            cevapcici1000counter += 1
        else:
            ostatak['Ćevapćići'] = ostatak['Ćevapćići'] - 2000
            cevapcici2000counter += 1
            
                
    while ostatak['Piletina'] > 0:
        if (500 >= ostatak['Piletina'] ):
            ostatak['Piletina'] = ostatak['Piletina'] - 500
            piletina500counter += 1
        else:
            ostatak['Piletina'] = ostatak['Piletina'] - 1000
            piletina1000counter += 1
                           

    while ostatak['Kobasice'] > 0:
        if (400 >= ostatak['Kobasice']):
            ostatak['Kobasice'] = ostatak['Kobasice'] - 400
            kobasice400counter += 1
        else:
            ostatak['Kobasice'] = ostatak['Kobasice'] - 800
            kobasice800counter += 1
                
                
    while ostatak['Kotleti'] > 0:
        if (500 >= ostatak['Kotleti'] ):
            ostatak['Kotleti'] = ostatak['Kotleti'] - 500
            kotleti500counter += 1
        else:
            ostatak['Kotleti'] = ostatak['Kotleti'] - 1000
            kotleti1000counter += 1


paket_1 = ["Ćevapćići", "Piletina", "Kobasice"]

paket_2 = ["Ćevapćići", "Kobasice"]

paket_3 = ["Kobasice", "Kotleti"]


    

#Moguce vrste mesa za prikaz korisniku
vrste = { 1 : 'Ćevapćići',
          2 : 'Piletina',
          3 : 'Kobasice',
          4 : 'Kotleti'}


#Unos broja ljudi za roštilj te izračun količine mesa za svaku podskupinu

broj_m = int(input("Unesite broj muškaraca koji će prisustvovati roštilju: "))
print(vrste)
nece_m = [int(x) for x in input("Unesite pripadajući broj jela koje muškarci neće jesti sa razmakom bez zareza, a ako će sve jesti onda ostavite prazno: ").split()]

vrste_m = {}
count_m = len(nece_m)

if(count_m==0): 
    vrste_m=vrste
else:
    for i in range(1, 5):
        postoji = False
        
        for j in nece_m:
            if (i==j):
                postoji = True
                break
        if (postoji == False):
            vrste_m[i] = vrste[i]
            
kolicina_m = {}
for values in vrste_m.values():
    kolicina_m[values] = round((340/(4 - count_m))*broj_m, 2)
    





broj_z = int(input("Unesite broj žena koji će prisustvovati roštilju: "))
print(vrste)
nece_z = [int(x) for x in input("Unesite pripadajući broj jela koje žene neće jesti sa razmakom bez zareza, a ako će sve jesti onda ostavite prazno: ").split()]

vrste_z = {}
count_z = len(nece_z)

if(count_z==0): 
    vrste_z=vrste
else:
    for i in range(1, 5):
        postoji = False
        
        for j in nece_z:
            if (i==j):
                postoji = True
                break
        if (postoji == False):
            vrste_z[i] = vrste[i]
            
kolicina_z = {}
for values in vrste_z.values():
    kolicina_z[values] = round((340/(4 - count_z))*broj_z, 2)


broj_d = int(input("Unesite broj djece koji će prisustvovati roštilju: "))
print(vrste)
nece_d = [int(x) for x in input("Unesite pripadajući broj jela koje djeca neće jesti sa razmakom bez zareza, a ako će sve jesti onda ostavite prazno: ").split()]

vrste_d = {}
count_d = len(nece_d)

if(count_d==0): 
    vrste_d=vrste
else:
    for i in range(1, 5):
        postoji = False
        
        for j in nece_d:
            if (i==j):
                postoji = True
                break
        if (postoji == False):
            vrste_d[i] = vrste[i]
            
kolicina_d = {}
for values in vrste_d.values():
    kolicina_d[values] = round((340/(4 - count_d))*broj_d, 2)
    

#stvaranje konacne ukupne liste za kupovinu

ukupna_kolicina = kolicina_m


for key in kolicina_z:
    postoji = False
    for key2 in ukupna_kolicina:
        if (key == key2):
            postoji = True 
            ukupna_kolicina[key2]=ukupna_kolicina[key2] + kolicina_z[key]
            break
    if(postoji == False):
        ukupna_kolicina[key]=kolicina_z[key]


        
for key in kolicina_d:
    postoji = False
    for key2 in ukupna_kolicina:
        if (key == key2):
            postoji = True 
            ukupna_kolicina[key2]=ukupna_kolicina[key2] + kolicina_d[key]
            break
    if(postoji == False):
        ukupna_kolicina[key]=kolicina_d[key]
    
    
print(ukupna_kolicina)


#Provjera odgovara li Roštilj paket 1 ili 2 (U paketu 3 ne postoji ušteda)

for i in paket_1:
    postoji = False
    for key in ukupna_kolicina:
        if (i==key):
            postoji = True 
            break
    if(postoji == False):
        paketBoolean1 = False
        break
    else:
        paketBoolean1 = True

paketBoolean2 = False
if (paketBoolean1 == False):
    for i in paket_2:
        postoji = False
        for key in ukupna_kolicina:
            if (i==key):
                postoji = True 
                break
        if(postoji == False):
            paketBoolean2 = False
            break
        else:
            paketBoolean2 = True
            

if (paketBoolean1 == True):
    #kod koji odlucuje koliko paketa1 treba + ostalo
    for key in ukupna_kolicina:
        postoji = False
        for i in paket_1:
            if ( key == i ):
                postoji = True
                paketi[key] = ukupna_kolicina[key]
                break
        if ( postoji == False ):
            ostatak[key]=ukupna_kolicina[key] 
            
            
    #paket 1 koliko treba       
    while paketi['Ćevapćići'] > 0 and paketi['Piletina'] > 0 and paketi['Kobasice'] > 0:
        paketi['Ćevapćići'] = paketi['Ćevapćići'] - 500
        paketi['Piletina'] = paketi['Piletina'] - 500
        paketi['Kobasice'] = paketi['Kobasice'] - 400
        paket1Counter += 1
    #prebacivanje u ostatak 
    ostatak.update(paketi)
    for i in paket_2:
        postoji = False
        for key in ostatak:
            if (i==key):
                postoji = True 
                break
        if(postoji == False):
            paketBoolean2 = False
            break
        else:
            paketBoolean2 = True
    #provjera moze li se dio ili cijeli ostatak kupit preko paketa 2        
    if (paketBoolean2 == True):
        while ostatak['Ćevapćići'] > 500 and ostatak['Kobasice'] > 400:
            ostatak['Ćevapćići'] = ostatak['Ćevapćići'] - 1000
            ostatak['Kobasice'] = ostatak['Kobasice'] - 800
            paket2Counter += 1
            
    #sve sto se ne moze preko paketa    
    
    ostatakMesa(ostatak)
                
elif (paketBoolean2 == True):
    #kod koji odlucuje koliko paketa2 treba + ostalo
    for key in ukupna_kolicina:
        postoji = False
        for i in paket_2:
            if ( key == i ):
                postoji = True
                paketi[key] = ukupna_kolicina[key]
                break
        if ( postoji == False ):
            ostatak[key]=ukupna_kolicina[key]
            
            
    while paketi['Ćevapćići'] > 500 and paketi['Kobasice'] > 400:
        paketi['Ćevapćići'] = paketi['Ćevapćići'] - 1000
        paketi['Kobasice'] = paketi['Kobasice'] - 800
        paket2Counter += 1
            
            
    ostatak.update(paketi)
    
    ostatakMesa(ostatak)           
else:
    #kod koji radi sve bez paketa
    ostatakMesa(ostatak)
    
    
#ispis svega što treba kupit    
print ("Kako bi se svi najeli za roštilj je potrebno: ")  
if (paket1Counter > 0):
    print (paket1Counter, " Roštilj paket 500g Ćevapa + 500g Piletine + 400g Kobasice ")

if (paket2Counter > 0):
       print (paket2Counter, " Roštilj paket 1000g Ćevapa + 800g Kobasice ")

if (cevapcici500counter > 0):
    print (cevapcici500counter, " Paketa 500g Ćevapa ")
if (cevapcici1000counter > 0):
    print (cevapcici1000counter, " Paketa 1000g Ćevapa ")
if (cevapcici2000counter > 0):
    print (cevapcici2000counter, " Paketa 2000g Ćevapa ") 

if (piletina500counter > 0):
    print (piletina500counter, " Paketa 500g Piletine ")
if (piletina1000counter > 0):
    print (piletina1000counter, " Paketa 1000g Piletine ")  

if (kobasice400counter > 0):
    print (kobasice400counter, " Paketa 400g Kobasica ")
if (kobasice800counter > 0):
    print (kobasice800counter, " Paketa 800g Kobasica ") 

if (kotleti500counter > 0):
    print (kotleti500counter, " Paketa 500g Kotleta")
if (kotleti1000counter > 0):
    print (kotleti1000counter, " Paketa 1000g Kotleta")
    
#konacna cijena   
suma = paket1Counter * 65 + paket2Counter * 55 + cevapcici500counter * 22 + cevapcici1000counter * 35 + cevapcici2000counter * 60 + piletina500counter * 35 + piletina1000counter * 60 + kobasice400counter * 15 + kobasice800counter * 25 + kotleti500counter * 20 + kotleti1000counter * 35
   
print ("Ukupna cijena svega je: ", suma, "Kn")  



#odbrojavanje do 1. svibnja
if (datetime.now().month >= 5):
    PRVI_SVIBANJ = datetime(year=datetime.now().year +1, month=5, day=1)
else: 
    PRVI_SVIBANJ = datetime(year=datetime.now().year, month=5, day=1)

countdown = PRVI_SVIBANJ - datetime.today()

print(f"Do prvog svibnja je ostalo još: {countdown}.")






        
    