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


def cdtMedico():
    print("->"*20 + "\nSeja bem vindo (a) a área para cadastro de médicos\n" + "<-"*20)
    nomeMedico = input("\nPrimeiramente, digite seu nome: ")
    endMedico = input("\nDigite o seu endereço de trabalho(clínicas, hospitais e etc...)")
    espMedico = input("\nAgora, digite a área da sua especialização: ")
    codigoMedico = input("\nDigite o seu código de identificação: (lembre-se, o código de identificação serve para acessar seus dados no sistema)\n")
    senhaMedico = input("\nDigite sua senha: \n")

    salvarMedico(nomeMedico, endMedico, espMedico, codigoMedico)
    escolhaLogin()


def escolhaLogin():
    print("\nDeseja entrar no menu de login? (1- sim, 2- não) \n")
    resp = int(input(""))
    if resp == 1:
        menuLogin()
    elif resp == 2:
        pInicial()
    else:
        print("\nOpção digitada incorreta.")
    pass


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




def cnsPontos ():
    print("\nBem vindo a área para consulta de planos!")



pInicial()