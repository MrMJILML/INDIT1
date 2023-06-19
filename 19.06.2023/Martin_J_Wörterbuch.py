# DE=["Apfel","Birne","Marille","Banane","Dattel"]
# EN=["Apple","Pear","Apricot","Banana","Date"]
# 
# max=len(DE)
# 
# Wort_DE=input("Deutscher Begriff: ")
# 
# i=0
# 
# while i<max:
#     if DE[i]==Wort_DE:
#         print(EN[i])
#         break
#     i+=1
#     
# if i==max:
#     print("Wort nicht gefunden.")


#Andere Variante:
    
W={"Apfel":"Apple","Birne":"Pear","Marille":"Apricot","Banane":"Banana","Dattel":"Date"}

Wort_DE=input("Deutscher Begriff: ")

for de, en in W.items():
    if Wort_DE == de:
        print(en)
        
W["Pflaume"]="Plum" #Das Wort wird dem Wörterbuch hinzugefügt