objeto_zip = zip([1,2,3])

print(list(objeto_zip))

id = [1, 2, 3, 4, 5]
regiao = ["Norte", "Nordeste", "Sudeste", "Centro-Oeste", "Sul"]

mapa = list(zip(id, regiao))
print(mapa)

codigos = ["1000", "1001", "1002", "1003", "1004", "1005"]
frutas = ["maçã", "uva", "banana", "laranja"]

mercadorias = list(zip(codigos, frutas))
print(mercadorias)

tupla_iteravel = [('J392', 'João'), ('M890', 'Maria'), ('J681', 'José'), ('C325', 'Claúdia'), ('A49', 'Ana')]
print(tupla_iteravel)
ids, nomes  = zip(*tupla_iteravel)

ids = list(ids)
nomes = list(nomes)

print("IDs = ", ids)
print("Nomes = ", nomes)

