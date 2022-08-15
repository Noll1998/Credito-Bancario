# Credito-Bancario
Crédito Bancário em Portugal entre 2010 e 2019


  Analisa-se que diversos fatores macroeconômicos e microeconômicos podem impactar o funcionamento dos bancos, e, dessa maneira, a concessão de crédito. Dentre as variáveis que demonstram ter importante influência sobre o nível de concessão de crédito estão PIB, taxa de inflação, taxa de desemprego e taxa de juros.
  A partir dos dados coletados referentes ao crédito para particulares, crédito para empresas, PIB, taxas de juro, inflação e taxa de desemprego para o período em análise, foram criados dois modelos econométricos. Tornou-se necessário a criação de mais de um modelo pelo fato de que as taxas de juros de crédito a particulares diferem daquelas cobradas no caso de crédito para empresas, sendo normalmente mais elevadas durante o período analisado.
  Para ambos modelos, o valor de crédito é a variável dependente, enquanto taxa de juro, PIB, inflação e taxa de desemprego atuam como variáveis explicativas. A significância individual das variáveis explicativas foi testada com o uso do teste t e em seguida o teste F foi usado para calcular a significância conjunta dessas variáveis.
  O primeiro modelo utiliza o crédito a particulares como variável dependente, enquanto β1 faz referência ao PIB, β2 é o coeficiente relativo à taxa de juros, β3 é a taxa de inflação e β4 é a taxa de desemprego, assim descrito na tabela abaixo:
  
