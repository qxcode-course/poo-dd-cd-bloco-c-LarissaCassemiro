# O objetivo desta atividade é implementar métodos para manipular uma sala de cinema, permitindo a reserva, cancelamento e consulta de cadeiras.

# - **Descrição**
#   - A sala de cinema é representada pela classe Sala `Theater`, que possui um conjunto de cadeiras, cada uma associada a um cliente ou vazia.
#   - Os métodos a serem implementados permitirão reservar uma cadeira para um cliente, cancelar a reserva de uma cadeira e consultar o estado das cadeiras na sala.
#   - Cada cadeira pode estar associada a um objeto Cliente `Client`, representando um cliente que reservou a cadeira, ou ser nula, indicando que a cadeira está vazia.
#   - Os métodos fornecidos devem lidar com validações, como verificar se a cadeira existe, se está ocupada e se o cliente já está presente na sala.

# - **Responsabilidades**
#   - A classe Sala `Theater` é responsável por gerenciar as operações relacionadas às cadeiras na sala de cinema.
#     - Métodos a serem implementados:
#       - públicos: são métodos acessados por outras classes.
#         - `reserve(id: string, phone: number, index: number)`: Reserva uma cadeira para um cliente com o ID e telefone especificados.
#         - `cancel(id: string)`: Cancela a reserva de uma cadeira para o cliente com o ID especificado.
#         - `getSeats(): Array<Client | null>`: Retorna um array contendo o estado atual de todas as cadeiras na sala.
#         - `toString(): string`: Retorna uma representação em string do estado atual das cadeiras na sala.
#       - privados: são métodos apenas de uso interno, utilizados para auxiliar as operações da classe.
#         - `search(name: string): int`: Procura o índice da cadeira reservada pelo cliente com o nome especificado.
#         - `verifyIndix(index: number)`: Verifica se um índice de cadeira é válido na sala.
#   - A classe `Client` é responsável por representar os clientes que reservam cadeiras na sala de cinema.
#     - A classe possui métodos para obter e definir o ID e telefone do cliente, bem como uma representação em string do cliente.

class Cliente: 
    def __init__(self, id: str, phone: int):
        self.id = id 
        self.phone = phone 
    
    def __str__(self):
        return f"{self.id}:{self.phone}"

class Sala: 
    def __init__(self, quant_cadeiras):
        self.cadeiras: list[Cliente | None]
        self.cadeiras = [None for _ in range(quant_cadeiras)]

    def reserve(self, id: str, phone: int, index: int):

        if index < 0 or index >= len(self.cadeiras):
            print("fail: cadeira nao existe")
            return

        for cadeira in self.cadeiras:
            if cadeira is not None and cadeira.id == id:
                print("fail: cliente ja esta no cinema")
                return
        
        if self.cadeiras[index] is not None:
            print("fail: cadeira ja esta ocupada")
            return

        self.cadeiras[index] = Cliente(id, phone)

    def cancel(self, id: str):
        for i, cadeira in enumerate(self.cadeiras):
            if cadeira is not None and cadeira.id == id:
                self.cadeiras[i] = None
                return
        print("fail: cliente nao esta no cinema")

    def __str__(self):
        return "[" + " ".join("-" if x is None else str(x) for x in self.cadeiras) + "]"

def main():
    sala = Sala(0)
    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break

        elif args[0] == "init":
            sala = Sala(int(args[1]))

        elif args[0] == "show":
            print(sala)
        
        elif args[0] == "reserve":
            id = args[1]
            phone = int(args[2])
            index = int(args[3])
            sala.reserve(id, phone, index)

        elif args[0] == "cancel":
            sala.cancel(args[1])


main()