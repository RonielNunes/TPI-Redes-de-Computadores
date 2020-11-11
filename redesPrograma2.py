import random
import statistics

#primeiro todas as maquinas vao tentar comunicar
#vamos ter colisão

#Vamos gerar aleatoriamente Algumas maquinas que vao tentar se comunicar gerar Nmaquinas()
#Gerar numeros de slots para cada uma
#caso os tempos n tenha colisão basta ->trasmite
#caso contrario pega as que se colidirao e sorteia novos valores para elas -> trasmite



def slottedAloha(N):
    maquinasRestantes = N #maqinas que falta enviar
    slots = 100 # pode esprar até mil slots de 51,2u segundos para enviar
    timePrimeiroEnvio = 1 #começa com um pois tem colisão no primeiro slots de tempo
    timeEnvioTotalMedio = 1 #começa com um pois tem colisão no primeiro slots de tempo
    teste = 0

    while( maquinasRestantes > 0 ):

        #Criando o n slots para cada um enviar
        #print('maquinas restantes:',maquinasRestantes)
        vetorSlots = []
        for i in range(maquinasRestantes):
            vetorSlots.append(random.randint(1,slots))

        #ordena o vetor crescente
        vetorSlots.sort()
        #print(vetorSlots)

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
            #print('posicao a enviar: ',vetorAux)
            if(maquinasRestantes == N and len(vetorAux) != 0):
                for i in range(len(vetorSlots)):
                    if(vetorAux[0] == i):
                        timePrimeiroEnvio += vetorSlots[i]

            maquinasRestantes = maquinasRestantes - len(vetorAux)



    vetorResultado = [timePrimeiroEnvio*51.2,timeEnvioTotalMedio*51.2]
    print('aloha')
    return vetorResultado

def csma(N):
    #Considerando que houve colisão, o csma calculará um tempo de espera para todas as maquinas.
    totalElementos = N
    slots = 100
    timeEnvioTotalMedio = 0
    timePrimeiroEnvio = 0
    vetorResultado = []

    while (totalElementos > 0):
        vetorSlots = []
        for i in range(totalElementos):
            vetorSlots.append(random.randint(1,slots))
        vetorSlots.sort()
        #print(vetorSlots)
        #verifica se o canal tá ocupado
        #caso que n tá ocupado
        if len(set(vetorSlots)) == len(vetorSlots):
            for i in range(len(vetorSlots)):
                timeEnvioTotalMedio +=vetorSlots[i]
            if (len(vetorSlots) == N):
                timePrimeiroEnvio = vetorSlots[0]
                break
            totalElementos = 0
        else:#ta ocupado
            #Quais que estão ocupados
            vetorPosica = []
            for i in range(totalElementos):
                count = 0
                for j in range(totalElementos):
                    if (vetorSlots[i] == vetorSlots[j]):
                        count +=1
                if count > 1:
                    vetorPosica.append(i) #guarda a posicao dos elementos que devem ser sorteados novamnete
                else:
                    if (len(vetorSlots) == N):
                        timePrimeiroEnvio = vetorSlots[0]
                    timeEnvioTotalMedio +=vetorSlots[i]


            totalElementos -= (len(vetorSlots) - len(vetorPosica))
            #passa que tem tempo diferente

    #print('valor:',totalElementos)

    vetorResultado.append(timePrimeiroEnvio*51.2)
    vetorResultado.append(timeEnvioTotalMedio*51.2)
    print('csma')
    return vetorResultado

def backoff(N): #limite de tentativas
    i = 1 #formula (0,2^i - 1)
    timeEnvioTotalMedio = 0
    timePrimeiroEnvio = 0
    estacoes = N
    slots = 100
    vetorResultado = []
    while(estacoes > 0 and i < 16):
        vetorSlots = []

        for i in range(estacoes):
            vetorSlots.append(random.randint(0,slots))
        vetorSlots.sort()
        #print(vetorSlots)
        #verificando se tivemos colisao entre as estações
        if len(set(vetorSlots)) == len(vetorSlots):
            for i in range(len(vetorSlots)):
                timeEnvioTotalMedio +=vetorSlots[i]
            if (len(vetorSlots) == N):
                timePrimeiroEnvio = vetorSlots[0]
                break
            estacoes = 0
        else:
            #tivemos colisao
            vetorPosica = []

            #indentifica quias estações se colidiram
            for i in range(estacoes):
                count = 0
                for j in range(estacoes):
                    if (vetorSlots[i] == vetorSlots[j]):
                        count +=1
                if count > 1:
                    vetorPosica.append(i) #guarda a posição de colisão
                else:
                    if (len(vetorSlots) == N):
                        timePrimeiroEnvio = vetorSlots[0] #guarda o primeiro tempo da estação que enviou
                    timeEnvioTotalMedio +=vetorSlots[i]   #guarda o tempo das estações que eviamos

                estacoes -= (len(vetorSlots) - len(vetorPosica))
                slots = (2**i) - 1
                i +=1

    if (i == 16):
        print("tempo maximo atigindo")
        return 0
    else:
        vetorResultado.append(timePrimeiroEnvio*51.2)
        vetorResultado.append(timeEnvioTotalMedio*51.2)
        print('backoff')
        return  vetorResultado


if __name__ == '__main__':
    N = 20 #Numero de estamos que vamo tentar transmitir
    print("Numero de estacoes(N):",N)


    vetorAlohaPrimeiro = []
    vetorAlohaTotal = []

    vetorCsmaPrimeiro = []
    vetorCsmaTotal = []

    vetorBackoffPrimeiro = []
    vetorBackoffTotal = []

    for i in range(33):
        print(i)
        vetorAlohaResultado = slottedAloha(N)
        vetorAlohaPrimeiro.append(vetorAlohaResultado[0])
        vetorAlohaTotal.append(vetorAlohaResultado[1])

        vetorCsmaResultado = csma(N)
        vetorCsmaPrimeiro.append(vetorCsmaResultado[0])
        vetorCsmaTotal.append(vetorCsmaResultado[1])

        vetorBackoffResultado = backoff(N)
        vetorBackoffPrimeiro.append(vetorBackoffResultado[0])
        vetorBackoffTotal.append(vetorBackoffResultado[1])


    print("ALOHA")
    print(statistics.mean(vetorAlohaPrimeiro))
    print(statistics.mean(vetorAlohaTotal))


    print("CSMA")
    print(statistics.mean(vetorCsmaPrimeiro))
    print(statistics.mean(vetorCsmaTotal))

    print("BACKOFF")
    print(statistics.mean(vetorBackoffPrimeiro))
    print(statistics.mean(vetorBackoffTotal))
