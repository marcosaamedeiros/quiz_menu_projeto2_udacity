#!/usr/bin/env python
# coding: utf-8 
#Título           :QUIZ 3 dificuldades (fácil, médio, difícil)
#Descrição    :Três níveis de questões de completar as lacunas
#autor          :Marcos Antônio Alves Medeiros
#data            :30/11/2018
#versão         :0.4
#uso           :python quiz Udacity: quiz_3_dificuldades.py
#notes           : Rodar cada nível 
#python_version  :2.7.13|Enthought|(x86_64)
#===============================================================

# ==============================================================
# Estruturas de dados tipo dicionário (texto, lacunas, gabarito)
# Dicionários: nível fácil, nível médio e nível difícil
# ==============================================================

dicionario_nivel_facil = {
    'texto': 'Uma função é criada com a palavra-chave __1__. Especifica-se as entradas da função, adicionando-se __2__ entre os __3__. A função pode ser string, números, __4__, tuple e dicionário.',
    'lacunas': ['__1__', '__2__', '__3__', '__4__'],
    'gabarito': ['def', 'parametros', 'parenteses', 'lista']
}

dicionario_nivel_medio = {
    'texto': 'Para o truqueiro que __1__ e que rouba o __2__, pelo fundo do baralho, se ele gritar __3__, com probabilidade de 50%. Preencha as lacunas: Limite inferior = __4__%; Limite superior = __5__%; média = __6__.',
    'lacunas': ['__1__', '__2__', '__3__', '__4__','__5__','__6__'],
    'gabarito': ["blefa", "zap", "truco", "65", "85", "75"]
}

dicionario_nivel_dificil = {
    'texto': 'Existem duas formas de se jogar o truco, o __1__ e o  __2__. Jogos em gritos! __3__, ladrão! Se trucou e eu com um zap na mão, toma __4__, ladrão!. O truco __1__ têm cartas fixas. Já o truco __2__, as cartas são renomeadas a cada mão.A marca maior desse jogo é o __5__ e a malandragem no embaralhar.Para aldo=[4,1,1] e maria=[1,2,2]. Se maria joga primeiro, quem ganha? Resposta: __6__.',
    'lacunas': ['__1__', '__2__', '__3__', '__4__', '__5__', '__6__'],
    'gabarito': ['goiano', 'paulista', 'truco', 'seis', 'blefe','maria']
} 

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
    texto = texto.replace(lacuna, resposta)
    return texto

def perguntas_percorre_dicionario_nivel (texto, lacunas, gabarito):
    """
    Entrada: Parametros do dicionário relacionado ao nível (fácil, médio, difícil)
    Tarefa: Percorrer o texto do nível e para cada lacuna, pergunta-se a resposta do usuário 
    Saída: Parâmetros do dicionário e respostas do usuário
    """
    for index, lacuna in enumerate(lacunas):
        print '\nTexto: ' + texto + '\n'
        resposta = gabarito[index]
        resposta_usuario = avalia_resposta_lacuna(lacuna, resposta)
        texto = preenche_lacuna_por_resposta(texto, lacuna, resposta_usuario)
    
    mensagem_final = " Maravilha!!! 100% de acertos. Você superou esse nível!!!"\
    "Continue assim! Escolha outro nível..."
    print texto + mensagem_final
    
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

def nivel_iniciar(nivel):
    """
    Entrada: Parâmetro nivel
    Tarefa: Obter texto, lacunas, gabarito do dicionáro para cada nível; 
            chamar função que recebe as resposta para cada lacuna do nível.            
    Saída: Parâmetro nível, tipo 'string'.
    """
    texto, lacunas, gabarito = consulta_dicionario(nivel)
    perguntas_percorre_dicionario_nivel(texto, lacunas, gabarito) 

def pergunta_dificuldade():
  """Pergunta ao usuário a dificuldade e retorna o índice correspondente."""
  dificuldade = raw_input('> Selecione um grau de dificuldade (facil, medio ou dificil):\n')
  while True:
    if dificuldade == 'facil':
      return 'facil'
    elif dificuldade == 'medio':
      return 'medio'
    elif dificuldade == 'dificil':
      return 'dificil'
    else:
      dificuldade = raw_input('> Opcao invalida, tente novamente (facil, medio ou dificil.\n')
      
dificuldade = pergunta_dificuldade()
nivel = dificuldade
nivel_iniciar(nivel)
