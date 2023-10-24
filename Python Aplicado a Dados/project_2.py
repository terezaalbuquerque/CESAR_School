import pandas as pd

def define_tipo_faixa_etaria(idade):
    if 3 <= idade <= 12:
        return 'Crianças: 3 a 12 anos'
    elif 13 <= idade <= 19:
        return 'Adolescentes: 13 a 19 anos'
    elif 20 <= idade <= 39:
        return 'Jovens adultos: 20 a 39 anos'
    elif 40 <= idade <= 59:
        return 'Adultos de meia-idade: 40 a 59 anos'
    else:
        return 'Idosos: 60 anos ou mais'

def define_regiao(cidade):
    metropolitana_cidades = ['Recife', 'Olinda', 'Jaboatão dos Guararapes', 'Paulista', 'Camaragibe', 'São Lourenço da Mata', 'Abreu e Lima', 'Igarassu', 'Cabo de Santo Agostinho']
    return 'Metropolitana' if cidade in metropolitana_cidades else 'Interior'

df = pd.DataFrame()
for ano in range(2021, 2024):
    url = f"http://dados.recife.pe.gov.br/dataset/perfil-das-pessoas-vacinadas-covid-19/resource/99b42b09-95af-47de-8411-ab99c380c3ef{2021}"
    df_ano = pd.read_csv('http://dados.recife.pe.gov.br/dataset/perfil-das-pessoas-vacinadas-covid-19/resource/99b42b09-95af-47de-8411-ab99c380c3ef', sep=';')
    url = f"http://dados.recife.pe.gov.br/dataset/perfil-das-pessoas-vacinadas-covid-19/resource/9664de94-9f07-4adc-848d-b6ef56510762?inner_span=True{2022}"
    df_ano = pd.read_csv('http://dados.recife.pe.gov.br/dataset/perfil-das-pessoas-vacinadas-covid-19/resource/9664de94-9f07-4adc-848d-b6ef56510762?inner_span=True', sep=';')
    url = f"http://dados.recife.pe.gov.br/dataset/perfil-das-pessoas-vacinadas-covid-19/resource/ca7fb968-3a2c-44ff-a2e8-730d1a689407?inner_span=True{2023}"
    df_ano = pd.read_csv('http://dados.recife.pe.gov.br/dataset/perfil-das-pessoas-vacinadas-covid-19/resource/ca7fb968-3a2c-44ff-a2e8-730d1a689407?inner_span=True', sep=';')
    df = pd.concat([df, df_ano])

numero_total_vacinadas = len(df)

cidade_mais_doses_coronavac = df[df['Vacina_fabricante'] == 'CORONAVAC - SINOVAC (BUTANTAN)']['Cidade'].value_counts().idxmax()

df['tipo_faixa_etaria'] = df['Idade'].apply(define_tipo_faixa_etaria)

df['região'] = df['Cidade'].apply(define_regiao)

contagem_por_regiao_faixa_etaria = df.groupby(['região', 'tipo_faixa_etaria'])['Nome'].count()

idade_media_por_regiao_faixa_etaria = df.groupby(['região', 'tipo_faixa_etaria'])['Idade'].mean()

vacina_mais_administrada_por_regiao_faixa_etaria = df.groupby(['região', 'tipo_faixa_etaria'])['Vacina_fabricante'].agg(lambda x: x.value_counts().idxmax())

proporcao_genero = df.groupby(['região', 'tipo_faixa_etaria', 'Sexo'])['Nome'].count() / df.groupby(['região', 'tipo_faixa_etaria'])['Nome'].count()

print("1. Número total de pessoas vacinadas:", numero_total_vacinadas)
print("2. Cidade com mais doses da vacina CORONAVAC:", cidade_mais_doses_coronavac)
print("\n5. Quantidade de pessoas vacinadas por região e tipo de faixa etária:")
print(contagem_por_regiao_faixa_etaria)
print("\n6. Idade média das pessoas vacinadas por região e tipo de faixa etária:")
print(idade_media_por_regiao_faixa_etaria)
print("\n7. Tipo de vacina mais administrada por região e tipo de faixa etária:")
print(vacina_mais_administrada_por_regiao_faixa_etaria)
print("\n8. Proporção de homens e mulheres vacinados por região e tipo de faixa etária:")
print(proporcao_genero)