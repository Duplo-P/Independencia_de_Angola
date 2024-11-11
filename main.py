from colorama import Fore
import os 
import time

def centralizar(texto):
    largura_terminal = os.get_terminal_size().columns
    posicao_inicial = (largura_terminal - len(texto)) // 2
    os.system("clear")
    print(" " * posicao_inicial + texto.replace("*"," "))

texto = """ 
********************************11**DE**NOVEMBRO**DIA**DA**INDEPENDCIA**NACIONAL****************************************************
************************************************************************************************************************************
**********AAAA**********NNNNNN******NNNNN****GGGGGGGGGGGGGGGGGG******OOOOOOOOOOOOOO********LLLLL*******************AAAA*************
*********AAAAAA*********NNNNNNN*****NNNNN***GGGGGGGGGGGGGGGGGGGG****OOOOOOOOOOOOOOOO******LLLLLLL*****************AAAAAA************
********AAAAAAAA********NNNNNNNN****NNNNN***GGGGGG*******GGGGGG*****OOOOOOOOOOOOOOOO******LLLLLLL****************AAAAAAAA***********
*******AAAAAAAAAA*******NNNNNNNNN***NNNNN***GGGGGG******************OOOO0******OOOO0******LLLLLLL***************AAAAAAAAAA**********
******AAAAA*AAAAAA******NNNNNNNNNN**NNNNN***GGGGGG******************OOOO********OOOO******LLLLLLL**************AAAAA*AAAAAA*********
*****AAAAA***AAAAAA*****NNNNNNNNNNNNNNNNN***GGGGGG***GGGGGGGGGG*****OOOO********OOOO******LLLLLLL*************AAAAA***AAAAAA********
****AAAAAAAAAAAAAAAA****NNNNNNNNNNNNNNNNN***GGGGGG***GGGGGGGGGGG****OOOO********OOOO******LLLLLLL************AAAAAAAAAAAAAAAA*******
***AAAAAAAAAAAAAAAAAA***NNNNN*NNNNNNNNNNN***GGGGGG*******GGGGGGG****OOOO********OOOO******LLLLLLL***********AAAAAAAAAAAAAAAAAA******
***AAAAAA******AAAAAA***NNNNN**NNNNNNNNNN***GGGGGG*******GGGGGGG****OOOO0******OOOO0******LLLLLLL***********AAAAAA******AAAAAA******
***AAAAAA******AAAAAA***NNNNN***NNNNNNNNN***GGGGGG*******GGGGGGG****OOOOOOOOOOOOOOOO******LLLLLLLLLLLLLL****AAAAAA******AAAAAA******
***AAAAA********AAAAA***NNNNN****NNNNNNNN***GGGGGGGGGGGGGGGGGGG*****OOOOOOOOOOOOOOOO******LLLLLLLLLLLLLL****AAAAA********AAAAA******
***AAAAA********AAAAA***NNNNN******NNNNNN****GGGGGGGGGGGGGGGGG*******OOOOOOOOOOOOOO********LLLLLLLLLLLL*****AAAAA********AAAAA******
"""
while(True):
    
    centralizar(Fore.RED + texto + Fore.RESET)
    time.sleep(1)
    centralizar(Fore.YELLOW + texto + Fore.RESET) 
    time.sleep(1)
    centralizar(Fore.BLACK + texto + Fore.RESET)
    time.sleep(1)

