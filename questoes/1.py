class CapsulaDoTempo:
    def __init__(self, autor, mensagem, ano_abertura, ano_atual):
        self.autor = autor
        self.mensagem = mensagem
        self.ano_abertura = ano_abertura
        self.ano_atual = ano_atual

    def pode_abrir(self):
        if self.ano_atual >= self.ano_abertura:
            print("A cápsula pode ser aberta!")
        else:
            print("Você ainda não pode abrir a cápsula.")

    def calcular_espera(self):
        return self.ano_abertura - self.ano_atual

    def classificar_espera(self):
        tempo_de_espera = self.calcular_espera()

        if tempo_de_espera <= 0:
            print("Pode abrir agora.")
        elif tempo_de_espera <= 3:
            print("Espera curta.")
        else:
            print("Espera longa.")

    def exibir_resumo(self):
        print("Autor:", self.autor)
        print("Ano de abertura:", self.ano_abertura)
        self.classificar_espera()
        print("Mensagem:", self.mensagem)


cap1 = CapsulaDoTempo("Joaquim", "oi", 2030, 2026)
cap1.exibir_resumo()