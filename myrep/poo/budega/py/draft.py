class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome 

    def __str__(self):
        return self.nome

class Budega: 
    def __init__(self, num_caixas: int):
        self.caixas: list[Pessoa | None] = []
        for _ in range(num_caixas):
            self.caixas.append(None)
        self.espera: list[Pessoa] = []

    def enter(self, pessoa: Pessoa):
        self.espera.append(pessoa)

    def call(self, index: int):
        if index < 0 or index >= len(self.caixas):
            print("indice inexistente")
            return 
        if self.caixas[index] is not None:
            print("caixa ocupado")
            return
        if len (self.espera) == 0:
            print("ninguem esperando")
            return 
        self.caixas[index] = self.espera[0]
        del self.espera[0]

    def finish(self, index: int):
        self.caixas[index] = None 


    def give_up(self, nome: str):
        for i, pessoa in enumerate(self.espera):
            if pessoa.nome == nome:
                aux = self.espera
                del self.espera[i]
                break


    def __str__(self):
        caixas = ", ".join(["----" if x is None else str(x) for x in self.caixas])
        espera = ", ".join([str(x) for x in self.espera])
        return f"Caixas: [{caixas}] /nEspera: [{espera}]"


pessoa = Pessoa ("Maria")
print(pessoa)

budega = Budega(5)
budega.enter(Pessoa("Virginia"))
budega.enter(Pessoa("Vini Jr"))
print(budega)
budega.call(2)