class RoboColetor:
    def __init__(self, nome, amostras, capacidade_maxima):
        self.nome = nome
        self.amostras = amostras
        self.capacidade_maxima = capacidade_maxima

    def adicionar_amostra(self, amostra):
        if amostra != "" and len(self.amostras) < self.capacidade_maxima:
            self.amostras.append(amostra)
            print("Amostra adicionada com sucesso.")
        else:
            print("Não foi possível adicionar a amostra.")

    def listar_amostras(self):
        print("Amostras coletadas:")
        for amostra in self.amostras:
            print(amostra)

    def contar_amostras(self):
        return len(self.amostras)

    def verificar_armazenamento(self):
        if len(self.amostras) >= self.capacidade_maxima:
            print("Armazenamento cheio.")
        else:
            print("Ainda há espaço disponível.")

    def exibir_relatorio(self):
        print("Nome do robô:", self.nome)
        print("Quantidade de amostras:", self.contar_amostras())
        print("Capacidade máxima:", self.capacidade_maxima)
        self.verificar_armazenamento()

robo = RoboColetor("Explorer-1", [], 3)

robo.adicionar_amostra("Rocha")
robo.adicionar_amostra("Areia")
robo.adicionar_amostra("Cristal")
robo.adicionar_amostra("Gás")  

robo.listar_amostras()
robo.exibir_relatorio()