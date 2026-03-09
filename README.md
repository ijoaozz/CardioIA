# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
  <img src="assets/logo-fiap.png" alt="FIAP Logo" width="50%">
</p>

❤️ CardioIA – Fase 1: Batimentos de Dados

📌 Visão Geral do Projeto

O **CardioIA** é um projeto acadêmico desenvolvido no curso de Inteligência Artificial com o objetivo de simular o ecossistema de uma cardiologia moderna, integrando:

* 📊 Dados Numéricos (Machine Learning)
* 🧠 Dados Textuais (NLP)
* 🖼 Dados Visuais (Visão Computacional – etapas futuras)

---

## 👨‍🎓 Integrantes e Responsabilidades

| Nome | RM | Responsabilidades Principais no Projeto (PBL de IA) |
| :--- | :--- | :--- |
| **Daniele Antonieta Garisto Dias** | RM565106 | **Data Preparation & Anotation:** Responsável pela preparação do dataset, estruturação de pastas para o YOLO, e garantia da qualidade e consistência das anotações (caixas delimitadoras e labels) utilizadas no treinamento. |
| **Leandro Augusto Jardim da Cunha** | RM561395 | **Model Training & Baseline:** Implementação inicial do modelo **YOLOv8 Padrão (10 Épocas)** e da arquitetura **CNN para Classificação**. Condução dos primeiros ciclos de treinamento (baseline). |
| **Luiz Eduardo da Silva** | RM561701 | **Model Optimization & Tuning:** Execução das simulações de alto desempenho (30 e **60 Épocas**). Otimização e ajuste fino de hiperparâmetros do YOLOv8 para alcançar o melhor $\text{mAP50-95}$. |
| **João Victor Viana de Sousa** | RM565136 | **Evaluation & Analysis:** Extração e consolidação de todas as métricas (mAP50-95, Acurácia). Criação das tabelas comparativas e desenvolvimento da **Análise Crítica Final** (Comparativo YOLO vs. CNN). |
| **Guilherme Ribeiro Slaviero** | RM561757 | **Project Lead & Documentation:** Gerenciamento do fluxo de trabalho, estruturação e padronização dos relatórios e do arquivo **README.md**. Garantia da reprodutibilidade do projeto no Google Colab. |

---

## 👩‍🏫 Professores

- **Tutor(a):** Leonardo Ruiz Orabona  
- **Coordenador(a):** Andre Godoi Chiovato  

---

Nesta **Fase 1 – Batimentos de Dados**, o foco está na construção, organização e análise das bases de dados que alimentarão os módulos inteligentes nas próximas fases do projeto.

🩺 Parte 1 – Dados Numéricos (Machine Learning)

📂 Origem dos Dados

O dataset utilizado é baseado no conhecido **Heart Disease Dataset**, amplamente utilizado em pesquisas acadêmicas e disponível em bases públicas como:

* UCI Machine Learning Repository
* Kaggle

Trata-se de um conjunto de dados reais anonimizados contendo informações clínicas de pacientes submetidos a exames cardiológicos.

O dataset possui:

* 303 registros
* 14 variáveis clínicas
* 1 variável alvo (doença cardíaca)

📊 Variáveis do Dataset

| Variável             | Descrição Clínica             |
| -------------------- | ----------------------------- |
| idade                | Idade do paciente             |
| sexo                 | 0 = Mulher / 1 = Homem        |
| tipo_dor_peito       | Tipo de dor torácica          |
| pressao_repouso      | Pressão arterial em repouso   |
| colesterol           | Colesterol sérico             |
| glicose_jejum        | Glicose em jejum              |
| eletrocardiograma    | Resultado do ECG              |
| freq_cardiaca_max    | Frequência cardíaca máxima    |
| angina_exercicio     | Angina induzida por exercício |
| depressao_st         | Depressão do segmento ST      |
| inclinacao_st        | Inclinação do ST              |
| num_vasos_principais | Número de vasos afetados      |
| talassemia           | Distúrbio sanguíneo associado |
| doenca_cardiaca      | 0 = Saudável / 1 = Doente     |

🧠 Variáveis Mais Relevantes Clinicamente

De acordo com o modelo Random Forest treinado, as variáveis mais importantes foram:

1. **depressao_st**
2. **freq_cardiaca_max**
3. **num_vasos_principais**
4. **tipo_dor_peito**

🔬 Justificativa Clínica

* **Depressão do segmento ST**: Alterações no segmento ST são fortemente associadas a isquemia miocárdica.
* **Frequência cardíaca máxima**: Capacidade funcional do coração sob esforço.
* **Número de vasos principais afetados**: Indica gravidade da obstrução arterial.
* **Tipo de dor no peito**: Diferencia dor cardíaca típica de outras causas.

Essas variáveis são fundamentais para modelos preditivos em cardiologia, pois representam sinais fisiológicos diretamente relacionados à perfusão cardíaca e risco de infarto.

🤖 Modelo de Machine Learning

Foi utilizado:

