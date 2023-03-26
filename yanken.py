import random
class yanken :
    combinaciones = ["Piedra", "Papel", "Tijeras"]
    def game(self):
        print("Escriba una de las siguientes palabras para que comienze el juego : Piedra, Papel o Tijera")
        userInput = input("Su elleción será->")
        userInput = self.inputChecker(userInput)
        return self.compareResults(userInput, random.randint(1,3))

    
    def inputChecker (self, userInput):
        userInput = userInput.upper()
        if userInput == "PIEDRA":
            userInput = 1
        elif userInput == "PAPEL" :
            userInput = 2
        elif userInput == "TIJERA" :
            userInput = 3
        else: 
             userInput = 0
        return userInput
    def compareResults (self, userInput, machineInput):
         if userInput == 0:
             result = "Has introducido una cadena no valida"
         elif userInput == machineInput :
            result = "Has empatado"
         elif userInput == 1 :
             if machineInput == 2:
                ##print(self.combinaciones[userInput]+" VS "+self.combinaciones[machineInput])
                result = "Has perdido"
             elif machineInput == 3 :
                 ##print(self.combinaciones[userInput]+" VS "+self.combinaciones[machineInput])
                 result = "Has ganado"
         elif userInput == 2: 
             if userInput == 1:
                ##print(self.combinaciones[userInput]+" VS "+self.combinaciones[machineInput])
                result = "Has ganado"
             elif userInput == 3 :
                ##print(self.combinaciones[userInput]+" VS "+self.combinaciones[machineInput])
                result = "Has perdido"
         elif userInput == 3: 
             if userInput == 1:
                ##print(self.combinaciones[userInput]+" VS "+self.combinaciones[machineInput])
                result = "Has perido"
             elif userInput == 3 :
                ##print(self.combinaciones[userInput]+" VS "+self.combinaciones[machineInput])
                result = "Has ganado"
         return result


    pass
