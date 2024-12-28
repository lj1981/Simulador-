Foi realizar análises financeiras e criar visualizações de dados.

Ferramentas utilizadas: Para o desenvolvimento deste projeto, foram utilizadas as seguintes bibliotecas Python:

Pandas: Manipulação e análise de dados.
NumPy: Operações numéricas e matriciais.
Matplotlib, Seaborn, Plotly: Criação de visualizações e gráficos.
yfinance: Obtenção de dados financeiros de diversas fontes.
statsmodels: Modelagem estatística e econometria.
scikit-learn: Aprendizado de máquina e mineração de dados.
gunicorn: Servidor HTTP para deploy da aplicação.

Coleta e preparação de dados: Utilizando a biblioteca yfinance, coletei dados históricos de preços de diversos ativos. Com o Pandas, organizei e limpei os dados, realizando cálculos como retornos e volatilidade.
Análise exploratória de dados: Através de Matplotlib e Seaborn, visualizei a distribuição dos retornos, a correlação entre os ativos e identifiquei padrões nos dados.

Modelagem e otimização: Construí modelos de precificação de ativos utilizando o statsmodels e otimizei portfólios com base na teoria de Markowitz, implementando algoritmos em NumPy.

Deploy: Para disponibilizar a aplicação, utilizei o gunicorn como servidor HTTP, permitindo a consulta dos resultados através de uma interface web.


A escolha das bibliotecas Pandas, NumPy e scikit-learn foi fundamental para a manipulação eficiente de grandes volumes de dados e a implementação de algoritmos de aprendizado de máquina. A biblioteca yfinance facilitou a obtenção de dados financeiros em tempo real, enquanto Matplotlib, Seaborn e Plotly permitiram a criação de visualizações personalizadas e interativas. 
