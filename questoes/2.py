class PortalDimensional:
    def __init__(self, nome, destino, energia_necessaria, energia_disponivel):
        self.nome = nome
        self.destino = destino
        self.enegia_nessesaria = energia_necessaria
        self.enegia_disponivel = energia_disponivel
    
    def pode_abrir(self):
        if self.enegia_disponivel >= 20:
            print("portal pode ser aberto.")

        else:
            print("portal nao pode ser aberto.")

    def calcular_falta_energia(self):
        total = self.enegia_disponivel - self.enegia_nessesaria
        print(f"essa e quantidade de energia disponivel: {total}")

    def classificar_estabilidade(self):
        if self.enegia_disponivel == 0:
            print(" portal estável.")

        elif self.enegia_disponivel == 20:
            print("portal quase estável.")

        else:
            print("portal instável.")

    def exibir_resumo(self):
        print(f"resumo nome:{self.nome}, destino:{self.destino}, energia nessenaria:{self.enegia_nessesaria}, situacao do portal:{self.classificar_estabilidade}")

p1 = PortalDimensional("portal gun","ifrs",20,100)
print(p1.pode_abrir())
print(p1.calcular_falta_energia())
p1.classificar_estabilidade()
p1.exibir_resumo()