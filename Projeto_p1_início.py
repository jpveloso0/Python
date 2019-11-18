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
            menuLoginPaciente()
                

        elif op == 5:
            cont = False
            menuLoginMedico()
                

        elif op == 6:
            cont = False
            


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
    arq = open('paciente.txt','a')
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
    arq.close()


def carregarPacientes():
    dicPaciente = {}
    with open('paciente.txt', 'r') as arq:
        
        listaArqPaciente = arq.readlines()
        qntPacientes = len(listaArqPaciente)//4
        cont = 0
        while cont < qntPacientes:
            cpfPaciente = tiraBarraEne(listaArqPaciente[4*cont])
            nomePaciente = tiraBarraEne(listaArqPaciente[4*cont+1])
            endPaciente = tiraBarraEne(listaArqPaciente[4*cont+2])
            senhaPaciente = tiraBarraEne(listaArqPaciente[4*cont+3])
            cont+=1
            tuplaPaciente = (nomePaciente, endPaciente, senhaPaciente)
            chavePaciente = cpfPaciente
            dicPaciente[chavePaciente] = tuplaPaciente
    print(listaArqPaciente)
    print(dicPaciente)
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
    arq = open('medicos.txt', 'a')
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
        arq.write(str(listConteudo[cont][3]))
        arq.write('\n')
        cont+=1
    arq.close()


def carregarMedicos():
    dicMedico = {}
    with open('medicos.txt', 'r') as arq:
        listaArqMedico = arq.readlines()
        qntMedicos = len(listaArqMedico)//5
        cont = 0
        while cont < qntMedicos:
            codigoMedico = tiraBarraEne(listaArqMedico[4*cont])
            nomeMedico = tiraBarraEne(listaArqMedico[4*cont+1])
            endMedico = tiraBarraEne(listaArqMedico[4*cont+2])
            espMedico = tiraBarraEne(listaArqMedico[4*cont+3])
            senhaMedico = tiraBarraEne(listaArqMedico[4*cont+4])
            cont+=1
            tuplaMedico = (nomeMedico, endMedico, espMedico, senhaMedico)
            chaveMedico = codigoMedico
            dicMedico[chaveMedico] = tuplaMedico

    return dicMedico 



def menuLoginMedico():
    cont = True
    usuario = ''
    while cont:
        print("->"*20+"\nBem vindo a área de login..."+"<-"*20)
        opcao = True
        cont = False
        while opcao:
            resp = int(input("\n1- Logar, 2- Sair: \n"))
            if resp == 1:
                idLoginMed = input("\nDigite seu login(o código): \n")
                senhaLoginMed = input("\nDigite sua senha: \n")
                if idLoginMed in dicMedico:
                    if dicMedico[idLoginMed][3] == senhaLoginMed:
                        usuario = dicMedico[idLoginMed][0]
                        print(f"\nBem vindo, {usuario}")
                        menuMedico(usuario, idLoginMed)

                    elif not senhaLoginMed:
                        print("\nA senha não pode estar em branco. Tente novamente")

                    else:
                        print("\nSenha inválida. Tente novamente")

                elif not idLoginMed:
                    print("\nO código não pode estar em branco. Tente novamente")

                else:
                    print("\nCódigo inválido. Tente novamente")

            elif resp == 2:
                opcao = False

    return usuario


def menuMedico(usuario, idLoginMed):
    codigo = idLoginMed
    cont = True
    while cont:
        print(f"\nOpções disponíveis, {usuario}")
        print(f"\n1- Atualizar dados")
        print("\n2- Ver feed de comentários")
        print("\n3- Excluir cadastro")
        print("\n4- Sair")
        op = int(input("\nEscolha uma opção: \n"))

        if not op:
            print("\nUma opção deve ser digitada")

        elif op == 1:
            atualizarDadosMedico()
            cont = False

        elif op == 2:
            feed()
            cont = False

        elif op == 3:
            excluirMedico()

        elif op == 4:
            cont = False

        else:
            print("\nOpção digitada incorreta. Tente novamente")
        


def cnsPontos ():
    print("\nBem vindo a área para consulta de planos!")



def menuLoginPaciente():
    cont = True
    usuario = ''
    while cont:
        print("->"*20+"\nBem vindo a área de login..."+"<-"*20)
        opcao = True
        cont = False
        while opcao:
            resp = int(input("\n1 - logar, 2- sair: \n"))
            if resp == 1:
            
                idLogin = input("\nDigite seu login(CPF): \n")
                senhaLogin = input("Digite sua senha: \n")
                    
                if (idLogin in dicPaciente):
                    if (dicPaciente[idLogin][2] == senhaLogin):
                        usuario = dicPaciente[idLogin][0]
                        print(f"\nBem vindo, {dicPaciente[idLogin][0]}")
                        menuPaciente(usuario, idLogin)
                        opcao = False 

                    elif not senhaLogin:
                        print("\nEspaço de senha digitado em branco. Tente novamente!")

                    else:
                        print("\nSenha inválida. Tente novamente!")

                elif not idLogin:
                    print("\nEspaço para login em branco. Tente novamente!")

                else:
                    print("\nCpf inválido. Tente novamente!")

            elif resp == 2:
                opcao = False
    return usuario

            

def menuPaciente(usuario, idLogin):
    usuario = usuario
    cpf = idLogin
    cont = True
    while cont:
        print(f"\nOpções disponíveis, {usuario}: ")
        print("\n1- Atualizar dados")
        print("\n2- Pesquisar médicos")
        print("\n3- Comentar sobre algum médico ")
        print("\n4- Excluir cadastro")
        print("\n5- Sair")
        op = int(input("\nEscolha uma opção: \n"))

        if not op:
            print("\nDigite uma opção, por favor")

        elif op == 1:
            cont = False
            atualizarDadosPaciente(usuario, cpf)

        elif op == 2:
            cont = False
            pesquisarMedicos()

        elif op == 3:
            cont = False
            comentar()

        elif op == 4:
            cont = False
            excluirPaciente()

        elif op == 5:
            cont = False

        else:
            print("\nOpção digitada incorreta. Tente novamente!")
            
        
    
    












    
dicMedico = carregarMedicos()   
dicPaciente = carregarPacientes()
 
pInicial()
