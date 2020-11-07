import random

#primeiro todas as maquinas vao tentar comunicar
#vamos ter colisão

#Vamos gerar aleatoriamente Algumas maquinas que vao tentar se comunicar gerar Nmaquinas()
#Gerar numeros de slots para cada uma
#caso os tempos n tenha colisão basta ->trasmite
#caso contrario pega as que se colidirao e sorteia novos valores para elas -> trasmite



def slottedAloha(N):
    maquinasRestantes = N #maqinas que falta enviar
    slots = 500 # pode esprar até mil slots de 51,2u segundos para enviar
    vetorSlots = []
    timePrimeiroEnvio = 1 #começa com um pois tem colisão no primeiro slots de tempo
    timeEnvioTotalMedio = 1 #começa com um pois tem colisão no primeiro slots de tempo

    while( maquinasRestantes > 0 ):

        #Criando o n slots para cada um enviar
        for i in range(maquinasRestantes):
            vetorSlots.append(random.randint(1,slots))

        #ordena o vetor crescente
        vetorSlots.sort()

        print(vetorSlots)

        #verifica se tem colisao (tempos iguais)
        if len(set(vetorSlots)) == len(vetorSlots):
            somaslots = 0
            for i in range(len(vetorSlots)):
                timeEnvioTotalMedio +=vetorSlots[i] #sem repetição
            maquinasRestantes = 0
            timePrimeiroEnvio = vetorSlots[0]
        else:
            # v = [1,1,1,2,3,4]
            vetorAux = []
            count = 0  #tem maquinas com slots repetidos
            for i in range(len(vetorSlots)):
                for j in range(len(vetorSlots)):
                    if (vetorSlots[i] != vetorSlots[j + i]):
                        vetorAux.append = i #armazena a posição nos indices de slots que n se tem colisão
                        timeEnvioTotalMedio +=vetorSlots[i] #faz o somatorio do tempo dos slots sem colisão


            if(maquinasRestantes == N): #
                for i in range(len(vetorSlots)):
                    if(vetorAux[0] == i):
                        print(vetorSlots)
                        timePrimeiroEnvio += vetorSlots[i]

            else:
                maquinasRestantes = N - len(vetorAux)

    vetorResultado = [timePrimeiroEnvio*51.2,timeEnvioTotalMedio*51.2]
    return vetorResultado



if __name__ == '__main__':
    N = 20 #Numero de estamos que vamo tentar transmitir
    print(slottedAloha(N))
