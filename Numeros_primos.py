#NUMEROS_PRIMOS

numero=int(input("introduce el numero a coomprobar: "))
list=[x for x in range(2,numero) if numero%2==0]
if numero==1:
  print("No es un numero primo")
elif numero==2:
  print("si es un numero primo")
elif len(list) != 0:
  print ("no es un numero primo")
else:
  print("Si es un numero primo")

print("La ejecucion de nuestro programa finalizo exictosamente")