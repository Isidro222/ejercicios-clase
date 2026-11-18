#pedir temperatura ¿cuantas temperaturas
#pedir x temperaturas al usuario
#hacer la media

temperatura = int(input("cusntas temperaturas:"))
temp =[]
for i in range(temperatura):
    new_temps = int(input(f"introduce temperaturas {i+1}:"))
    temp.append(new_temps)

total = 0
for temp in temp:
    total = total + temp

average = total / temperatura
print(average)
