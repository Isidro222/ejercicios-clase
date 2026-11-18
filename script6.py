edad= int(input("¿cual es tu edad?:"))
dia= (input("¿que dia es?:"))
estudiante= input("¿eres un estudiante?:")
precio_normal= 8
if dia== "miercoles":
    precio= 4
elif estudiante == True:
    precio= precio_normal*0.70
elif estudiante == False:
    precio= precio_normal
elif edad<= 12:
    precio= 4
elif edad>= 65:
    precio= 5
else:
    precio= precio_normal
print(f"tu entrada cuesta: {precio}€")
