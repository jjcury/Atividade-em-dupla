class MochilaDeMissao:
    def __init__(self, agente, equipamentos, capacidade_maxima):
        self.agente = agente
        self.equipamentos = equipamentos
        self.capacidade_maxima = capacidade_maxima

    def adicionar_equipamento(self, equipamento):
        equipamento = input("diga o equipamento que deseja: ")
        if equipamento != "":
            print("equipamento adicionado")
            self.equipamentos.append(equipamento)

        elif equipamento == "":
            print("nao foi possivel adicionar na lista.")

    def listar_equipamentos(self):
        print(f"essa e a lista de equipamentos da sua lista: {self.equipamentos}.")
    
    def contar_equipamentos(self):
        print(f"essa e quantidade de equipamentos guardados: {len(self.equipamentos)}")

    def verificar_espaco(self):
        capacidade = int(self.equipamentos - self.capacidade_maxima)
        if capacidade > self.capacidade_maxima:
            print("nao e possivel adicionar mais nada a mochila")

        else:
            print("pode adicionar mais coisas na mochila")


    def exibir_relatorio(self):
        print(f"esse e o resumo:agente: {self.agente}, esses sao os equipamentos: {self.equipamentos} e a capacidade maxima:{self.capacidade_maxima}")
m1 = MochilaDeMissao("anthony",[],10)
print(m1.adicionar_equipamento(2))
print(m1.listar_equipamentos("faca"))
print(m1.contar_equipamentos(len([])))
print(m1.verificar_espaco())