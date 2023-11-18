#PARTE 3
archivo="colores.txt"
f = open(archivo,"a+")
mas_colores=["Morado\n","Celeste\n","Rosa\n"]
f.writelines(mas_colores)
f.close()