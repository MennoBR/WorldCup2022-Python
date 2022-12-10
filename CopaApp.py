

from datetime import date
from time import sleep
import pygame
pygame.init()
pygame.mixer.music.load('afrente.mp3')      #adicionar a faixa a todas as pastas
pygame.mixer.music.play()
pygame.event.wait()

gpa = ['Holanda', 'Equador', 'Qatar', 'Senegal']
gpb = ['Inglaterra', 'EUA', 'Irã', 'País de Gales']
gpc = ['Argentina', 'Polônia', 'México', 'Arábia Saudita']
gpd = ['França', 'Austrália', 'Tunísia', 'Dinamarca']
gpe = ['Espanha', 'Alemanha', 'Japão', 'Costa Rica']
gpf = ['Marrocos', 'Croácia', 'Bélgica', 'Canadá']
gpg = ['Brasil', 'Suiça', 'Sérvia', 'Camarões']
gph = ['Portugal', 'Uruguai', 'Gana', 'Coréia do sul']
out = 'Itália'
cnt = 0

print('\033[44m#\033[m' * 35)
print('\033[41mBEM VINDO AO APP COPA DO MUNDO QATAR 2022!\033[m')
print('-' * 35)
print(f'===== MENU ====='
'\n[ 1 ] - Classificação da Fase de Grupos.'
'\n[ 2 ] - Classificação das Finais(Fase Playoff).'
'\n[ 3 ] - Artilharia da Competição.'
'\n[ 4 ] - Todos os Campeões das Copas.'
'\n[ 5 ] - Game - Quiz das Copas.    '  
      
'\nObs: (DIGITE 9 PARA ENCERRAR O PROGRAMA A QUALQUER MOMENTO)')


