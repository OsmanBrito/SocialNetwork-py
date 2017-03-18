def insertAccount():
    Conta = []

    Conta.append(raw_input("Nome: "))
    Conta.append(raw_input("Status de relacionamento: "))
    Conta.append(raw_input("Telefone: "))
    Conta.append(raw_input("Email: "))
    Conta.append(raw_input("Data de Nascimento: "))
    Conta.append(raw_input("Estado onde esta morando: "))

    return Conta


def createMatrix(Matrix, Relationship):
    Grafo = []
    for i in range(0, len(Matrix)):
        listaAux = []
        for j in range(0, len(Matrix)):
            listaAux.append(0)
        Grafo.append(listaAux)
    # orderList(Ligacoes, Grafo)

    for k in range(len(Relationship)):
        # print("epa", Ligacoes[k], Ligacoes[k][0], Ligacoes[k][1], Ligacoes[k][2])
        matrix = verCaminho(Grafo, Relationship[k][0], Relationship[k][1], Relationship[k][2])

    return Grafo, matrix


def verCaminho(matrix, sai, chega, Relationship):
    for i in range(sai, len(matrix)):
        for j in range(0, len(matrix)):
            if matrix[sai][j] == 0 and j == chega:
                matrix[sai][chega] = Relationship
                matrix[chega][sai] = Relationship

    return matrix


def profundidade(atual, visits, ForkFriend, listAux):
    visits[int(atual)] = True
    listAux.append(atual)  # retorna a lista de caminhos percorridos
    for i in range(len(ForkFriend) - 2):
        if ForkFriend[int(atual)][int(i)] != 0 and not visits[int(i)]:
            profundidade(i, visits, ForkFriend, listAux)

def SugestFriend(codig, forkRel):
    Friends = []
    for i in range(0, len(forkRel)):
        if forkRel[codig][i] != 0:
         Friends.append(i)
    return Friends

def getGroup(s, matrizAmizades, listaI):
    listaSujestao = []
    for i in range(0, len(listaI)):
        if matrizAmizades[s][listaI[i]] != 0:
            listaSujestao.append(listaI[i])
    return listaSujestao

def AddRelation(One, Two, Type, matrix):
    matrix[One][Two] = Type
    matrix[Two][One] = Type

def FillFork(nFork, Fork):
    Vector = []
    for i in range(0, nFork):
        Vector.append(0)
        if (i < len(Fork)):
            Fork[i].append(0)
    Fork.append(Vector)
    return Fork

def sujestFriendShip(firstCodig, matrizamizades, friendShip, codAnalist):
    Friends = []
    for i in range(0, len(matrizamizades)):
        if matrizamizades[codAnalist][i] != 0 and i != firstCodig:
            aux = 0
            for j in range(0, len(friendShip)):
                if i == friendShip[j]:
                    aux += 1
            if aux == 0:
                Friends.append(i)

    return Friends

def deleteUser(matrixUs, fork, user):
    del matrixUs[user]
    del fork[user]
    for i in range(0,len(fork)):
        del fork[i][user]



