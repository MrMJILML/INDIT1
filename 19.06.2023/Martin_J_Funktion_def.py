#Funktion

namen = ["Peter","Dora","Kevin","Fritz","Sarah"]

def begruessung_1(name):
    print("Hallo ",name)
    print("Schön dich zu sehen!")
    print("Viel Spaß mit dem Programm!")
    
def begruessung_2(namensliste):
    for ein_name in namensliste:
        print("Hallo ",ein_name)
        print("Schön dich zu sehen!")
        print("Viel Spaß mit dem Programm!")
        
print("Programmstart")

print("for-Schleife im Hauptprogramm")
for ein_name in namen:
    begruessung_1(ein_name)
    
i=0
while i<len(namen):
    begruessung_1(namen[i])
    i+=1
