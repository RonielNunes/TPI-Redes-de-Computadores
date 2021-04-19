 
<h1 align="center">
  Trabalho prático I Redes de Computadores
</h1>


<h4 align="center">
  🚧  Trabalho prático I Redes de Computadores 🚀CONCLUÍDO  🚧
</h4>

<h1>
   🚀Descrição do Projeto
</h1>
<p>
O trabalho baseou-se na implementação de três cenários de simulação, cada um deles considerando um algoritmo diferente para o
controle de acesso ao meio em uma rede local com N estações compartilhando um mesmo meio de difusão:

-> cenário 1: Slotted ALOHA

-> cenário 2: CSMA p-persistente, com p = 1%

-> cenário 3: algoritmo de recuo binário exponencial
</p>
 
 <h1>
    🎯Sobre
 </h1>
 <p>


Para cada cenário, foi encontrado:
(1) qual foi o tempo médio gasto até que a primeira estação consiga transmitir seus dados no meio de comunicação com sucesso; 
(2) qual foi o tempo médio gasto até que todas as estações tenham conseguido transmitir.


Os cenários definidos acima foram implementados da seguinte maneira:

-> Considere que existam N máquinas compartilhando um mesmo meio de difusão em uma
rede local. As simulações deverão ser realizadas para N=20, N=40, N=100.

-> Sempre que duas ou mais máquinas tentarem realizar transmissões simultâneas em um
mesmo canal de tempo uma colisão ocorrerá.

->  O tempo da simulação será divido em canais de tempo, com duração de 51,2 segundos
cada.

-> Toda colisão deve durar exatamente um canal de tempo, ou seja, 51,2u segundos.

-> O primeiro canal será sempre considerado ocupado pelas estações.

->  Todas as estações deverão tentar realizar uma transmissão no segundo canal de tempo. Isso
obviamente leva a ocorrência de colisões, que deverão ser tratadas. Cada cenário utilizará
um algoritmo diferente, conforme listado acima.

-> A simulação termina quando uma das N estações consegue realizar sua transmissão com
sucesso. Nesse caso a simulação deverá apresentar como saída qual foi o tempo gasto (em u
segundos ou em número de canais de tempo) para realização de tal transmissão.

-> Cada cenário deverá ser simulado 33 vezes, sendo o resultado final do mesmo a média e o
desvio padrão dos 33 resultados obtidos.
 </p>
 
<h1>
🛠 Tecnologia
</h1>
<p>
As seguintes ferramentas foram usadas na construção do projeto:
</p>
<ul> 
<li>Linguagem de programação python</li> 
<li>Visual Studio Code</li> 
 
</ul>

 <h1>
✅ Contribuidores
 </h1>
 <table><tr>
 <td align="center"><a href="https://github.com/taisbsantos"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/39168931?v=4" width="100px;" alt=""/><br /><sub><b>Tais Santos</b></sub></a><br /><a href="https://github.com/taisbsantos" title="DUpla Redes">🚀</a>
 </td>
 
</tr>
</table>
 
 <h1>
✅ Autores:
 </h1>
 
<ul> 
 
<li>Roniel Nunes Barbosa</li> 
<li>Tais Santos</li> 
</ul>
