#Parte laboratorio 2
archivo="colores.txt"
f = open(archivo,"w+")
f.write("Rojo\n")
f.write("Amarillo\n")
f.write("Verde\n")
mas_colores=["Morado\n","Celeste\n","Rosa\n"]
f.writelines(mas_colores)
f.close()