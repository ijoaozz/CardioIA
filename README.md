# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
  <img src="assets/logo-fiap.png" alt="FIAP Logo" width="50%">
</p>

# ❤️ CardioIA – Fase 1: Batimentos de Dados

## 📌 Visão Geral do Projeto

O **CardioIA** é um projeto acadêmico desenvolvido no curso de Inteligência Artificial da **FIAP** com o objetivo de simular um **ecossistema inteligente de apoio à cardiologia moderna**, utilizando técnicas de **Ciência de Dados e Inteligência Artificial aplicadas à saúde**.

O projeto integra diferentes tipos de dados médicos para apoiar a **identificação de fatores de risco cardiovascular**, explorando três grandes áreas da Inteligência Artificial:

- 📊 **Dados Numéricos (Machine Learning)**
- 🧠 **Dados Textuais (Processamento de Linguagem Natural - NLP)**
- 🖼 **Dados Visuais (Visão Computacional – etapas futuras)**

Essa abordagem multidisciplinar permite explorar como diferentes fontes de dados podem ser utilizadas para **auxiliar decisões clínicas baseadas em dados**.

---

# 🎯 Objetivos do Projeto

O **CardioIA** tem como principais objetivos:

- Aplicar técnicas de **Machine Learning** para prever risco de doenças cardíacas.
- Utilizar **Processamento de Linguagem Natural (NLP)** para extrair conhecimento de textos científicos da área médica.
- Preparar uma base de **imagens de eletrocardiograma (ECG)** para futuras aplicações de **Visão Computacional**.
- Demonstrar como a **Inteligência Artificial pode apoiar diagnósticos médicos**.

---

# 👨‍🎓 Integrantes e Responsabilidades

| Nome | RM | Responsabilidades Principais no CardioIA |
|-----|-----|-----|
| **Daniele Antonieta Garisto Dias** | RM565106 | **Data Preparation & Organização do Dataset:** preparação e limpeza do dataset `heart.csv`, verificação de valores faltantes, padronização das variáveis, criação do dicionário de dados e organização da estrutura de pastas do projeto. |
| **Leandro Augusto Jardim da Cunha** | RM561395 | **Model Training (Machine Learning):** implementação e treinamento do modelo **Random Forest**, divisão treino/teste, execução da validação cruzada e salvamento do modelo treinado (`modelo_cardioia.pkl`). |
| **Luiz Eduardo da Silva** | RM561701 | **Data Analysis & Visualization:** realização da análise exploratória dos dados (EDA), geração de gráficos estatísticos e análise de correlação entre variáveis utilizando bibliotecas como **Matplotlib** e **Seaborn**. |
| **João Victor Viana de Sousa** | RM565136 | **Evaluation, NLP & Documentação:** extração e análise das métricas do modelo (acurácia e validação cruzada), implementação do processamento textual com **NLTK**, geração de frequência de palavras/WordCloud e elaboração da análise crítica final e documentação do projeto. |

---

# 👩‍🏫 Professores

**Tutor:** Caique Nonato da Silva Bezerra 
**Coordenador:** Andre Godoi Chiovato  

---

# 🩺 Parte 1 – Dados Numéricos (Machine Learning)

## 📂 Origem dos Dados

O dataset utilizado é baseado no conhecido **Heart Disease Dataset**, amplamente utilizado em pesquisas acadêmicas e disponível em bases públicas como:

- UCI Machine Learning Repository
- Kaggle

Trata-se de um conjunto de dados **reais e anonimizados** contendo informações clínicas de pacientes submetidos a exames cardiológicos.

### Estrutura do Dataset

- **303 registros**
- **14 variáveis clínicas**
- **1 variável alvo (doença cardíaca)**

---

# 📊 Variáveis do Dataset

| Variável | Descrição Clínica |
|--------|--------|
| idade | Idade do paciente |
| sexo | 0 = Mulher / 1 = Homem |
| tipo_dor_peito | Tipo de dor torácica |
| pressao_repouso | Pressão arterial em repouso |
| colesterol | Colesterol sérico |
| glicose_jejum | Glicose em jejum |
| eletrocardiograma | Resultado do ECG |
| freq_cardiaca_max | Frequência cardíaca máxima |
| angina_exercicio | Angina induzida por exercício |
| depressao_st | Depressão do segmento ST |
| inclinacao_st | Inclinação do ST |
| num_vasos_principais | Número de vasos afetados |
| talassemia | Distúrbio sanguíneo associado |
| doenca_cardiaca | 0 = Saudável / 1 = Doente |

---

# 🧠 Variáveis Mais Relevantes Clinicamente

De acordo com o modelo **Random Forest** treinado, as variáveis mais importantes foram:

1. **depressao_st**
2. **freq_cardiaca_max**
3. **num_vasos_principais**
4. **tipo_dor_peito**

### 🔬 Justificativa Clínica

- **Depressão do segmento ST**: associada a isquemia miocárdica.
- **Frequência cardíaca máxima**: indica capacidade funcional do coração sob esforço.
- **Número de vasos principais afetados**: indica gravidade da obstrução arterial.
- **Tipo de dor no peito**: ajuda a diferenciar dores cardíacas de outras causas.

Essas variáveis representam **sinais fisiológicos diretamente relacionados ao risco de infarto**.

---

# 🤖 Modelo de Machine Learning

Foi utilizado o algoritmo:

**Random Forest Classifier**

Configuração do modelo:

- **Divisão dos dados:** 80% treino | 20% teste
- **Validação cruzada:** 5 Folds

