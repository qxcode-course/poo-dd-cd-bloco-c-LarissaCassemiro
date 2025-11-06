# # Nosso objetivo no trabalho é modelar um gestor de pula pulas em um parquinho, controlando as pessoas que entram e saem do pula pula, além de coordenar as pessoas que estão na fila de espera.

# # ## Intro

# # - Inserir crianças na fila de espera do pula pula
# # - Mover a primeira criança da fila de espera do pula pula para dentro do pula pula.
# # - Mover a primeira criança que entrou no pula pula para o final da fila de espera.


class Crianca:
    def __init__(self, nome: str, idade: int ):
        self.nome = nome
        self.idade = idade  

    def __str__(self):
        return f"{self.nome}:{self.idade}"
    
class PulaPula:
    def __init__(self):
        self.espera: list[Crianca] = []
        self.pulapula: list[Crianca] = []
    
    def arrive(self, nome:str, idade:int): 
        self.espera.insert(0, Crianca(nome, idade))

    def enter(self): 
        if self.espera:
            crianca = self.espera.pop()
            self.pulapula.insert(0, crianca)
        else: 
            print("Ninguém na fila")

    def leave(self):
        if self.pulapula:
            crianca = self.pulapula.pop()
            self.espera.insert(0, crianca)

    def remove(self, nome: str):
        for i , crianca in enumerate(self.espera):
            if crianca.nome == nome: 
                del self.espera[i]
                return 
        for i, crianca in enumerate(self.pulapula):
            if crianca.nome == nome: 
                del self.pulapula[i]
                return 
        print(f"fail: {nome} nao esta no pula-pula")

    def __str__(self):
        espera = ", ".join([str(crianca) for crianca in self.espera])
        pulapula = ", ".join([str(crianca) for crianca in self.pulapula])
        return f"[{espera}] => [{pulapula}]"
    

def main():
    pula = PulaPula()
    while True:
        line = input()
        print("$"+ line)
        args = line.split(" ")

        if args[0] == "end":
            break 

        elif args[0] == "show":
            print(pula)

        elif args[0] == "enter":
            pula.enter()

        elif args[0] == "leave":
            pula.leave()

        elif args[0] == "remove":
            pula.remove(args[1])

        elif args[0] == "arrive":
            pula.arrive(args[1], int(args[2]))
main()

