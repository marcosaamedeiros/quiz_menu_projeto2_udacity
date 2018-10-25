#!/usr/bin/env python
#  coding: utf-8 
#Título           :QUIZ Udacity
#Descrição    :Três níveis de questões de completar e cada em três dificuldades.
#autor          :Marcos Antônio Alves Medeiros
#data            :18/10/2018
#versão         :0.1
#uso           :python quiz menu Udacity: quiz_menu.py
#notes           :
#python_version  :2.7.13|Enthought|(x86_64)
#=======================================================================
 
import sys, os # Importar módulos para rodar o script.
 
def nivel_quiz(): # Tela de abertura das opções de níveis do QUIZ.
    os.system('clear')    
    print "Bem vindo ao QUIZ!\n"
    print "Escolher o nível do QUIZ:"
    print "1. Nível 1: Truco Goiano vs truco Paulista" #dicionario do nivel 1
    print "2. Nível 2: Conceitos da Linguagem Python: Function 'def'" #dicionario do nivel 2   
    print "3. Nível 3: A magia do truco: blefar e embaralhar" #dicionario do nivel 3
    print "\n0. Sair do QUIZ"
    escolha_nivel = raw_input(" >>  ")
    obter_resposta(escolha_nivel) 
    return
 
def obter_resposta(escolha_nivel): # Avaliar entrada digitada para o QUIZ
    os.system('clear')
    escolha = escolha_nivel.lower()
    if escolha == '':
        navegar_menu['nivel_quiz']()
    else:
        try: # try ... except tem uma cláusula else opcional, com todas as cláusulas exceto. 
            navegar_menu[escolha]()
        except KeyError: #Chave não encontrada em mapeamento do dicionário
            print "Seleção ERRADA, por favor, tente novamente.\n"
            navegar_menu['nivel_quiz']()
    return 
   
dicionario_nivel1 = {
    'texto': 'Para o truqueiro que __1__ e que rouba o __2__, pelo fundo do baralho, se ele gritar __3__, com probabilidade de 50%. Preencha as lacunas: Limite inferior = __4__%; Limite superior = __5__%; média = __6__',
    'lacunas': ['__1__', '__2__', '__3__', '__4__','__5__','__6__'],
    'gabarito': ["blefa", "zap", "truco", "65", "85", "75"]
} 

dicionario_nivel2 = {
    'texto': 'Uma função é criada com a palavra-chave __1__. Especifica-se as entradas da função, adicionando-se __2__ entre os __3__. A função pode ser string, números, ___4___, tuple e dicionário.',
    'lacunas': ['__1__', '__2__', '__3__', '__4__'],
    'gabarito': ['def', 'parametros', 'parenteses', 'lista']
} 

dicionario_nivel3 = {
    'texto': 'Existem duas formas de se jogar o truco, o __1__ e o  __2__. Jogos em gritos! __3__, ladrão! Se trucou e eu com um zap na mão, toma __4__, ladrão!. O truco __1__ têm cartas fixas. Já o truco __2__, as cartas são renomeadas a cada mão.A marca maior desse jogo é o __5__ e a malandragem no embaralhar.Para aldo=[4,1,1] e maria=[1,2,2]. Se maria joga primeiro, quem ganha? Resposta: __6__',
    'lacunas': ['__1__', '__2__', '__3__', '__4__', '__5__', '__6__'],
    'gabarito': ['goiano', 'paulista', 'truco', 'seis', 'blefe','maria']
} 

def consultar_dicionario_nivel1(): #QUIZ nível 1     
    texto = dicionario_nivel1['texto']
    lacunas = dicionario_nivel1['lacunas']
    gabarito = dicionario_nivel1['gabarito']    
    return texto, lacunas, gabarito

def consultar_dicionario_nivel2(): #QUIZ nível 2        
    texto = dicionario_nivel2['texto']
    lacunas = dicionario_nivel2['lacunas']
    gabarito = dicionario_nivel2['gabarito']    
    return texto, lacunas, gabarito

def consultar_dicionario_nivel3(): #QUIZ nível 3        
    texto = dicionario_nivel3['texto']
    lacunas = dicionario_nivel3['lacunas']
    gabarito = dicionario_nivel3['gabarito']    
    return texto, lacunas, gabarito

