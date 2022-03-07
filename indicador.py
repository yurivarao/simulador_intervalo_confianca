# Classe contendo os métodos dos Indicadores do Simulador
class Indicador:

    def __init__(self,codigoIndicador):
        self.codigoIndicador = codigoIndicador
        self.topos = []
        self.fundos = []
        self.maximaMaximas = 0.0
        self.minimaMinimas = 0.0
        self.ultimo = ""
        self.sinal = 0.0
        self.start = False
                
    def mediaMovelAritmetica(self,periodo,listaDePreco):
        media = 0
        if len(listaDePreco) > periodo:
            recorte = len(listaDePreco) - periodo
        elif len(listaDePreco) < periodo:
            listaDePreco = []
            recorte = len(listaDePreco)
        else:
            recorte = 0

        for i in range(recorte,len(listaDePreco)):
            media += listaDePreco[i]
        #
        self.sinal = media/periodo
        #
        #print("MMA = ",self.media/periodo)
        #
        return self.sinal

    def detectorDeToposEFundos(self,aberturas,maximas,minimas,fechamentos):
        self.inverteu = False
        if self.ultimo == "Fundo" or self.ultimo == "":
            
            if max(maximas) > self.maximaMaximas or self.maximaMaximas == 0.0:
                self.maximaMaximas = max(maximas)

            #if maximas[2] > maximas[0] and maximas[2] > maximas[1] and minimas[2] > minimas[0] and minimas[2] > minimas[1]:     
            if maximas[0] < maximas[2] and maximas[1] < maximas[2]:     
                topo = self.maximaMaximas
                self.inverteu = True
                self.maximaMaximas = 0.0
                self.sinal = topo
                self.topos.append(topo)
                self.ultimo = "Topo"

        if self.ultimo == "Topo" or self.ultimo == "":
            
            if min(minimas) < self.minimaMinimas or self.minimaMinimas == 0.0:
                self.minimaMinimas = min(minimas)

            #if minimas[2] < minimas[0] and minimas[2] < minimas[1] and maximas[2] < maximas[0] and maximas[2] < maximas[1]:
            if minimas[0] > minimas[2] and minimas[1] > minimas[2]:
                fundo = self.minimaMinimas
                self.inverteu = True
                self.minimaMinimas = 0.0
                self.sinal = fundo
                self.fundos.append(fundo)
                self.ultimo = "Fundo"
        #
        #print("Topos ",self.topos,"Fundos ",self.fundos)
        #
        return self.sinal

    def retracaoDeFibonacci(self,nivel,aberturas,maximas,minimas,fechamentos):
        
        if len(fechamentos) >= 3:
            # Níveis mais comuns: 0.236,0.382,0.500,0.618,0.764,1.000
            topo = max(maximas)
            fundo = min(minimas)
            amplitude = topo - fundo
            self.sinal = fundo + (amplitude * nivel)
            #
            #print("Nível da Retração de Fibonacci\n",nivel," sinal ",self.sinal)
            #
        
        return self.sinal

    def parabolicoSAR(self,aberturas,maximas,minimas,fechamentos):            
        
        # Inicialização das variáveis locais
        if len(fechamentos) >= 3 and self.start == False:
            self.fator = 0.02
            self.fatorMax = 0.2
            self.precisao = 0.00
            self.SarAnterior = 0.0
            self.SarParabolico = fechamentos[0:len(fechamentos)]   
            self.endPointMax = maximas[1]       
            self.endPointMin = minimas[1]
            self.sinalLista = [0.0] * len(fechamentos)
            self.tendenciaAlta = True
            self.start = True
            
        elif len(fechamentos) == 3 and self.start == True:
            self.SarParabolico[1] = self.SarAnterior
            
        else:
            self.sinalLista = []

        # Função para calcular o indicador SAR Parabólico    
        for i in range(2,len(fechamentos)):
            if self.tendenciaAlta:
                self.SarParabolico[i] = self.SarParabolico[i - 1] + self.fator * (self.endPointMax - self.SarParabolico[i - 1])
                self.sinalLista[i] = self.SarParabolico[i]

            else:
                self.SarParabolico[i] = self.SarParabolico[i - 1] + self.fator * (self.endPointMin - self.SarParabolico[i - 1])
                self.sinalLista[i] = self.SarParabolico[i]
            self.reverse = False
                
            if self.tendenciaAlta:                    ########## Precisão ##########
                if minimas[i] < self.SarParabolico[i]-(self.SarParabolico[i]*self.precisao):
                    self.tendenciaAlta = False
                    self.reverse = True
                    self.SarParabolico[i] = self.endPointMax
                    self.sinalLista[i] = self.SarParabolico[i]
                    self.endPointMin = minimas[i]
                    self.topos.append(self.endPointMax)
                    self.fator = 0.02
                        
            else:                                     ########## Precisão ##########
                if maximas[i] > self.SarParabolico[i]+(self.SarParabolico[i]*self.precisao):
                    self.tendenciaAlta = True
                    self.reverse = True
                    self.SarParabolico[i] = self.endPointMin
                    self.sinalLista[i] = self.SarParabolico[i]
                    self.endPointMax = maximas[i]
                    self.fundos.append(self.endPointMin)
                    self.fator = 0.02
                
            if not self.reverse:
                if self.tendenciaAlta:
                    if maximas[i] > self.endPointMax:
                        self.endPointMax = maximas[i]
                        self.fator = min(self.fator + 0.02, self.fatorMax)

                else:

                    if minimas[i] < self.endPointMin:
                        self.endPointMin = minimas[i]
                        self.fator = min(self.fator + 0.02, self.fatorMax)

        if len(fechamentos) == 3:
            self.SarAnterior = self.SarParabolico[2]
            self.sinal = self.sinalLista[2]
            
        else:
            self.sinal = self.sinalLista
                   
        #print("Topos ",self.topos,"Fundos ",self.fundos)

        return self.sinal
