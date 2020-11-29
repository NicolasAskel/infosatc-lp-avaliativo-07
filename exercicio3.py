ListaNumero = []
for x in range(5):
 numeroInput = int(input("digite um numero: "))
 ListaNumero.append(numeroInput)
filtro = list(filter(lambda x: x>10, ListaNumero))
print("Numeros filtrados: ")
for x in filtro:
 print(x)