* Algoritmo: **Random Forest Classifier**
* Divisão: 80% treino | 20% teste
* Validação Cruzada: 5 Folds

📈 Resultados Obtidos

* Acurácia Teste: **83,61%**
* Média Validação Cruzada: **83,82%**
* Desvio padrão: 0,0288

🔎 Interpretação

O modelo apresenta desempenho consistente, sem indícios relevantes de overfitting, demonstrando boa capacidade de generalização para novos pacientes.

O modelo treinado foi salvo como:

models/modelo_cardioia.pkl

Permitindo reutilização futura sem necessidade de novo treinamento.


🧠 Parte 2 – Dados Textuais (NLP)

📂 Origem dos Textos

Foram utilizados textos acadêmicos relacionados a:

* Fatores de risco cardiovascular
* Promoção da saúde
* Doenças cardiovasculares

As fontes incluem materiais públicos e científicos voltados à saúde.

Os arquivos foram convertidos de PDF para `.txt`, organizados na pasta `docs/`.

🔎 Processamento Realizado

Foi aplicado:

* Tokenização
* Remoção de pontuação
* Remoção de stopwords (NLTK)
* Normalização de texto
* Geração de frequência de palavras
* WordCloud

Os textos limpos foram salvos como:

*_limpo.txt


🤖 Como NLP Pode Ser Aplicado

Os textos podem ser explorados por algoritmos de NLP para:

1️⃣ Extração de Sintomas

Identificação automática de termos como:

* dor torácica
* dispneia
* fadiga
* hipertensão

Aplicável em triagem automatizada.

2️⃣ Classificação de Tópicos

Agrupar textos por:

* prevenção
* diagnóstico
* tratamento
* fatores de risco

Importante para organização de prontuários médicos digitais.

3️⃣ Análise de Frequência

Identificação de termos mais recorrentes pode revelar:

* Principais fatores de risco mencionados
* Tendências em literatura médica
* Padrões em sintomas relatados

4️⃣ Análise de Sentimentos (Etapas Futuras)

Aplicável para:

* Avaliar relatos de pacientes
* Monitorar saúde mental associada a doenças cardíacas


🎯 Relevância para IA na Saúde

O uso de NLP na saúde permite:

* Automatização de triagens
* Apoio à decisão clínica
* Extração de informação de prontuários
* Redução de carga administrativa médica
* Detecção precoce de padrões de risco


📊 Governança de Dados e Viés

Este projeto considera:

* Dados anonimizados
* Possíveis vieses relacionados a sexo e idade
* Necessidade de validação clínica antes de uso real

É importante destacar que modelos preditivos em saúde devem ser utilizados apenas como apoio à decisão médica, nunca como substituição da avaliação profissional.


📁 Estrutura do Projeto

CardioIA_Fase1/
│
├── .venv/                          # Ambiente virtual Python
├── __pycache__/                    # Arquivos compilados automaticamente
│
├── dataset/                        # Base de dados numérica
│   └── heart.csv
│
├── docs/                           # Dados Textuais (NLP)
│   ├── analise_visual.py
│   ├── conversor_nlp.py
│   ├── frequencia_palavras.py
│   ├── limpeza_nlp.py
│   ├── dicionario_dados.md
│   │
│   ├── Fatores Associados às Doenças Cardiovasculares.pdf
│   ├── Fatores Associados às Doenças Cardiovasculares.txt
│   ├── Fatores Associados às Doenças Cardiovasculares_limpo.txt
│   │
│   ├── Promoção da Saúde às Doenças Cardiovasculares.pdf
│   ├── Promoção da Saúde às Doenças Cardiovasculares.txt
│   └── Promoção da Saúde às Doenças Cardiovasculares_limpo.txt
│
├── models/                         # Modelos treinados e serializados
│   ├── modelo_cardioia.pkl
│   └── colunas_modelo.pkl
│
├── outputs/                        # Gráficos gerados na análise
│
├── main.py                         # Análise exploratória dos dados
├── modelo_preditivo.py             # Treinamento e avaliação do modelo ML
├── visualizacao_dados.py           # Geração de gráficos estatísticos
├── utils.py                        # Funções auxiliares (carregamento do dataset)
├── run.py                          # Execução central do projeto
├── teste_modelo_salvo.py           # Teste de carregamento do modelo salvo
├── requirements.txt                # Dependências do projeto
└── README.md

O projeto foi organizado de forma modular, separando responsabilidades entre:

* preparação de dados,
* análise exploratória,
* treinamento do modelo,
* processamento textual (NLP),
* persistência do modelo treinado.

Essa estrutura facilita manutenção, escalabilidade e futuras integrações com APIs ou interfaces gráficas.


🚀 Conclusão

A Fase 1 estabeleceu uma base sólida para o CardioIA, integrando:

* Ciência de Dados
* Machine Learning
* Processamento de Linguagem Natural
* Organização estruturada de dados

Os resultados demonstram a viabilidade de aplicação de Inteligência Artificial na identificação de fatores de risco cardiovascular, abrindo caminho para as próximas fases do projeto.

