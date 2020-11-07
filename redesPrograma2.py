import random

#primeiro todas as maquinas vao tentar comunicar
#vamos ter colisão

#Vamos gerar aleatoriamente Algumas maquinas que vao tentar se comunicar gerar Nmaquinas()
#Gerar numeros de slots para cada uma
#caso os tempos n tenha colisão basta ->trasmite
#caso contrario pega as que se colidirao e sorteia novos valores para elas -> trasmite



def slottedAloha(N):
    maquinasRestantes = N #maqinas que falta enviar
    slots = 10 # pode esprar até mil slots de 51,2u segundos para enviar
    timePrimeiroEnvio = 1 #começa com um pois tem colisão no primeiro slots de tempo
    timeEnvioTotalMedio = 1 #começa com um pois tem colisão no primeiro slots de tempo
    teste = 0

    while( maquinasRestantes > 0 ):

        #Criando o n slots para cada um enviar
        print('maquinas restantes:',maquinasRestantes)
        vetorSlots = []
        for i in range(maquinasRestantes):
            vetorSlots.append(random.randint(1,slots))

        #ordena o vetor crescente
        vetorSlots.sort()
        print(vetorSlots)

        #verifica se tem colisao (tempos iguais)
        if len(set(vetorSlots)) == len(vetorSlots):
            if(maquinasRestantes == N):
                timePrimeiroEnvio = vetorSlots[0]
            maquinasRestantes = 0
            for i in range(len(vetorSlots)):
                timeEnvioTotalMedio +=vetorSlots[i] #sem repetição
        else:
            vetorAux = []
            count = 0  #tem maquinas com slots repetidos
            for i in range(len(vetorSlots)):
                for j in range(len(vetorSlots)):
                    if ((vetorSlots[i]) == (vetorSlots[j])):
                        count +=1

                if (count == 1):
                    vetorAux.append(i) #armazena a posição nos indices de slots que n se tem colisão
                    timeEnvioTotalMedio +=vetorSlots[i] #faz o somatorio do tempo dos slots sem colisão
                count = 0
            print('posicao a enviar: ',vetorAux)
            if(maquinasRestantes == N and len(vetorAux) != 0):
                for i in range(len(vetorSlots)):
                    if(vetorAux[0] == i):
                        timePrimeiroEnvio += vetorSlots[i]

            maquinasRestantes = maquinasRestantes - len(vetorAux)


    vetorResultado = [timePrimeiroEnvio*51.2,timeEnvioTotalMedio*51.2]
    return vetorResultado



if __name__ == '__main__':
    N = 10 #Numero de estamos que vamo tentar transmitir
    vertorResultado = slottedAloha(N)
    print('**********Saida**********')
    print(vertorResultado)
    print('Tempo primeiro envio: ',vertorResultado[0],'microssegundos')
    print('Tempo medio total: ',(vertorResultado[1])/(N),'microssegundos')
