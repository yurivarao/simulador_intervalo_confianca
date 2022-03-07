# Classe contendo os métodos para realizar Operação do ativo no Simulador
class Operacao:
    
    
    def __init__(self):
        self.estadoOperacao = "Aguardando"
        self.precoAtual = 0.0
        self.comprado = 0.0
        self.vendido = 0.0
        self.saldo = 500.0
        self.quantidadeInicial = 1
        self.quantidade = self.quantidadeInicial
        self.compras = []
        self.vendas = []
        self.posicoes = []
        self.ganhos = []
        self.perdas = []

    def iniciarOperacao(self):
        print("\n")
        
    def atualizar(self,precoAtual_,resultados_):
        saldo = 0.0
        self.precoAtual = precoAtual_
        self.tendencia = resultados_[0]
        self.entrada = resultados_[1]
        self.stopLoss = resultados_[2]
        self.stopGain = resultados_[3]
        self.parcial = resultados_[4]
        print("Tendência de {0} Entrada {1:6.2f} SL {2:6.2f} SG {3:6.2f} {4}".format(self.tendencia,self.entrada,self.stopLoss,self.stopGain,self.estadoOperacao))
        #
        if self.posicoes == []:
            posicoes = 1
        else:
            posicoes = len(self.posicoes)
        
        if self.comprado > 0 and self.estadoOperacao != "Aguardando":
            print("{0} {1:6.2f} {2:3d}".format(self.estadoOperacao,self.comprado,posicoes))
            
        elif self.vendido > 0 and self.estadoOperacao != "Aguardando":
            print("{0} {1:6.2f} {2:3d}".format(self.estadoOperacao,self.vendido,posicoes))
            
        #
        if self.tendencia == "Alta":
            if self.estadoOperacao == "Aguardando":            
                if self.precoAtual >= self.entrada and self.entrada > 0.0:
                    print("Comprando pelo gatilho de entrada...\n")   
                    self.comprar(self.entrada)
                    self.estadoOperacao = "Comprado"
    
            elif self.estadoOperacao == "Vendido":
                if self.precoAtual > self.stopLoss:
                    print("Comprando pelo gatilho de stop loss...\n")
                    saldo = (self.vendido - self.stopLoss) * self.quantidade
                    self.comprar(self.stopLoss)
                    self.quantidade = self.quantidadeInicial
                    self.estadoOperacao = "Aguardando"
                    
                else:
                    #print("Continua vendido em ",self.vendido)
                    print("Continua... ")

            elif self.estadoOperacao == "Comprado":
                if self.precoAtual < self.stopLoss:   
                    print("Vendendo pelo gatilho de stop loss...\n")                
                    saldo = (self.stopLoss - self.comprado) * self.quantidade
                    self.vender(self.stopLoss)
                    self.quantidade = self.quantidadeInicial
                    self.estadoOperacao = "Aguardando"
                    
                elif self.precoAtual > self.stopGain:   
                    print("Vendendo pelo gatilho de stop gain...\n")                
                    saldo = (self.stopGain - self.comprado) * self.quantidade
                    self.vender(self.stopGain)
                    self.quantidade = self.quantidadeInicial
                    self.estadoOperacao = "Aguardando"
                    
                elif self.precoAtual > self.parcial and len(self.posicoes) != []:
                    print("Diminuindo a posição...\n") 
                    self.diminuirPosicao(self.parcial)
                    self.estadoOperacao = "Comprado"

                elif self.parcial > 0.0 and self.entrada > 0.0:
                    print("Aumentando a posição...\n")
                    self.aumentarPosicao(self.entrada)
                    self.estadoOperacao = "Comprado"

            else:
                #print("Continua comprado em ",self.comprado)
                print("Continua... ")
                
        elif self.tendencia == "Baixa": 
            if self.estadoOperacao == "Aguardando":            
                if self.precoAtual <= self.entrada and self.entrada > 0.0:
                    print("Vendendo pelo gatilho de entrada...\n")
                    self.vender(self.entrada)
                    self.estadoOperacao = "Vendido"
                    
            elif self.estadoOperacao == "Comprado":            
                if self.precoAtual < self.stopLoss:   
                    print("Vendendo pelo gatilho de stop loss...\n")                
                    saldo = (self.stopLoss - self.comprado) * self.quantidade
                    self.vender(self.stopLoss)
                    self.quantidade = self.quantidadeInicial
                    self.estadoOperacao = "Aguardando"
                    
                else:
                    print("Continua comprado em ",self.comprado)

            elif self.estadoOperacao == "Vendido":
                if self.precoAtual > self.stopLoss:   
                    print("Comprando pelo gatilho de stop loss...\n")                
                    saldo = (self.vendido - self.stopLoss) * self.quantidade
                    self.comprar(self.stopLoss)
                    self.quantidade = self.quantidadeInicial
                    self.estadoOperacao = "Aguardando"

                elif self.precoAtual < self.stopGain:   
                    print("Comprando pelo gatilho de stop gain...\n")                
                    saldo = (self.vendido - self.stopGain) * self.quantidade
                    self.comprar(self.stopGain)
                    self.quantidade = self.quantidadeInicial
                    self.estadoOperacao = "Aguardando"

            else:
                print("Continua vendido em ",self.vendido)

        else:
            print("Sem tendência...\n")
            self.estadoOperacao = "Aguardando"                                      
        
        #Relação numero de acertos(ganhos) pelo numero de erros(perdas)
        if (saldo != 0):
            if (saldo > 0):
                self.ganhos.append(saldo)
            else:
                self.perdas.append(saldo)

        if ((len(self.ganhos) > 0) and (len(self.perdas) > 0)):
            relacao = sum(self.ganhos)/(sum(self.perdas)*-1)
            print("\nFator Lucro {0:6.2f}".format(relacao))        
        #Percentual de Acertos
            tam = len(self.ganhos) + len(self.perdas)
            print("\nTaxa de Acertos {0:6.2f}%".format(len(self.ganhos)*100/tam))
        #Máximo e Mínimo dos Ganhos e Perdas
            print("\nGanho Máx {0:6.2f}".format(max(self.ganhos)),"- Min {0:6.2f}".format(min(self.ganhos)))
            print("Perda Máx {0:6.2f}".format(min(self.perdas)),"- Min {0:6.2f}".format(max(self.perdas)))
        #Média de Lucro por entrada
            lucro = sum(self.ganhos)+sum(self.perdas)
            print("\nMédia de Lucro por operação {0:6.2f}".format(lucro/tam))

        self.atualizarSaldo(saldo)
        consulta = self.consultarSaldo()
        print("\nSaldo {0:6.2f}".format(consulta))
        #
        return self.saldo
    
    def comprar(self,preco):
        self.comprado = preco
        self.vendido = 0.0
        self.posicoes = []
                  
    def vender(self,preco):    
        self.vendido = preco
        self.comprado = 0.0
        self.posicoes = []

    def aumentarPosicao(self,preco):
        self.compras.append(preco)
        
        if self.posicoes == []:
            self.posicoes.append(self.comprado)
            
        self.posicoes.append(preco)
        #
        precoMedio = 0.0
        for i in range(len(self.posicoes)):
            precoMedio += self.posicoes[i]
        #
        self.comprado = precoMedio / len(self.posicoes)
        self.quantidade += 1
        self.vendido = 0.0
        
    def diminuirPosicao(self,preco):
        self.vendas.append(preco)
        
        self.posicoes.delete(0)

        precoMedio = 0.0
        for i in range(len(self.posicoes)):
            precoMedio += self.posicoes[i]
        #
        self.comprado = (precoMedio - preco) / len(self.posicoes) - 1
        self.quantidade -= 1
        self.vendido = 0.0        
        
    def atualizarSaldo(self,saldo_):
        self.saldo += saldo_
    
    def consultarSaldo(self):
        return self.saldo
    
    def consultarPosicao(self):
        if self.estadoOperacao == "Comprado":
            self.posicao = self.comprado
        elif self.estadoOperacao == "Vendido":
            self.posicao = self.vendido
        else:
            self.posicao = 0.0
        #
        return self.posicao