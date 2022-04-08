from ImovelResidencial import ImovelResidencial
from Frequencias import Frequencias
from TratamentoDeDados import TratamentoDeDados
from AnaliseValores import AnaliseValores
from Agrupar import Agrupar
from Grafico import Grafico
from Outliers import Outlier

ir = ImovelResidencial()
ir.pegar() #Gera o aluguel_residencial

frequencias = Frequencias()
tratamento = TratamentoDeDados()
analise = AnaliseValores()
agrupar = Agrupar()
grafico = Grafico()
outlier = Outlier()

frequencias.total_de_apartamento()
frequencias.total_de_casas()
frequencias.area_60_a_100()
frequencias.mais_4_quartos_aluguel_menor_4000()

tratamento.retirarNulos()
tratamento.ColocarZero() #Altera o aluguel_residencial

#Alteram o aluguel_residencial
analise.valor_bruto()
analise.valor_metros()
analise.valor_metros_bruto()
analise.tipo_agregado()

agrupar.media("Valor")
agrupar.media_grupo("Bairro","Valor")
agrupar.descrever("Bairro","Valor")
agrupar.minha_descricao("Bairro","Valor")

grafico.desvio_padrao("Bairro","Valor", "orange")
grafico.desvio_padrao("Bairro","Valor", "blue")
grafico.boxplot("Bairro","Valor")
grafico.histograma("Valor")
grafico.histogramaGrupos("Bairro","Valor")

outlier.remover()
#poderia mostrar graficos com valores corrigidos