---

# 📈 Resultados Obtidos

| Métrica | Resultado |
|------|------|
| Acurácia no Teste | **83,61%** |
| Média Validação Cruzada | **83,82%** |
| Desvio Padrão | 0,0288 |

### 🔎 Interpretação

O modelo apresenta **desempenho consistente**, sem indícios relevantes de **overfitting**, demonstrando boa capacidade de generalização para novos pacientes.

O modelo treinado foi salvo como:

`models/modelo_cardioia.pkl`

Permitindo reutilização futura sem necessidade de novo treinamento.


# 🧠 Parte 2 – Dados Textuais (NLP)

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

`*_limpo.txt`



---

# 🤖 Aplicações do NLP na Saúde

Os textos podem ser explorados por algoritmos de NLP para:

### 1️⃣ Extração de Sintomas

Identificação automática de termos como:

- dor torácica
- dispneia
- fadiga
- hipertensão

Aplicável em **triagem automatizada de pacientes**.

### 2️⃣ Classificação de Tópicos

Agrupamento de textos em categorias como:

- prevenção
- diagnóstico
- tratamento
- fatores de risco

### 3️⃣ Análise de Frequência

Permite identificar:

- fatores de risco mais citados
- tendências em literatura médica
- padrões de sintomas relatados

### 4️⃣ Análise de Sentimentos (Futuro)

Pode ser utilizada para:

- analisar relatos de pacientes
- monitorar saúde mental associada a doenças cardíacas

---

# 🖼 Parte 3 – Dados Visuais (Visão Computacional)

## 📂 Dataset de Imagens de ECG

Para futuras etapas do projeto será utilizado o dataset:

**ECG Images dataset of Cardiac Patients**

Disponível em:

https://data.mendeley.com/datasets/gwbz3fsgp8/2

DOI:

https://doi.org/10.17632/gwbz3fsgp8.2

Esse dataset foi desenvolvido para apoiar pesquisas em **detecção automática de doenças cardíacas a partir de exames de ECG**.

---

# 📊 Estrutura do Dataset de ECG

| Categoria | Quantidade de Imagens |
|------|------|
| Imagens de ECG de pacientes com infarto do miocárdio | 239 |
| Imagens de ECG de pacientes com batimentos cardíacos anormais | 233 |
| Imagens de ECG de pacientes com histórico de infarto do miocárdio | 172 |
| Imagens de ECG de pessoa normal | 284 |

Total aproximado:

**928 imagens de ECG**

Essas imagens podem ser utilizadas para treinamento de modelos de **Redes Neurais Convolucionais (CNN)**.

---

# ☁ Armazenamento das Imagens

As imagens utilizadas no projeto estão armazenadas no Google Drive do grupo:

https://drive.google.com/drive/folders/10J-JmmMmHfqOYicCnK0faUF11TV-F7xZ

Esse repositório permite:

- compartilhamento entre integrantes
- organização do dataset
- integração com notebooks de treinamento

---

# 📁 Estrutura do Projeto

```
CardioIA_Fase1/
│
├── .venv/                          # Ambiente virtual Python
├── __pycache__/                    # Arquivos compilados automaticamente
│
├── asset/                        
│   └── logo-fiap.png
│
├── dataset/                        # Base de dados numérica
│   └── heart.csv

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
```

O projeto foi organizado de forma modular, separando responsabilidades entre:

* preparação de dados,
* análise exploratória,
* treinamento do modelo,
* processamento textual (NLP),
* persistência do modelo treinado.


A estrutura modular facilita:

- manutenção
- escalabilidade
- reutilização do modelo

---

# 📊 Governança de Dados e Viés

O projeto considera aspectos importantes de **IA responsável**:

- utilização de **dados anonimizados**
- possíveis **vieses relacionados a sexo e idade**
- necessidade de **validação clínica**

Modelos de IA devem ser utilizados **apenas como apoio à decisão médica**, e nunca como substituição da avaliação profissional.

---

# 🚀 Conclusão

A **Fase 1 do CardioIA** estabeleceu uma base sólida para o desenvolvimento do projeto, integrando:

- Ciência de Dados
- Machine Learning
- Processamento de Linguagem Natural
- Organização estruturada de datasets

Os resultados demonstram o potencial da **Inteligência Artificial na identificação de fatores de risco cardiovascular**, abrindo caminho para futuras fases que incluirão **Visão Computacional aplicada a exames de ECG**.

---

# 📜 Licença do Dataset de Imagens ECG

As imagens de eletrocardiograma utilizadas neste projeto são provenientes do dataset público:

**ECG Images dataset of Cardiac Patients**

Autores do dataset:

- Ali Haider Khan  
- Muzammil Hussain  

---

## 🪪 Licença

Este dataset está licenciado sob a licença:

**Creative Commons Attribution 4.0 International (CC BY 4.0)**

Isso significa que os dados podem ser:

- compartilhados
- copiados
- distribuídos
- modificados
- utilizados em pesquisas

Desde que sejam respeitadas as seguintes condições:

- seja dado **crédito apropriado aos autores**
- seja incluído um **link para a licença original**
- seja indicado **se modificações foram realizadas**

Licença completa disponível em:

https://creativecommons.org/licenses/by/4.0/

---

## ⚠ Observação Importante

O uso deste dataset **não implica endosso dos autores ou das instituições responsáveis** pelo projeto CardioIA.

Além disso, conteúdos eventualmente identificados como pertencentes a terceiros podem exigir permissões adicionais para reutilização.




