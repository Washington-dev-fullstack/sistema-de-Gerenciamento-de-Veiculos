from abc import ABC, abstractmethod

# Classe Abstrata Veiculo
class Veiculo(ABC):
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    # Método concreto que retorna as informações básicas
    def info(self):
        return f"{self.marca} {self.modelo} (Ano: {self.ano})"

    # Método abstrato que obriga as subclasses a implementarem o cálculo
    @abstractmethod
    def calcular_aluguel(self, dias):
        pass

# Classes Concretas
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, num_portas):
        super().__init__(marca, modelo, ano)
        self.num_portas = num_portas

    # Sobrescrevemos o método info para incluir o atributo extra
    def info(self):
        return f"Carro: {super().info()} - {self.num_portas} portas"

    def calcular_aluguel(self, dias):
        return 150.00 * dias


class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas

    def info(self):
        return f"Moto: {super().info()} - {self.cilindradas}cc"

    def calcular_aluguel(self, dias):
        return 80.00 * dias


class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, capacidade_ton):
        super().__init__(marca, modelo, ano)
        self.capacidade_ton = capacidade_ton

    def info(self):
        return f"Caminhão: {super().info()} - Capacidade: {self.capacidade_ton} Ton"

    def calcular_aluguel(self, dias):
        return 350.00 * dias

# Criando a lista
lista_veiculos = [
    Carro("Chevrolet", "Onix", 2023, 4),
    Moto("Honda", "CB 500", 2022, 500),
    Caminhao("Volvo", "FH 540", 2021, 25)
]

# Interação com o usuário
while True:
    try:
        print("\n" + "="*50)
        print("Bem-vindo ao Sistema de Gerenciamento de Veículos")
        print("(ou 's' caso queira encerrar o sistema)")
        print("="*50 + "\n")
        resposta = input("Digite a quantidade de dias para o aluguel (ou s): ").strip().lower()

        if resposta == "s":
            print("\nEncerrando...")
            break

        dias_aluguel = int(resposta)
        
        print("\n" + "="*50)
        print(" "*13 + "ALUGUEL DE VEÍCULOS")
        print("="*50)

        # O laço percorre a lista chamando o mesmo método para objetos diferentes (Polimorfismo)
        for veiculo in lista_veiculos:
            valor_total = veiculo.calcular_aluguel(dias_aluguel)
        
            # Formatando o valor para o padrão de moeda brasileiro (R$)
            valor_formatado = f"R$ {valor_total:.2f}".replace(".", ",")
            print(f"{veiculo.info()}")
            print(f"-> Valor total para {dias_aluguel} dias: {valor_formatado}")
            print("-" * 50)

    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido para os dias.")
