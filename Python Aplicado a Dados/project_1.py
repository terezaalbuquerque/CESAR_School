class Aluno: 
    def __init__ (self, nome, id, notas):
        self.nome = nome
        self.id = id
        self.notas = notas

alunos = []

def obter_informacoes_aluno():
    nome = input('\nNome do aluno: ')
    id = input('Informe a matrícula do aluno: ')
    notas = input('Informe as notas separadas por espaço: ').split()
    notas = [float(nota) for nota in notas]
    return nome, id, notas

def adicionar_aluno():
    nome, id, notas = obter_informacoes_aluno()
    aluno = Aluno(nome, id, notas)
    alunos.append(aluno)
    print(f'Aluno {nome} registrado com sucesso!')

def encontrar_aluno_por_id(id):
    for aluno in alunos:
        if aluno.id == id:
            return aluno
        return None

def calcular_media_notas():
    if alunos:
        total_notas = sum(sum(aluno.notas) for aluno in alunos)
        total_alunos = len(alunos)
        return total_notas / total_alunos
    return 0

def salvar_registros_em_arquivo(nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        for aluno in alunos:
            arquivo.write(f"{aluno.nome} {aluno.id} {' '.join(map(str, aluno.notas))}\n")
        print(f'Registros salvos em {nome_arquivo}')

def carregar_registros_de_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            alunos.clear()
            for linha in arquivo:
                dados = linha.strip().split()
                nome, matricula, *notas = dados
                alunos.append(Aluno(nome, matricula, [float(nota) for nota in notas]))
            print(f"Registros carregados de {nome_arquivo}")
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} não foi encontrado.")

while True: 
    print('\nOPÇÕES\n')
    print('1. Adicionar aluno')
    print('2. Procurar aluno pelo ID')
    print('3. Calcular a média das notas dos alunos')
    print('4. Salvar registros em um arquivo')
    print('5. Carregar registros de um arquivo')
    print('6. Sair')

    escolha = input('\nSelecione uma opção: ')

    if escolha == '1':
        adicionar_aluno()
    elif escolha == '2':
        id = input('\nInforme o ID do aluno que deseja procurar: ')
        aluno = encontrar_aluno_por_id(id)
        if aluno:
            print(f"Nome: {aluno.nome}")
            print(f'ID: {aluno.id}')
            print(f"Notas: {', '.join(map(str, aluno.notas))}")
        else:
            print('Aluno não encontrado.')
    elif escolha == '3':
        media = calcular_media_notas()
        print(f'A média das notas dos alunos é: {media:.2f}') 

    elif escolha == '4':
        nome_arquivo = input('Informe o nome do arquivo para salvar os registros: ')
        salvar_registros_em_arquivo(nome_arquivo)
    elif escolha == '5':
        nome_arquivo = input('Informe o nome do arquivo para carregar os registros: ')
        carregar_registros_de_arquivo(nome_arquivo)
    elif escolha == '6':
        break
    else: 
        print('Opção inválida. Tente novamente')