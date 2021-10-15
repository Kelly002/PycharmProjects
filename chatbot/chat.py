# Este código traz a estrutura de conversa de um chatbot
# que faz a captura de informações de um cliente e verifica se ele é um possível lead qualificado
# Material confeccionado para o TCC da especialização em IA da Puc Minas
# Kelly Lopes
# Campinas, set de 21.


#########################################################
# Importando os pacotes e bibliotecas
#########################################################
# pip install nltk    # instalação do pacote NLTK
#import re
#from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS as sklearn_stop_words
import nltk
import pandas as pd
from nltk.corpus import stopwords
#nltk.download()
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from datetime import datetime
nltk.download('stopwords')
stop_words = nltk.corpus.stopwords.words('portuguese')
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot


#########################################################
# Inicio da conversa com o bot
#########################################################
nome = str(input('Olá, qual é o seu nome?'))
print('Oi' ,nome,',' 'sou o bot da Atlas' )

pedido = input('Em que posso te ajudar?')
#texto = 'Essa capinha de celular é muito boa'

# transformando o texto em sentenças
sentencas = sent_tokenize(pedido)
#print(sentencas)

# transformando o texto em palavras e em minusculo
palavras = word_tokenize(pedido.lower())
#print(palavras)

# faz a limpeza da sentença retirando os stop words
sentenca_limpa = [palavra for palavra in palavras if palavra not in stop_words]
#print(sentenca_limpa)

# Colocar aqui uma sequencia de possíveis respostas, que será dada de acorodo com a similariedade
val=2

resposta_1 = print('Entendi, você quer ', val )
resposta_2 = print( 'Me passe por favor algumas informações:')

#########################################################
# Captação dos dados da empresa
#########################################################
nome_empresa = str(input('Qual o nome da empresa?'))
conselheiro = float(input('Você é um conselheiro? 1-Não ou 2-Sim: '))
while conselheiro > 2:
    conselheiro = float(input('Você é um conselheiro? 1-Não ou 2-Sim: '))
else:
    governaca = float(int(input('A empresa possui governança corporativa? 1-Não ou 2-Sim: ')))
    while governaca > 2:
        governaca = float(int(input('A empresa possui governança corporativa? 1-Não ou 2-Sim: ')))
    else:
        administracao = int(input('A empresa possui conselho administrativo? 1-Não ou 2-Sim: '))
        while administracao >2:
            administracao = int(input('A empresa possui conselho administrativo? 1-Não ou 2-Sim: '))
        else:
            fiscal = int(input('A empresa possui conselho fiscal ? 1-Não ou 2-Sim: '))
            while fiscal > 2:
                fiscal = int(input('A empresa possui conselho fiscal ? 1-Não ou 2-Sim: '))
            else:
                deliberativo = int(input('A empresa possui conselho deliberativo ? 1-Não ou 2-Sim: '))
                while deliberativo > 2:
                    deliberativo = int(input('A empresa possui conselho deliberativo ? 1-Não ou 2-Sim: '))
                else:
                    comites = int(input('A empresa possui comitês? 1-Não ou 2-Sim: '))
                    while comites > 2:
                        comites = int(input('A empresa possui comitês? 1-Não ou 2-Sim: '))
                    else:
                        assembleias = int(input('A empresa possui Assembeias ? 1-Não ou 2-Sim: '))
                        while assembleias > 2:
                            assembleias = int(input('A empresa possui Assembeias ? 1-Não ou 2-Sim: '))
                        else:
                            outros = int(input('Existe algum outro tipo de conselho dentro da empresa? 1-Não ou 2-Sim: '))
                            while outros >2:
                                outros = int(input('Existe algum outro tipo de conselho dentro da empresa? Especifique: '))
                            else:
                                frequencia = int(input('Com qual frequência os conselhos realizam reuniões? Mensal, Bimestral, Trimestral: '))
                                while frequencia > 3:
                                    frequencia = str(input('Com qual frequência os conselhos realizam reuniões? Especifique: '))
                                else:
                                    atas = int(input('Os comitês fazem uso de Atas? 1-Não ou 2-Sim: '))
                                    while atas > 2:
                                        atas = int(input('Os comitês fazem uso de Atas? 1-Não ou 2-Sim: '))
                                    else:
                                        publicadas = int(input('Essas Atas são publicadas? 1-Não ou 2-Sim: '))


#########################################################
# O bot fornece um resposta
#########################################################
print('Só um minuto, estou processando seus dados...')
#fazer o count aqui de acordo com os valores das entradas dos inputs


#########################################################
# Calculo que verifica se a empresa possui uma governança robusta
#########################################################
soma =int(conselheiro) + 10*int(governaca) +int(administracao) + int(fiscal) + int(deliberativo) + int(comites) + int(assembleias) + int(outros) + int(frequencia) + int(atas) + int(publicadas)
#print(soma)


#########################################################
# Bot finaliza a conversa oferecendo ou não um determinado produto para o cliente
#########################################################
# colocar alguns if condicionais
if soma > 26:
    if atas == 2 and publicadas ==2:
        print('O produto que irá satisfazer as necessidades da sua empresa é o Professional')
    elif atas == 2:
        print('O produto que irá satisfazer as necessidades da sua empresa é o Enterprise')
    else:
        print('O produto que irá satisfazer as necessidades da sua empresa é Basic')

    print('Um de nossos gerentes irá entrar em contato.')
    print('Seja muito bem vindo a Atlas Governance, aqui se inicia uma grande jornada!')
else:
    print('Sinto muito mas, sua empresa não possui uma governança madura suficiente para utilizar nossos produtos.')
    print('Se desejar, temos especialistas que podem ajudar a sua empresa a chegar à maturidade desejada!')


#########################################################
# Coletando o horário em que a pessoa conversou com o bot
#########################################################

data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#########################################################
# Organizando os dados no formato pandas
#########################################################

dataset = pd.DataFrame([data,nome, pedido, nome_empresa, conselheiro, governaca, administracao, fiscal, deliberativo, comites, assembleias, outros, frequencia, atas, publicadas]).T
#print(dataset)
dataset.columns = ['data', 'nome', 'pedido', 'nome empresa', 'conselheiro', 'governaca', 'administracao', 'fiscal', 'deliberativo', 'comites', 'assembleias', 'outros', 'frequencia', 'atas', 'publicadas']
print(dataset)


#########################################################
# Salvando o conjunto de dados em um arquivo .csv
#########################################################
dataset.to_csv('Users\kelly\PycharmProjects\chatbot\dataset.csv', sep=';', index=False, encoding='utf-8-sig')
#C:\Users\kelly\PycharmProjects\chatbot

#limpa = []
#def limpa_sentenca(x):
#    for palavra in palavras:
#        if palavra not in stop_words:
#            limpa.append(palavras)
#    return
#print(limpa_sentenca(palavras))

