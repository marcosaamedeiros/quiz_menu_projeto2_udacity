#!/usr/bin/env python
# coding: utf-8 
#Título           :QUIZ (fácil, médio, difícil)
#Descrição    :Três níveis de questões de completar as lacunas
#autor          :Marcos Antônio Alves Medeiros
#data            :26/10/2018
#versão         :0.2
#uso           :python quiz menu Udacity: quiz_facil_medio_dificil.py
#notes           :
#python_version  :2.7.13|Enthought|(x86_64)
#=======================================================================
 
import sys, os
 
def nivel_quiz():
    """
    Entrada: Parâmetro vazio
    Tarefa: Informar níveis do QUIZ e entrada de resposta do usuário para o nível 
    Saída: Parâmetro do nível escolhido
    """
    os.system('clear')    
    print "\nSeja bem vindo ao QUIZ!\n"
    print "Escolher o nível do QUIZ (fácil, médio ou difícil): "    
    print "--> digitar facil, para questão sobre conceitos da Linguagem Python: Function 'def'"
    print "--> digitar medio, para questão sobre truco Goiano vs truco Paulista"    
    print "--> digitar dificil, para questão sobre a magia do truco: blefar e embaralhar"
    print "\n0. Sair do QUIZ"
    escolha_nivel = raw_input(" >>  ")
    obter_resposta(escolha_nivel) 
    return
 
def obter_resposta(escolha_nivel):    
    """
    Entrada: Parâmetro do nível (facil, médio, difícil)
    Tarefa: Avaliar resposta do usuário e informar estado atual
    Saída: Parâmetros do dicionário do menu QUIZ
    """    
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

#==============================================================
#Estruturas de dados tipo dicionário (texto, lacunas, gabarito)
#Dicionários: nível fácil, nível médio e nível difícil
#==============================================================

dicionario_nivel_facil = {
    'texto': 'Uma função é criada com a palavra-chave __1__. Especifica-se as entradas da função, adicionando-se __2__ entre os __3__. A função pode ser string, números, __4__, tuple e dicionário.',
    'lacunas': ['__1__', '__2__', '__3__', '__4__'],
    'gabarito': ['def', 'parametros', 'parenteses', 'lista']
}

dicionario_nivel_medio = {
    'texto': 'Para o truqueiro que __1__ e que rouba o __2__, pelo fundo do baralho, se ele gritar __3__, com probabilidade de 50%. Preencha as lacunas: Limite inferior = __4__%; Limite superior = __5__%; média = __6__',
    'lacunas': ['__1__', '__2__', '__3__', '__4__','__5__','__6__'],
    'gabarito': ["blefa", "zap", "truco", "65", "85", "75"]
}

dicionario_nivel_dificil = {
    'texto': 'Existem duas formas de se jogar o truco, o __1__ e o  __2__. Jogos em gritos! __3__, ladrão! Se trucou e eu com um zap na mão, toma __4__, ladrão!. O truco __1__ têm cartas fixas. Já o truco __2__, as cartas são renomeadas a cada mão.A marca maior desse jogo é o __5__ e a malandragem no embaralhar.Para aldo=[4,1,1] e maria=[1,2,2]. Se maria joga primeiro, quem ganha? Resposta: __6__',
    'lacunas': ['__1__', '__2__', '__3__', '__4__', '__5__', '__6__'],
    'gabarito': ['goiano', 'paulista', 'truco', 'seis', 'blefe','maria']
} 

def mensagem_inicia_quiz(nivel):
    """
    Entrada: Parâmetro do nível tipo 'string'
    Tarefa: Informar na tela mensagem de apresentação e nível escolhido pelo usuário
    Saída: Parâmetro vazio
    """
    print '\nSeja bem vindo ao quiz nível: ' + nivel  
    
def avalia_resposta_lacuna(lacuna, gabarito):
    """
    Entrada: Parâmetros do dicionário nível (fácil, médio, difícil)
    Tarefa: Comparar respostas do usuário com o gabarito e controlar o laço (acerto x erro)
    Saída: Parâmetro da resposta do usuário
    """
    resposta_usuario = raw_input('Digite a palavra correspondente da lacuna ' + lacuna + ':\n').lower()
    while resposta_usuario != gabarito:
        resposta_usuario = raw_input('Palavra errada!!! Digite novamente:\n').lower()        
    print 'Muito bom!!! Resposta correta\n'
    return resposta_usuario
    
def preenche_lacuna_por_resposta(texto, lacuna, resposta):
    """
    Entrada: Parâmetros do dicionário nível (fácil, médio, difícil)
    Tarefa: Completar a lacuna pela resposta correta
    Saída: Texto com a lacuna corrigida
    """
    return texto.replace(lacuna, resposta)

