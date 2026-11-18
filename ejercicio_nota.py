
mark= float(input("cual es tu nota:"))
if mark ==10:
    print("sobrsaliente")
elif mark>=8 and mark<=10:
    print("notable")
elif mark>=6 and mark<=8:
    print("bien")
elif mark==5:
    print("aprobado")
elif mark>=10:
    print("no se puede tener esa nota")
elif mark<=0:
    print("no se puede tener esa nota")
else:
    print("suspenso")