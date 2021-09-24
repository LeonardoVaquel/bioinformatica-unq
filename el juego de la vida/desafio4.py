#!/usr/bin/env python3

# Diseñá un juego rpg interactivo sobre la expresión génica que se muestre en la consola 
# (que se ejecute mediante CLI de manera similar a lo visto en el Bashaton).
# Tené en cuenta que lo vas a tener que compartir con la clase.

from threading import Timer

class STYLES:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   ITALIC = '\033[3m'
   END = '\033[0m'

PREGUNTAS = [
    {
        'question': '¿Dónde ocurre la primer parte de la Transcripción?',
        'options': [
            'En el Citoplasma',
            'En el Núcleo',
            'En los Ribosomas'
            ], 
        'answer': '2'
    },
    {
        'question': '¿Cuál es la funsión del ADN?',
        'options': [
            'Guiar la síntesis del ARN',
            'Metabolizar las proteínas',
            'Ninguna'
            ], 
        'answer': '1'
    },
    {
        'question': '¿Cómo es conocido también el ARN Mensajero?',
        'options': [
            'ARN Cartero',
            'ARN Comunicador',
            'ARN Polimerasa',
            'Todas son correctas'
            ], 
        'answer': '3'
    },
    {
        'question': '¿Qué realiza el ARNm luego de ser sintetizado?',
        'options': [
            'Se fusiona con el código genético del ADN',
            'Transmuta en una proteína',
            'Sale del núcleo y mediante el citosol llega a los ribosomas'
            ], 
        'answer': '3'
    },
    {
        'question': '¿Qué sucede en los ribosomas?',
        'options': [
            'El ARNm se empalman con los aminoácidos para generar la proteína',
            'El ARNm autoproduce encimas proteicas'
            ], 
        'answer': '1'
    },
    {
        'question': '¿Quién ayuda al anterior proceso?',
        'options': [
            'El ADN',
            'El ARN Mensajero',
            'El ARN de Transferencia',
            'El ADN y el ARN Mensajero',
            'Nadie'
            ], 
        'answer': '3'
    },
    {
        'question': '¿Cómo se llama esa etapa?',
        'options': [
            'Traducción',
            'Interpretación',
            'Amalgamación'
            ], 
        'answer': '1'
    }
]

NO = '2'
SI = '1'
SIN_RESPONDER = ''

player = {
    'name': '',
    'correctas': 0,
    'incorrectas': 0
}

def bold(text):
    return f'{STYLES.BOLD}{text}{STYLES.END}'

def underline(text):
    return f'{STYLES.UNDERLINE}{text}{STYLES.END}'

def italic(text):
    return f'{STYLES.ITALIC}{text}{STYLES.END}'

def yellow(text):
    return f'{STYLES.YELLOW}{text}{STYLES.END}'

def red(text):
    return f'{STYLES.RED}{text}{STYLES.END}'

def green(text):
    return f'{STYLES.GREEN}{text}{STYLES.END}'

def cyan(text):
    return f'{STYLES.CYAN}{text}{STYLES.END}'

def darkcyan(text):
    return f'{STYLES.DARKCYAN}{text}{STYLES.END}'

def no_respondio(answer):
    return answer == SIN_RESPONDER

def respuesta_negativa(answer):
    return answer == NO

def respuesta_positiva(answer):
    return answer == SI

def respuesta_correcta(respuesta, opcion):
    return respuesta == opcion

def respuestas_correctas(player):
    return player['correctas']

def respuestas_incorrectas(player):
    return player['incorrectas']

def bot_says(text):
    print(f'{BOT} {text}')

def player_answer(player):
    return input(f'{player["name"]} ')

def options(options):
    print(underline('OPCIONES')+':')
    for idx, option in enumerate(options):
        print(bold(idx+1), italic(option))

def show_scoreboard(player):
    print(bold(darkcyan('============================')))
    print(f'{bold(darkcyan("====="))}  {bold(darkcyan(underline("PUNTAJE")))}: {respuestas_correctas(player) - respuestas_incorrectas(player)}      {bold(darkcyan("====="))}')
    print(f'{bold(darkcyan("====="))}  {bold(green(underline("CORRECTAS")))}: {respuestas_correctas(player)}    {bold(darkcyan("====="))}')
    print(f'{bold(darkcyan("====="))}  {bold(red(underline("INCORRECTAS")))}: {respuestas_incorrectas(player)}  {bold(darkcyan("====="))}')
    print(bold(darkcyan('============================')))

def analizar_respuesta(respuesta, player):
    if respuesta:
        bot_says(green(italic('¡Correcto!')))
        bot_says(italic('Sumaste un punto\n'))
        player['correctas'] += 1
    else:
        bot_says(red(italic('Incorrecto :(\n')))
        player['incorrectas'] += 1

def final(player):
    bot_says(italic('Bien, esa fue la última pregunta'))
    bot_says(italic('Veamos como te fue...'))
    show_scoreboard(player)

def make_question(question_number, question, player):
    bot_says(bold(f'Pregunta número {question_number}'))
    bot_says(italic(question['question']))
    options(question['options'])
    analizar_respuesta(respuesta_correcta(player_answer(player), question['answer']), player)

def question_generator(player):
    for idx, obj in enumerate(PREGUNTAS):
        make_question(str(idx+1), obj, player)
    final(player)

def start_game(player):
    comenzar = input(f'{player["name"]} ').upper()
    if no_respondio(comenzar) or respuesta_negativa(comenzar):
        bot_says(italic('Pense que eramos amigxs :('))
        bot_says(italic('¿No querés jugar?'))
        start_game(player)
    else:
        bot_says(italic('Yeeep! :D Comencemos...\n'))
        question_generator(player)

def titulo():
    print(bold(green('===================================================')))
    print(bold(green('===================================================')))
    print(f'{bold(green("==========="))} {yellow(bold("Bienvenidx al juego del ADN"))} {bold(green("==========="))}')
    print(bold(green('===================================================')))
    print(bold(green('===================================================')))

def presentacion(player):
    print('\nHola, mi nombre es << Boti >> y voy a estar jugando con vos')
    bot_says(italic("¿Cúal es tú nombre?"))
    player_name = input('Anónimx > ')
    bot_says(italic(f'Hola {player_name}, un placer conocerte :D'))
    player['name'] = bold(yellow(player_name+' >'))
    return player

BOT = darkcyan(bold('Boti >'))
titulo()
player = presentacion(player)
bot_says(italic('El juego consiste en preguntas y respuesta.'))
bot_says(italic(f'¿Queres comenzar?'))
options(['SI', 'NO'])
start_game(player)

