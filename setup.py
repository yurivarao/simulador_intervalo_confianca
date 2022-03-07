# Classe contendo os métodos para configurar os Setups a serem operados no ativo no Simulador
from indicador import Indicador


class Setup:
    
    def __init__(self,codigoSetup_,codigoIndicadorTendencia_,codigoIndicadorEntrada_):
        self.codigoSetup = codigoSetup_
        # Criar Instância do Indicador para Tendencia
        self.codigoIndicadorTendencia = codigoIndicadorTendencia_
        self.indicadorTendencia = Indicador(self)        
        # Criar Instância do Indicador para Entrada
        self.codigoIndicadorEntrada = codigoIndicadorEntrada_
        self.indicadorEntrada = Indicador(self)
        #
        # Variáveis para Média Móvel Aritmética
        self.MMATendenciaAtual = 0
        self.MMAEntradaAtual = 0
        # Variáveis reutilizada para todos os Setups
        self.valorIndicadorTendencia = 0.0
        self.valorIndicadorEntrada = 0.0
        self.sinalIndicadorTendecia = 0.0
        self.sinalIndicadorEntrada = 0.0
        self.tendencia = ""
        self.entrada = 0.0
        self.stopLoss = 0.0
        self.stopGain = 0.0
        self.listaDePrecosAcumulado = []
        self.eventos = 0
        self.parcial = 0.0
        self.stopGainAnterior = 0.0
        self.stopLossAnterior = 0.0
        #
        self.nivelFibonacci = 0.618
        #0.382
        #0.500
        #0.618
        
        self.atingiuLimiar = "Não"
        #Variáveis para Pullback com Dow
        self.p1 = 0.0
        self.p2 = 0.0
        self.p3 = 0.0
        self.ultimoFundo = 0.0
        self.ultimoTopo = 0.0
        self.topoEoUltimo = None
        # Variáveis para Movimento e Correções
        # Variáveis para Movimentos e Correções
        self.tendenciaAnterior = "Baixa"
        self.pontoA = [0.0]
        self.pontoB = [0.0]
        self.movimento = []
        self.correcao = []
        #
        self.precoAtual = 0.0
        self.precoAnterior = 0.0

    def atualizar(self,tipoPreco_,precoAtual_,precoAnterior_,periodo_,aberturas_,maximas_,minimas_,fechamentos_):
        self.tipoPreco = tipoPreco_
        self.precoAtual = precoAtual_
        self.precoAnterior = precoAnterior_
        self.periodo = periodo_
        self.aberturas = aberturas_
        self.maximas = maximas_
        self.minimas = minimas_
        self.fechamentos = fechamentos_
        # Identificando o Tipo de Preço a ser usando nos Indicadores
        if self.tipoPreco == "Abertura":
            listaDePrecos_ = self.aberturas
                
        elif self.tipoPreco == "Máxima":
            listaDePrecos_ = self.maximas
                
        elif self.tipoPreco == "Mínima":
            listaDePrecos_ = self.minimas
                
        elif self.tipoPreco == "Último":
            listaDePrecos_ = self.fechamentos
            
        ##############################################################################################################
        #print("Atualizando Indicadores de Tendência ",self.codigoIndicadorTendencia)
        #
        
        # Teoria de Dow
        if self.codigoIndicadorTendencia == "1.1.1" or self.codigoIndicadorTendencia == "3.1.1":
            self.teoriaDeDow = 0
            
        # Detector de Topos e Fundos
        elif self.codigoIndicadorTendencia == "1.1.2" or self.codigoIndicadorTendencia == "3.1.2"\
            or self.codigoIndicadorTendencia == "4.1.2" or self.codigoIndicadorTendencia == "6.1.1":
            self.valorIndicadorTendencia = self.indicadorTendencia.detectorDeToposEFundos(\
                self.aberturas,self.maximas,self.minimas,self.fechamentos)

        # Parabolico SAR
        elif self.codigoIndicadorTendencia == "1.1.3" or self.codigoIndicadorTendencia == "3.1.3":
            self.valorIndicadorTendencia = self.indicadorTendencia.parabolicoSAR(\
                self.aberturas,self.maximas,self.minimas,self.fechamentos)
            
        # Média Móvel
        elif self.codigoIndicadorTendencia == "2.1.1" or self.codigoIndicadorTendencia == "4.1.1":
            self.valorIndicadorTendencia = self.indicadorTendencia.mediaMovelAritmetica(self.periodo,listaDePrecos_)
            print("listaDePrecos_",listaDePrecos_)
            
        # Long only
        elif self.codigoIndicadorTendencia == "5.1.1":
            self.valorIndicadorTendencia = self.precoAtual
            
        else:
            print("Indicador de Tendência não localizado...\n")

        ##############################################################################################################
        #print("Atualizando Indicadores de Entrada ",self.codigoIndicadorEntrada)
        #
        
        # Média Móvel
        if self.codigoIndicadorEntrada == "1.2.1" or self.codigoIndicadorEntrada == "2.2.1"\
            or self.codigoIndicadorEntrada == "4.2.1":
            self.valorIndicadorEntrada = self.indicadorEntrada.mediaMovelAritmetica(self.periodo,listaDePrecos_)
            
        # Retração de Fibonacci
        elif self.codigoIndicadorEntrada == "1.2.2" or self.codigoIndicadorEntrada == "3.2.1":
            self.valorIndicadorEntrada = self.indicadorEntrada.retracaoDeFibonacci(self.nivelFibonacci,self.aberturas,self.maximas,self.minimas,self.fechamentos)

        # Parabólico SAR
        elif self.codigoIndicadorEntrada == "1.2.3":
            self.valorIndicadorEntrada = self.indicadorEntrada.parabolicoSAR(self.aberturas,self.maximas,self.minimas,self.fechamentos)
            #print("Preços...\n",self.aberturas,self.maximas,self.minimas,self.fechamentos)

        # Long only
        elif self.codigoIndicadorEntrada == "5.2.1":
            self.valorIndicadorEntrada = self.precoAtual

        # Reversão por Tendência
        elif self.codigoIndicadorEntrada == "6.2.1":
            self.valorIndicadorEntrada = self.precoAtual

        else:
            print("Indicador de Entrada não localizado...\n")

        ##############################################################################################################
        #print("Atualizando Setup: ",self.codigoSetup)
        print("Setup",self.codigoSetup,"Indicador Tendencia",self.codigoIndicadorTendencia,"Indicador Entrada",self.codigoIndicadorEntrada,"\n")
        if self.codigoSetup == "1":
            self.rompimentoPullback()

        elif self.codigoSetup == "2":
            self.rompimentoMMA()

        elif self.codigoSetup == "3":
            self.scalpingDolar()
            
        elif self.codigoSetup == "4":
            self.reversaoPorMedias()

        elif self.codigoSetup == "5":
            self.longOnly()

        elif self.codigoSetup == "6":
            self.reversaoPorToposEFundos()

        else:
            print("Setup não localizado...\n")

        #
        return self.tendencia,self.entrada,self.stopLoss,self.stopGain,self.precoAtual,self.parcial    
    
    def atualizarAcumulado(self,aberturasAcumulado,maximasAcumulado,minimasAcumulado,fechamentosAcumulado):
        self.aberturasAcumulado = aberturasAcumulado
        self.maximasAcumulado = maximasAcumulado
        self.minimasAcumulado = minimasAcumulado
        self.fechamentosAcumulado = fechamentosAcumulado
        
        # Identificando o Tipo de Preço a ser usando nos Indicadores
        if self.tipoPreco == "Abertura":
            self.listaDePrecosAcumulado = self.aberturasAcumulado
                
        elif self.tipoPreco == "Máxima":
            self.listaDePrecosAcumulado = self.maximasAcumulado
                
        elif self.tipoPreco == "Mínima":
            self.listaDePrecosAcumulado = self.minimasAcumulado
                
        elif self.tipoPreco == "Último":
            self.listaDePrecosAcumulado = self.fechamentosAcumulado
            
    # Cenário 1 - Setup de Rompimento do Pullback com Indicador de Teoria de Dow => gatilho de entrada no rompimento do P2 após correção (P3 < P2 e P3 > P1), stop loss no P1 e stop gain no tamanho do movimento a partir de P3 (P3 + P2 - P1).    
    def rompimentoPullback(self):
        #print("")
        tamanhoListaTopos = len(self.indicadorTendencia.topos)
        tamanhoListaFundos = len(self.indicadorTendencia.fundos)
        self.sinalIndicadorTendencia = self.valorIndicadorTendencia
        #print("print dos topos:", self.indicadorTendencia.topos)
        #print("print dos fundos:", self.indicadorTendencia.fundos)
        
        #Checando se o ultimo ponto extremo foi um topo ou fundo
        if tamanhoListaTopos >= 2:    
            if self.ultimoTopo != self.indicadorTendencia.topos[tamanhoListaTopos - 1]:
                self.ultimoTopo = self.indicadorTendencia.topos[tamanhoListaTopos - 1]
                self.topoEoUltimo = True
        if tamanhoListaFundos >= 2:
            if self.ultimoFundo != self.indicadorTendencia.fundos[tamanhoListaFundos - 1]:
                self.ultimoFundo = self.indicadorTendencia.fundos[tamanhoListaFundos - 1]
                self.topoEoUltimo = False
        #
        if self.codigoIndicadorTendencia == "1.1.3":
            if tamanhoListaTopos >= 2 and tamanhoListaFundos >= 2:
                if self.indicadorTendencia.topos[tamanhoListaTopos - 1] > self.indicadorTendencia.topos[tamanhoListaTopos - 2] and self.indicadorTendencia.fundos[tamanhoListaFundos - 1] > self.indicadorTendencia.fundos[tamanhoListaFundos - 2]:
                    self.tendencia = "Alta"

                    if not self.topoEoUltimo:
                        self.p1 = self.indicadorTendencia.fundos[tamanhoListaFundos - 2]
                        self.p2 = self.indicadorTendencia.topos[tamanhoListaTopos - 1]
                        self.p3 = self.indicadorTendencia.fundos[tamanhoListaFundos - 1]
                                  
                elif self.indicadorTendencia.topos[tamanhoListaTopos - 1] < self.indicadorTendencia.topos[tamanhoListaTopos - 2] and self.indicadorTendencia.fundos[tamanhoListaFundos - 1] < self.indicadorTendencia.fundos[tamanhoListaFundos - 2]:
                    self.tendencia = "Baixa"
                    
                    if self.topoEoUltimo:
                        self.p1 = self.indicadorTendencia.topos[tamanhoListaTopos - 2]
                        self.p2 = self.indicadorTendencia.fundos[tamanhoListaFundos - 1]
                        self.p3 = self.indicadorTendencia.topos[tamanhoListaTopos - 1]
                        
                else:
                    self.tendencia = ""
        #            
        if self.codigoIndicadorEntrada == "1.2.3":
            self.sinalIndicadorEntrada = self.valorIndicadorEntrada
            if self.tendencia == "Alta":
                if not self.topoEoUltimo:
                    if self.precoAtual > self.p2 and self.p3 < self.p2 and self.p3 > self.p1\
                        and self.precoAnterior < self.p2:
                        #self.entrada = self.precoAtual
                        self.entrada = self.p2
                        #self.stopLoss = self.p1
                        self.stopLoss = self.p3
                        self.stopGain = self.p3 + self.p2 - self.p1
                        
                    else:
                        self.entrada = 0.0
            #
            if self.tendencia == "Baixa":
                if self.topoEoUltimo:
                    if self.precoAtual < self.p2 and self.p3 > self.p2 and self.p3 < self.p1\
                        and self.precoAnterior > self.p2:
                        #self.entrada = self.precoAtual
                        self.entrada = self.p2
                        #self.stopLoss = self.p1
                        self.stopLoss = self.p3
                        self.stopGain = self.p3 + self.p2 - self.p1
                        
                    else:
                        self.entrada = 0.0
        
        #
        self.parcial = 0.0
        print("Preço Atual {0:6.2f} Preço Anterior {1:6.2f}".format(self.precoAtual,self.precoAnterior))

    # Cenário 2 - Setup de Rompimento de Média Móvel Aritmética de X Períodos => gatilho de entrada na confirmação do rompimento da MMA_X (fechamento do segundo candle acima da MMA_X), stop loss abaixo da mínima do primeiro candle e stop gain quando romper a MMA_X invertendo o movimento.    
    def rompimentoMMA(self):
        if self.codigoIndicadorTendencia == "2.1.1":
            self.MMATendenciaAnterior = self.MMATendenciaAtual
            self.MMATendenciaAtual = self.valorIndicadorTendencia
            self.sinalIndicadorTendencia = self.MMATendenciaAtual
            #print("MMA Tendência Atual ",self.MMATendenciaAtual," MMA Tendência Anterior",self.MMATendenciaAnterior)
            #
            diferencaMMA = self.MMATendenciaAtual - self.MMATendenciaAnterior
            if diferencaMMA > 0:
                self.tendencia = "Alta"

            elif diferencaMMA < 0:
                self.tendencia = "Baixa"
                
            else:
                self.tendencia = ""
                    
        if self.codigoIndicadorTendencia == "2.1.2":
            self.detectorDeToposEFundosTendencia = self.valorIndicadorTendencia
            self.sinalIndicadorTendencia = self.detectorDeToposEFundosTendencia
            print("Detector de Topos e Fundos ",self.detectorDeToposEFundosTendencia)
            #
            if self.precoAtual > self.detectorDeToposEFundosTendencia:
                self.tendencia = "Alta"
                
            elif self.precoAtual < self.detectorDeToposEFundosTendencia:
                self.tendencia = "Baixa"
                
            else:
                self.tendencia = ""

        if self.codigoIndicadorEntrada == "2.2.1":
            #self.MMAEntradaAnterior = self.MMAEntradaAtual
            self.MMAEntradaAtual = self.valorIndicadorEntrada
            self.sinalIndicadorEntrada = self.MMAEntradaAtual
            #print("MMA Entrada Atual ",self.MMAEntradaAtual," MMA Entrada Anterior",self.MMAEntradaAnterior)            
            if self.tendencia == "Alta":
                if self.precoAtual > self.MMAEntradaAtual and self.precoAnterior < self.MMAEntradaAtual:
                    self.entrada = self.precoAtual
                else:
                    self.entrada = 0.0
                    
            elif self.tendencia == "Baixa":        
                if self.precoAtual < self.MMAEntradaAtual and self.precoAnterior > self.MMAEntradaAtual:
                    self.entrada = self.precoAtual
                else:
                    self.entrada = 0.0
                  
            #
            self.stopLoss = self.MMAEntradaAtual
            self.stopGain = self.precoAtual
        #
        self.parcial = 0.0
        print("Preço Atual {0:6.2f} Preço Anterior {1:6.2f}".format(self.precoAtual,self.precoAnterior))
        
    # Cenário 3 - Scalping no Dólar com Teoria de Dow e Fibonacci no Renko 2R => gatilho de entrada no Fibonacci 50% da correção da dezena atual (P3), stop loss em P1 (início da dezena atual) e stop gain com tamanho de 100% do movimento a parti de P3 (P3 + P2 - P1).    
    def scalpingDolar(self):  
        if self.codigoIndicadorTendencia == "3.1.2":
            self.detectorDeToposEFundosTendencia = self.valorIndicadorTendencia
            self.sinalIndicadorTendencia = self.detectorDeToposEFundosTendencia
            #
            if self.precoAtual > self.detectorDeToposEFundosTendencia:
                self.tendencia = "Alta"
                
            elif self.precoAtual < self.detectorDeToposEFundosTendencia:
                self.tendencia = "Baixa"
                
            else:
                self.tendencia = ""

        if self.codigoIndicadorTendencia == "3.1.3":
            self.parabolicoSARTendencia = self.valorIndicadorTendencia
            self.sinalIndicadorTendencia = self.parabolicoSARTendencia
            #
            if self.precoAtual > self.parabolicoSARTendencia:
                self.tendencia = "Alta"
                
            elif self.precoAtual < self.parabolicoSARTendencia:
                self.tendencia = "Baixa"

            else:
                self.tendencia = ""
                
        if self.codigoIndicadorEntrada == "3.2.1":
            self.retracaoDeFibonacciEntrada = self.valorIndicadorEntrada
            self.sinalIndicadorEntrada = self.retracaoDeFibonacciEntrada
            if self.tendencia == "Alta":
                if self.precoAtual > self.retracaoDeFibonacciEntrada and self.precoAnterior < self.retracaoDeFibonacciEntrada:
                    self.entrada = self.retracaoDeFibonacciEntrada
                    self.stopLoss = min(self.minimas)
                    self.stopGain = max(self.maximas)
                    
                else:
                    self.entrada = 0.0
                    
            elif self.tendencia == "Baixa":        
                if self.precoAtual < self.retracaoDeFibonacciEntrada and self.precoAnterior > self.retracaoDeFibonacciEntrada:
                    self.entrada = self.retracaoDeFibonacciEntrada
                    self.stopLoss = max(self.maximas)
                    self.stopGain = min(self.minimas)

                else:
                    self.entrada = 0.0
                  
        #
        self.parcial = 0.0
        print("Preço Atual {0:6.2f} Preço Anterior {1:6.2f} Gatilho {2:2.2f}".format(self.precoAtual,self.precoAnterior,self.entrada))

    # Cenário 4 - Reversão Por Médias => Gatilho de Entrada no alinhamento das MMAs (com 50 abaixo da 200 para compra
    # ou 50 acima da 200 para venda) e Tendência quando a MMA estiver apontando para acima ou para baixo. Stop loss e 
    # Stop gain quando cruzar a MMA50 em sentido contrário ao da entrada ou o Detector de Topos e Fundos.
    def reversaoPorMedias(self):

        if self.codigoIndicadorTendencia == "4.1.1":
            self.MMATendenciaAnterior = self.MMATendenciaAtual
            #self.MMATendenciaAtual = self.valorIndicadorTendencia
            self.MMATendenciaAtual = self.indicadorTendencia.mediaMovelAritmetica(50,self.listaDePrecosAcumulado)
            self.sinalIndicadorTendencia = self.MMATendenciaAtual
            #print("Sinal Indicador Tendência",self.sinalIndicadorTendencia)
            #
            diferencaMMA = self.MMATendenciaAtual - self.MMATendenciaAnterior
            if diferencaMMA > 0:
                self.tendencia = "Alta"

            elif diferencaMMA < 0:
                self.tendencia = "Baixa"

            else:
                self.tendencia = ""                

        if self.codigoIndicadorTendencia == "4.1.2":
            self.detectorDeToposEFundosTendencia = self.valorIndicadorTendencia
            self.sinalIndicadorTendencia = self.detectorDeToposEFundosTendencia
            print("Detector de Topos e Fundos ",self.detectorDeToposEFundosTendencia)
            #
            if self.precoAtual > self.detectorDeToposEFundosTendencia:
                self.tendencia = "Alta"
                
            elif self.precoAtual < self.detectorDeToposEFundosTendencia:
                self.tendencia = "Baixa"
                
            else:
                self.tendencia = ""

        if self.codigoIndicadorEntrada == "4.2.1":
            MMAEntradaAtual = self.valorIndicadorEntrada
            MMAEntradaAtual20 = self.indicadorEntrada.mediaMovelAritmetica(20,self.listaDePrecosAcumulado)
            MMAEntradaAtual50 = self.indicadorEntrada.mediaMovelAritmetica(50,self.listaDePrecosAcumulado)
            MMAEntradaAtual200 = self.indicadorEntrada.mediaMovelAritmetica(200,self.listaDePrecosAcumulado)
            self.sinalIndicadorEntrada = MMAEntradaAtual
            #print("MMA Entrada Atual ",self.MMAEntradaAtual)
            if self.tendencia == "Alta":
                if self.precoAtual > MMAEntradaAtual\
                    and MMAEntradaAtual > MMAEntradaAtual20\
                    and MMAEntradaAtual20 > MMAEntradaAtual50\
                    and MMAEntradaAtual20 > MMAEntradaAtual200\
                    and MMAEntradaAtual50 < MMAEntradaAtual200:
                    #self.entrada = self.precoAtual
                    self.entrada = MMAEntradaAtual
                else:
                    self.entrada = 0.0
                    
            elif self.tendencia == "Baixa":        
                if self.precoAtual < MMAEntradaAtual\
                    and MMAEntradaAtual < MMAEntradaAtual20\
                    and MMAEntradaAtual20 < MMAEntradaAtual50\
                    and MMAEntradaAtual20 < MMAEntradaAtual200\
                    and MMAEntradaAtual50 > MMAEntradaAtual200:
                    #self.entrada = self.precoAtual
                    self.entrada = MMAEntradaAtual
                else:
                    self.entrada = 0.0
                  
            #
            self.stopLoss = self.sinalIndicadorTendencia
            self.stopGain = self.precoAtual

        #
        self.parcial = 0.0
        print("Preço Atual {0:6.2f} Preço Anterior {1:6.2f} Gatilho {2:2.2f}".format(self.precoAtual,self.precoAnterior,self.entrada))

    # Cenário 5 - Long only (position trading). Compras feitas ao longo do tempo com realizações parciais ao atingir um 
    # percentual X.
    def longOnly(self):
        self.sinalIndicadorTendencia = self.valorIndicadorTendencia
        self.sinalIndicadorEntrada = self.valorIndicadorEntrada
        self.tendencia = "Alta"
        
        momentoDaCompra = 10
        self.eventos += 1
        
        if momentoDaCompra == self.eventos:
            self.entrada = self.precoAtual
            self.eventos = 0
            self.stopGainAnterior = self.stopGain
            self.stopLoss = min(self.precoAnterior,self.precoAtual)
            self.stopGain = self.entrada * 1.50
            
        else:
            self.entrada = 0.0
            self.parcial = self.stopGainAnterior

        #            
        print("Preço Atual {0:6.2f} Preço Anterior {1:6.2f} Gatilho {2:2.2f}".format(self.precoAtual,self.precoAnterior,self.entrada))        
    
    # Cenário 6 - Reversão por Topos e Fundos. A cada X períodos, entrar comprando se o preço estiver
    # acima do último Fundo ou vendendo se o preço estiver abaixo do último Topo. Stop Loss na mínima
    # dos dois últimos candle para compra ou na máxima dos dois últimos candles para venda.
    def reversaoPorToposEFundos(self):

        ######### TODO
        self.sinalIndicadorTendencia = self.valorIndicadorTendencia
        self.sinalIndicadorEntrada = self.valorIndicadorEntrada

        if self.indicadorTendencia.inverteu == True:
            if self.indicadorTendencia.ultimo == "Topo":
                self.tendencia = "Alta"
                self.entrada = self.precoAtual
                self.stopGain = self.precoAtual * 1.50
                
            elif self.indicadorTendencia.ultimo == "Fundo":
                self.tendencia = "Baixa"
                self.entrada = self.precoAtual
                self.stopGain = self.precoAtual * 0.50

        else:
            if self.indicadorTendencia.ultimo == "Topo":
                self.stopLoss = max(self.maximas)
                
            elif self.indicadorTendencia.ultimo == "Fundo":
                self.stopLoss = min(self.minimas)


        #            
        print("Preço Atual {0:6.2f} Preço Anterior {1:6.2f} Gatilho {2:2.2f}".format(self.precoAtual,self.precoAnterior,self.entrada))        
                
        
    ############# Rotina para Obter Sinais Gerados pelos Indicadores de Entrada e Tendência #############
    def obterSinaisIndicadores(self):
        if self.sinalIndicadorTendencia == []:
            sinalIndicadorTendencia = self.precoAtual

        else:
            sinalIndicadorTendencia = self.sinalIndicadorTendencia
            
        if  self.sinalIndicadorEntrada == []:             
            sinalIndicadorEntrada = self.precoAtual
            
        else:
            sinalIndicadorEntrada = self.sinalIndicadorEntrada
        #    
        return sinalIndicadorTendencia,sinalIndicadorEntrada

    ############# Rotina para Obter Movimentos e Correções #############
    def obterMovimentosECorrecoes(self):  
        if self.tendencia == "Baixa" and self.tendenciaAnterior == "Alta":
            self.tendenciaAnterior = "Baixa"
            self.pontoB.append(self.valorIndicadorTendencia)
            #print("Ponto B ",self.pontoB)
            
            if self.pontoA[len(self.pontoA)-1] > 0 and self.pontoB[len(self.pontoB)-1] > 0:
                if self.pontoA[len(self.pontoA)-1] < self.pontoB[len(self.pontoB)-1]:
                    distancia = (self.pontoB[len(self.pontoB)-1] - self.pontoA[len(self.pontoA)-1]) / \
                        self.pontoB[len(self.pontoB)-1]
                elif self.pontoA[len(self.pontoA)-1] > self.pontoB[len(self.pontoB)-1]:
                    distancia = (self.pontoA[len(self.pontoA)-1] - self.pontoB[len(self.pontoB)-1]) / \
                        self.pontoA[len(self.pontoA)-1]
                # Calcular Movimento
                if distancia != 0:
                    self.movimento.append(distancia)
                    
                #print("Distância BA",distancia," Ponto A ",self.pontoA[len(self.pontoA)-1]," Ponto B ",self.pontoB[len(self.pontoB)-1])
                        
        elif self.tendencia == "Alta" and self.tendenciaAnterior == "Baixa":
            self.tendenciaAnterior = "Alta"
            self.pontoA.append(self.valorIndicadorTendencia)
            #print("Ponto A ",self.pontoA)
            
            if self.pontoA[len(self.pontoA)-1] > 0 and self.pontoB[len(self.pontoB)-1] > 0:
                if self.pontoA[len(self.pontoA)-1] < self.pontoB[len(self.pontoB)-1]:
                    distancia = (self.pontoB[len(self.pontoB)-1] - self.pontoA[len(self.pontoA)-1]) / \
                        self.pontoB[len(self.pontoB)-1]
                elif self.pontoA[len(self.pontoA)-1] > self.pontoB[len(self.pontoB)-1]:
                    distancia = (self.pontoA[len(self.pontoA)-1] - self.pontoB[len(self.pontoB)-1]) / \
                        self.pontoA[len(self.pontoA)-1]
                # Calcular Correção
                if distancia != 0:
                    self.correcao.append(distancia)
                    
                #print("Distância ",distancia," Ponto A ",self.pontoA[len(self.pontoA)-1]," Ponto B ",self.pontoB[len(self.pontoB)-1])
        #
        #print("Ponto A ",self.pontoA," Ponto B ",self.pontoB)
        #
        return self.movimento,self.correcao
        
        