def dashboard(matrizDeLigacoes, matrixPerson):
    # name, Status, phone, email, birthday, state
    Fork, ForkRelationship = createMatrix(matrixPerson, matrizDeLigacoes)
    Option = 0

    while (Option != 8):

        Option = int(input("1- Cadastrar Usuarios\n2- Fazer Amizades\n3- Sugerir grupos de amigos\n"
                           "4- Sugestao de Amizades\n5- Bloquear Amizade\n6- Excluir conta\n"
                           "7- Pesquisar\n8 -SAIR\nEscolha: "))

        if Option == 1:
            print("Inserir Usuario")

            Perfil = insertAccount()

            matrixPerson.append(Perfil)
            ForkRelationship = FillFork(len(matrixPerson),
                                        Fork)  # Create this because person does not have a relationship anybody

        elif Option == 2:
            for i in range(0, len(matrixPerson)):
                print("Codigo = ", i, " ", matrixPerson[i][0])

            Person1 = input("Qual o codigo da primeira pessoa da amizade. ")
            Person2 = input("Qual o codigo da segunda pessoa da amizade. ")
            Type = input("Qual o tipo de relacionamento<1 - Familia, 2 - Amigos, 3 - Conhecidos>")

            AddRelation(Person1, Person2, Type, ForkRelationship)
            print(matrizDeLigacoes)

        elif Option == 3:
            for i in range(0, len(matrixPerson)):
                print("Codigo = ", i, " ", matrixPerson[i][0])
            GroupPerson = input("Digite o codigo da pessoa que deseja ver solicita")

            visiteds = []
            for aux in range(0, len(ForkRelationship)):
                visiteds.append(0)
            listGroup = []

            profundidade(GroupPerson, visiteds, ForkRelationship, listGroup)
            sujests = getGroup(GroupPerson, ForkRelationship, listGroup)

            if len(sujests) <= 1:
                print("Adicione mais pessoas na conta, ele n tem amigos suficientes para um grupo")
            else:
                sujest = []
                for opa in range(0, len(sujests)):
                    sujest.append(getGroup(sujests[opa], ForkRelationship, sujests))
                print("Gruo sugerido: ")

                epa = len(sujest) - 1
                while epa >= 0:
                    if sujest[epa] != []:
                        print(matrixPerson[int(sujest[epa][0])][0])
                    epa -= 1

        elif Option == 4:

            print("USUARIOS CADASTRADOS:")
            for i in range(0, len(matrixPerson)):
                print("Codigo = ", i, matrixPerson[i][0])

            print("Deseja ver as sujestoes de amizades para qual usuario?")
            cod = int(input("Codigo: "))

            visi = SugestFriend(cod,  ForkRelationship)
            sujestaoAmizades = sujestFriendShip(cod, ForkRelationship, visi, visi[0])

            print("Sujestao amizades: ")
            for i in range(0, len(sujestaoAmizades)):
                print("Codigo:", sujestaoAmizades[i], matrixPerson[sujestaoAmizades[i]][0])

        elif Option == 5:
            print("5")

            print("Bloquear amizade")
            print("USUARIOS CADASTRADOS:")
            for i in range(0, len(matrixPerson)):
                print("Codigo= ", i, matrixPerson[i][0])

            print("Deseja desfazer amizade de quais usuarios? \n digite o codigo dos usuarios.")
            one= int(input("Codigo 1: "))
            two= int(input("Codigo 2: "))

            #Is 'add' but the function does something because of the type
            AddRelation(one, two, 0, ForkRelationship)

        elif Option == 6:
            print("USUARIOS CADASTRADOS:")
            for i in range(0, len(matrixPerson)):
                print("Codigo= ", i, matrixPerson[i][0])

            print("Deseja excluir qual conta de usuario?")
            user = int(input("Codigo : "))
            deleteUser(matrixPerson, ForkRelationship, user)

        elif Option == 7:

            print("EXCLUIR CONTA ")

            print("USUARIOS CADASTRADOS:")
            for i in range(0, len(matrixPerson)):
                print("Codigo= ", i, matrixPerson[i][0])

            print("Digite quem deseja visualizar as relacoes. ")
            cod = int(input("Codigo: "))

            #return list friends
            visi = SugestFriend(cod, ForkRelationship)
            for i in range(0, len(visi)):
                if ForkRelationship[cod][visi[i]] == 1:
                    print(matrixPerson[visi[i]])
                elif ForkRelationship[cod][visi[i]] == 2:
                    print (matrixPerson[visi[i]][0], matrixPerson[visi[i]][1], matrixPerson[visi[i]][3], matrixPerson[visi[i]][4])
                elif ForkRelationship[cod][visi[i]] == 3:
                    print (matrixPerson[visi[i]][0], matrixPerson[visi[i]][3])

        else:
            break
