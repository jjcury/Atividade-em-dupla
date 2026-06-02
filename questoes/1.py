class CapsulaDoTempo:
    def __init__(self, autor, mensagem, ano_abertura, ano_atual):
        self.autor=autor
        self.mensagem=mensagem
        self.ano_abertura=ano_abertura
        self.ano_atual=ano_atual
    
    def pode_abrir(self):
        if self.ano_atual==self.ano_abertura:
            print("A cápsula pode ser aberta!")
        else:
            print("Você ainda não pode abrir a cápsula.")
    
    def calcular_espera(self):
        return(f"Faltam {self.ano_abertura-self.ano_atual} anos para a cápsula ser aberta.")

    def classificar_espera(self):
        TempoDeEspera=self.pode_abrir()
        if TempoDeEspera==0:
            print("Pode abrir agora.")
        
        elif TempoDeEspera>=1 and TempoDeEspera<=3:
            print("Espera curta.")
        
        else: print("Espera longa.")
    
    def exibir_resumo(self):
        print(self.autor)
        print(self.ano_abertura)
        self.classificar_espera()
        print(self.mensagem)
    
cap1 = CapsulaDoTempo("Joaquim", "oi", 2030, 2026)
cap1.exibir_resumo