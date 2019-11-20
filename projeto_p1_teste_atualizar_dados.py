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


def criptografar(dado):

    arq = open('chavePublica.txt', 'r')
    e = int(tiraBarraEne(arq.readline()))
    n = int(arq.readline())
    arq.close()
    resultado = ''
    for char in dado:
        resultado+= str(ord(char)**e%n)+ ' '

    return resultado

def descriptografar(dado):

    arq = open('chavePublica.txt', 'r')
    d = int(tiraBarraEne(arq.readline()))
    n = int(arq.readline())
    arq.close()
    result = ''
    for numero in dado.split():
        result += chr(int(numero)**d%n)

    return result



def pInicial():
    from sys import exit
    cont = True
    while cont:
        print("-="*25)
        print(
            "->" * 20 + "\nOlá, seja bem vindo ao nosso fórum. Aqui você encontra diversos médicos especialistas em diversas regiões.\n" + "<-" * 20)
        print("-="*25)
        print("\n[ 1 ]- Cadastro paciente")
        print("-="*25)
        print("\n[ 2 ]- Cadastro médico")
        print("-="*25)
        print("\n[ 3 ]- Consulta número de pontos")
        print("-="*25)
        print("\n[ 4 ]- Login Paciente")
        print("-="*25)
        print("\n[ 5 ]- Login Médico")
        print("-="*25)
        print("\n[ 6 ]- Sair")
        print("-="*25)

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
            salvarArquivoMedico(dicMedico)
            salvarArquivoPaciente(dicPaciente)
            cont = False
            


def cdtPaciente():
    print("->" * 20 + "\nSeja bem vindo a área para cadastro de pacientes\n" + "<-" * 20)
    nomePaciente = input("\nPrimeiramente, digite seu nome: ")
    cpfPaciente = input("\nDigite seu cpf: ")
    endPaciente = input("\nDigite seu endereço: ")
    senhaPaciente = input("\nDigite sua senha para login: ")
    dataCadastro = dataHora()
    dataModificacao = "-"
    salvarPaciente(nomePaciente, cpfPaciente, endPaciente, senhaPaciente, dataCadastro, dataModificacao)
    escolhaLoginPaciente()

def salvarPaciente(nomePaciente, cpfPaciente, endPaciente, senhaPaciente, dataCadastro, dataModificacao):
    tuplaPaciente = (nomePaciente, endPaciente, senhaPaciente, dataCadastro, dataModificacao)
    chavePaciente = cpfPaciente
    dicPaciente[chavePaciente] = tuplaPaciente
    print(dicPaciente)



def salvarArquivoPaciente(dicPaciente):
    arq = open('paciente.txt','w')
    listConteudo = list(dicPaciente.values())
    cont = 0
    for codigo in dicPaciente:
        arq.write(criptografar(str(codigo)))
        arq.write('\n')
        arq.write(criptografar(str(listConteudo[cont][0])))
        arq.write('\n')
        arq.write(criptografar(str(listConteudo[cont][1])))
        arq.write('\n')
        arq.write(criptografar(str(listConteudo[cont][2])))
        arq.write('\n')
        arq.write(criptografar(str(listConteudo[cont][3])))
        arq.write('\n')
        arq.write(criptografar(str(listConteudo[cont][4])))
        arq.write('\n')
        cont+=1
    arq.close()


def carregarPacientes():
    dicPaciente = {}
    with open('paciente.txt', 'r') as arq:
        
        listaArqPaciente = arq.readlines()
        qntPacientes = len(listaArqPaciente)//6
        cont = 0
        while cont < qntPacientes:
            cpfPaciente = descriptografar(tiraBarraEne(listaArqPaciente[6*cont]))
            nomePaciente = descriptografar(tiraBarraEne(listaArqPaciente[6*cont+1]))
            endPaciente = descriptografar(tiraBarraEne(listaArqPaciente[6*cont+2]))
            senhaPaciente = descriptografar(tiraBarraEne(listaArqPaciente[6*cont+3]))
            dataCadastro = descriptografar(tiraBarraEne(listaArqPaciente[6*cont+4]))
            dataMofificacao = descriptografar(tiraBarraEne(listaArqPaciente[6*cont+5]))
            cont+=1
            tuplaPaciente = (nomePaciente, endPaciente, senhaPaciente, dataCadastro, dataModificacao)
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
        cdtPaciente()
    elif resp == 3:
        pInicial()
    else:
        print("\nOpção digitada inválida!")

