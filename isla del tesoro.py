#ISLA DEL TESORO
#Empieza a jugar
print("Bienvenido a la isla tu misión será encontrar el tesoro")
print("¿Tenemos un mapa?")
print("Si tenemos un mapa (1) No tenemos un mapa (2)")
opt1=int(input())
if (opt1 == 2):
   print ("Quitarle el mapa al mono ¿Lograste robar el mapa? Si (1), No (2)")
else: 
  print ("Resolver el mapa. Entrar detrás de los arboles (1), seguir caminando (2)")
  op2=int(input())
  if (op2==1): 
    print ("caíste en arena movediza. Game over")
  if (op2==2):
      print("Encontraste una tribu ¿Le pedimos ayuda? Si (1), No (2)")
  op3=int(input())
  if (op3==1):
    print("Te atacan y echan de la isla. Game over")
  if (op3==2):
      print("Pasamos de largo y seguimos las pistas ¿Cuál cueva entrar? La primera (1), o La segunda (2)")
  op4=int(input())
  if (op4==1):
      print("Caíste en un hueco. Gamer over")
  if (op4==2):
      print("Encontraste la cueva del tesoro. ¿Derrotaste la bestia? Si (1) No (2)")