while True:
    resp = int(input('\nDigite o número da opção desejada(9 para encerrar): '))
    if resp == 1:
      print(f'Classificação Final: {date.today()}')
      print(f'\n=Grupo A=     | Pontos | \n\033[0;30;42m1o {gpa[0]}        7 \033[m \n\033[0;30;42m2o {gpa[3]}        6 \033[m \n\033[0;30;41m3o {gpa[1]}        4 \033[m \n\033[0;30;41m4o {gpa[2]}          0 \033[m')
      print(f'\n=Grupo B=     | Pontos | \n\033[0;30;42m1o {gpb[0]}     7 \033[m \n\033[0;30;42m2o {gpb[1]}            5 \033[m \n\033[0;30;41m3o {gpb[2]}            3 \033[m \n\033[0;30;41m4o {gpb[3]}  1 \033[m')
      print(f'\n=Grupo C=     | Pontos | \n\033[0;30;42m1o {gpc[0]}      6 \033[m \n\033[0;30;42m2o {gpc[1]}        4 \033[m \n\033[0;30;41m3o {gpc[2]}         4 \033[m \n\033[0;30;41m4o {gpc[3]} 3 \033[m')
      print(f'\n=Grupo D=     | Pontos | \n\033[0;30;42m1o {gpd[0]}         6 \033[m \n\033[0;30;42m2o {gpd[1]}      6 \033[m \n\033[0;30;41m3o {gpd[2]}        4 \033[m \n\033[0;30;41m4o {gpd[3]}      1 \033[m')
      print(f'\n=Grupo E=     | Pontos | \n\033[0;30;42m1o {gpe[2]}          6 \033[m \n\033[0;30;42m2o {gpe[0]}        4 \033[m \n\033[0;30;41m3o {gpe[1]}       4 \033[m \n\033[0;30;41m4o {gpe[3]}     3 \033[m')
      print(f'\n=Grupo F=     | Pontos | \n\033[0;30;42m1o {gpf[0]}       7 \033[m \n\033[0;30;42m2o {gpf[1]}        5 \033[m \n\033[0;30;41m3o {gpf[2]}        4 \033[m \n\033[0;30;41m4o {gpf[3]}         0 \033[m')
      print(f'\n=Grupo G=     | Pontos | \n\033[0;30;42m1o {gpg[0]}         6 \033[m \n\033[0;30;42m2o {gpg[1]}          6 \033[m \n\033[0;30;41m3o {gpg[3]}       4 \033[m\n\033[0;30;41m4o {gpg[2]}         1 \033[m')
      print(f'\n=Grupo H=     | Pontos | \n\033[0;30;42m1o {gph[0]}       6 \033[m \n\033[0;30;42m2o {gph[3]}  4 \033[m \n\033[0;30;41m3o {gph[1]}        4 \033[m \n\033[0;30;41m4o {gph[2]}           3 \033[m')

      print('\nLegenda: Seleções em \033[0;30;42mVERDE\033[m estão CLASSIFICADAS para a próxima fase.'
            '         \nSeleções em \033[0;30;41mVERMELHO\033[m estão ELIMINADAS DA COPA.')

    if resp == 2:
        print(f'\n##### FASE OITAVAS DE FINAL #####')
        print('Seleções em \033[0;30;42mVERDE\033[m estão classificadas á próxima fase.')
        print(f'\n\033[0;30;42m{gpa[0]}\033[m      3     x     1  \033[0;30;41m{gpb[1]}\033[m             ========  \033[0;30;42m{gpb[0]}\033[m    3   x   0     \033[0;30;41m{gpa[3]}\033[m |')
        print(f'\n\033[0;30;42m{gpc[0]}\033[m    2     x     1  \033[0;30;41m{gpd[1]}\033[m       ========  \033[0;30;42m{gpd[0]}\033[m        3   x   1     \033[0;30;41m{gpc[1]}\033[m |')
        print(f'\n\033[0;30;41m{gpe[2]}\033[m        1 (1) x (3) 1  \033[0;30;42m{gpf[1]}\033[m         ========  \033[0;30;41m{gpe[0]}\033[m     0 (1) x (3) 0  \033[0;30;42m{gpf[0]}\033[m |')
        print(f'\n\033[0;30;42m{gpg[0]}\033[m       4     x     1  \033[0;30;41m{gph[3]}\033[m   ========  \033[0;30;42m{gph[0]}\033[m      6   x   1       \033[0;30;41m{gpg[1]}\033[m |')

        print(f'\n##### FASE QUARTAS DE FINAL #####')
        print(f'\n\n\033[0;30;41m{gpa[0]}\033[m 2 (3) x (4) 2 \033[0;30;42m{gpc[0]}\033[m  =======  {gpb[0]}  x  {gpd[0]} |')
        print(f'\n\n\033[0;30;41m{gpg[0]}\033[m  1 (2) x (4) 1  \033[0;30;42m{gpf[1]}\033[m   =======  {gpf[0]}  x  {gph[0]} |')

        print(f'\n##### SEMI-FINAIS #####')

        print(f'\n##### DISPUTA DE 3o LUGAR #####')

        print(f'\n##### FINAL DA COPA DO MUNDO 2022 QATAR #####')

    if resp == 3:
        print(f'\nARTILHARIA DA COPA 2022: ')
        print(f'(*ÚLTIMA ATUALIZAÇÃO: {date.today()})')
        print( '\n5 Gols: Mbappé (FRA). '
      '\n3 Gols: Richarlison(BRA), Saka(ING), Giroud(FRA), Messi(ARG), Morata(ESP), Valencia(EQU) e Gakpo(HOL).'
      '\n2 Gols: Arrascaeta(URU), Lewandowski(POL), Goodwin(AUS), Mitrovic(SER), Kramaric(CRO) '
      '\n        Bruno Fernandes(POR), Ferran(ESP), Kudus(GAN), Aldawsari(SAU) e Taremi(IRÃ).')

    elif resp == 4:
        print('#' * 10)
        print('\nAs Seleções Campeãs da Copa do Mundo são:')
        print(f'\n5 Títulos: {gpg[0]}.')
        print(f'\n4 Títulos: {gpe[1]} e {out}.')
        print(f'\n2 Títulos: {gph[1]}, {gpc[0]} e {gpd[0]}.')
        print(f'\n1 Título: {gpe[0]} e {gpb[0]}.')

    elif resp == 5:
        print('\nGAME QUIZ DAS COPAS')
        print('\n\033[0;30;41mO Game ainda não está pronto :( Voltando ao Menu principal...\033[m')
        sleep(2.5)

    if resp == 9:
        sleep(0.6)
        print('\n\033[0;30;45mPROGRAMA ENCERRADO! ATÉ LOGO!\033[m')
        break

    if resp > 5 and resp != 9:
        print('\nOPÇÃO INVÁLIDA! TENTE NOVAMENTE...')




      

