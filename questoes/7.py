class ExpedicaoTemplo:
    def __init__(self, nome_expedicao, desafios, energia_inicial):
        self.nome_expedicao = nome_expedicao
        self.desafios = desafios
        self.energia = energia_inicial
        self.pontos = 0
        self.desafios_concluidos = []

    def listar_desafios(self):
        print("Desafios disponíveis:")

        for i in range(len(self.desafios)):
            desafio = self.desafios[i]

            print(
                i,
                "-",
                desafio["nome"],
                "- Custo:",
                desafio["custo"],
                "- Recompensa:",
                desafio["recompensa"]
            )

    def tentar_desafio(self, numero_desafio):
        if numero_desafio < 0 or numero_desafio >= len(self.desafios):
            print("Desafio inválido.")
            return

        desafio = self.desafios[numero_desafio]

        if desafio in self.desafios_concluidos:
            print("Esse desafio já foi concluído.")
            return

        if self.energia >= desafio["custo"]:
            self.energia -= desafio["custo"]
            self.pontos += desafio["recompensa"]
            self.desafios_concluidos.append(desafio)

            print("Desafio concluído:", desafio["nome"])
        else:
            print("Energia insuficiente.")

    def calcular_progresso(self):
        return len(self.desafios_concluidos)

    def verificar_situacao(self):
        if len(self.desafios_concluidos) == len(self.desafios):
            return "Expedição concluída."
        elif self.energia == 0:
            return "Expedição encerrada sem energia."
        else:
            return "Expedição em andamento."

    def exibir_relatorio(self):
        print("Nome da expedição:", self.nome_expedicao)
        print("Energia restante:", self.energia)
        print("Pontos:", self.pontos)
        print("Desafios concluídos:", self.calcular_progresso())
        print("Situação:", self.verificar_situacao())

desafios = [
    {"nome": "Ponte Quebrada", "custo": 20, "recompensa": 30},
    {"nome": "Sala Escura", "custo": 15, "recompensa": 20},
    {"nome": "Guardião Antigo", "custo": 40, "recompensa": 80}
]

expedicao = ExpedicaoTemplo("Templo Perdido", desafios, 100)

expedicao.listar_desafios()

expedicao.tentar_desafio(0)
expedicao.tentar_desafio(1)
expedicao.tentar_desafio(2)

expedicao.exibir_relatorio()