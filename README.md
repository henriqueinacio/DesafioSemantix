# DesafioSemantix


Qual​ ​o​ ​objetivo​ ​do​ ​comando​ ​​cache​ ​​em​ ​Spark? 
O comando cache cria um ponto de verificação que pode ser reutilizado para processamento adicional.
Exemplos, quando o RDD for usado várias vezes, como em um loop;
ou executando várias ações no mesmo RDD;

val textFile = sc.textFile("/user/arquivo.txt") 
textFile.cache

O RDD acima não faz nada, pois o arquivo ainda não foi lido. 
Após, o RDD lê o arquivo e armazena em cache o conteúdo. Se for executado o comando textFile.count pela primeira vez, o arquivo será carregado, armazenado em cache e contado. Se você executar o comando textFile.count pela segunda vez, a operação usará o cache. Ele apenas pega os dados do cache e conta as linhas.

 
O​ ​mesmo​ ​código​ ​implementado​ ​em​ ​Spark​ ​é​ ​normalmente​ ​mais​ ​rápido​ ​que​ ​a​ ​implementação​ ​equivalente​ ​em MapReduce.​ ​Por​ ​quê? 
O Spark é um framework para clusterização que executa processamento em memória, sem utilização de escrita e leitura em disco rígido.
O MapReduce é escrito em disco e toda vez que tiver que ler o dado, deverá ler o disco.
O Spark faz uso de Resilient Distributed Datasets (RDDs), o qual implementa estruturas de dados em memória e que são utilizadas para armazenar em cache os dados existentes entre os nós de um cluster. Uma vez que as RDDs ficam em memória, os algoritmos podem interagir nesta área de RDD várias vezes de forma eficiente.

 
Qual​ ​é​ ​a​ ​função​ ​do​ ​​SparkContext​? 
SparkContext é o ponto de entrada da funcionalidade Spark. 
Nele passam as configurações como nome da aplicação Spark, que será apresentada na interface do cluster, e o Cluster Manager a ser utilizado.


Explique​ ​com​ ​suas​ ​palavras​ ​​ ​o​ ​que​ ​é​ ​​Resilient​ ​Distributed​ ​Datasets​​ ​(RDD). 
RDD´s são a abstração de dados do Spark e os recursos com os quais são criados e implementados são responsáveis ​​por sua velocidade significativa. 
São armazenamentos de dados particionados para somente leitura, distribuídos por muitas máquinas (geralmente em um cluster)
Os RDDs do Spark são tolerantes a falhas, é um mecanismo de processamento na memória que depende de acesso barato à RAM.


GroupByKey​ ​​é​ ​menos​ ​eficiente​ ​que​ ​​reduceByKey​ ​​em​ ​grandes​ ​dataset.​ ​Por​ ​quê? 
O reduceByKey​ funciona muito melhor em um grande conjunto de dados. Isso ocorre porque o Spark sabe que pode combinar a saída com uma chave comum em cada partição antes de embaralhar os dados.
Por outro lado, ao chamar groupByKey - todos os pares de chave-valor são embaralhados. São muitos dados ​​para serem transferidos pela rede.
 
 
Explique​ ​o​ ​que​ ​o​ ​código​ ​Scala​ ​abaixo​ ​faz.

val​​ ​​textFile​​ ​​=​​ ​​sc​.​textFile​(​"hdfs://..."​) 
val​​ ​​counts​​ ​​=​​ ​​textFile​.​flatMap​(​line​​ ​​=>​​ ​​line​.​split​(​"​ ​"​)) ​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​
.​map​(​word​​ ​​=>​​ ​​(​word​,​​ ​​1​)) ​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ 
​​.​reduceByKey​(​_​​ ​​+​​ ​​_​) 
counts​.​saveAsTextFile​(​"hdfs://..."​)

O código acima está criando um RDD, acessando um arquivo texto do hdfs.
A cada linha do arquivo e a cada espaço “ “, está “quebrando” e armazenando em uma lista.
Para cada palavra está sendo transformada em chave-valor, com o valor 1.
O reduceByKey agrupa essas palavras, somando a ocorrência de cada palavra.
o resultado é salvo em um arquivo texto no hdfs.



Responda as seguintes questões devem ser desenvolvidas em Spark utilizando a sua linguagem de preferência. 
1. Número de hosts únicos. 
Hosts no mês de julho: 39
Hosts no mês de agosto: 53

2. O total de erros 404. 
Erro 404 no mes de Julho: 17
Erro 404 no mes de Agosto: 10056

3. Os 5 URLs que mais causaram erro 404. 


4. Quantidade de erros 404 por dia. 
01/Jul/1995', 17


'23/Aug/1995', 345)
'03/Aug/1995', 304)
'16/Aug/1995', 259)
'08/Aug/1995', 391)
'07/Aug/1995', 537)
'15/Aug/1995', 327)
'21/Aug/1995', 305)
'22/Aug/1995', 288)
'17/Aug/1995', 271)
'01/Aug/1995', 243)
'10/Aug/1995', 315)
'24/Aug/1995', 420)
'19/Aug/1995', 209)
'26/Aug/1995', 366)





5. O total de bytes retornados. 
