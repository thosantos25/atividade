import os 
os.system("cls || clear") # Limpa o terminal

# Função 

class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial  # Atributo privado

    @property
    def saldo(self):
        """Getter para o saldo."""
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        """Setter para o saldo."""
        if valor >= 0:
            self.__saldo = valor
        else:
            print("Saldo não pode ser negativo.")

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

# Criando uma conta bancária
conta = ContaBancaria("Maria", 1000)

# Usando o getter para consultar o saldo
print(f"Saldo inicial: R$ {conta.saldo:.2f}")  # Saída: Saldo inicial: R$ 1000.00

# Usando o setter para alterar o saldo diretamente
conta.saldo = 2000
print(f"Novo saldo: R$ {conta.saldo:.2f}")  # Saída: Novo saldo: R$ 2000.00

# Tentando definir um saldo inválido
conta.saldo = -500  # Saída: Saldo não pode ser negativo.

# Realizando depósito e saque
conta.depositar(500)            # Saída: Depósito de R$ 500.00 realizado com sucesso!
print(f"Saldo após depósito: R$ {conta.saldo:.2f}")  # Saída: Saldo após depósito: R$ 2500.00

conta.sacar(700)                # Saída: Saque de R$ 700.00 realizado com sucesso!
print(f"Saldo final: R$ {conta.saldo:.2f}")         # Saída: Saldo final: R$ 1800.00