def cdtMedico():
    cont = True
    while cont:
        print("->"*20 + "\nSeja bem vindo (a) a área para cadastro de médicos\n" + "<-"*20)
        nomeMedico = input("\nPrimeiramente, digite seu nome: ")
        endMedico = input("\nDigite o seu endereço de trabalho(clínicas, hospitais e etc...)")
        espMedico = input("\nAgora, digite a área da sua especialização: ")
        codigoMedico = input("\nDigite o seu código de identificação: (lembre-se, o código de identificação serve para acessar seus dados no sistema)\n")
        senhaMedico = input("\nDigite sua senha: \n")
        dataCadastro = dataHora()
        dataModificacao = "-"
        salvarMedico(nomeMedico, endMedico, espMedico, codigoMedico, senhaMedico, dataCadastro, dataModificacao)
        escolhaLoginMedico()
        cont = False


def escolhaLoginMedico():
    cont = True
    while cont:
        print("\nDeseja entrar no menu de login? (1- sim, 2- continuar no cadastro, 3- página inicial) \n")
        resp = int(input(""))
        if resp == 1:
            menuLoginMedico()
            cont = False
        elif resp == 2:
            cdtMedico()
            cont = False
        elif resp == 3:
            pInicial()
            cont = False
        else:
            print("\nOpção digitada inválida!")


def salvarMedico(nomeMedico, endMedico, espMedico, codigoMedico, senhaMedico, dataCadastro, dataModificacao):
    tuplaMedico = (nomeMedico, endMedico, espMedico, senhaMedico, dataCadastro, dataModificacao)
    chaveMedico = codigoMedico
    dicMedico[chaveMedico] = tuplaMedico
    print(dicMedico)

def salvarArquivoMedico(dicMedico):
    print('salvar',dicMedico)
    arq = open('medicos.txt', 'w')
    listConteudo = list(dicMedico.values())
    cont = 0
    for codigo in dicMedico:
        arq.write(criptografar(str(codigo)))
        arq.write('\n')
        arq.write(criptografar(str(listConteudo[cont][0])))
        arq.write('\n')
        arq.write(criptografar(str(listConteudo[cont][1])))
        arq.write('\n')
        arq.write(criptografar(str(listConteudo[cont][2])))
        arq.write('\n')
        arq.write(criptografar(str(listConteudo[cont][3])))
        arq.write('\n')
        arq.write(criptografar(str(listConteudo[cont][4])))
        arq.write('\n')
        arq.write(criptografar(str(listConteudo[cont][5])))
        arq.write('\n')
        cont+=1
    arq.close()


def carregarMedicos():
    dicMedico = {}
    with open('medicos.txt', 'r') as arq:
        listaArqMedico = arq.readlines()
        qntMedicos = len(listaArqMedico)//7
        cont = 0
        while cont < qntMedicos:
            codigoMedico = descriptografar(tiraBarraEne(listaArqMedico[7*cont]))
            nomeMedico = descriptografar(tiraBarraEne(listaArqMedico[7*cont+1]))
            endMedico = descriptografar(tiraBarraEne(listaArqMedico[7*cont+2]))
            espMedico = descriptografar(tiraBarraEne(listaArqMedico[7*cont+3]))
            senhaMedico = descriptografar(tiraBarraEne(listaArqMedico[7*cont+4]))
            dataCadastro = descriptografar(tiraBarraEne(listaArqMedico[7*cont+5]))
            dataModificacao = descriptografar(tiraBarraEne(listaArqMedico[7*cont+6]))
            cont+=1
            tuplaMedico = (nomeMedico, endMedico, espMedico, senhaMedico, dataCadastro, dataModificacao)
            chaveMedico = codigoMedico
            dicMedico[chaveMedico] = tuplaMedico
    print('arquivo',dicMedico)
    return dicMedico 



