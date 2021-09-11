# Reto VI
print('Retro VI')
ls = [1,2,3,4,5]
print('lista original: ',ls)
ls.append(0)
print('agregado el 0: ', ls)
ls.sort()
print('lista ordenada: ', ls)
ls.remove(0)
print('lista sin 0: ', ls)
cantidad = len(ls)
print('cantidad de elementos: ', cantidad)
suma_total = 0
for elem in ls:
    suma_total = suma_total + elem
print('suma total de los elementos: ', suma_total)
ls_2 = map(lambda elem: {str(elem): elem}, ls)
print('nueva lista con dicts: ', list(ls_2), '\n')

print('Retro VII')
prot_diminuta = 'ATGGAAGTTGGAATCCAAGTTGGA'
prot_rana_terrestre = 'ATGGAAGTTAATGGAAGTTGGAGGAGA'
if len(prot_diminuta) > len(prot_rana_terrestre):
    print(f'el gen {prot_diminuta} es mayor')
elif len(prot_diminuta) == len(prot_rana_terrestre):
    print('son iguales')
else:
    print(f'el gen {prot_rana_terrestre} es mayor')
print('\n')

print('Reto VIII')
for i in range(0,20):
	print(f'somos {2**i} clones')

