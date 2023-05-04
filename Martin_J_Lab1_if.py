a_str=input("Zahl1:")
a_int=int(a_str)

b_str=input("Zahl2:")
b_int=int(b_str)

#Aufgabe 1: +, -, *, /

# print(a_int+b_int)
# 
# print(a_int-b_int)
# 
# print(a_int*b_int)
# 
# print(a_int/b_int)

#if [Bedingung]:
if a_int==0:
    print("Zahl 1 = 0!")
    print("a_int darf nicht 0 sein. Geben Sie eine andere Zahl ein.")
    a_str=input("Zahl1:")
    a_int=int(a_str)
    
    print(a_int+b_int)
    print(a_int-b_int)
    print(a_int*b_int)
    print(a_int/b_int)

else:
    print(a_int+b_int)
    print(a_int-b_int)
    print(a_int*b_int)
    print(a_int/b_int)
    