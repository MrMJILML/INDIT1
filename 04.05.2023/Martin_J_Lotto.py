import random

l = 0 #Laufvariable 1
tipps =[]


anz_t = int(input("Wie viele Tipps möchten Sie abgeben: ")) #Abfrage nach der gewünschten Anzahl der Tipps

if anz_t <=6: 
    while l <anz_t:
        x = random.randint(1,45) #Es wird eine zufallszahl zwischen 1 und 45 generiert
        if x in tipps: #Überprüfung ob die Zahl bereits vorhanden ist 
        else:
            tipps.append(x)
            l+=1

    print("Ihre Tipps sind: ", tipps)

else:
    print("Bitte wählen Sie eine Zahl zwichen 1 und 6!")