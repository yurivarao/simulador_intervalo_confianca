# Classe contendo os métodos do Menu do Simulador
import os
from simulador import Simulador


class Menu:

    def __init__(self,opcao):
        # Iniciar o Menu em loop
        if opcao == True:
            self.opcaoPrincipal = opcao
        else:
            self.opcaoPrincipal = False

    def chamarMenu(self):
        while self.opcaoPrincipal:
            print('Menu Principal')
            print("""
            1. Simular Dados Reais ou Dados Artificiais
            0. Sair
            """)
            opcaoPrincipal = input("Digite uma opção:")
            os.system("clear || cls")

            if opcaoPrincipal == "1":
                self.opcaoSimular = True
                opcaoOrigem = ""
                while self.opcaoSimular:
                    print("\n Menu Simular Dados Reais ou Dados Artificiais - Menu Principal")
                    print("""
                    1. Origem dos Dados (Reais ou Artificiais)
                    2. Tipo de Simulação (Com ou Sem Operação)
                    0. Sair
                    """)
                    opcaoSimular = input("Digite uma opção:")
                    os.system("clear || cls")

                    if opcaoSimular == "1":
                        self.opcaoOrigem = True
                        while self.opcaoOrigem:
                            print("\n Menu Origem dos Dados ""(Reais ou Artificiais)"" - Menu Simular")                        
                            print("""
                            1. Dados Reais do Arquivo
                            2. Dados Reais da API Alpha Vantage
                            3. Dados Artificiais
                            0. Sair
                            """)
                            opcaoOrigem = input("Digite uma opção:")
                            os.system("clear || cls")
                            
                            if opcaoOrigem == "1":
                                print("Dados Reais do Arquivo...\n")
                                self.opcaoOrigem = False       
                                
                            elif opcaoOrigem == "2":    
                                print("Dados Reais da Alpha Vantage...\n")
                                self.opcaoOrigem = False

                            elif opcaoOrigem == "3":    
                                print("Dados Artificiais...\n")
                                self.opcaoOrigem = False
                                
                            elif opcaoOrigem == "0":    
                                print("Saindo...\n")
                                self.opcaoOrigem = False
                                
                            else:
                                print("\n Opção inválida")                            
                                
                    elif opcaoSimular == "2":
                        self.opcaoTipoSimulacao = True
                        while self.opcaoTipoSimulacao:
                            print("\n Menu Tipo de Simulação ""(Com ou Sem Operação)"" - Menu Simular")
                            print("""
                            1. Com Operação
                            2. Sem Operação
                            0. Sair
                            """)
                            opcaoTipoSimulacao = input("Digite uma opção:")
                            os.system("clear || cls")

                            if opcaoTipoSimulacao == "1":
                                print("Com Operação...\n")
                                self.opcaoTipoSimulacao = False 
                                self.opcaoSetup = True
                                while self.opcaoSetup:
                                    print("\n Menu Setup - Menu Com Operação")                        
                                    print("""
                                    1. Rompimento de Pullback
                                    2. Rompimento de Média Móvel Aritmética
                                    3. Scalping no Dólar
                                    4. Reversão por Médias
                                    0. Sair
                                    """)
                                    opcaoSetup = input("Digite uma opção:")
                                    os.system("clear || cls")

                                    if opcaoSetup == "1":
                                        print("Rompimento de Pullback")
                                        self.setup = "1"
                                        self.opcaoRompimentoPullback = True
                                        while self.opcaoRompimentoPullback:
                                            print("\n Menu Rompimento de Pullback - Menu Setup")                        
                                            print("""
                                            1. Indicador de Tendência
                                            2. Indicador de Entrada
                                            0. Sair
                                            """)
                                            opcaoRompimentoPullback = input("Digite uma opção:")
                                            os.system("clear || cls")
                                            
                                            if opcaoRompimentoPullback == "1":
                                                self.opcaoIndicadorTendenciaRompimentoPullback = True
                                                while self.opcaoIndicadorTendenciaRompimentoPullback:
                                                    print("\n Menu Indicador de Tendência - Menu Rompimento de Pullback")
                                                    print("""
                                                    1. Indicador Teoria de Dow
                                                    2. Indicador Detector de Topos e Fundos
                                                    3. Indicador Parabolico SAR
                                                    0. Sair
                                                    """)
                                                    opcaoIndicadorTendenciaRompimentoPullback = input("Digite uma opção:")
                                                    os.system("clear || cls")
                                                    
                                                    if opcaoIndicadorTendenciaRompimentoPullback == "1":
                                                        print("Teoria de Dow")
                                                        self.tendencia = "1.1.1"
                                                        self.opcaoIndicadorTendenciaRompimentoPullback = False
                                                        
                                                    elif opcaoIndicadorTendenciaRompimentoPullback == "2":
                                                        print("Detector de Topos e Fundos")
                                                        self.tendencia = "1.1.2"
                                                        self.opcaoIndicadorTendenciaRompimentoPullback = False 
                                                        
                                                    elif opcaoIndicadorTendenciaRompimentoPullback == "3":
                                                        print("Parabolico SAR")
                                                        self.tendencia = "1.1.3"
                                                        self.opcaoIndicadorTendenciaRompimentoPullback = False 

                                                        
                                                    elif opcaoIndicadorTendenciaRompimentoPullback == "0":
                                                        print("Saindo...\n")
                                                        self.opcaoIndicadorTendenciaRompimentoPullback = False
                                                        
                                                    else:
                                                        print("\n Opção inválida")                            
                        
                                            elif opcaoRompimentoPullback == "2":
                                                self.opcaoIndicadorEntradaRompimentoPullback = True
                                                while self.opcaoIndicadorEntradaRompimentoPullback:
                                                    print("\n Menu Indicador de Entrada - Menu Rompimento de Pullback")
                                                    print("""
                                                    1. Indicador Média Móvel
                                                    2. Indicador Retração de Fibonacci
                                                    3. Parabólico SAR (Teoria Dow)
                                                    0. Sair
                                                    """)
                                                    opcaoIndicadorEntradaRompimentoPullback = input("Digite uma opção:")
                                                    os.system("clear || cls")
                                                    
                                                    if opcaoIndicadorEntradaRompimentoPullback == "1":
                                                        print("Média Móvel")
                                                        self.entrada = "1.2.1"
                                                        self.opcaoIndicadorEntradaRompimentoPullback = False
                                                        
                                                    elif opcaoIndicadorEntradaRompimentoPullback == "2":
                                                        print("Retração de Fibonacci")
                                                        self.entrada = "1.2.2"
                                                        self.opcaoIndicadorEntradaRompimentoPullback = False

                                                    elif opcaoIndicadorEntradaRompimentoPullback == "3":
                                                        print("Parabólico SAR (Teoria Dow)")
                                                        self.entrada = "1.2.3"
                                                        self.opcaoIndicadorEntradaRompimentoPullback = False                     
                                                        
                                                    elif opcaoIndicadorEntradaRompimentoPullback == "0":
                                                        print("Saindo...\n")
                                                        self.opcaoIndicadorEntradaRompimentoPullback = False

                                                    else:
                                                        print("\n Opção inválida")                            
                                                        
                                            elif opcaoRompimentoPullback == "0":
                                                print("Saindo...\n")
                                                self.opcaoRompimentoPullback = False
                                                
                                            else:
                                                print("\n Opção inválida")                            
                                            
                                    elif opcaoSetup == "2":
                                        print("Rompimento de Média Móvel Aritmética")
                                        self.setup = "2"
                                        self.opcaoRompimentoMMA = True
                                        while self.opcaoRompimentoMMA:
                                            print("\n Menu Rompimento de Média Móvel Aritmética")                        
                                            print("""
                                            1. Indicador de Tendência
                                            2. Indicador de Entrada
                                            0. Sair
                                            """)
                                            opcaoRompimentoMMA = input("Digite uma opção:")
                                            os.system("clear || cls")
                                            
                                            if opcaoRompimentoMMA == "1":
                                                self.opcaoIndicadorTendenciaRompimentoMMA = True
                                                while self.opcaoIndicadorTendenciaRompimentoMMA:
                                                    print("\n Menu Indicador de Tendência - Rompimento de Média Móvel Aritmética")
                                                    print("""
                                                    1. Indicador Média Móvel
                                                    0. Sair
                                                    """)
                                                    opcaoIndicadorTendenciaRompimentoMMA = input("Digite uma opção:")
                                                    os.system("clear || cls")
                                                    
                                                    if opcaoIndicadorTendenciaRompimentoMMA == "1":
                                                        print("Média Móvel")
                                                        self.tendencia = "2.1.1"
                                                        self.opcaoIndicadorTendenciaRompimentoMMA = False                       
                                                        
                                                    elif opcaoIndicadorTendenciaRompimentoMMA == "0":
                                                        print("Saindo...\n")
                                                        self.opcaoIndicadorTendenciaRompimentoMMA = False

                                                    else:
                                                        print("\n Opção inválida")                            
                                                    
                                            if opcaoRompimentoMMA == "2":
                                                self.opcaoIndicadorEntradaRompimentoMMA = True
                                                while self.opcaoIndicadorEntradaRompimentoMMA:
                                                    print("\n Menu Indicador de Entrada - Rompimento de Média Móvel Aritmética")
                                                    print("""
                                                    1. Indicador Média Móvel
                                                    0. Sair
                                                    """)
                                                    opcaoIndicadorEntradaRompimentoMMA = input("Digite uma opção:")
                                                    os.system("clear || cls")
                                                    
                                                    if opcaoIndicadorEntradaRompimentoMMA == "1":
                                                        print("Média Móvel")
                                                        self.entrada = "2.2.1"
                                                        self.opcaoIndicadorEntradaRompimentoMMA = False
                                                        
                                                    elif opcaoIndicadorEntradaRompimentoMMA == "0":
                                                        print("Saindo...\n")
                                                        self.opcaoIndicadorEntradaRompimentoMMA = False

                                                    else:
                                                        print("\n Opção inválida")                                          
                                        
                                            elif opcaoRompimentoMMA == "0":
                                                print("Saindo...\n")
                                                self.opcaoRompimentoMMA = False

                                    elif opcaoSetup == "3":    
                                        print("Scalping no Dólar")
                                        self.setup = "3"
                                        self.opcaoScalpingDolar = True
                                        while self.opcaoScalpingDolar:
                                            print("\n Menu Scalping Dólar")                        
                                            print("""
                                            1. Indicador de Tendência
                                            2. Indicador de Entrada
                                            0. Sair
                                            """)
                                            opcaoScalpingDolar = input("Digite uma opção:")
                                            os.system("clear || cls")
                                            
                                            if opcaoScalpingDolar == "1":
                                                self.opcaoIndicadorTendenciaScalpingDolar = True
                                                while self.opcaoIndicadorTendenciaScalpingDolar:
                                                    print("\n Menu Indicador de Tendência - Scalping no Dólar")
                                                    print("""
                                                    1. Indicador Teoria de Dow
                                                    2. Indicador Detector de Topos e Fundos
                                                    3. Indicador Parabolico SAR
                                                    0. Sair
                                                    """)
                                                    opcaoIndicadorTendenciaScalpingDolar = input("Digite uma opção:")
                                                    os.system("clear || cls")
                                                    
                                                    if opcaoIndicadorTendenciaScalpingDolar == "1":
                                                        print("Teoria de Dow")
                                                        self.tendencia = "3.1.1"
                                                        self.opcaoIndicadorTendenciaScalpingDolar = False
                                                        
                                                    elif opcaoIndicadorTendenciaScalpingDolar == "2":
                                                        print("Detector de Topos e Fundos")
                                                        self.tendencia = "3.1.2"
                                                        self.opcaoIndicadorTendenciaScalpingDolar = False  
                                                        
                                                    elif opcaoIndicadorTendenciaScalpingDolar == "3":
                                                        print("Parabolico SAR")
                                                        self.tendencia = "3.1.3"
                                                        self.opcaoIndicadorTendenciaScalpingDolar = False  

                                                    elif opcaoIndicadorTendenciaScalpingDolar == "0":
                                                        print("Saindo...\n")
                                                        self.opcaoIndicadorTendenciaScalpingDolar = False

                                                    else:
                                                        print("\n Opção inválida")                            
                        
                                            if opcaoScalpingDolar == "2":
                                                self.opcaoIndicadorEntradaScalpingDolar = True
                                                while self.opcaoIndicadorEntradaScalpingDolar:
                                                    print("\n Menu Indicador de Entrada - Scalping no Dólar")
                                                    print("""
                                                    1. Indicador Retração de Fibonacci
                                                    0. Sair
                                                    """)
                                                    opcaoIndicadorEntradaScalpingDolar = input("Digite uma opção:")
                                                    os.system("clear || cls")
                                                    
                                                    if opcaoIndicadorEntradaScalpingDolar == "1":
                                                        print("Retração de Fibonacci")
                                                        self.entrada = "3.2.1"
                                                        self.opcaoIndicadorEntradaScalpingDolar = False
                                                        
                                                    elif opcaoIndicadorEntradaScalpingDolar == "0":
                                                        print("Saindo...\n")
                                                        self.opcaoIndicadorEntradaScalpingDolar = False

                                                    else:
                                                        print("\n Opção inválida")  
                                                        
                                            elif opcaoScalpingDolar == "0":
                                                print("Saindo...\n")
                                                self.opcaoScalpingDolar = False

                                            else:
                                                print("\n Opção inválida")  
                                                
                                    elif opcaoSetup == "4":    
                                        print("Reversão por Médias")
                                        self.setup = "4"
                                        self.opcaoReversaoPorMedias = True
                                        while self.opcaoReversaoPorMedias:
                                            print("\n Menu Reversão Por Médias")                        
                                            print("""
                                            1. Indicador de Tendência
                                            2. Indicador de Entrada
                                            0. Sair
                                            """)
                                            opcaoReversaoPorMedias = input("Digite uma opção:")
                                            os.system("clear || cls")
                                            
                                            if opcaoReversaoPorMedias == "1":
                                                self.opcaoIndicadorTendenciaReversaoPorMedias = True
                                                while self.opcaoIndicadorTendenciaReversaoPorMedias:
                                                    print("\n Menu Indicador de Tendência - Reversão Por Médias")
                                                    print("""
                                                    1. Indicador Médias Móveis
                                                    2. Indicador Detector de Topos e Fundos
                                                    0. Sair
                                                    """)
                                                    opcaoIndicadorTendenciaReversaoPorMedias = input("Digite uma opção:")
                                                    os.system("clear || cls")
                                                    
                                                    if opcaoIndicadorTendenciaReversaoPorMedias == "1":
                                                        print("Médias Móveis")
                                                        self.tendencia = "4.1.1"
                                                        self.opcaoIndicadorTendenciaReversaoPorMedias = False
                                                        
                                                    if opcaoIndicadorTendenciaReversaoPorMedias == "2":
                                                        print("Detector de Topos e Fundos")
                                                        self.tendencia = "4.1.2"
                                                        self.opcaoIndicadorTendenciaReversaoPorMedias = False

                                                    elif opcaoIndicadorTendenciaReversaoPorMedias == "0":
                                                        print("Saindo...\n")
                                                        self.opcaoIndicadorTendenciaReversaoPorMedias = False

                                                    else:
                                                        print("\n Opção inválida")                            
                        
                                            if opcaoReversaoPorMedias == "2":
                                                self.opcaoIndicadorEntradaReversaoPorMedias = True
                                                while self.opcaoIndicadorEntradaReversaoPorMedias:
                                                    print("\n Menu Indicador de Entrada - Reversão Por Médias")
                                                    print("""
                                                    1. Indicador Médias Móveis
                                                    0. Sair
                                                    """)
                                                    opcaoIndicadorEntradaReversaoPorMedias = input("Digite uma opção:")
                                                    os.system("clear || cls")
                                                    
                                                    if opcaoIndicadorEntradaReversaoPorMedias == "1":
                                                        print("Médias Móveis")
                                                        self.entrada = "4.2.1"
                                                        self.opcaoIndicadorEntradaReversaoPorMedias = False
                                                        
                                                    elif opcaoIndicadorEntradaReversaoPorMedias == "0":
                                                        print("Saindo...\n")
                                                        self.opcaoIndicadorEntradaReversaoPorMedias = False

                                                    else:
                                                        print("\n Opção inválida")  
                                                        
                                            elif opcaoReversaoPorMedias == "0":
                                                print("Saindo...\n")
                                                self.opcaoReversaoPorMedias = False

                                            else:
                                                print("\n Opção inválida")  
                                                

                                    elif opcaoSetup == "0":    
                                        print("Saindo...\n")
                                        self.opcaoSetup = False
                                        
                                    else:
                                        print("\n Opção inválida")                            

                                # Preparando a Simulação Com Operação
                                print("\n Simulando...")
                                # Criar uma instância do Simulador baseada na escolha do usuário
                                if opcaoOrigem == "":
                                    print("Falta escolher a Origem dos Dados\n")
                                    self.opcaoTipoSimulacao = False
                                else:    
                                    sim = Simulador(opcaoOrigem)
                                    # Chamar o método para Iniciar a Simulação Com Operação
                                    vaiOperar = True
                                    sim.simular(vaiOperar,self.setup,self.tendencia,self.entrada)   
                                
                            elif opcaoTipoSimulacao == "2":    
                                print("Sem Operação...\n")
                                self.opcaoTipoSimulacao = False
                                # Preparando a Simulação Sem Operação                                
                                print("\n Simulando...")
                                # Criar uma instância do Simulador baseada na escolha do usuário
                                if opcaoOrigem == "":
                                    print("Falta escolher a Origem dos Dados\n")
                                    self.opcaoTipoSimulacao = False
                                else:    
                                    sim = Simulador(opcaoOrigem)
                                    # Chamar o método para Iniciar a Simulação Sem Operação
                                    vaiOperar = False
                                    sim.simular(vaiOperar,0,0,0)         
                                
                            elif opcaoTipoSimulacao == "0":    
                                self.opcaoTipoSimulacao = False
                                
                            else:
                                print("\n Opção inválida")                            
                                
                    elif opcaoSimular == "0":
                        print("Saindo...\n")
                        self.opcaoSimular = False                                
                            
                    else:
                      print("\n Opção inválida")

            elif opcaoPrincipal == "-1":
                print("\n Opção de Testes...")
                self.setup = input("Digite o Código do Setup ")
                self.tendencia = input("Digite o Código do Indicador de Tendência ")
                self.entrada = input("Digite o Código do Indicador de Entrada ")
                opcaoOrigem = "1"
                sim = Simulador(opcaoOrigem)
                vaiOperar = True
                sim.simular(vaiOperar,self.setup,self.tendencia,self.entrada)   

            elif opcaoPrincipal == "0":
                print("\n Saindo...")
                self.opcaoPrincipal = False
                quit()
                
            else:
               print("\n Opção inválida")

    def obterOpcaoMenu(self):
        return self.opcaoPrincipal
    
    def obterOpcaoOrigem(self):
        return self.opcaoOrigem
    
    def obterOpcaoSetup(self):
        return self.opcaoSetup