def menuLoginMedico():
    cont = True
    opcao = True
    usuario = ''
    while cont:
        print("->"*20+"\nBem vindo a área de login..."+"<-"*20)
        while opcao:
            resp = int(input("\n1- Logar, 2- Sair: \n"))
            if resp == 1:
                idLoginMed = input("\nDigite seu login(o código): \n")
                senhaLoginMed = input("\nDigite sua senha: \n")
                if idLoginMed in dicMedico:
                    if dicMedico[idLoginMed][3] == senhaLoginMed:
                        usuario = dicMedico[idLoginMed][0]
                        print(f"\nBem vindo, {usuario}")
                        menuMedico(usuario, idLoginMed, senhaLoginMed)
                        cont = False
                        opcao = False

                    elif not senhaLoginMed:
                        print("\nA senha não pode estar em branco. Tente novamente")

                    else:
                        print("\nSenha inválida. Tente novamente")

                elif not idLoginMed:
                    print("\nO código não pode estar em branco. Tente novamente")

                else:
                    print("\nCódigo inválido. Tente novamente")

            elif resp == 2:
                salvarArquivoMedico(dicMedico)
                salvarArquivoPaciente(dicPaciente)
                opcao = False
                cont = False

    return usuario


def menuMedico(usuario, idLoginMed, senhaLoginMed):
    codigo = idLoginMed
    senhaMed = senhaLoginMed
    cont = True
    while cont:
        print("-="*25)
        print(f"\nOpções disponíveis")
        print("-="*25)
        print(f"\n[ 1 ]- Atualizar dados")
        print("-="*25)
        print("\n[ 2 ]- Ver feed de comentários")
        print("-="*25)
        print("\n[ 3 ]- Excluir cadastro")
        print("-="*25)
        print("\n[ 4 ]- Sair")
        print("-="*25)
        print("\n[ 5 ]- Página inicial")
        print("-="*25)
        op = int(input("\nEscolha uma opção: \n"))
        print("-="*25)

        if not op:
            print("\nUma opção deve ser digitada")

        elif op == 1:
            atualizarDadosMedico(usuario, codigo, senhaMed)
            cont = False

        elif op == 2:
            feed()
            cont = False

        elif op == 3:
            excluirMedico()
            cont = False

        elif op == 4:
            salvarArquivoMedico(dicMedico)
            salvarArquivoPaciente(dicPaciente)
            cont = False

        elif op == 5:
            cont = False
            pInicial()

        else:
            print("\nOpção digitada incorreta. Tente novamente")
        

def atualizarDadosMedico(usuario, codigo, senhaMed):
    dataCriacao = dicMedico[codigo][5]
    cont = True
    while cont:
        print("->"*20+f"\nOlá, {usuario}, digite as informações que você quer atualizar: ")
        nomeAtualizar = input("\nNovo nome: ")
        endAtualizar = input("\nNovo endereço: ")
        espAtualizar = input("\nNova especialização: ")

        op = int(input("\nDeseja atualizar a senha? 1 - sim, 2- não \n"))

        if op == 1:
            senhaAtualizar = input("\nDigite a nova senha: ")
            senhaRepetir = input("\nRepita a senha: ")
            if senhaAtualizar == senhaRepetir:
                senhaMed = senhaAtualizar
                dataModificacao = dataHora()
                tuplaAtualizarMedico = (nomeAtualizar, endAtualizar, espAtualizar, senhaMed, dataCriacao, dataModificacao)
                dicMedico[codigo] = tuplaAtualizarMedico
                print(dicMedico[codigo])
                print("\nInformações alteradas com sucesso!")
                cont = False

            elif not senhaAtualizar or not senhaRepetir:
                print("\nDigite a senha e repita a senha.")

            else:
                print("\nSenhas não conferem.")

        elif op == 2:
            dataModificacao = dataHora()
            tuplaAtualizarMedico = (nomeAtualizar, endAtualizar, espAtualizar, senhaMed, dataCriacao, dataModificacao)
            dicMedico[codigo] = tuplaAtualizarMedico
            pInicial()
            cont = False

        else:
            print("\nOpção incorreta. Tente novamente")


