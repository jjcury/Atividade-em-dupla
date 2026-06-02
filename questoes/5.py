class CofreDoDragao:
    def __init__(self, nome_dragao, tesouros):
        self.nome_dragao = nome_dragao
        self.tesouros = tesouros

    def adicionar_item(self, nome, valor):
        if nome != "" and valor > 0:
            tesouro = {
                "nome": nome,
                "valor": valor
            }
            self.tesouros.append(tesouro)
            print("Tesouro adicionado.")
        else:
            print("Dados inválidos.")

    def listar_itens(self):
        print("Tesouros do cofre:")
        for tesouro in self.tesouros:
            print("Nome:", tesouro["nome"], "- Valor:", tesouro["valor"])

    def calcular_total(self):
        total = 0

        for tesouro in self.tesouros:
            total += tesouro["valor"]

        return total

    def encontrar_item_mais_valioso(self):
        maior = self.tesouros[0]

        for tesouro in self.tesouros:
            if tesouro["valor"] > maior["valor"]:
                maior = tesouro

        return maior

    def classificar_colecao(self):
        total = self.calcular_total()

        if total < 500:
            return "Coleção pequena"
        elif total <= 1500:
            return "Coleção respeitável"
        else:
            return "Coleção lendária"

    def exibir_relatorio(self):
        item = self.encontrar_item_mais_valioso()

        print("Nome do dragão:", self.nome_dragao)
        print("Total acumulado:", self.calcular_total())
        print("Item mais valioso:", item["nome"], "-", item["valor"])
        print("Classificação:", self.classificar_colecao())

cofre = CofreDoDragao("Smaug", [])

cofre.adicionar_item("Coroa", 500)
cofre.adicionar_item("Anel", 120)
cofre.adicionar_item("Espada", 300)

cofre.listar_itens()
cofre.exibir_relatorio()