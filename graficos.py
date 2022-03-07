# Classe contendo os métodos para gerar Gráficos dos resultados no Simulador
import matplotlib.pyplot as plt
import plotly.graph_objects as go
#import talib


class Graficos:
    
    def __init__(self):
        # 
        print("Gráficos...\n")

    def plotarDadosReais(self,DadosReais):
        fig = plt.figure(figsize=(15, 8))
        fig.suptitle("Simulação", fontsize=15)
        spec = fig.add_gridspec(ncols=1, nrows=1)

        axs0 = fig.add_subplot(spec[0, 0])

        axs0.plot(DadosReais, "-")
        axs0.set_title("Dados Reais")
        axs0.set_xlabel("Iteração")
        axs0.set_ylabel('Preço')

        plt.show()
        
    def plotarDadosReaisPrecosSimulados(self,dadosPrecosSimulados):
        fig = plt.figure(figsize=(15, 8))
        fig.suptitle("Simulação", fontsize=15)
        spec = fig.add_gridspec(ncols=1, nrows=1)

        axs0 = fig.add_subplot(spec[0, 0])

        dadosSimuladosAbertura = [float(abertura[0]) for abertura in dadosPrecosSimulados]
        dadosSimuladosMaxima = [float(maxima[1]) for maxima in dadosPrecosSimulados]
        dadosSimuladosMinima = [float(minima[2]) for minima in dadosPrecosSimulados]
        dadosSimuladosFechamento = [float(fechamento[3]) for fechamento in dadosPrecosSimulados]

        axs0.plot(dadosSimuladosAbertura,"sc",label="Abertura")
        axs0.plot(dadosSimuladosMaxima,"sg",label="Máxima")
        axs0.plot(dadosSimuladosMinima,"sr",label="Mínima")
        axs0.plot(dadosSimuladosFechamento,"sb",label="Fechamento")
        
        axs0.legend(loc="upper left")
        axs0.set_title("Dados Preços Simulados")
        axs0.set_xlabel("Iteração")
        axs0.set_ylabel('Preço')

        plt.show()

    def plotarDadosReaisCandleStick(self,DadosReais):
        fig = go.Figure(data=[go.Candlestick(x=DadosReais["Data"],
                       open=DadosReais["Abertura"], high=DadosReais["Máxima"],
                       low=DadosReais["Mínima"], close=DadosReais["Último"])])
        
        fig.update_layout(xaxis_rangeslider_visible=False,
            title="Dados Reais",
            yaxis_title="Preços")
        
        fig.show()

    def plotarResultadosSetup(self,resultadosSetup):        
        fig = plt.figure(figsize=(15, 8))
        fig.suptitle("Simulação", fontsize=15)
        spec = fig.add_gridspec(ncols=1, nrows=1)

        axs0 = fig.add_subplot(spec[0, 0])
        
        # Tupla: (Preço Atual, Entrada, Stop Loss, Stop Gain)
        valoresEntrada = [float("NaN") if entrada[1] == 0 else entrada[1] for entrada in resultadosSetup]
        valoresSL = [float("NaN") if sl[2] == 0 else sl[2] for sl in resultadosSetup]
        valoresSG = [float("NaN") if sg[3] == 0 else sg[3] for sg in resultadosSetup]
        valoresPrecoAtual= [float("NaN") if precoAtual[4] == 0 else precoAtual[4] for precoAtual in resultadosSetup]
        #
        #print("Resultados SETUP...\n",resultadosSetup)
        axs0.plot(valoresPrecoAtual,"ok",label="Preço Atual")
        axs0.plot(valoresEntrada,"*y",label="Entrada")
        axs0.plot(valoresSL,"-r",label="Stop Loss")
        axs0.plot(valoresSG,"-g",label="Stop Gain")
        axs0.legend(loc="upper left")
        axs0.set_title("Resultados do Setup")        
        axs0.set_ylabel('Preço')

        plt.show()

    def plotarSaldo(self,saldoAcumulado):
        fig = plt.figure(figsize=(15, 8))
        fig.suptitle("Simulação", fontsize=15)
        spec = fig.add_gridspec(ncols=1, nrows=1)

        axs0 = fig.add_subplot(spec[0, 0])

        axs0.plot(saldoAcumulado, "-")
        axs0.set_title("Saldo das Operações")
        axs0.set_xlabel("Iteração")
        axs0.set_ylabel('Preço')

        plt.show()

    def plotarSinaisIndicadores(self,dadosSimulados,sinaisIndicadores,posicoes):        
        fig = plt.figure(figsize=(15, 8))
        fig.suptitle("Simulação", fontsize=15)
        spec = fig.add_gridspec(ncols=1, nrows=1)

        axs0 = fig.add_subplot(spec[0, 0])
        
        #
        #print("Dados Simulados\n",dadosSimulados)
        #
        dadosSimuladosAbertura = [float("NaN") if abertura[0] == 0 else float(abertura[0]) for abertura in dadosSimulados]
        dadosSimuladosMaxima = [float("NaN") if maxima[1] == 0 else float(maxima[1]) for maxima in dadosSimulados]
        dadosSimuladosMinima = [float("NaN") if minima[2] == 0 else float(minima[2]) for minima in dadosSimulados]
        dadosSimuladosFechamento = [float("NaN") if fechamento[3] == 0 else float(fechamento[3]) for fechamento in dadosSimulados]
        #
        #print("Sinais Indicadores\n",sinaisIndicadores)
        #
        #print("Dados Simulados Abertura\n",dadosSimuladosAbertura)
        #print("Dados Simulados Maxima\n",dadosSimuladosMaxima)
        #print("Dados Simulados Minima\n",dadosSimuladosMinima)
        #print("Dados Simulados Fechamento\n",dadosSimuladosFechamento)

        # Tupla: (Sinal Indicador de Tendência, Sinal Indicador de Entrada)
        valoresIndicadorTendencia = [float("NaN") if (sinalTendencia[0] == [] or sinalTendencia[0] == 0.0) else float(sinalTendencia[0]) for sinalTendencia in sinaisIndicadores]
        valoresIndicadorEntrada = [float("NaN") if (sinalEntrada[1] == [] or sinalEntrada[1] == 0.0) else float(sinalEntrada[1]) for sinalEntrada in sinaisIndicadores]
        
        #
        #print("Sinais de Tendência\n",valoresIndicadorTendencia)
        #print("Sinais de Entrada\n",valoresIndicadorEntrada)
        
        #
        valoresPosicoes = [float("NaN") if (posicao == [] or posicao == 0.0) else float(posicao) for posicao in posicoes]
        #
        axs0.plot(dadosSimuladosAbertura,"sc",label="Abertura")
        axs0.plot(dadosSimuladosMaxima,"sg",label="Máxima")
        axs0.plot(dadosSimuladosMinima,"sr",label="Mínima")
        axs0.plot(dadosSimuladosFechamento,"sb",label="Fechamento")
        axs0.plot(valoresIndicadorTendencia,"-*k",label="Sinal do Indicador de Tendência")
        axs0.plot(valoresIndicadorEntrada,"-m",label="Sinal do Indicador de Entrada")
        axs0.plot(valoresPosicoes,"oy",label="Posições")
        axs0.legend(loc="upper left")
        axs0.set_title("Sinais dos Indicadores")        
        axs0.set_ylabel('Sinais')

        plt.show()

    def plotarPontosDadosArtificiais(self,pontosDadosArtificiais):
        fig = plt.figure(figsize=(15, 8))
        fig.suptitle("Dados Artificiais do Simulador", fontsize=15)
        spec = fig.add_gridspec(ncols=1, nrows=1)

        axs0 = fig.add_subplot(spec[0, 0])

        axs0.plot(pontosDadosArtificiais)
        axs0.set_title("Pontos Artificiais Relevantes")
        axs0.set_xlabel("Iteração")
        axs0.set_ylabel("Pontos de Movimento e Correção")

        plt.show()
        
    def plotarHistogramas(self,movimentosDadosReais,correcoesDadosReais,movimentosDadosArtificiais,correcoesDadosArtificiais):
        fig = plt.figure(figsize=(15, 8))
        fig.suptitle("Histograma dos Dados Reais e Artificiais do Simulador", fontsize=15)
        spec = fig.add_gridspec(ncols=2, nrows=2)

        axs0 = fig.add_subplot(spec[0, 0])
        axs1 = fig.add_subplot(spec[0, 1])
        axs2 = fig.add_subplot(spec[1, 0])
        axs3 = fig.add_subplot(spec[1, 1])

        axs0.hist(movimentosDadosReais,10,color="green")
        axs0.set_title("Movimentos Dados Reais")
        axs0.set_xlabel("Pontos")
        axs0.set_ylabel("Frequência")

        axs1.hist(correcoesDadosReais,10,color="red")
        axs1.set_title("Correções Dados Reais")
        axs1.set_xlabel("Pontos")
        axs1.set_ylabel("Frequência")

        axs2.hist(movimentosDadosArtificiais,10,color="green")
        axs2.set_title("Movimentos Dados Artificiais")
        axs2.set_xlabel("Pontos")
        axs2.set_ylabel("Frequência")

        axs3.hist(correcoesDadosArtificiais,10,color="red")
        axs3.set_title("Correções Dados Artificiais")
        axs3.set_xlabel("Pontos")
        axs3.set_ylabel("Frequência")

        plt.show()

    def plotarSARParabolico (self, dadosSimulados, sinaisIndicadores):

        #psar = talib.SAR(np.array(DadosReais['Máxima']), np.array(DadosReais['Mínima']), acceleration=0.02, maximum=0.2)
        dadosFechamentos =  [float(0.0) if fechamento == [] else float(fechamento[0]) for fechamento in dadosSimulados]
        indicadorTendencia = [float(0.0) if sinalTendencia == [] else float(sinalTendencia[0]) for sinalTendencia in sinaisIndicadores]

        #fig1 = plt.style.use('fast')
        #fig1 = plt.figure(figsize=(15, 8))
        #fig1.suptitle("Simulação", fontsize=20)
        #spec1 = fig1.add_gridspec(ncols=1, nrows=1)
        #aux1 = fig1.add_subplot(spec1[0, 0])

        #aux1.plot(DadosReais['Último'][:100], '-o', DadosReais['Máxima'][:100], 'sb', DadosReais['Mínima'][:100], 'sr', psar[:100], 'sy')

        fig2 = plt.style.use('fast')
        fig2 = plt.figure(figsize=(15, 8))
        spec2 = fig2.add_gridspec(ncols=1, nrows=1)
        aux2 = fig2.add_subplot(spec2[0, 0])

        aux2.plot(dadosFechamentos, '-o', indicadorTendencia, 'sy')

        plt.grid()
        plt.show()     