def excluirMedico():
    cont = True
    while cont:
        print("<-"*20+"\nÁrea para excluir conta."+"->"*20)
        print("\nPara excluir sua conta, confirme seu login\n")
        login = input("\nDigite seu login(código): ")
        senhaLogin = input("\nDigite sua senha: ")

        if login in dicMedico:
            if dicPaciente[login][2] == senhaLogin:
                dicMedico.pop(login)
                print("\nUsuário removido com sucesso!")
                cont = False

            elif dicMedico[login][2] != senhaLogin:
                print("\nSenha incorreta.")

        elif not login in dicMedico:
            print("\nLogin incorreto. Tente novamente")




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
                senhaLoginPaciente = input("Digite sua senha: \n")
                    
                if (idLogin in dicPaciente):
                    if (dicPaciente[idLogin][2] == senhaLoginPaciente):
                        usuario = dicPaciente[idLogin][0]
                        print(f"\nBem vindo, {dicPaciente[idLogin][0]}")
                        menuPaciente(usuario, idLogin, senhaLoginPaciente)
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





def menuPaciente(usuario, idLogin, senhaLoginPaciente):
    cpf = idLogin
    cont = True
    while cont:
        print("-="*25)
        print(f"\nOpções disponíveis: ")
        print("-="*25)
        print("\n[ 1 ]- Atualizar dados")
        print("-="*25)
        print("\n[ 2 ]- Pesquisar médicos")
        print("-="*25)
        print("\n[ 3 ]- Comentar sobre algum médico ")
        print("-="*25)
        print("\n[ 4 ]- Excluir cadastro")
        print("-="*25)
        print("\n[ 5 ]- Menu Inicial")
        print("-="*25)
        print("\n[ 6 ]- Sair")
        print("-="*25)
        op = int(input("\nEscolha uma opção: \n"))
        print("-="*25)

        if not op:
            print("\nDigite uma opção, por favor")

        elif op == 1:
            cont = False
            atualizarDadosPaciente(usuario, cpf, senhaLoginPaciente)

        elif op == 2:
            cont = False
            pesquisarMedico()

        elif op == 3:
            cont = False
            comentar()

        elif op == 4:
            cont = False
            excluirPaciente()

        elif op == 5:
            pInicial()
            cont = False

        elif op == 6:
            cont = False

        else:
            print("\nOpção digitada incorreta. Tente novamente!")
            
        
def atualizarDadosPaciente(usuario, cpf, senhaLoginPaciente):
    dataCriacao = dicPaciente[cpf][3]
    cont = True
    while cont:
        print("->" * 20 + f"\nOlá, {usuario}, digite as informações que você quer atualizar: ")
        nomeAtualizar = input("\nNovo nome: ")
        endAtualizar = input("\nNovo endereço: ")
        op = int(input("\nDeseja atualizar a senha? 1 - sim, 2- não \n"))
        if op == 1:
            senhaAtualizar = input("\nDigite a nova senha: ")
            senhaRepetir = input("\nRepita a senha: ")
            if senhaAtualizar == senhaRepetir:
                dataModificacao = dataHora()
                senhaLoginPaciente = senhaAtualizar
                tuplaAtualizarPaciente = (nomeAtualizar, endAtualizar, senhaLoginPaciente, dataCriacao, dataModificacao)
                dicPaciente[cpf] = tuplaAtualizarPaciente
                print(dicPaciente[cpf])
                print("\nInformações alteradas com sucesso!")
                menuPaciente()
                cont = False

            elif not senhaAtualizar or not senhaRepetir:
                print("\nDigite a senha e repita a senha.")

            else:
                print("\nSenhas não conferem.")

        elif op == 2:
            dataModificacao = dataHora()
            tuplaAtualizarPaciente = (nomeAtualizar, endAtualizar, senhaLoginPaciente, dataCriacao, dataModificacao)
            dicPaciente[cpf] = tuplaAtualizarPaciente
            print(dicPaciente)
            pInicial()
            cont = False

        else:
            print("\nOpção incorreta. Tente novamente")


