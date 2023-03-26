from yanken import *

print("Hola has iniciado el juego de piedra papel o tijeras")

flag = True
controller =  yanken()
while flag == True :
    print("Hola has iniciado el juego de piedra papel o tijeras")
    result = controller.game()
    print(result)
    newFlag = input("Escribe S para continuar y cualquier otra cosa para terminar el juego")
    if newFlag.upper() == "S":
        flag = True
    else:
        flag = False 
