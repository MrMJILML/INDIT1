#Aufgabe: Soll so lange nach einer neuen Zahl fragen, bis b_int ungleich 0 ist

a_str=input("Zahl1:")
a_int=int(a_str)

b_str=input("Zahl2:")
b_int=int(b_str)

while b_int==0:
    print("Zahl 2 = 0!")
    print("b_int darf nicht 0 sein. Geben Sie eine andere Zahl ein.")
    b_str=input("Zahl2:")
    b_int=int(b_str)
    
print(a_int+b_int)
print(a_int-b_int)
print(a_int*b_int)
print(a_int/b_int)
