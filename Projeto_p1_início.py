def tiraBarraEne(string):
    novaString = ''
    for caractere in string:
        if caractere != '\n':
            novaString += caractere

    return novaString

def dataHora():
    from datetime import datetime
    dataHora = datetime.now()
    dataHora = dataHora.strftime("%d/%m/%y %H:%M")

    return dataHora


def pInicial():
    from sys import exit
    print(
        "->" * 20 + "\nOlá, seja bem vindo ao nosso fórum. Aqui você encontra diversos médicos especialistas em diversas regiões.\n" + "<-" * 20)
    print("1- Cadastro paciente")
    print("2- Cadastro médico")
    print("3- Consulta número de pontos")
    print("4- Sair")

    try:
        op = int(input("\nEscolha a opção desejada: "))

        if op == 1:
            cdtPaciente()

        if op == 2:
            cdtMedico()

        if op == 3:
            cnsPontos()

        if op == 4:
            sys.exit()

    except:
        print("\nOpção digitada incorreta! Tente novamente...")


def cdtPaciente():
    print("->" * 20 + "\nSeja bem vindo a área para cadastro de pacientes\n" + "<-" * 20)
    nomePaciente = input("\nPrimeiramente, digite seu nome: ")
    cpfPaciente = input("\nDigite seu cpf: ")
    endPaciente = input("\nDigite seu endereço: ")
    senhaPaciente = input("\nDigite sua senha para login: ")

    salvarPaciente(nomePaciente, cpfPaciente, endPaciente)
    escolhaLoginPaciente()

def salvarPaciente(nome, cpf, end):
    tuplaPaciente = (nomePaciente, endPaciente)
    dic = {}
    chavePaciente = cpfPaciente
    dic[chavePaciente] = tuplaPaciente
    print(dic)
    salvarArquivoPaciente(dic)


def salvarArquivoPaciente():
    with open('paciente.txt','w') as arq:
        listaConteudo = list(dic.values())
        cont = 0
        for codigo in dic:
            arq.write(str(codigo))
            arq.write('\n')
            arq.write(str(listConteudo[cont][0]))
            arq.write('\n')
            arq.write(str(listConteudo[cont][1]))
            arq.write('\n')
            cont+=1



def escolhaLoginPaciente():
    print("\nDeseja entrar no menu de login? (1- sim, 2- continuar no cadastro, 3- página inicial) \n")
    resp = int(input(""))
    if resp == 1:
        menuLogin()
    elif resp == 2:
        pInicial()
    elif resp == 3:
        cdtPaciente()
    else:
        print("\nOpção digitada inválida!")

def cdtMedico():
    print("->"*20 + "\nSeja bem vindo (a) a área para cadastro de médicos\n" + "<-"*20)
    nomeMedico = input("\nPrimeiramente, digite seu nome: ")
    endMedico = input("\nDigite o seu endereço de trabalho(clínicas, hospitais e etc...)")
    espMedico = input("\nAgora, digite a área da sua especialização: ")
    codigoMedico = input("\nDigite o seu código de identificação: (lembre-se, o código de identificação serve para acessar seus dados no sistema)\n")
    senhaMedico = input("\nDigite sua senha: \n")

    salvarMedico(nomeMedico, endMedico, espMedico, codigoMedico)
    escolhaLoginMedico()


def escolhaLoginMedico():
    print("\nDeseja entrar no menu de login? (1- sim, 2- continuar no cadastro, 3- página inicial) \n")
    resp = int(input(""))
    if resp == 1:
        menuLogin()
    elif resp == 2:
        pInicial()
    elif resp == 3:
        cdtMedico()
    else:
        print("\nOpção digitada inválida!")


def salvarMedico(nomeMedico, endMedico, espMedico, codigoMedico):
    tuplaMedico = (nomeMedico, endMedico, espMedico)
    dic = {}
    chaveMedico = codigoMedico
    dic[chaveMedico] = tuplaMedico
    print(dic)
    salvarArquivoMedico(dic)

def salvarArquivoMedico(dic):
    with open('medicos.txt', 'w') as arq:
        listConteudo = list(dic.values())
        cont = 0
        for codigo in dic:
            arq.write(str(codigo))
            arq.write('\n')
            arq.write(str(listConteudo[cont][0]))
            arq.write('\n')
            arq.write(str(listConteudo[cont][1]))
            arq.write('\n')
            arq.write(str(listConteudo[cont][2]))
            arq.write('\n')
            cont+=1



def carregarMedicos():
    dicMedico = {}
    with open('medicos.txt', 'r') as arq:
        listaArqMedico = arq.readlines()
        qntMedicos = len(listaArqMedico)//4
        cont = 0
        while cont < qntMedicos:
            codigoMedico = tiraBarraEne(listaArqMedico[4*cont])
            nomeMedico = tiraBarraEne(listaArqMedico[4*cont+1])
            endMedico = tiraBarraEne(listaArqMedico[4*cont+2])
            espMedico = tiraBarraEne(listaArqMedico[4*cont+3])
            cont+=1
            tuplaMedico = (nomeMedico, endMedico, espMedico)
            chaveMedico = codigoMedico
            dicMedico[chaveMedico] = tuplaMedico

    return dicMedico 



def cnsPontos ():
    print("\nBem vindo a área para consulta de planos!")

 
pInicial()
