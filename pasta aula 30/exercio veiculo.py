import os 
os.system("cls || clear") #Limpa o terminal

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_detalhes(self):
        return f"{self.ano} {self.marca} {self.modelo}"

    def ligar(self):
        return f"O {self.modelo} está ligado."

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)  # Chama o construtor da classe base
        self.portas = portas

    def abrir_portas(self):
        return f"O {self.modelo} tem {self.portas} portas abertas."

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas

    def empinar(self):
        return f"A moto {self.modelo} com {self.cilindradas} cilindradas está empinando!"

# Criando objetos
carro1 = Carro("Toyota", "Corolla", 2020, 4)
moto1 = Moto("Honda", "CBR 600RR", 2022, 600)

# Utilizando métodos
print(carro1.exibir_detalhes())  # Saída: 2020 Toyota Corolla
print(carro1.ligar())           # Saída: O Corolla está ligado.
print(carro1.abrir_portas())    # Saída: O Corolla tem 4 portas abertas.

print(moto1.exibir_detalhes())  # Saída: 2022 Honda CBR 600RR
print(moto1.ligar())            # Saída: O CBR 600RR está ligado.
print(moto1.empinar())          # Saída: A moto CBR 600RR com 600 cilindradas está empinando!