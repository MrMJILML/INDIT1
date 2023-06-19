#Aufgabe: Soll so lange nach einer neuen Zahl fragen, bis b_int ungleich 0 ist
while True:
    a_str=input("Zahl1:")
    try:
        a_int=int(a_str)
        break
    except ValueError:
        print("Keine Gültige Eingabe, gewen Sie eine Zahl ein.")

while True:
    b_str=input("Zahl2:")
    try:
        b_int=int(b_str)
        break
    except ValueError:
        print("Keine Gültige Eingabe, gewen Sie eine Zahl ein.")

print("korrekt")

while b_int==0:
    print("Zahl 2 = 0!")
    print("b_int darf nicht 0 sein. Geben Sie eine andere Zahl ein.")
    b_str=input("Zahl2:")
    b_int=int(b_str)
    
print(a_int+b_int)
print(a_int-b_int)
print(a_int*b_int)
print(a_int/b_int)