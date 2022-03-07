# AssetsSim

{Simulador de Ativos Financeiros}

O objetivo deste simulador é estudar o desempenho de vários indicadores no ativo financeiro escolhido pelo usuário. Isso permite que o usuário aprenda a realizar operações de trade com maior precisão, usando conceitos da Análise Técnica, tais como Teoria de Dow e Fibonacci. O simulador também pode ser usado para verificar como é o desempenho de seus setups em operações no ambiente de backtesing.

Dessa forma, o usuário treina operações financeiras antes de ir direto para a conta real, obtendo informações mais precisas de que indicadores e setups usar no mercado financeiro para o ativo escolhido.

# Funcionamento do Simulador

{Requisitos}

O simulador precisa ler um arquivo .csv contendo os preços de um ativo financeiro no formato de tabela com rótulos 'Nome, Abertura, Máximo, Mínimo, Fechamento, Volume'. Tais arquivos podem ser baixados em sites como br.Investing.com, onde você escolhe o ativo a ser estudado e o período dos preços.

{Início}

Ao iniciar o simulador, o usuário deve escolher as opções disponíveis no menu principal e os submenus que se seguem. Para a simulação com Operação, o usuário terá disponível 3 Cenários, conforme descrições abaixo: 

* Cenário 1 - Setup de Rompimento do Pullback com Indicador de Teoria de Dow => gatilho de entrada no rompimento do P2 após correção (P3 < P2 e P3 > P1), stop loss no P1 e stop gain no tamanho do movimento a partir de P3 (P3 + P2 - P1).
* Cenário 2 - Setup de Rompimento de Média Móvel Aritmética de 9 Períodos => gatilho de entrada na confirmação do rompimento da MMA9 (fechamento do segundo candle acima da MMA9), stop loss abaixo da mínima do primeiro candle e stop gain quando romper a MMA9 invertendo o movimento.
* Cenário 3 - Scalping no Dólar com Teoria de Dow e Fibonacci no Renko 2R => gatilho de entrada no Fibonacci 50% da correção da dezena atual (P3), stop loss em P1 (início da dezena atual) e stop gain com tamanho de 100% do movimento a parti de P3 (P3 + P2 - P1).

Nota: Cada Cenário deve conter o Setup, o Indicador de Tendência e o Indicador de Entrada.

[Menus Disponíveis no Simulador]

(Menu Principal)
1. Simular Dados Reais ou Dados Artificiais
2. Sair

(Menu Simular Dados Reais ou Dados Artificiais - Menu Principal)
1. Origem dos Dados (Reais ou Artificiais)
2. Tipo de Simulação (Com ou Sem Operação)
3. Sair

(Menu Origem dos Dados (Reais ou Artificiais) - Menu Simular)
1. Dados Reais
2. Dados Artificiais
3. Sair

(Menu Tipo de Simulação (Com ou Sem Operação) - Menu Simular)
1. Com Operação
2. Sem Operação
3. Sair

(Menu Setup - Menu Com Operação)                        
1. Rompimento de Pullback
2. Rompimento de Média Móvel Aritmética
3. Scalping no Dólar
4. Sair

(Menu Rompimento de Pullback - Menu Setup)                        
1. Indicador de Tendência
2. Indicador de Entrada
3. Sair

(Menu Indicador de Tendência - Menu Rompimento de Pullback)
1. Indicador Teoria de Dow
2. Indicador Detector de Topos e Fundos
3. Sair

(Menu Indicador de Entrada - Menu Rompimento de Pullback)
1. Indicador Retração de Fibonacci
2. Indicador Rompimento do Movimento Anterior
3. Sair

(Menu Rompimento de Média Móvel Aritmética)                        
1. Indicador de Tendência
2. Indicador de Entrada
3. Sair

(Menu Indicador de Tendência - Rompimento de Média Móvel Aritmética)
1. Indicador Média Móvel
2. Sair
                                                    
(Menu Indicador de Entrada - Rompimento de Média Móvel Aritmética)
1. Indicador Média Móvel
2. Sair

(Menu Scalping Dólar)                        
1. Indicador de Tendência
2. Indicador de Entrada
3. Sair

(Menu Indicador de Tendência - Scalping no Dólar)
1. Indicador Teoria de Dow
2. Indicador Detector de Topos e Fundos
3. Sair

(Menu Indicador de Entrada - Scalping no Dólar)
1. Indicador Retração de Fibonacci
2. Indicador Rompimento do Movimento Anterior
3. Sair

Nota: Alguns indicadores podem ser vistos no livro 'Análise Técnicas dos Mercados Financeiros - Um Guia Completo e Definitivo dos Métodos de Negociação de Ativos' de Flávio Lemos.

{Eventos do Simulador}

Os eventos discretos são baseados na iteração da matriz de Preços os quais são obtidos do arquivo lido pelo simulador. A cada iteração, um método obtém o Preço passo a passo ou todos os preços ao mesmo tempo. Os Tipos de Preços do mercado financeiro são: Abertura, Máxima, Mínima e Fechamento.