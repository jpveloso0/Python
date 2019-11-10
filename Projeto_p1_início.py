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
    cont = True
    while cont:
        print(
            "->" * 20 + "\nOlá, seja bem vindo ao nosso fórum. Aqui você encontra diversos médicos especialistas em diversas regiões.\n" + "<-" * 20)
        print("1- Cadastro paciente")
        print("2- Cadastro médico")
        print("3- Consulta número de pontos")
        print("4- Login Paciente")
        print("5- Login Médico")
        print("6- Sair")

        try:
            op = int(input("\nEscolha a opção desejada: "))

            if op == 1:
                cont = False
                cdtPaciente()

            elif op == 2:
                cont = False
                cdtMedico()

            elif op == 3:
                cont = False
                cnsPontos()
                

            elif op == 4:
                cont = False
                menuLoginPaciente(dicPaciente)
                

            elif op == 5:
                cont = False
                menuLoginMedico(dicMedico)
                

            elif op == 6:
                sys.exit()

        except:  
                print("\nOpção digitada incorreta. Tente novamente")


def cdtPaciente():
    print("->" * 20 + "\nSeja bem vindo a área para cadastro de pacientes\n" + "<-" * 20)
    nomePaciente = input("\nPrimeiramente, digite seu nome: ")
    cpfPaciente = input("\nDigite seu cpf: ")
    endPaciente = input("\nDigite seu endereço: ")
    senhaPaciente = input("\nDigite sua senha para login: ")

    salvarPaciente(nomePaciente, cpfPaciente, endPaciente, senhaPaciente)
    escolhaLoginPaciente()

def salvarPaciente(nomePaciente, cpfPaciente, endPaciente, senhaPaciente):
    tuplaPaciente = (nomePaciente, endPaciente, senhaPaciente)
    dic = {}
    chavePaciente = cpfPaciente
    dic[chavePaciente] = tuplaPaciente
    print(dic)
    salvarArquivoPaciente(dic)


def salvarArquivoPaciente(dic):
    with open('paciente.txt','w') as arq:
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


def carregarPacientes():
    dicPaciente = {}
    with open('paciente.txt', 'r') as arq:
        listaArqPaciente = arq.readlines()
        qntPacientes = len(listaArqPaciente)//3
        cont = 0
        while cont < qntPacientes:
            nomePaciente = tiraBarraEne(listaArqPaciente[4*cont])
            endPaciente = tiraBarraEne(listaArqPaciente[4*cont+1])
            cpfPaciente = tiraBarraEne(listaArqPaciente[4*cont+2])
            senhaPaciente = tiraBarraEne(listaArqPaciente[4*cont+3])
            cont+=1
            tuplaPaciente = (nomePaciente, endPaciente, senhaPaciente)
            chavePaciente = cpfPaciente
            dicPaciente[chavePaciente] = tuplaPaciente
    return dicPaciente


def escolhaLoginPaciente():
    print("\nDeseja entrar no menu de login? (1- sim, 2- continuar no cadastro, 3- página inicial)")
    resp = int(input(""))
    if resp == 1:
        menuLoginPaciente(dicPaciente)
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

    salvarMedico(nomeMedico, endMedico, espMedico, codigoMedico, senhaMedico)
    escolhaLoginMedico()


def escolhaLoginMedico():
    print("\nDeseja entrar no menu de login? (1- sim, 2- continuar no cadastro, 3- página inicial) \n")
    resp = int(input(""))
    if resp == 1:
        menuLoginMedico()
    elif resp == 2:
        pInicial()
    elif resp == 3:
        cdtMedico()
    else:
        print("\nOpção digitada inválida!")


def salvarMedico(nomeMedico, endMedico, espMedico, codigoMedico, senhaMedico):
    tuplaMedico = (nomeMedico, endMedico, espMedico, senhaMedico)
    dic = {}
    chaveMedico = codigoMedico
    dic[chaveMedico] = tuplaMedico
    print(dic)
    salvarArquivoMedico(dic)
    return dic

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
            senhaMedico = tiraBarraEne(listaArqMedico[4*cont+4])
            cont+=1
            tuplaMedico = (nomeMedico, endMedico, espMedico)
            chaveMedico = codigoMedico
            dicMedico[chaveMedico] = tuplaMedico

    return dicMedico 



def cnsPontos ():
    print("\nBem vindo a área para consulta de planos!")


def menuLoginPaciente(dicPaciente):
    cont = True
    while cont:
        print("->"*20+"\nBem vindo a área de login..."+"<-"*20)
        idLogin = input("\nDigite seu login(CPF): \n")
        senhaLogin = input("Digite sua senha: \n")

        if idLogin == dicPaciente[cpfPaciente]:
            if senhaLogin == dicPaciente[cpfPaciente][2]:
                print(f"\nBem vindo {dicPaciente[cpf][0]}")
                cont = False

            elif not senhaLogin:
                print("\nCampo digitado em brando. Tente novamente")

            else:
                print("\nLogin não encontrado")
            

        elif not idLogin:
            print("\nCampo digitado em branco. Tente novamente")

        else:
            print("\nLogin não encontrado")

    
    
dicPaciente = carregarPacientes()
 
pInicial()