def mensagem_finaliza_nivel(texto):
    """
    Entrada: Parametro texto corrigido
    Tarefa: Mostrar texto corrigido e comentário de display
    Saída: Parâmetro vazio
    """
    print texto + " \ Maravilha!!! 100% de acertos. Você superou esse nível!!!\n"
    print "Continue assim! Escolha outro nível..."

def perguntas_percorre_dicionario_nivel (texto, lacunas, gabarito):
    """
    Entrada: Parametros do dicionário relacionado ao nível (fácil, médio, difícil)
    Tarefa: Percorrer o texto do nível e para cada lacuna, pergunta-se a resposta do usuário 
    Saída: Parâmetros do dicionário e respostas do usuário
    """
    for index, lacuna in enumerate(lacunas):
        print '\nTexto: ' + texto
        resposta = gabarito[index]
        resposta_usuario = avalia_resposta_lacuna(lacuna, resposta)
        texto = preenche_lacuna_por_resposta(texto, lacuna, resposta_usuario)
    mensagem_finaliza_nivel(texto)        
    retornar_nivel_quiz()
    return 
    
def consulta_dicionario(nivel):
    """
    Entrada: Parâmetro do nível selecionado (fácil, médio, difícil)
    Tarefa: Determinar qual dicionário a ser consultado
    Saída: Parâmetros do dicionário (texto, lacunas, gabarito)
    """
    nivel_dicionario = nivel
    if nivel_dicionario == 'facil':
        texto = dicionario_nivel_facil['texto']
        lacunas = dicionario_nivel_facil['lacunas']
        gabarito = dicionario_nivel_facil['gabarito']            
    elif nivel_dicionario == 'medio':
        texto = dicionario_nivel_medio['texto']
        lacunas = dicionario_nivel_medio['lacunas']
        gabarito = dicionario_nivel_medio['gabarito']         
    elif nivel_dicionario == 'dificil':
        texto = dicionario_nivel_dificil['texto']
        lacunas = dicionario_nivel_dificil['lacunas']
        gabarito = dicionario_nivel_dificil['gabarito']    
    return texto, lacunas, gabarito

def nivel_facil_iniciar():
    """
    Entrada: Parâmetro vazio
    Tarefa: Inicializar variável nível tipo 'string' e variáveis dicionário do nível
    Saída: Parâmetros do dicionário (texto, lacunas, gabarito) e nível
    """
    nivel = 'facil'   
    mensagem_inicia_quiz(nivel)  
    texto, lacunas, gabarito = consulta_dicionario(nivel)
    perguntas_percorre_dicionario_nivel(texto, lacunas, gabarito) 
    retornar_nivel_quiz()
    return 
    
def nivel_medio_iniciar():
    """
    Entrada: Parâmetro vazio
    Tarefa: Inicializar variável nível tipo 'string' e variáveis dicionário do nível
    Saída: Parâmetros do dicionário (texto, lacunas, gabarito) e nível
    """
    nivel = 'medio'   
    mensagem_inicia_quiz(nivel)  
    texto, lacunas, gabarito = consulta_dicionario(nivel)
    perguntas_percorre_dicionario_nivel(texto, lacunas, gabarito)
    retornar_nivel_quiz()
    return 

def nivel_dificil_iniciar():    
    """
    Entrada: Parâmetro vazio
    Tarefa: Inicializar variável nível tipo 'string' e variáveis dicionário do nível
    Saída: Parâmetros do dicionário (texto, lacunas, gabarito) e nível
    """
    nivel = 'dificil'     
    mensagem_inicia_quiz(nivel)  
    texto, lacunas, gabarito = consulta_dicionario(nivel)
    perguntas_percorre_dicionario_nivel(texto, lacunas, gabarito)
    retornar_nivel_quiz()
    return 

#Tela de apresentação dos níveis: fácil, médio, difícil
def retornar_nivel_quiz():
    navegar_menu['nivel_quiz']()
 
# Sair do programa
def sair():
    sys.exit()
 
# ============================================================================
#menu QUIZ 
#Estrutura de dados tipo Dicionário = {}
#Dicionários são indexados por chaves, que podem ser de qualquer tipo imutável;
#Opções menu QUIZ - níveis: fácil, médio, dificícil
#Opção 0: 'sair'
# ============================================================================
 
navegar_menu  = {} 
navegar_menu = {    
    'nivel_quiz': nivel_quiz,       
    'facil': nivel_facil_iniciar,
    'medio': nivel_medio_iniciar,    
    'dificil': nivel_dificil_iniciar,  
    '9': retornar_nivel_quiz,
    '0': sair,
}

# =====================
#    Programa Principal
# =====================
 
if __name__ == "__main__":
    # Iniciar o QUIZ
    nivel_quiz()