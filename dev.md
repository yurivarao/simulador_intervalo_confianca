# AssetsSim for Devs

{Simulador de Ativos Financeiros}

Classes

Setup - configura os momentos de entrada e saída (com e sem perda) - stop loss e stop gain
Indicador - configura os indicadores usados pelos Setups (Indicador de Entrada e o Indicador de Tendência)
Graficos - plotar algumas saídas dos setups
Operacao - configura as operações de entrada e saída com saldo
Simulador - core do simulador (agrega as outras classes)
Menu - configura as opções de menu
Estatistica - configura algumas funções de modelagem e simulação. Arquivo TabelaStudentT.csv com valores para o intervalo de confiança

Classe Setup

Importa a classe Indicador para definição dos momentos de entrada (gatilho - se o preço atingir o gatilho a operação de compra ou venda é iniciada) e tendência (alta ou baixa).

Função atualizar para checar as condições do Setup preço a preço, ou seja, a cada mudança do preço escolhido (Abertura, Máxima, Mínima e Fechamento) verificar os indicadores de entrada e tendência.

Função atualizarAcumulados para atualizar o array de preços total.

Funções dos Cenários para os Setups: rompimentoPullback, rompimentoMMA, scalpingDolar, reversaoPorMedias, longOnly, reversaoPorToposEFundos etc (de acordo com a necessidade de cada aluno).

Função obterSinaisIndicadores para armazenar e plotar os sinais de saída dos indicadores.

Função obterMovimentosECorrecoes para fazer o estudo da Teoria de Dow (retrações).


Classe Indicador

Implementações dos indicadores de entrada e tendência.

Funções mediaMovelAritmetica, detectorDeToposEFundos, retracaoDeFibonacci, parabolicoSAR etc (de acordo com a necessidade de cada aluno).

Classe Graficos

Implementa as configurações para plotar os gráficos.

Funções plotarDadosReais, plotarDadosReaisPrecosSimulados, plotarDadosReaisCandleStick, plotarResultadosSetup, plotarSaldo, plotarSinaisIndicadores, plotarPontosDadosArtificiais, plotarHistogramas, plotarSARParabolico.


Classe Operacao

Implementa as rotinas para realizar operaçoes de compra e venda, bem como registrar o saldo.

Função iniciarOperacao - revisar a sua necessidade???

Função atualizar para checar se foi atingido o stop loss ou o stop gain preço a preço.

Funções comprar e vender para atualizar o estado da operação e registrar se foi compra ou venda.

Função aumentarPosicao e diminuirPosicao para realizar mais ou menos compras ou vendas de acordo com as condições do Setup.

Função atualizarSaldo para registrar os ganhos e perdas.

Função consultarSaldo para verificar o saldo atual.

Função consultarPosicao para verificar quantas operações de compra ou venda estão em aberto.


Classe Simulador

Implementa a interação entre as classes Operacao, Setup, Graficos e Estatistica.

Função obterDadosReaisAlphavantage para obter dados da API com informações sobre o ativo em um histórico de 100 amostras.

Função precoPassoAPasso onde avança a simulação preço a preço.

Função reinicializarDadosReais e reinicializarDadosArtificiais para zerar os dados nos arrays a cada nova simulação.

Função inicializarOperacaoESetup para instanciar as classes Operacao e Setup.

Função simular para executar as simulações de acordo com a escolha do usuário no menu.

Função precos para obter e armazenar os preços por iteração.

Função precosAcumulados para armazenar os preços obtidos nas execuções anteriores.

Função ordenarPrecos (rever a necessidade desta função????)

Função replicarNVezesDadosReais e replicarNVezesDadosArtificiais para executar a simulação e obter as retrações (movimentos e correções.

Função pausar (verificar a utilidade com os alunos???)


Classe Menu

Importa a classe Simulador e implementa as opções do menu, incluindo os códigos dos indicadores e setup a serem executados.

Função chamarMenu para executar as opções escolhidas pelo usuário.

Funções obterOpcaoMenu, obterOpcaoOrigem e obterOpcaoSetup para obter estado das escolhas do usuário pelo menu.



Classe Estatistica

Implementação das rotinas de modelagem e simulação.

Funções obterMediaLognormal e obterMedia, obterDesvioPadraoLognormal e obterDesvioPadrao para gerar dados estatísticos dos preços ou retrações.

Função gerarDadosArtificiaisLognormal para gerar dados com função randômica.

Função obterPrecisao_H e estimar_N para calcular o intervalo de confiança e controlar as replicações do simulador.



Fluxo do Simulador

Inicialmente o usuário executa o arquivo principal (main) que instancia a classe Menu. Por sua vez, a classe Menu instancia a classe Simulador com as escolhas do usuário (origem dos dados: reais ou artificias, indicador de entrada e indicador de tendência).

A classe Simulador instancia as classes Operacao, Indicador, Setup, Graficos e Estatistica. A classe Setup é acionada pelo código correspondente às escolhas do usuário no menu, a qual aciona os indicadores de entrada e de tendência na classe Indicador.

Uma outra escolha a ser feita pelo usuário é o tipo de preço a ser considerado na execução da simulação passo a passo, ou seja, pode ser escolhido os preços de Abertura, Máxima, Mínima e Fechamento. 

A classe Simulador inicia com o loop de escolhas do tipo de preço e posteriormente passa a executar preço a preço. A cada iteração, um menu pode ser acionado para continuar a execução da seguinte forma: Passo a passo, Todos, Até o Preço, A partir do Preço, Intervalo de Preços. Além disso, é possível no mesmo menu, escolher entre plotar os Gráficos ou gerar a Estatística dos dados já executados.

Nas opções Passo a passo, Todos, Até o Preço, A partir do Preço, Intervalo de Preços é possível definir quais os preços devem ser levados em consideração na execução da simulação. Na opção Estatística, somente os preço que atenderem as critérios de precisão para o intervalo de confiança configurado serão levados em conta na execução.

