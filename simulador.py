# Classe contendo o núcleo do Simulador
import pandas as pd
import os

#from pandas.core.frame import DataFrame
from operacao import Operacao
#from indicador import Indicador
from setup import Setup
from graficos import Graficos
from estatistica import Estatistica
# Para utilizar a API deve-se instalar o módulo "!sudo pip install alpha-vantage"
from alpha_vantage.timeseries import TimeSeries

class Simulador:

    def __init__(self,origemDados):
        self.origemDados = origemDados
        self.periodo = 3
        self.precoAtual = 0.0
        self.aberturasAcumulado = []
        self.maximasAcumulado = []
        self.minimasAcumulado = []
        self.fechamentosAcumulado = []
        self.primeiroPrecoSimulado = 0.0
        self.resultadosSetup = []
        self.saldoAcumulado = []
        self.sinaisIndicadores = []
        self.dadosReaisPrecosSimulados = []
        self.posicoes = []
        self.tamanhoDadosIniciais = 10
        self.achou = False

        # Definição dos valores da Precisão e do Alfa para a simulação
        # Alfa para 99% = 0.01; Alfa para 95% = 0.05; Alfa para 90% = 0.10; Alfa para 80% = 0.20
        precisao = 0.05
        self.alfa = "0.05"

        self.movimentosDadosReais_Hpretendido = precisao
        self.correcoesDadosReais_Hpretendido = precisao
        self.movimentosDadosArtificiais_Hpretendido = precisao
        self.correcoesDadosArtificiais_Hpretendido = precisao
        #
        self.pontosDadosArtificiais = []
        #
        self.movimentosECorrecoesDadosReais = []
        self.movimentosDadosReais = []
        self.correcoesDadosReais = []
        self.movimentosDadosArtificiais = []
        self.correcoesDadosArtificiais = []
        #
        self.count = 0
        self.maior = 0
        # Definir qual o Tipo de Preço deve ser usado para Simular
        self.opcaoTipoPreco = True
        while self.opcaoTipoPreco:
            print("Digite qual Tipo de Preço será usado para gerar os dados\n")
            tipoEscolhido = input("Digite uma opção: ""1. Abertura"", ""2. Máxima"", ""3. Mínima"", ""4. Fechamento""\n")
            os.system("clear || cls")
            if tipoEscolhido == "1":            
                self.tipoPreco = "Abertura"
                self.opcaoTipoPreco = False
            elif tipoEscolhido == "2":            
                self.tipoPreco = "Máxima"
                self.opcaoTipoPreco = False                
            elif tipoEscolhido == "3":            
                self.tipoPreco = "Mínima"
                self.opcaoTipoPreco = False                
            elif tipoEscolhido == "4":            
                #self.tipoPreco = "Fechamento"
                self.tipoPreco = "Último"
                self.opcaoTipoPreco = False                
            else:
                print("\n Opção inválida") 
        
        # Obter os Preços Por Tipo escolhido pelo usuário
        if self.origemDados == "1":
            #arquivoCompleto = pd.read_csv("./dados_historicos/dolar_cheio4.csv",decimal=",")
            arquivoCompleto = pd.read_csv("C:/Users/yuriv/Dropbox/PC/Documents/backup/Universidade/Bloco 9/TCC II/simulador/AssetsSim/dados_historicos/dolar_cheio1.csv",decimal=",")
            df = pd.DataFrame(data=arquivoCompleto)

        elif self.origemDados == "2":
            dadosArtificiais = self.obterDadosReaisAlphavantage()
            df = pd.DataFrame(data=dadosArtificiais)
            
        elif self.origemDados == "3":
            dadosArtificiais = 0
            df = pd.DataFrame(data=dadosArtificiais)

        else:
            df = []
            print("Origem dos Dados não escolhida")

        # Coverter campos strings em float
        df["Abertura"] = df["Abertura"].str.replace(".","")
        df["Abertura"] = df["Abertura"].str.replace(",",".")
        df["Abertura"] = df["Abertura"].astype(float)
        df["Máxima"] = df["Máxima"].str.replace(".","")
        df["Máxima"] = df["Máxima"].str.replace(",",".")
        df["Máxima"] = df["Máxima"].astype(float)
        df["Mínima"] = df["Mínima"].str.replace(".","")
        df["Mínima"] = df["Mínima"].str.replace(",",".")
        df["Mínima"] = df["Mínima"].astype(float)
        df["Último"] = df["Último"].str.replace(".","")
        df["Último"] = df["Último"].str.replace(",",".")
        df["Último"] = df["Último"].astype(float)
        #print(df.dtypes)

        df = df.iloc[::-1]
        self.dadosCompletos = df.reset_index()

    def obterDadosReaisAlphavantage(self):
        # Mais informações sobre a API em https://github.com/RomelTorres/alpha_vantage
        api_key = "7O0DU78K9TWJXI0H"
        
        # Configuração da API
        ts = TimeSeries(key=api_key, output_format="pandas", indexing_type="date")

        # Buscar o Sticker
        #buscaSticker = input("Digite o ativo para busca do Sticker: \n")
        buscaSticker = "mglu3.sao"

        stickers = ts.get_symbol_search(buscaSticker)
        print("Ativos encontrados:\n",stickers)

        #sticker = input("Digite o código do Sticker: \n")
        sticker = "mglu3.sao"
        res_data, res_meta = ts.get_daily_adjusted(symbol=sticker, outputsize="full")
        #res_data, res_meta = ts.get_daily_adjusted(symbol=sticker)
        
        # Aqui apenas para dizer ao intellisense do vscode que os dados estão no formato Pandas
        data: DataFrame = res_data

        # Renomear o índice para pt_BR
        data.index.rename(name="Data", inplace=True)

        # Formator a data para utilizado no brasil
        data.index = data.index.strftime('%d/%m/%Y')

        # Renomear o índice para pt_BR
        data.rename(columns={
            "date": "Data",
            "1. open": "Abertura",
            "2. high": "Máxima",
            "3. low": "Mínima",
            "4. close": "Último",
            "5. adjusted close": "Fechamento ajustado",
            "6. volume": "Volume"
        }, inplace=True)
        #
        return data

    def precoPassoAPasso(self,i):
        self.precoAnterior = self.precoAtual
        self.precoAtual = self.dadosCompletos[self.tipoPreco].iloc[i]
        
        self.dadosReaisPrecosSimulados.append((self.dadosCompletos["Abertura"].iloc[i],self.dadosCompletos["Máxima"].iloc[i],\
            self.dadosCompletos["Mínima"].iloc[i],self.dadosCompletos["Último"].iloc[i]))
        #print("Dados Simulados\n",self.dadosReaisPrecosSimulados)
        #
        print("\nPreço ",i," de ",len(self.dadosCompletos) - 1," da ",self.tipoPreco,"\n")
        #
        self.precos(i)
        self.precosAcumulados(i)
        #
        if self.operar == True:
            resultado = self.setup.atualizar(self.tipoPreco,self.precoAtual,self.precoAnterior,self.periodo,\
                self.aberturas,self.maximas,self.minimas,self.fechamentos)            
            self.resultadosSetup.append(resultado)
            #print("Resultados do Setup\n",self.resultadosSetup)
            #
            self.setup.atualizarAcumulado(self.aberturasAcumulado,self.maximasAcumulado,\
                self.minimasAcumulado,self.fechamentosAcumulado)
            #
            sinais = self.setup.obterSinaisIndicadores()
            self.sinaisIndicadores.append(sinais)
            #print("Sinais dos Indicadores\n",self.sinaisIndicadores)
            #
            self.saldo = self.operacao.atualizar(self.precoAtual,resultado)
            self.saldoAcumulado.append(self.saldo)
            #
            self.posicoes.append(self.operacao.consultarPosicao())
            #print("Posições das Operações\n",self.posicoes)
            #
            movimentosECorrecoesDadosReais = self.setup.obterMovimentosECorrecoes()
            #print("Movimentos e Correções",movimentosECorrecoesDadosReais)
            self.movimentosECorrecoesDadosReais.append(movimentosECorrecoesDadosReais)
            #print("Movimentos e Correções ",self.movimentosECorrecoesDadosReais)
            #

        elif self.operar == False:
            print("Sem Operações...\n")

    def reinicializarDadosReais(self):
        self.precoAtual = 0.0
        self.resultadosSetup = []
        self.saldoAcumulado = []
        self.dadosReaisPrecosSimulados = []
        self.sinaisIndicadores = []
        self.movimentosECorrecoesDadosReais = []
        self.movimentosDadosReais = []
        self.correcoesDadosReais = []
        self.dadosReaisSimuladosNecessarios = []        
        self.aberturasAcumulado = []
        self.maximasAcumulado = []
        self.minimasAcumulado = []
        self.fechamentosAcumulado = []
        self.posicoes = []

    def reinicializarDadosArtificiais(self):
        self.pontosDadosArtificiais = []
        self.movimentosDadosArtificiais = []
        self.correcoesDadosArtificiais = []
        self.dadosArtificiaisSimuladosNecessarios = []
        
    def inicializarOperacaoESetup(self):

        if self.operar == True:                
            print("Iniciando Operação e Setup...\n")
            # Criar Instância de Operação
            self.operacao = Operacao()
            # Criar Instância do Setup
            self.setup = Setup(self.codigoSetup,self.codigoIndicadorTendencia,self.codigoIndicadorEntrada)
            # Chamar método para realizar operação
            self.operacao.iniciarOperacao()
            
        else:
            print("Sem operações...\n")
        
    def simular(self,operar,codigoSetup,codigoIndicadorTendencia,codigoIndicadorEntrada):
        self.operar = operar
        self.codigoSetup = codigoSetup
        self.codigoIndicadorTendencia = codigoIndicadorTendencia
        self.codigoIndicadorEntrada = codigoIndicadorEntrada
        #
        p = self.periodo - 1
        inicializar = True
        #
        self.opcaoSimular = True
        self.opcaoContinuarPreco = True
        # Loop de Preço
        #self.ordenados = []
        while self.opcaoSimular:
            while self.opcaoContinuarPreco:
                print("\n Preços a serem visualizados")
                print("""
                1. Passo a passo
                2. Todos
                3. Até o Preço
                4. A partir do Preço
                5. Intervalo de Preços
                6. Gráficos
                7. Estatística
                0. Parar
                """)
                opcaoContinuarPreco = input("Digite uma opção:")
                os.system("clear || cls")
                
                if opcaoContinuarPreco == "1" and p <= len(self.dadosCompletos):
                    if inicializar:
                        # Definir início do Preço Passo A Passo a partir do tamanho do Período
                        p = self.periodo - 1
                        self.inicializarOperacaoESetup()
                        self.reinicializarDadosReais()
                        self.reinicializarDadosArtificiais()
                        inicializar = False

                    self.precoPassoAPasso(p)
                    # Avançar no array de preços
                    p += 1

                elif opcaoContinuarPreco == "2":
                    print("Todos os Preços...\n")
                    self.inicializarOperacaoESetup()
                    self.reinicializarDadosReais()
                    self.reinicializarDadosArtificiais()
                    inicializar = True
                    p = self.periodo - 1
                    
                    for t in range(p,len(self.dadosCompletos)):
                        self.precoPassoAPasso(t)
                    
                elif opcaoContinuarPreco == "3":
                    print("Até o Preço...\n")
                    self.inicializarOperacaoESetup()
                    self.reinicializarDadosReais()
                    self.reinicializarDadosArtificiais()
                    inicializar = True
                    p = self.periodo - 1
                    
                    final = int(input("Digite o índice do Preço Final Desejado...\n"))
                    if final < len(self.dadosCompletos):
                        for t in range(p,final):
                            self.precoPassoAPasso(t)

                elif opcaoContinuarPreco == "4":
                    print("A partir do Preço...\n")
                    self.inicializarOperacaoESetup()
                    self.reinicializarDadosReais()
                    self.reinicializarDadosArtificiais()
                    inicializar = True
                    
                    inicial = int(input("Digite o índice do Preço Inicial Desejado...\n"))
                    if inicial < len(self.dadosCompletos):
                        for t in range(inicial,len(self.dadosCompletos)):
                            self.precoPassoAPasso(t)

                elif opcaoContinuarPreco == "5":
                    print("Intervalo de Preços...\n")
                    self.inicializarOperacaoESetup()
                    self.reinicializarDadosReais()
                    self.reinicializarDadosArtificiais()
                    inicializar = True
                    
                    inicial = int(input("Digite o índice do Preço Inicial Desejado...\n"))
                    final = int(input("Digite o índice do Preço Final Desejado...\n"))

                    if inicial < len(self.dadosCompletos) and final < len(self.dadosCompletos) and inicial < final:
                        for t in range(inicial,final):
                            self.precoPassoAPasso(t)

                elif opcaoContinuarPreco == "6":
                    print("Plotando Gráficos...\n")
                    grafico = Graficos()
                    grafico.plotarDadosReais(self.dadosCompletos[self.tipoPreco])
                    grafico.plotarDadosReaisPrecosSimulados(self.dadosReaisPrecosSimulados)
                    # Necessita instalar pacote para importar a biblioteca "plotly.graph_objects"
                    #grafico.plotarDadosReaisCandleStick(self.dadosCompletos)                    
                    grafico.plotarResultadosSetup(self.resultadosSetup)
                    grafico.plotarSaldo(self.saldoAcumulado)
                    grafico.plotarSinaisIndicadores(self.dadosReaisPrecosSimulados,self.sinaisIndicadores,self.posicoes)
                    grafico.plotarPontosDadosArtificiais(self.pontosDadosArtificiais)
                    grafico.plotarHistogramas(self.movimentosDadosReais,self.correcoesDadosReais,\
                        self.movimentosDadosArtificiais,self.correcoesDadosArtificiais)
                    #grafico.plotarSARParabolico(self.dadosReaisPrecosSimulados, self.sinaisIndicadores)

                elif opcaoContinuarPreco == "7":
                    
                    # Replicar N vezes até obter a Precisão H nos Dados Reais
                    self.replicarNVezesDadosReais()
                    # Replicar N vezes até obter a Precisão H nos Dados Artificiais
                    self.replicarNVezesDadosArtificiais()
                        
                elif opcaoContinuarPreco == "0":
                    print("\n Parando...")
                    self.opcaoSimular = False       
                    self.opcaoContinuarPreco = False   

                else:
                    print("\n Opção inválida ou Fim dos Dados Reais... ",p,"/",len(self.dadosCompletos))
                
    def precos(self,i):
        self.aberturas = []
        self.maximas = []
        self.minimas = []
        self.fechamentos = []
        if i < (self.periodo - 1):
            self.aberturas = []
            self.maximas = []
            self.minimas = []
            self.fechamentos = []
                
        else:            
            for p in range(i,i-self.periodo,-1):
                abertura = self.dadosCompletos["Abertura"].iloc[p]
                maxima = self.dadosCompletos["Máxima"].iloc[p]
                minima = self.dadosCompletos["Mínima"].iloc[p]
                fechamento = self.dadosCompletos["Último"].iloc[p]
                #
                self.aberturas.append(abertura)
                self.maximas.append(maxima)
                self.minimas.append(minima)
                self.fechamentos.append(fechamento)
                #
                
        #print("Aberturas: ",self.aberturas)
        #print("Máximas: ",self.maximas)
        #print("Mínimas: ",self.minimas)
        #print("Fechamentos: ",self.fechamentos)
            
    def precosAcumulados(self,i):
        abertura = self.dadosCompletos["Abertura"].iloc[i]
        maxima = self.dadosCompletos["Máxima"].iloc[i]
        minima = self.dadosCompletos["Mínima"].iloc[i]
        fechamento = self.dadosCompletos["Último"].iloc[i]
        #
        self.aberturasAcumulado.append(abertura)
        self.maximasAcumulado.append(maxima)
        self.minimasAcumulado.append(minima)
        self.fechamentosAcumulado.append(fechamento)
        #
        #print("Aberturas: ",self.aberturasAcumulado)
        #print("Máximas: ",self.maximasAcumulado)
        #print("Mínimas: ",self.minimasAcumulado)
        #print("Fechamentos: ",self.fechamentosAcumulado)

    def ordenarPrecos(self):
        print("Preços Ordenados...\n")
        #if abertura not in self.ordenados:
            #self.ordenados.append(abertura)
        #if maxima not in self.ordenados:
            #self.ordenados.append(maxima)
        #if minima not in self.ordenados:
            #self.ordenados.append(minima)
        #if fechamento not in self.ordenados:
            #self.ordenados.append(fechamento)                    
        #
        # Depurar Ordenados
        #self.ordenados = sorted(self.ordenados)
        #print(len(self.ordenados)," Preços Ordenados: ",self.ordenados)
        #

    def replicarNVezesDadosReais(self):
        # Criar Instância para Estatísticas
        estatisticaDadosReais = Estatistica()
        #
        self.inicializarOperacaoESetup()
        self.reinicializarDadosReais()
        # Replicar N vezes até obter a Precisão H nos Dados Reais
        tamanhoDadosNovo = self.tamanhoDadosIniciais
        print("Preços Necessários...\n")
        #
        sair = False
        nMaximo = False
        while (not sair):
            self.inicializarOperacaoESetup()
            self.reinicializarDadosReais()
            
            pTodos = len(self.dadosCompletos) - round(tamanhoDadosNovo)
            p = pTodos - self.periodo - 1
            for t in range(p,len(self.dadosCompletos)):
                self.precoPassoAPasso(t)
                self.dadosReaisSimuladosNecessarios.append(self.precoAtual)
                
                if t == pTodos:
                    self.primeiroPrecoSimulado = self.precoAtual
            
            #print("Dados Simulados Necessários ",self.tipoPreco,self.dadosReaisSimuladosNecessarios)
            
            mediaLognormal = estatisticaDadosReais.obterMediaLognormal(self.dadosReaisSimuladosNecessarios)
            print("\nMédia Lognormal dos Preços de Dados Reais...\n",mediaLognormal)
            desvioPadraoLognormal = estatisticaDadosReais.obterDesvioPadraoLognormal(\
                self.dadosReaisSimuladosNecessarios,mediaLognormal)
            print("\nDesvio Padrão Lognormal dos Preços de Dados Reais...\n",desvioPadraoLognormal)
            #
            # Movimentos e Correções
            self.movimentosDadosReais = self.movimentosECorrecoesDadosReais[0][0]
            #print("\nMovimentos dos Preços de Dados Reais...\n",self.tipoPreco,"\n",self.movimentosDadosReais)
            self.correcoesDadosReais = self.movimentosECorrecoesDadosReais[0][1]
            #print("\nCorreções dos Preços de Dados Reais...\n",self.tipoPreco,"\n",self.correcoesDadosReais)

            if len(self.movimentosDadosReais) > 0 and len(self.correcoesDadosReais) > 0:  
                self.mediaMovimentosDadosReais = estatisticaDadosReais.obterMediaLognormal(self.movimentosDadosReais)
                print("\nMédia dos Movimentos dos Preços de Dados Reais...\n",\
                    self.mediaMovimentosDadosReais)
                self.mediaCorrecoesDadosReais = estatisticaDadosReais.obterMediaLognormal(self.correcoesDadosReais)
                print("\nMédia das Correções dos Preços de Dados Reais...\n",self.mediaCorrecoesDadosReais)
                self.desvioPadraoMovimentosDadosReais = estatisticaDadosReais.obterDesvioPadraoLognormal(\
                    self.movimentosDadosReais,self.mediaMovimentosDadosReais)
                print("\nDesvio Padrão dos Movimentos dos Preços de Dados Reais...\n",\
                    self.desvioPadraoMovimentosDadosReais)
                self.desvioPadraoCorrecoesDadosReais = estatisticaDadosReais.obterDesvioPadraoLognormal(\
                    self.correcoesDadosReais,self.mediaCorrecoesDadosReais)
                print("\nDesvio Padrão das Correções dos Preços de Dados Reais...\n",\
                    self.desvioPadraoCorrecoesDadosReais)
                dadosArtificiais = estatisticaDadosReais.gerarDadosArtificiaisLognormal(mediaLognormal,\
                    desvioPadraoLognormal,len(self.dadosReaisPrecosSimulados))
                print("\nGerando Dados Artificiais de Preço ",self.tipoPreco," para Amostras de Tamanho ",\
                    len(self.dadosReaisPrecosSimulados))
                print("\nLucro Bruto... {0:6.2f}".format(self.saldoAcumulado[-1] - self.saldoAcumulado[0]))

                # Verificar a Precisão dos Dados Reais para Definir o Tamanho da Amostra Necessária
                #
                # Alfa para 99% = 0.01; Alfa para 95% = 0.05; Alfa para 90% = 0.10; Alfa para 80% = 0.20              
                movimentosDadosReais_H = estatisticaDadosReais.obterPrecisao_H(tamanhoDadosNovo,\
                    self.desvioPadraoMovimentosDadosReais, self.alfa)
                movimentosDadosReais_N = estatisticaDadosReais.estimar_N(tamanhoDadosNovo,\
                    self.movimentosDadosReais_Hpretendido,movimentosDadosReais_H)
                #
                correcoesDadosReais_H = estatisticaDadosReais.obterPrecisao_H(tamanhoDadosNovo,\
                    self.desvioPadraoCorrecoesDadosReais, self.alfa)
                correcoesDadosReais_N = estatisticaDadosReais.estimar_N(tamanhoDadosNovo,\
                    self.correcoesDadosReais_Hpretendido,correcoesDadosReais_H)
                # Comparar a Precisão Obtida nos Dados Reais com a Pretendida
                print("\nH dos Movimentos ",movimentosDadosReais_H," H Pretendido ",\
                    self.movimentosDadosReais_Hpretendido," H das Correções ",correcoesDadosReais_H,\
                    " H Pretendido ",self.correcoesDadosReais_Hpretendido)

                # Calcula a razão entre os movimentos/correções e a quantidade de preços do arquivo 
                if len(self.movimentosDadosReais) > 0 and len(self.movimentosDadosReais) >= len(self.correcoesDadosReais):
                    razao = 1 + (len(self.movimentosDadosReais) / tamanhoDadosNovo) 
                    print("\nRazaoMovCor: ", razao, "Tamanho_Movimentos: ", len(self.movimentosDadosReais))
                elif len(self.correcoesDadosReais) > 0 and len(self.movimentosDadosReais) < len(self.correcoesDadosReais):
                    razao = 1 + (len(self.correcoesDadosReais) / tamanhoDadosNovo) 
                    print("\nRazaoMovCor: ", razao, "Tamanho_Correções: ", len(self.correcoesDadosReais))

                # Verifica qual n_estimado é o maior
                if movimentosDadosReais_H >= correcoesDadosReais_H:
                    self.maior = movimentosDadosReais_N
                else:
                    self.maior = correcoesDadosReais_N

                if (movimentosDadosReais_H > self.movimentosDadosReais_Hpretendido) or\
                    (correcoesDadosReais_H > self.correcoesDadosReais_Hpretendido):
                    
                    if not nMaximo:

                        # Atribui o n_estimado multiplicado pela razão
                        tamanhoDadosNovo = self.maior * razao
                        print("N_Estimado: ", self.maior, "Tamanho_N: ", tamanhoDadosNovo)
                        self.pausar()

                        if tamanhoDadosNovo > 0 and tamanhoDadosNovo < len(self.dadosCompletos):
                            print("\nAmostra Inicial de Dados Reais = ",self.tamanhoDadosIniciais,\
                                " Replicação com N estimado = ",tamanhoDadosNovo)
                        else:
                            print("\nAmostra Inicial de Dados Reais = ",self.tamanhoDadosIniciais,\
                                " Replicação Atingiu N Máximo = ",tamanhoDadosNovo,"/",len(self.dadosCompletos))
                            nMaximo = True
                            tamanhoDadosNovo = len(self.dadosCompletos) - self.periodo - 1

                    else:
                        sair = True

                else:
                    # Atribui o n_estimado multiplicado pela razão
                    #tamanhoDadosNovo = self.maior * razao
                    #print("N_Estimado: ", self.maior, "Tamanho_N: ", tamanhoDadosNovo)
                    #self.pausar() 
                    sair = True
        
            else:
                tamanhoDadosNovo += self.tamanhoDadosIniciais
                print("N_Estimado: ", self.maior, "Tamanho_N: ", tamanhoDadosNovo)
                self.pausar()
                
        # Fim do while
        
    def replicarNVezesDadosArtificiais(self):
        # Criar Instância para Estatísticas
        estatisticaDadosArtificiais = Estatistica()                    

        # Replicar N vezes até obter a Precisão H nos Dados Artificiais
        tamanhoDadosNovo = self.tamanhoDadosIniciais
        sair = False
        nMaximo = False
    
        while (not sair):
            self.reinicializarDadosArtificiais()
            
            print("\n\nGerando Dados Artificiais de Movimentos e Correções de Preço ",\
                " para Amostras de Tamanho ",tamanhoDadosNovo,"\n")
            self.movimentosDadosArtificiais = estatisticaDadosArtificiais.gerarDadosArtificiaisLognormal(\
                self.mediaMovimentosDadosReais,self.desvioPadraoMovimentosDadosReais,tamanhoDadosNovo)
            print("\nGerando Dados Artificiais de Movimentos dos Preços...\n")
            self.correcoesDadosArtificiais = estatisticaDadosArtificiais.gerarDadosArtificiaisLognormal(\
                self.mediaCorrecoesDadosReais,self.desvioPadraoCorrecoesDadosReais,tamanhoDadosNovo)
            print("\nGerando Dados Artificiais de Correções dos Preços...\n")
            # Verificar a Precisão dos Dados Artificiais Gerados pela Função Randômica Lognormal
            #
            # Recalcula as médias e os desvios padrões dos Dados Artificiais para saber se é hora de parar
            # Movimentos
            mediaMovimentosDadosArtificiais = estatisticaDadosArtificiais.obterMediaLognormal(\
                self.movimentosDadosArtificiais)
            desvioPadraoMovimentosDadosArtificiais = estatisticaDadosArtificiais.obterDesvioPadraoLognormal(\
                self.movimentosDadosArtificiais,mediaMovimentosDadosArtificiais)
            # Correções
            mediaCorrecoesDadosArtificiais = estatisticaDadosArtificiais.obterMediaLognormal(\
                self.correcoesDadosArtificiais)
            desvioPadraoCorrecoesDadosArtificiais = estatisticaDadosArtificiais.obterDesvioPadraoLognormal(\
                self.correcoesDadosArtificiais,mediaCorrecoesDadosArtificiais)
            #
            # Alfa para 99% = 0.01; Alfa para 95% = 0.05; Alfa para 90% = 0.10; Alfa para 80% = 0.20
            movimentosDadosArtificiais_H = estatisticaDadosArtificiais.obterPrecisao_H(tamanhoDadosNovo,\
                desvioPadraoMovimentosDadosArtificiais, self.alfa)
            movimentosDadosArtificiais_N = estatisticaDadosArtificiais.estimar_N(tamanhoDadosNovo,\
                self.movimentosDadosArtificiais_Hpretendido,movimentosDadosArtificiais_H)
            #
            correcoesDadosArtificiais_H = estatisticaDadosArtificiais.obterPrecisao_H(tamanhoDadosNovo,\
                desvioPadraoCorrecoesDadosArtificiais, self.alfa)
            correcoesDadosArtificiais_N = estatisticaDadosArtificiais.estimar_N(tamanhoDadosNovo,\
                self.correcoesDadosArtificiais_Hpretendido,correcoesDadosArtificiais_H)
            # Comparar a Precisão Obtida nos Dados Artificiais com a Pretendida
            print("\nH dos Movimentos Art. ",movimentosDadosArtificiais_H," H Pretendido ",\
                self.movimentosDadosArtificiais_Hpretendido," H das Correções Art. ",correcoesDadosArtificiais_H,\
                " H Pretendido ",self.correcoesDadosArtificiais_Hpretendido)
                
            #if len(self.movimentosDadosArtificiais) > 0 and len(self.movimentosDadosArtificiais) >= len(self.correcoesDadosArtificiais):
            #    razao = 1 + (len(self.movimentosDadosArtificiais) / tamanhoDadosNovo) 
            #    print("\nRazaoMovCor: ", razao, "Tamanho_Movimentos: ", len(self.movimentosDadosArtificiais))
            #elif len(self.correcoesDadosArtificiais) > 0 and len(self.movimentosDadosArtificiais) < len(self.correcoesDadosArtificiais):
            #    razao = 1 + (len(self.correcoesDadosArtificiais) / tamanhoDadosNovo)
            #    print("\nRazaoMovCor: ", razao, "Tamanho_Correções: ", len(self.correcoesDadosArtificiais))           
            
            if (movimentosDadosArtificiais_H > self.movimentosDadosArtificiais_Hpretendido) or\
                (correcoesDadosArtificiais_H > self.correcoesDadosArtificiais_Hpretendido):
                
                if movimentosDadosArtificiais_H >= correcoesDadosArtificiais_H:
                    self.maior = movimentosDadosArtificiais_N
                else:
                    self.maior = correcoesDadosArtificiais_N

                if not nMaximo:
                    
                    tamanhoDadosNovo = self.maior
                    print("N_Estimado: ", self.maior, "Tamanho_N Artificial: ", tamanhoDadosNovo)
                    self.pausar()
                    
                    if tamanhoDadosNovo > 0 and tamanhoDadosNovo < len(self.dadosReaisSimuladosNecessarios):
                        print("\nAmostra Inicial de Dados Artificiais = ",self.tamanhoDadosIniciais,\
                            " Replicação com N estimado = ",tamanhoDadosNovo)
                    else:
                        print("\nAmostra Inicial de Dados Artificiais = ",self.tamanhoDadosIniciais,\
                            " Replicação Atingiu N Máximo = ",tamanhoDadosNovo,"/",len(self.dadosReaisSimuladosNecessarios))
                        nMaximo = True
                        if len(self.correcoesDadosReais) < len(self.movimentosDadosReais):
                            tamanhoDadosNovo = len(self.correcoesDadosReais)
                        else:
                            tamanhoDadosNovo = len(self.movimentosDadosReais)
                else:
                    sair = True

            else:
                #tamanhoDadosNovo = self.maior * razao
                #print("N_Estimado: ", self.maior, "Tamanho_N Artificial: ", tamanhoDadosNovo)
                #self.pausar()
                sair = True

        # Fim do while
                        
            # Gerar Pontos Artificiais
            self.pontosDadosArtificiais = []      
            if len(self.correcoesDadosArtificiais) < len(self.movimentosDadosArtificiais):
                tamanhoPontosDadosArtificiais = len(self.correcoesDadosArtificiais)
            elif len(self.correcoesDadosArtificiais) >= len(self.movimentosDadosArtificiais):
                tamanhoPontosDadosArtificiais = len(self.movimentosDadosArtificiais)
            #
            for i in range(tamanhoPontosDadosArtificiais):
                self.pontosDadosArtificiais.append(0)
                if i == 0:
                    self.pontosDadosArtificiais[i] = self.primeiroPrecoSimulado
                    impar = True
                    par = False
                    j = 0
                    k = 0
                else:
                    if par == True:
                        self.pontosDadosArtificiais[i] = self.pontosDadosArtificiais[i-1] *\
                            (1 + self.movimentosDadosArtificiais[j])
                        j += 1
                        par = False
                        impar = True
                    elif impar == True:
                        self.pontosDadosArtificiais[i] = self.pontosDadosArtificiais[i-1] *\
                            (1 - self.correcoesDadosArtificiais[k])
                        k += 1
                        impar = False
                        par = True
            #
            #print("\nPontos Artificiais...\n",self.pontosDadosArtificiais)
    
    def pausar(self):
        self.count += 1
        print("CONTADOR: ", self.count)
        pause = input("Pressione ENTER para continuar...")