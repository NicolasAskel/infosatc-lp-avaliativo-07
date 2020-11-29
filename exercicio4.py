ListaNumero = []
for x in range(10):
  numeroInput = int(input("Insira o numero: "))
  ListaNumero.append(numeroInput)
ListaNumero2 = ListaNumero.copy()
  filtro = list(filter(lambda x: x % 2 == 0, ListaNumero))
  filtro2 = list(filter(lambda x: x % 2 != 0, ListaNumero2))

print("Numeros Pares: ")
for x in filtro:
    print(x)
    
print("Numeros Impares: ")
for x in filtro2:
    print(x)
