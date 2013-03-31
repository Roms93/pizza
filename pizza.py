import random

nb = 0
pr = "0"
pr = float(pr)

ch = input("Nombre de pizzas? ")
ch = int(ch)
continuer = True
i = ch

while nb < ch:
  i = i-1
		
	r = random.randint(1,31)

	if r==1:
        	print("FROMAGERE")
        	nb = nb+1
        	print("Prix: 13.50")          
	if r==2:
                print("MARGUERITA")
                nb = nb+1
                print("Prix: 09.00")
	if r==3:
                print("NAPOLITAINE")
                nb = nb+1
                print("Prix: 12.50")            
	if r==4:
                print("CALZONE")
                nb = nb+1
                print("Prix: 12.50")            
	if r==5:
                print("REINE")
                nb = nb+1
                print("Prix: 12.50")             
	if r==6:
                print("VEGETARIENNE")
                nb = nb+1
                print("Prix: 12.50")            
	if r==7:
                print("TONATA")
                nb = nb+1
                print("Prix: 12.50")              
	if r==8:
                print("REGINA")
                nb = nb+1
                print("Prix: 12.50")          
	if r==9:
                print("4 SAISONS")
                nb = nb+1
                print("Prix: 12.50")         
	if r==10:
                print("FRUIT DE MER")
                nb = nb+1
                print("Prix: 12.50")          
	if r==11:
                print("ORIENTALE")
                nb = nb+1
                print("Prix: 12.50")        
	if r==12:
                print("4 FROMAGES")
                nb = nb+1
                print("Prix: 12.50")          
	if r==13:
                print("CAMPIONE")
                nb = nb+1
                print("Prix: 12.50")        
	if r==14:
                print("RACLETTE")
                nb = nb+1
                print("Prix: 12.50")        
	if r==15:
                print("FAMILY")
                nb = nb+1
                print("Prix: 12.50")         
	if r==16:
                print("MOUSSAKA")
                nb = nb+1
                print("Prix: 12.50")        
	if r==17:
                print("MEAT")
                nb = nb+1
                print("Prix: 12.50")        
	if r==18:
                print("HAWAIENNE")
                nb = nb+1
                print("Prix: 13.50")        
	if r==19:
                print("KEBAB")
                nb = nb+1
                print("Prix: 13.50")        
	if r==20:
                print("CHEVRE")
                nb = nb+1
                print("Prix: 13.50")      
	if r==21:
                print("FERMIERE")
                nb = nb+1
                print("Prix: 13.50")       
	if r==22:
                print("COUNTRY")
                nb = nb+1
                print("Prix: 13.50")       
	if r==23:
                print("PACIFICO")
                nb = nb+1
                print("Prix: 13.50")             
	if r==24:
                print("TARTIFLETTE")
                nb = nb+1
                print("Prix: 13.50")     
	if r==25:
                print("CHICAGO")
                nb = nb+1
                print("Prix: 13.50")      
	if r==26:
                print("CHICKEN SUPREME")
                nb = nb+1
                print("Prix: 13.50")      
	if r==27:
                print("PAYSANNE")
                nb = nb+1
                print("Prix: 13.50")                      
	if r==28:
                print("MIAMI")
                nb = nb+1
                print("Prix: 14.00")                   
	if r==29:
                print("BUFFALO")
                nb = nb+1
                print("Prix: 14.00")                         
	if r==30:
                print("HOT FANTAS")
                nb = nb+1
                print("Prix: 14.50")                     
	if r==31:
                print("INDIENNE")
                nb = nb+1
                print("Prix: 14.00")


print("\n Numéro: 01 43 88 33 33")

quit=input("\nAppuyer sur une touche pour continuer..") 

