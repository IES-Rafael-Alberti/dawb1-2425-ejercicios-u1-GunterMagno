
fecha = input("Dame tu fecha de nacimiento en el siguiente formato dd/mm/aaaa: ")

dia = fecha.split("/")[0]
mes = fecha.split("/")[1]
año = fecha.split("/")[2]

print(dia,mes,año)