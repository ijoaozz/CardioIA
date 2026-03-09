import pandas as pd

# Configuração para mostrar todas as colunas no terminal sem cortar
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

def analisar_dados():
    print("--- 1. Carregando o dataset heart.csv ---")
    try:
        # Lê o arquivo CSV que está dentro da pasta dataset
        from utils import carregar_dataset
        df = carregar_dataset()
        
    except FileNotFoundError:
        print("Erro: O arquivo 'heart.csv' não foi encontrado. Verifique se ele está na pasta 'dataset'.")
        return

    # --- Primeiras linhas do dataset ---
    print("\n--- Primeiras 5 linhas do dataset (Cabeçalho) ---")
    print(df.head())

    # --- Verificação de dados faltantes ---
    # Modelos de IA não lidam bem com dados vazios (nulos)
    print("\n--- Verificação de Dados Faltantes (Valores Nulos) ---")
    print(df.isnull().sum())

    # --- Resumo Estatístico ---
    # Mostra a média, o valor mínimo, máximo e os quartis de cada coluna
    print("\n--- Resumo Estatístico ---")
    print(df.describe())

    # --- Distribuição da variável alvo ---
    # Verifica se a base está balanceada (quantos pacientes doentes vs saudáveis)
    if 'doenca_cardiaca' in df.columns:
        print("\n--- Distribuição de Pacientes ---")
        print("0 = Saudável, 1 = Doença Cardíaca")
        print(df['doenca_cardiaca'].value_counts())
    else:
        print("\nColuna 'doenca_cardiaca' não encontrada. Verifique o nome original da coluna alvo.")

# Executa a função principal
if __name__ == "__main__":
    analisar_dados()