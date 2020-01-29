from pyspark import SparkContext
from pyspark import SparkConf
from operator import add

conf = SparkConf().setAppName("arquivo texto")
sc = SparkContext(conf=conf)

DadosJulho = sc.textFile("file:///home/aluno/Desktop/Semantix/log_Jul95.txt")
DadosJulho = DadosJulho.cache()

DadosAgosto = sc.textFile("file:///home/aluno/Desktop/Semantix/log_Aug95.txt")
DadosAgosto = DadosAgosto.cache()

DadosAgosto.count()

DadosJulho_count = DadosJulho.flatMap(lambda linha: linha.split(' ')[0]).distinct().count()
DadosAgosto_count = DadosAgosto.flatMap(lambda linha: linha.split(' ')[0]).distinct().count()
print('Numero de Hosts uúnicos no mês de julho: %s' % DadosJulho_count)
print('Numero de Hosts uúnicos no mês de agosto: %s' % DadosAgosto_count)


    
DadosJulho_404 = DadosJulho.filter(lambda linha: linha.split(' ')[-2] == '404').cache()
DadosAgosto_404 = DadosAgosto.filter(lambda linha: linha.split(' ')[-2] == '404').cache()
print('Erro 404 no mes de Julho: %s' % DadosJulho_404.count())
print('Erro 404 no mes de Agosto: %s' % DadosAgosto_404.count())


def Total_erros_404_por_dia(rdd):
    days = rdd.map(lambda line: line.split('[')[1].split(':')[0])
    counts = days.map(lambda day: (day, 1)).reduceByKey(add).collect()
   
    print('\nErros 404 por dia:')
    for day, count in counts:
        print(day, count)
        
    return counts

Total_erros_404_por_dia(DadosJulho_404)
Total_erros_404_por_dia(DadosAgosto_404)