def comentar(usuario):
    cont = True
    while cont:
        codigoMedicoComentario = input("\nDigite o nome do médico sobre o qual você deseja deixar um comentário: ")
        cidadeMedicoComentario = input("\nDigite a cidade de atendimento desse médico: ")
        comentarioMedico = input("\nDigite o seu comentário: ")

        salvarComentarioMedico(codigoMedicoComentario, cidadeMedicoComentario, comentarioMedico)
        cont = False


def excluirPaciente():
    cont = True
    while cont:
        print("<-"*20+"\nÁrea para excluir conta."+"->"*20)
        print("\nPara excluir sua conta, confirme seu login\n")
        login = input("\nDigite seu login(cpf): ")
        senhaLogin = input("\nDigite sua senha: ")

        if login in dicPaciente:
            if dicPaciente[login][2] == senhaLogin:
                dicPaciente.pop(login)
                print("\nUsuário removido com sucesso!")
                cont = False

            elif dicPaciente[login][2] != senhaLogin:
                print("\nSenha incorreta.")

        elif not login in dicPaciente:
            print("\nLogin incorreto. Tente novamente")


        
    



def pesquisarMedico():
    cont = True
    listaPesquisarMedico = list(dicMedico.values())
    while cont:
        nomePesquisar = input("\nDigite o nome do médico que está procurando: ")
        if nomePesquisar in dicMedico:
            print(f"\nO médico {nomePesquisar} está cadastrado no sistema")
            resp = int(input("\nDeseja visualizar as informações do médico cadastrado(1- sim, 2- não)? "))
            if resp == 1:
                print(listaPesquisarMedico[nomePesquisar])
                op = input("\nDeseja voltar para o menu(1- Sim, 2- Não)? ")
                if op == 1:
                    cont = False

                elif op == 2:
                    pass

                else:
                    print("\nOpção digitada incorreta. Tente novamente")

            elif resp == 2:
                cont = False

        elif not nomePesquisar in dicMedico:
            print("\nNome do médico digitado não está cadastrado no sistema.")




def salvarComentarioMedico(codigo, cidade, comentario):
    tuplaComentarioMedico = (cidade, comentario)
    dicComentario[codigo] = tuplaComentarioMedico


def salvarComentarioArquivoMedico(dicComentario):
    arq = open('comentario.txt', 'a')
    listaConteudo = list(dicComentario.values())
    cont = 0
    for codigo in dicComentario:
        arq.write(str(codigo))
        arq.write('\n')
        arq.write(str(listaConteudo[cont][0]))
        arq.write('\n')
        arq.write(str(listaConteudo[cont][1]))
        arq.write('\n')
        cont+=1

    arq.close()


def carregarComentario():
    dicComentario = {}
    with open('comentario.txt','r') as arq:
        listaComentario = arq.readlines()
        qntComentario = len(listaComentario)//3
        cont = 0
        while cont < qntComentario:
            codigoMedicoComentario = tiraBarraEne(listaComentario[3*cont])
            cidadeMedicoComentario = tiraBarraEne(listaComentario[3*cont+1])
            comentarioMedico = tiraBarraEne(listaComentario[3*cont+2])
            cont+=1
            tuplaComentarioMedico = (cidadeMedicoComentario, comentarioMedico)
            dicComentario[codigoMedicoComentario] = tuplaComentarioMedico

        return dicComentario


dicComentario = {}
dicMedico = carregarMedicos()   
dicPaciente = carregarPacientes()
 
pInicial()