def nivel_1(): #Defina o grau de dificuldade do QUIZ     
    print "nivel_1: Truco Goiano vs truco Paulista !\n"
    print "Regras:"    
    print "Digitar fácil, médio ou difícil seguido do número do nível.\n"    
    print "9. Voltar aos níveis de QUIZ"
    print "0. Sair do QUIZ"
    escolha_nivel = raw_input(" >>  ")
    obter_resposta(escolha_nivel)           
    return 

def nivel_2(): #Defina o grau de dificuldade do QUIZ   
    print "nivel_2: Conceitos da Linguagem Python: Function 'def'\n"
    print "Digitar fácil, médio ou difícil seguido do número do nível.\n"    
    print "9. Voltar às opções de QUIZ"
    print "0. Sair do Quiz"     
    escolha_nivel = raw_input(" >>  ")
    obter_resposta(escolha_nivel)
    return    
        
def nivel_3(): #Defina o grau de dificuldade do QUIZ   
    print "nivel_3: A magia do truco: blefar e embaralhar !\n"
    print "Digitar fácil, médio ou difícil seguido do número do nível.\n"    
    print "9. Voltar às opções de QUIZ"
    print "0. Sair do Quiz"    
    escolha_nivel = raw_input(" >>  ")
    obter_resposta(escolha_nivel)
    return  
  
def nivel_1_facil():           
    tentativa = 3 #Preencha as lacunas em até 3(três) tentativas. 
    texto, lacunas, resposta_gabarito = consultar_dicionario_nivel1()
    for index, lacuna in enumerate(lacunas):        
        print 'texto: ' + texto
        resposta = resposta_gabarito[index]        
        resposta_usuario = raw_input('Digite a palavra correspondente da lacuna ' + lacuna + ':\n').lower()    
        while resposta_usuario != resposta:
            tentativa = tentativa - 1
            if tentativa == 2:                
                print 'Erro!!! A palavra inicia com a letra:' + resposta[0]
                resposta_usuario = raw_input('Tente novamente a palavra da lacuna ' + lacuna + ':\n').lower()            
            elif tentativa == 1:
                print 'A palavra termina com a letra:' + resposta[-1]
                resposta_usuario = raw_input('Tente novamente a palavra da lacuna ' + lacuna + ':\n').lower()        
            elif tentativa == 0: #sair()                
                retornar_nivel_quiz()        
        texto = texto.replace(lacuna, resposta)                    
    print texto + '\nMuito bom!!! 100%!!!'      
    retornar_nivel_quiz() 
    return    

def nivel_2_facil():           
    tentativa = 3 #Preencha as lacunas em até 3(três) tentativas.
    texto, lacunas, resposta_gabarito = consultar_dicionario_nivel2()
    for index, lacuna in enumerate(lacunas):        
        print 'texto: ' + texto
        resposta = resposta_gabarito[index]        
        resposta_usuario = raw_input('Digite a palavra correspondente da lacuna ' + lacuna + ':\n').lower()    
        while resposta_usuario != resposta:
            tentativa = tentativa - 1
            if tentativa == 2:                
                print 'Erro!!! A palavra inicia com a letra:' + resposta[0]
                resposta_usuario = raw_input('Tente novamente a palavra da lacuna ' + lacuna + ':\n').lower()            
            elif tentativa == 1:
                print 'A palavra termina com a letra:' + resposta[-1]
                resposta_usuario = raw_input('Tente novamente a palavra da lacuna ' + lacuna + ':\n').lower()        
            elif tentativa == 0: #sair()                
                retornar_nivel_quiz()        
        texto = texto.replace(lacuna, resposta)                    
    print texto + '\nMuito bom!!! 100%!!!'      
    retornar_nivel_quiz()        
    return 

def nivel_3_facil():            
    tentativa = 3 #Preencha as lacunas em até 3(três) tentativas.
    texto, lacunas, resposta_gabarito = consultar_dicionario_nivel3()
    for index, lacuna in enumerate(lacunas):        
        print 'texto: ' + texto
        resposta = resposta_gabarito[index]        
        resposta_usuario = raw_input('Digite a palavra correspondente da lacuna ' + lacuna + ':\n').lower()    
        while resposta_usuario != resposta:
            tentativa = tentativa - 1
            if tentativa == 2:                
                print 'Erro!!! A palavra inicia com a letra:' + resposta[0]
                resposta_usuario = raw_input('Tente novamente a palavra da lacuna ' + lacuna + ':\n').lower()            
            elif tentativa == 1:
                print 'A palavra termina com a letra:' + resposta[-1]
                resposta_usuario = raw_input('Tente novamente a palavra da lacuna ' + lacuna + ':\n').lower()        
            elif tentativa == 0: #sair()                
                retornar_nivel_quiz()        
        texto = texto.replace(lacuna, resposta)                    
    print texto + '\nMuito bom!!! 100%!!!'      
    retornar_nivel_quiz()   
    return 