![image](https://user-images.githubusercontent.com/68149933/184701067-eb468725-e1cd-4697-a00f-25bc38a82e7d.png)

  Foi utilizado o teste t para testar a significância individual das variáveis explicativas, no qual a hipótese nula é H0: βi = 0 e a hipótese alternativa é Ha: βi ≠ 0. O valor da estatítica t para distribuição com 5 graus de liberdade é tc= 2,571 para um nível de significância de 5%. Dessa maneira, todas as variáveis explicativas terão suas hipóteses nulas não rejeitadas, visto que nenhum tβi possui valor maior do que 2,571 ou menor do que -2,571. Além disso, os valores P-value (Sig.) das variáveis são superiores à 0,05 e, portanto, não são significativos para o modelo e reforçam a evidência de não rejeição da hipótese nula.
  
  ![image](https://user-images.githubusercontent.com/68149933/184701926-4202e94d-5705-4d1b-a5ed-3c2471111e4f.png)
  
  Por outro lado, o teste F foi utilizado para calcular a significância conjunta das variáveis e, a um nível de significância de 5%, seu valor crítico é de Fc = 5,19 para 5 graus de liberdade no denominador e 4 graus de liberdade no numerador. Dessa maneira, o valor F = 7,158 que consta na tabela acima indica que H0: βi = 0 deve ser rejeitado e, portanto, as variáveis são significativas em conjunto para o modelo. O P-value de 0,0267 (inferior à 0,05) também evidencia que a hipótese nula deve ser rejeitada.
  O outro modelo utiliza crédito às empresas como variável dependente, PIB como β1, taxa de juros como β2, taxa de inflação como β3, e taxa de desemprego como β4. O teste t foi realizado novamente, ao nível de significância de 5%, utilizando os valores da tabela abaixo. Com o valor crítico tc = 2,571, a hipótese nula não deve ser rejeitada para as variáveis explicativas, exceto para a taxa de juros que possui tβi = 4,491. Também, o único P-value que possui valor aceitável é o da taxa de juros, mais uma vez comprovando que a hipótese nula dessa variável deve ser rejeitada e que, portanto, ela tem significância individual para o modelo. 
  
  ![image](https://user-images.githubusercontent.com/68149933/184701980-7282e1e8-9b18-4b26-bb93-06fac4e011cc.png)
  
  Igualmente ao primeiro modelo, o teste F possui o valor crítico Fc = 5,19 com 5 graus de liberdade no denominador, 4 graus de liberdade no numerador e nível de significância de 5%. A tabela abaixo mostra F = 14,75 e P-value = 0,00564, indicando que a hipótese nula deve ser rejeitada e que, dessa maneira, as variáveis possuem significância conjunta para o modelo.
  
  ![image](https://user-images.githubusercontent.com/68149933/184702018-429d0237-d3c2-4d33-82a0-e0cd7a02cd31.png)
  
Em ambos modelos nota-se a rejeição da hipótese nula (H0: βi = 0) nos testes F e a não rejeição dessa hipótese nos testes t (H0: βi = 0), com exceção da variável Taxa de Juro no modelo 2 que obteve valores significativos. Assim, conclui-se que a taxa de juro, PIB, taxa de inflação e taxa de desemprego não são bons estimadores para o valor do crédito concedido quando aplicados de maneira individual, porém podem ser úteis como variáveis preditivas quando utilizadas de maneira conjunta.

  Testes Estatísticos
  
  Além dos modelos econométricos, foram realizados dois testes estatísticos utilizando as medidas de associação, covariância e coeficiente de correlação. A covariância indica o sentido da variação conjunta das variáveis. Dessa forma, se a covariância é positiva ambas as variáveis variam no mesmo sentido e se a covariância for negativa, elas variam em sentido oposto. 
  
  ![image](https://user-images.githubusercontent.com/68149933/184702060-200e3cc3-c816-4b21-9c97-45a6036682c4.png)
  
  Foi decidido dividir em dois períodos a variável PIB em relação ao momento econômico, durante os anos 2010 e 2014 o PIB reduziu, evidenciando uma possível recessão, enquanto os anos 2015 a 2019 indicam um crescimento econômico, visto que era possível obter resultados não esperados. Após o cálculo de covariância, é possível observar que a maioria das relações são diretas, sendo elas a covariância entre empréstimo total e PIB para ambos os períodos e empréstimos às empresas e taxa de juros às empresas, em contrapartida, as covariâncias de empréstimo total e PIB e empréstimo a particulares e taxa de juros à particulares apresentam relações inversas.
  
![image](https://user-images.githubusercontent.com/68149933/184702093-7502f188-8155-4664-bab1-d89a7ce1e959.png)

  Contudo, a magnitude da covariância, ou seja, seu valor, nem sempre está relacionada com a intensidade da associação entre as variáveis. Por isso, utiliza-se outra medida de associação: o coeficiente de correlação, que tem limites entre -1 e 1. A partir dessa medida, torna-se conhecida a intensidade das relações, mantendo-se os sinais iguais à covariância. Desse modo, observa-se que as correlações com forte correlação positiva são as de empréstimo total e PIB, nos anos 2015 a 2019, e empréstimo às empresas e taxa de juros às empresas. Os coeficientes de empréstimo total e PIB, nos anos 2010 a 2014, e empréstimos a particulares e taxas de juros a particulares apresentam uma moderada correlação, sendo o último negativo e o primeiro positivo. Por último, o empréstimo total e PIB para o período inteiro analisado obteve uma fraca correlação positiva.
  Já em referência às variáveis taxa de inflação e taxa de desemprego, suas respectivas correlações com os dois tipos de crédito podem ser visualizadas na tabela abaixo. É notável que enquanto o crédito às empresas possui relação direta com ambas as variáveis, o crédito a particulares se comporta de maneira oposta, obtendo relações inversas com esses fatores.
  
![image](https://user-images.githubusercontent.com/68149933/184702160-c7a94ea7-d0e0-4534-8e5f-e11ff9140aea.png)

  Além disso, o crédito a particulares está mais fortemente correlacionado com a taxa de desemprego, enquanto o crédito às empresas possui correlação três vezes maior com a taxa de inflação. Essa divergência de resultados pode ser explicada pela relação entre a taxa de desemprego e o risco de inadimplência para crédito a particulares, de maneira que em períodos de alto desemprego há menos concessão de crédito a particulares. Paralelamente, a maior influência da taxa de inflação sobre o crédito às empresas pode ser explicada pela importante relação entre taxa de inflação e rentabilidade bancária.
