class CofreDoDragao:
    def __init__(self, nome_dragao, tesouros):
        self.nome_dragao = nome_dragao
        self.tesouros = tesouros

    def adicionar_item(self, nome, valor):
        if nome != "" and valor > 0:
            self.tesouros.append(nome + ":" + str(valor))
            print("Tesouro adicionado.")
        else:
            print("Dados inválidos.")

    def listar_itens(self):
        print("Tesouros do cofre:")
        for tesouro in self.tesouros:
            print(tesouro)

    def calcular_total(self):
        total = 0

        for tesouro in self.tesouros:
            partes = tesouro.split(":")
            valor = int(partes[1])
            total += valor

        return total

    def encontrar_item_mais_valioso(self):
        maior_nome = ""
        maior_valor = 0

        for tesouro in self.tesouros:
            partes = tesouro.split(":")
            nome = partes[0]
            valor = int(partes[1])

            if valor > maior_valor:
                maior_valor = valor
                maior_nome = nome

        return maior_nome + ":" + str(maior_valor)

    def classificar_colecao(self):
        total = self.calcular_total()

        if total < 500:
            return "Coleção pequena"
        elif total <= 1500:
            return "Coleção respeitável"
        else:
            return "Coleção lendária"

    def exibir_relatorio(self):
        print("Nome do dragão:", self.nome_dragao)
        print("Total acumulado:", self.calcular_total())
        print("Item mais valioso:", self.encontrar_item_mais_valioso())
        print("Classificação:", self.classificar_colecao())


# Teste
cofre = CofreDoDragao("Lelo", [])

cofre.adicionar_item("coroa", 500)
cofre.adicionar_item("anel", 120)
cofre.adicionar_item("espada", 300)

cofre.listar_itens()
cofre.exibir_relatorio()