def nivel_1_medio():           
    tentativa = 2 #Preencha as lacunas em até 2(duas) tentativas. 
    texto, lacunas, resposta_gabarito = consultar_dicionario_nivel1()
    for index, lacuna in enumerate(lacunas):        
        print 'texto: ' + texto
        resposta = resposta_gabarito[index]        
        resposta_usuario = raw_input('Digite a palavra correspondente da lacuna ' + lacuna + ':\n').lower()    
        while resposta_usuario != resposta:
            tentativa = tentativa - 1
            if tentativa == 2:                
                print 'Erro!!! A palavra inicia com a letra:' + resposta[0]
                resposta_usuario = raw_input('Tente novamente a palavra da lacuna ' + lacuna + ':\n').lower()            
            elif tentativa == 1:
                print 'A palavra termina com a letra:' + resposta[-1]
                resposta_usuario = raw_input('Tente novamente a palavra da lacuna ' + lacuna + ':\n').lower()        
            elif tentativa == 0: #sair()                
                retornar_nivel_quiz()        
        texto = texto.replace(lacuna, resposta)                    
    print texto + '\nMuito bom!!! 100%!!!'      
    retornar_nivel_quiz() 
    return    

def nivel_2_medio():           
    tentativa = 2 #Preencha as lacunas em até 2(duas) tentativas.
    texto, lacunas, resposta_gabarito = consultar_dicionario_nivel2()
    for index, lacuna in enumerate(lacunas):        
        print 'texto: ' + texto
        resposta = resposta_gabarito[index]        
        resposta_usuario = raw_input('Digite a palavra correspondente da lacuna ' + lacuna + ':\n').lower()    
        while resposta_usuario != resposta:
            tentativa = tentativa - 1
            if tentativa == 2:                
                print 'Erro!!! A palavra inicia com a letra:' + resposta[0]
                resposta_usuario = raw_input('Tente novamente a palavra da lacuna ' + lacuna + ':\n').lower()            
            elif tentativa == 1:
                print 'A palavra termina com a letra:' + resposta[-1]
                resposta_usuario = raw_input('Tente novamente a palavra da lacuna ' + lacuna + ':\n').lower()        
            elif tentativa == 0: #sair()                
                retornar_nivel_quiz()        
        texto = texto.replace(lacuna, resposta)                    
    print texto + '\nMuito bom!!! 100%!!!'      
    retornar_nivel_quiz()        
    return 

def nivel_3_medio():           
    tentativa = 2 #Preencha as lacunas em até 2(duas) tentativas. 
    texto, lacunas, resposta_gabarito = consultar_dicionario_nivel3()
    for index, lacuna in enumerate(lacunas):        
        print 'texto: ' + texto
        resposta = resposta_gabarito[index]        
        resposta_usuario = raw_input('Digite a palavra correspondente da lacuna ' + lacuna + ':\n').lower()    
        while resposta_usuario != resposta:
            tentativa = tentativa - 1
            if tentativa == 2:                
                print 'Erro!!! A palavra inicia com a letra:' + resposta[0]
                resposta_usuario = raw_input('Tente novamente a palavra da lacuna ' + lacuna + ':\n').lower()            
            elif tentativa == 1:
                print 'A palavra termina com a letra:' + resposta[-1]
                resposta_usuario = raw_input('Tente novamente a palavra da lacuna ' + lacuna + ':\n').lower()        
            elif tentativa == 0: #sair()                
                retornar_nivel_quiz()        
        texto = texto.replace(lacuna, resposta)                    
    print texto + '\nMuito bom!!! 100%!!!'      
    retornar_nivel_quiz()   
    return 

