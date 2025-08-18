# %% [markdown]
# <a href="https://colab.research.google.com/github/Renato1485/Criando-um-API/blob/main/database_python.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# %%
import plotly.io as pio
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


# %%
df = pd.read_csv(
    "https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

# %%
df.head()

# %%
df.info()

# %%
df.describe()

# %%
df.shape

# %%
linhas, colunas = df.shape[0], df.shape[1]
print("Número de linhas é: ", linhas)
print("Número de colunas é: ", colunas)

# %%
df.columns

# %%


# %%
renomear_coluna = {
    'ano_trabalho': 'ano',
    'nivel_experiencia': 'senhoridade',
    'tipo_emprego': 'contrato',
    'cargo': 'cargo',
    'salario': 'salario',
    'moeda_salario': 'moeda',
    'salario_em_usd': 'usd',
    'residencia_empregado': 'residencia',
    'taxa_remoto': 'remoto',
    'localizacao_empresa': 'empresa',
    'tamanho_empresa': 'tamanho_empresa'
}

df.rename(columns=renomear_coluna, inplace=True)
df.columns

# %%
traduzir_coluna = {
    'work_year': 'ano',
    'experience_level': 'senhoridade',
    'employment_type': 'contrato',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda',
    'salary_in_usd': 'usd',
    'employee_residence': 'residencia',
    'remote_ratio': 'remoto',
    'company_location': 'empresa',
    'company_size': 'tamanho_empresa'
}

df.rename(columns=traduzir_coluna, inplace=True)
df.columns

# %%
df["ano"].value_counts()

# %%
df["senhoridade"].value_counts()

# %%
df["contrato"].value_counts()

# %%
df["cargo"].value_counts()

# %%
df["salario"].value_counts()

# %%
df["moeda"].value_counts()

# %%
df["usd"].value_counts()

# %%
df["residencia"].value_counts()

# %%
df["remoto"].value_counts()

# %%
df["empresa"].value_counts()

# %%
df["tamanho_empresa"].value_counts()

# %%
senhoridade = {
    'SE': 'Senior',
    'MI': 'Junior',
    'EN': 'Pleno',
    'EX': 'Executivo'
}

df["senhoridade"] = df["senhoridade"].replace(senhoridade)
df["senhoridade"].value_counts()

# %%
contrato = {
    'FT': 'Tempo integral',
    'PT': 'Tempo parcial',
    'FL': 'Freelancer',
    'CT': 'Contrato'
}

df["contrato"] = df["contrato"].replace(contrato)
df["contrato"].value_counts()

# %%
tamanho_empresa = {
    'M': 'Médio',
    'L': 'Grande',
    'S': 'Pequeno'
}

df["tamanho_empresa"] = df["tamanho_empresa"].replace(tamanho_empresa)
df["tamanho_empresa"].value_counts()

# %%
remoto = {
    '0': 'Presencial',
    '50': 'Hibrido',
    '100': 'Remoto'
}

df["remoto"] = df["remoto"].replace(remoto)
df["remoto"].value_counts()

# %%
df.head()

# %%
df.describe(include='object')

# %% [markdown]
#

# %%
df.describe()

# %%
df.isnull()

# %%
df.isnull().sum()

# %%
df['ano'].unique()

# %%
df[df.isnull().any(axis=1)]

# %%
# criação de dataframe teste
df_salarios = pd.DataFrame({
    'nome': ["Ana", "Paula", "Ricardo", "Paulo", "Val"],
    'salario': [4000, np.nan, 5000, np.nan, 100000]
})
# calcula a média e arredonda os valores
df_salarios['salario_media'] = df_salarios['salario'].fillna(
    df_salarios['salario'].mean().round(2))
# calcula a mediana
df_salarios['salario_media'] = df_salarios['salario'].fillna(
    df_salarios['salario'].median())
df_salarios

# %%
df_temperaturas = pd.DataFrame({
    'dias': ["segunda", "terça", "quarta", "quinta", "sexta"],
    'temperatura': [30, np.nan, np.nan, 28, 27]
})

df_temperaturas['preenchido_ffill'] = df_temperaturas['temperatura'].ffill()
df_temperaturas

# %%
df_cidades = pd.DataFrame({
    'nome': ["Ana", "Paula", "Ricardo", "Paulo", "Val"],
    'cidade': ["São Paulo", np.nan, "curitiva", np.nan, "Belém"]
})

df_cidades['cidade_preenchida'] = df_cidades['cidade'].fillna("Não informada")
df_cidades


# %%
df_limpo = df.dropna()

# %%
df_limpo.isnull().sum()

# %%
df_limpo.head()

# %%
df_limpo.info()

# %%
# converter o Dtype de flout para int
df_limpo = df_limpo.assign(ano=df_limpo["ano"].astype("int64"))


# %%
# criação de gráfico
df_limpo['senhoridade'].value_counts().plot(kind='bar', title='Senhoridade')

# %%

# criação de gráfico com salários médio anual em dólar
sns.barplot(data=df_limpo, x='senhoridade', y='usd')

# %%
# configurando o gráfico
plt.figure(figsize=(10, 6))
sns.barplot(data=df_limpo, x='senhoridade', y='usd')
plt.title('Salário médio por senhoridade')
plt.xlabel('Senhoridade')
plt.ylabel('Salário médio anual(usd)')
plt.show()


# %%
df_limpo.groupby('senhoridade')['usd'].mean().sort_values(ascending=False)

# %%
# função para alterar o gráfico do menor para o maior ou contrário
ordem = df_limpo.groupby('senhoridade')[
    'usd'].mean().sort_values(ascending=True).index
ordem


# %%
plt.figure(figsize=(10, 6))
sns.barplot(data=df_limpo, x='senhoridade', y='usd', order=ordem)
plt.title('Salário médio por senhoridade')
plt.xlabel('Senhoridade')
plt.ylabel('Salário médio anual(usd)')
plt.show()


# %%
plt.figure(figsize=(10, 5))  # largura e altura do gráfito
# bins=50, é a largura das linhas do gráfico, e o True é a linha azul que acompanha as colunas
sns.histplot(df_limpo['usd'], bins=50, kde=True)
plt.title('Distribuição salarial')
plt.xlabel('Salário anual(usd)')
plt.ylabel('Frequência')
plt.show()

# %%
plt.figure(figsize=(8, 5))
sns.boxplot(x=df_limpo['usd'])
plt.title('Boxplot salarial')
plt.xlabel('Salário anual(usd)')
plt.show()

# %%
ordem_senhoridade = ['Junior', 'Pleno', 'Senior', 'Executivo']
plt.figure(figsize=(8, 5))
sns.boxplot(x=df_limpo['senhoridade'],
            y=df_limpo['usd'], order=ordem_senhoridade)
plt.title('Boxplot salarial por senhoridade')
plt.xlabel('senhoridade')
plt.show()

# %%
ordem_senhoridade = ['Junior', 'Pleno', 'Senior', 'Executivo']
plt.figure(figsize=(8, 5))
sns.boxplot(x=df_limpo['senhoridade'], y=df_limpo['usd'],
            order=ordem_senhoridade, palette='Set2', hue='senhoridade', data=df_limpo)
plt.title('Boxplot salarial por senhoridade')
plt.xlabel('senhoridade')
plt.show()

# %%
# Configuração para abrir os gráficos no navegador
pio.renderers.default = 'browser'


# %%


# %%
remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

fig = px.pie(remoto_contagem,  # criando gráfico pizza
             names='tipo_trabalho',
             values='quantidade',
             title='Distribuição por tipo de trabalho remoto')
fig.show()

# %%
remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

fig = px.pie(remoto_contagem,  # criando gráfico pizza
             names='tipo_trabalho',
             values='quantidade',
             title='Distribuição por tipo de trabalho remoto',
             hole=0.5)  # Criar um espaço dentro do gráfico (tipo rosquinhas)
fig.show()

# %%
remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

fig = px.pie(remoto_contagem,  # criando gráfico pizza
             names='tipo_trabalho',
             values='quantidade',
             title='Distribuição por tipo de trabalho remoto',
             hole=0.5)  # Criar um espaço dentro do gráfico (tipo rosquinhas)
fig.update_traces(textinfo='percent+label')  # adicionar texto no gráfico
fig.show()
