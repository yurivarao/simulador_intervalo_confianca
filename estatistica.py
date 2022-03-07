# Classe contendo os métodos para gerar a Estatística do Simulador
import math
import numpy as np
import pandas as pd


class Estatistica:

    def __init__(self):
        # 
        print("Gerando estatísticas...\n")

    def obterMediaLognormal(self,valores):
        # Calcular a Média com Logaritmo
        soma = 0
        count = len(valores)
        for i in range(0, count):
            soma += math.log(valores[i])
        self.media = soma/count
        return self.media

    def obterMedia(self,valores):
        return np.mean(valores)
        
    def obterDesvioPadraoLognormal(self,valores,media):
        # Calcula Desvio Padrão com Logaritmo
        soma = 0
        count = len(valores)
        for i in range(0, count):
            soma += (math.log(valores[i]) - self.media) ** 2
        self.desvioPadrao = (soma/count) ** 0.5
        return self.desvioPadrao
    
    def obterDesvioPadrao(self,valores):
        return np.std(valores)

    def gerarDadosArtificiaisLognormal(self,media,desvioPadrao,tamanhoArtificial):
        dadosArtificiais = np.random.lognormal(media,desvioPadrao,round(tamanhoArtificial))
        return dadosArtificiais

    def obterPrecisao_H(self,tamanhoAmostra, desvioPadrao, alfa):
        # Calcular a Precisão estatística
        tabelaStudentT = pd.read_csv("TabelaStudentT.csv")
        #tabelaStudentT = pd.read_csv("C:/Users/Yuri/Documents/Yuri/Projetos Python/simulador-148/AssetsSim/TabelaStudentT.csv")
        tAlfa = str(float(alfa) / 2)
        tabelaStudentTAlfa = tabelaStudentT[tAlfa]
        tabelaStudentTN = tabelaStudentT['v']
        nStudent = tamanhoAmostra - 1
        t = 0
        for i in range(len(tabelaStudentTAlfa)):
            if nStudent == tabelaStudentTN[i]:
                t = tabelaStudentTAlfa[i]
            elif 30 <= nStudent < 32:
                t = tabelaStudentTAlfa[29]
            elif 32 <= nStudent < 34:
                t = tabelaStudentTAlfa[30]
            elif 34 <= nStudent < 36:
                t = tabelaStudentTAlfa[31]
            elif 36 <= nStudent < 38:
                t = tabelaStudentTAlfa[32]
            elif 38 <= nStudent < 40:
                t = tabelaStudentTAlfa[33]
            elif 40 <= nStudent < 42:
                t = tabelaStudentTAlfa[34]
            elif 42 <= nStudent < 44:
                t = tabelaStudentTAlfa[35]
            elif 44 <= nStudent < 46:
                t = tabelaStudentTAlfa[36]
            elif 46 <= nStudent < 48:
                t = tabelaStudentTAlfa[37]
            elif 48 <= nStudent < 50:
                t = tabelaStudentTAlfa[38]
            elif 50 <= nStudent < 52:
                t = tabelaStudentTAlfa[39]
            elif 52 <= nStudent < 54:
                t = tabelaStudentTAlfa[40]
            elif 54 <= nStudent < 56:
                t = tabelaStudentTAlfa[41]
            elif 56 <= nStudent < 58:
                t = tabelaStudentTAlfa[42]
            elif 58 <= nStudent < 60:
                t = tabelaStudentTAlfa[43]
            elif 60 <= nStudent < 120:
                t = tabelaStudentTAlfa[44]
            elif nStudent == 120:
                t = tabelaStudentTAlfa[45]
            elif nStudent > 120:
                t = tabelaStudentTAlfa[46]
        self.valorPrecisao = t * (desvioPadrao / math.sqrt(tamanhoAmostra))
        return self.valorPrecisao

    def estimar_N(self,tamanhoAmostra, hPretendido, hEstimado):
        # Estimar o valor de N
        self.nEstimado = round(tamanhoAmostra * pow((hEstimado / hPretendido), 2))
        return self.nEstimado