def nivel_1_dificil():           
    tentativa = 1 #Preencha as lacunas em até 1(uma) tentativa.
    texto, lacunas, resposta_gabarito = consultar_dicionario_nivel1()
    for index, lacuna in enumerate(lacunas):        
        print 'texto: ' + texto
        resposta = resposta_gabarito[index]        
        resposta_usuario = raw_input('Digite a palavra correspondente da lacuna ' + lacuna + ':\n').lower()    
        while resposta_usuario != resposta:
            tentativa = tentativa - 1
            if tentativa == 2:                
                print 'Erro!!! A palavra inicia com a letra:' + resposta[0]
                resposta_usuario = raw_input('Tente novamente a palavra da lacuna ' + lacuna + ':\n').lower()            
            elif tentativa == 1:
                print 'A palavra termina com a letra:' + resposta[-1]
                resposta_usuario = raw_input('Tente novamente a palavra da lacuna ' + lacuna + ':\n').lower()        
            elif tentativa == 0: #sair()                
                retornar_nivel_quiz()        
        texto = texto.replace(lacuna, resposta)                    
    print texto + '\nMuito bom!!! 100%!!!'      
    retornar_nivel_quiz() 
    return    

def nivel_2_dificil():            
    tentativa = 1 #Preencha as lacunas em até 1(uma) tentativa.
    texto, lacunas, resposta_gabarito = consultar_dicionario_nivel2()
    for index, lacuna in enumerate(lacunas):        
        print 'texto: ' + texto
        resposta = resposta_gabarito[index]        
        resposta_usuario = raw_input('Digite a palavra correspondente da lacuna ' + lacuna + ':\n').lower()    
        while resposta_usuario != resposta:
            tentativa = tentativa - 1
            if tentativa == 2:                
                print 'Erro!!! A palavra inicia com a letra:' + resposta[0]
                resposta_usuario = raw_input('Tente novamente a palavra da lacuna ' + lacuna + ':\n').lower()            
            elif tentativa == 1:
                print 'A palavra termina com a letra:' + resposta[-1]
                resposta_usuario = raw_input('Tente novamente a palavra da lacuna ' + lacuna + ':\n').lower()        
            elif tentativa == 0: #sair()                
                retornar_nivel_quiz()        
        texto = texto.replace(lacuna, resposta)                    
    print texto + '\nMuito bom!!! 100%!!!'      
    retornar_nivel_quiz()        
    return 

def nivel_3_dificil():         
    tentativa = 1 #Preencha as lacunas em até 1(uma) tentativa.
    texto, lacunas, resposta_gabarito = consultar_dicionario_nivel3()
    for index, lacuna in enumerate(lacunas):        
        print 'texto: ' + texto
        resposta = resposta_gabarito[index]        
        resposta_usuario = raw_input('Digite a palavra correspondente da lacuna ' + lacuna + ':\n').lower()    
        while resposta_usuario != resposta:
            tentativa = tentativa - 1
            if tentativa == 2:                
                print 'Erro!!! A palavra inicia com a letra:' + resposta[0]
                resposta_usuario = raw_input('Tente novamente a palavra da lacuna ' + lacuna + ':\n').lower()            
            elif tentativa == 1:
                print 'A palavra termina com a letra:' + resposta[-1]
                resposta_usuario = raw_input('Tente novamente a palavra da lacuna ' + lacuna + ':\n').lower()        
            elif tentativa == 0: #sair()                
                retornar_nivel_quiz()        
        texto = texto.replace(lacuna, resposta)                    
    print texto + '\nMuito bom!!! 100%!!!'      
    retornar_nivel_quiz()   
    return

def retornar_nivel_quiz(): # Retornar para a tela inicial dos níveis QUIZ (nivel_quiz)
    navegar_menu['nivel_quiz']()
 
def sair(): # Sair do programa
    sys.exit()
 
navegar_menu  = {} # Navegabilidade e ações entre as opções em nivel_quiz
navegar_menu = {   # dicionários são indexados por chaves, que podem ser de qualquer tipo imutável;
    'nivel_quiz': nivel_quiz,
    '1': nivel_1,
    '2': nivel_2,
    '3': nivel_3,     
    'facil1': nivel_1_facil,
    'facil2': nivel_2_facil,
    'facil3': nivel_3_facil,
    'medio1': nivel_1_medio,
    'medio2': nivel_2_medio,
    'medio3': nivel_3_medio,
    'dificil1': nivel_1_dificil,
    'dificil2': nivel_2_dificil,
    'dificil3': nivel_3_dificil,       
    '9': retornar_nivel_quiz,
    '0': sair,
}

if __name__ == "__main__": # Programa principal
    # Iniciar o QUIZ
    nivel_quiz()