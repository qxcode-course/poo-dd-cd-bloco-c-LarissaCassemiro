# - Iniciar lapiseira
#   - Inicia uma lapiseira de determinado calibre sem grafite.
#   - Lapiseiras possuem um bico e um tambor.
#   - O bico guarda o grafite que está em uso.
#   - O tambor guarda os grafites reservas.
# - Inserir grafite
#   - Insere um grafite passando
#     - o calibre: float.
#     - a dureza: string.
#     - o tamanho em mm: int.
#   - Não deve aceitar um grafite de calibre não compatível.
#   - O grafite é colocado como o ÚLTIMO grafite do tambor.
# - Puxar grafite
#   - Puxa o grafite do tambor para o bico.
#   - Se já tiver um grafite no bico, esse precisa ser removido primeiro.
# - Remover grafite
#   - Retira o grafite do bico.
# - Escrever folha
#   - Não é possível escrever se não há grafite no bico.
#   - Quanto mais macio o grafite, mais rapidamente ele se acaba. Para simplificar, use a seguinte regra:
#     - Grafite HB: 1mm por folha.
#     - Grafite 2B: 2mm por folha.
#     - Grafite 4B: 4mm por folha.
#     - Grafite 6B: 6mm por folha.
#   - O último centímetro de um grafite não pode ser aproveitado, quando o grafite estiver com 10mm, não é mais possível escrever e o grafite deve ser retirado.
#   - Se não houver grafite suficiente para terminar a folha, avise que o texto ficou incompleto.

class Grafite: 
    def __init__(self, tamanho: int, dureza: str, calibre: float):
        self._tamanho = tamanho
        self._dureza = dureza
        self._calibre = calibre 
    
    def get_tamanho(self):
        return self._tamanho
    
    def get_dureza(self):
        return self._dureza
    
    def get_calibre(self):
        return self._calibre
    
    def __str__(self):
        return f"{self._calibre}:{self._dureza}:{self._tamanho}"

class Lapiseira: 
    def __init__(self, calibre: float):
        self._calibre = calibre
        self._bico: Grafite | None = None 
        self._tambor = []

    def __str__(self):
        return f"calibre: {self._calibre}, bico: {self.get_bico()}, tambor: <{self.get_tambor()}>" 


    
    def get_tambor(self):
        grafites_reserva = ""
        for elem in self._tambor:
            grafites_reserva += "["
            grafites_reserva += str(elem)
            grafites_reserva += "]"

        return grafites_reserva
    
    def get_bico(self):
        if self._bico is None: 
            return "[]"
        return "["+ str(self._bico) + "]"


    def inserirGrafite(self, grafite: Grafite):
        if grafite._calibre != self._calibre:
            print("fail: calibre incompatível")
            return 
        self._tambor.append(grafite)

    def puxarGrafite(self):
        if self._bico is not None: 
            print("fail: ja existe grafite no bico")
            return 
        if len(self._tambor) == 0:
            return
        self._bico = self._tambor.pop(0)
    
    def remover(self):
        if self._bico is None:
            print("fail: nao existe grafite no bico")
            return
        if self._bico is not None: 
            self._bico = None 
    
    def escrever(self):
        if self._bico is None: 
            print("fail: nao existe grafite no bico")
            return
        if self._bico.get_tamanho() <= 10:
            print("fail: tamanho insuficiente")
            self._bico = None
            return 
        
        expessura: dict[str, int] = {
        "HB": 1,
        "2B": 2, 
        "4B": 4,
        "6B": 6
        }

        consumo = expessura[self._bico.get_dureza()]

        if self._bico.get_tamanho() < 10:
            print("fail: tamanho insuficiente")
            self._bico = None
            return

        if self._bico.get_tamanho() - consumo < 10:
            print("fail: folha incompleta")
            self._bico._tamanho = 10 
            return
        
        self._bico._tamanho -= consumo

        
        
def main():
    lapiseira = Lapiseira(None)
    while True:
        line = input()
        print (f"${line}")
        args = line.split()

        if args[0] == "end":
            break 

        elif args[0] == "init":
            lapiseira = Lapiseira(float(args[1]))
        
        elif args[0] == "insert":
            calibre = float(args[1])
            dureza = args[2]
            tamanho = int(args[3])
            grafite = Grafite(tamanho, dureza, calibre)
            lapiseira.inserirGrafite(grafite)
            
        elif args[0] == "show":
            print(lapiseira)
        
        elif args[0] == "pull":
            lapiseira.puxarGrafite()

        elif args[0] == "remove":
            lapiseira.remover()
        
        elif args[0] == "write":
            lapiseira.escrever()


main()