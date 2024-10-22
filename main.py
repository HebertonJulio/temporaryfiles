## Script para limpar arquivos temporarios do windows: 
# %temp%
# temp
# recent
# prefetch

import time
import pyautogui
import os

# Tempo de espera do script começar (3 segundos).
time.sleep(1.5)

### =================== FUNCAO TEMP =================== ###
def temp():
    # ====== Abrir o executar (hotkey serve para clicar em duas teclas ao mesmo tempo) ====== #
    pyautogui.hotkey('win', 'r')
    time.sleep(0.5)

    # ====== Apaga o ultimo registro dentro do executar para evitar algum tipo de erro. ====== #
    pyautogui.press("backspace")
    time.sleep(0.5)

    # ====== Escreve "temp" na barra de executar. ====== #
    pyautogui.write("temp")
    time.sleep(0.5)

    # ====== Pressiona o enter para entrar na pasta temp ====== #
    pyautogui.press("enter")
    time.sleep(1)

    # ====== Caso peça permissão para entrar na pasta, o script aceita com a tecla enter ====== #
    pyautogui.press("enter")
    time.sleep(1)

    # ====== Seleciona todos os itens da pasta e deleta ====== #
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1.5)
    pyautogui.press('delete')
    time.sleep(0.5)

    # ====== Marca a caixinha "fazer isto com todos os arquivos" ====== #
    pyautogui.press('up')
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(0.5)

    # ====== E por fim, desce para a confirmacao de exclusao de dados temporarios ====== #
    pyautogui.press('down')
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.press('right')
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(1)


    # ====== E fecha a pasta (temp). ====== #
    pyautogui.hotkey('alt', 'f4')

### =================== FUNCAO %TEMP% =================== ###
def temp_directory():
    # ====== Abrir o executar (hotkey serve para clicar em duas teclas ao mesmo tempo) ====== #
    pyautogui.hotkey('win', 'r')
    time.sleep(0.5)

    # ====== Apaga o ultimo registro dentro do executar para evitar algum tipo de erro. ====== #
    pyautogui.press("backspace")
    time.sleep(0.5)

    # ====== Escreve "temp" na barra de executar. ====== #
    pyautogui.write("%temp%")
    time.sleep(0.5)

    # ====== Pressiona o enter para entrar na pasta temp ====== #
    pyautogui.press("enter")
    time.sleep(1)

    # ====== Caso peça permissão para entrar na pasta, o script aceita com a tecla enter ====== #
    pyautogui.press("enter")
    time.sleep(1)

    # ====== Seleciona todos os itens da pasta e deleta ====== #
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1.5)
    pyautogui.press('delete')
    time.sleep(0.5)

    # ====== Marca a caixinha "fazer isto com todos os arquivos" ====== #
    pyautogui.press('up')
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(0.5)

    # ====== E por fim, desce para a confirmacao de exclusao de dados temporarios ====== #
    pyautogui.press('down')
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.press('right')
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(1)

    # ====== E fecha a pasta (%temp%). ====== #
    pyautogui.hotkey('alt', 'f4')


### =================== FUNCAO PREFETCH =================== ###
def prefetch():
    # ====== Abrir o executar (hotkey serve para clicar em duas teclas ao mesmo tempo) ====== #
    pyautogui.hotkey('win', 'r')
    time.sleep(0.5)

    # ====== Apaga o ultimo registro dentro do executar para evitar algum tipo de erro. ====== #
    pyautogui.press("backspace")
    time.sleep(0.5)

    # ====== Escreve "prefetch" na barra de executar. ====== #
    pyautogui.write("prefetch")
    time.sleep(0.5)

    # ====== Pressiona o enter para entrar na pasta prefetch ====== #
    pyautogui.press("enter")
    time.sleep(1)

    # ====== Caso peça permissão para entrar na pasta, o script aceita com a tecla enter ====== #
    pyautogui.press("enter")
    time.sleep(1)

    # ====== Seleciona todos os itens da pasta e deleta ====== #
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1.5)
    pyautogui.press('delete')
    time.sleep(0.5)

    # ====== Marca a caixinha "fazer isto com todos os arquivos" ====== #
    pyautogui.press('up')
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(0.5)

    # ====== E por fim, desce para a confirmacao de exclusao de dados temporarios ====== #
    pyautogui.press('down')
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.press('right')
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(1)

    # ====== E fecha a pasta (prefetch). ====== #
    pyautogui.hotkey('alt', 'f4')


### =================== FUNCAO RECENT =================== ###
def recent():
    # ====== Abrir o executar (hotkey serve para clicar em duas teclas ao mesmo tempo) ====== #
    pyautogui.hotkey('win', 'r')
    time.sleep(0.5)

    # ====== Apaga o ultimo registro dentro do executar para evitar algum tipo de erro. ====== #
    pyautogui.press("backspace")
    time.sleep(0.5)

    # ====== Escreve "recent" na barra de executar. ====== #
    pyautogui.write("recent")
    time.sleep(0.5)

    # ====== Pressiona o enter para entrar na pasta recent ====== #
    pyautogui.press("enter")
    time.sleep(1)

    # ====== Caso peça permissão para entrar na pasta, o script aceita com a tecla enter ====== #
    pyautogui.press("enter")
    time.sleep(1)

    # ====== Seleciona todos os itens da pasta e deleta ====== #
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1.5)
    pyautogui.press('delete')
    time.sleep(0.5)

    # ====== Marca a caixinha "fazer isto com todos os arquivos" ====== #
    pyautogui.press('up')
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(0.5)

    # ====== E por fim, desce para a confirmacao de exclusao de dados temporarios ====== #
    pyautogui.press('down')
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.press('right')
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(1)

    # ====== E fecha a pasta (recent). ====== #
    pyautogui.hotkey('alt', 'f4')
    time.sleep(1)


## ============  FUNCAO APAGAR LIXEIRA ============ ##
def apagar_lixeira():
    os.startfile(r'shell:RecycleBinFolder')
    time.sleep(1.5)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1.5)
    pyautogui.press('delete')
    time.sleep(1.5)
    pyautogui.press('enter')
    time.sleep(1.5)
    pyautogui.press('up')
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.press("down")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.hotkey('alt', 'f4')


## ============  FUNCAO PARA APAGAR TUDO. ============ ##
def apagar_tudo():
    temp()
    temp_directory()
    prefetch()
    recent()
    apagar_lixeira()



### ======== HOME ======== ###
print("Script | Delete temporary files")
print("=" * 40)

### ======== OPCOES PARA O USUARIO ======== ### 
diretorios = {
    #numero     #nome
    1:          '1) Temp' ,  
    2:          '2) Tempdirectory',
    3:          '3) Prefetch',
    4:          '4) Recent',
    5:          '5) Lixeira',
    6:          '6) Apagar tudo.',
}

# A cada Numero na lista diretorios, o python ira imprimir o nome até chegar no ultimo da lista.
for numero, nome in diretorios.items():
    print(nome)


# ======= PEDE AO USUARIO QUE ESCOLHA UMA OPCAO DENTRO DO SCRIPT. ======= #
while True:
    try:
        resposta = int(input("Informe um número entre 1 a 6: "))
        if resposta == 1:
            pyautogui.hotkey('win', 'd')
            time.sleep(1)           
            temp()
            break 
        elif resposta == 2:
            pyautogui.hotkey('win', 'd') 
            time.sleep(1)
            temp_directory()
            break 
        elif resposta == 3:
            pyautogui.hotkey('win', 'd')
            time.sleep(1)
            prefetch()
        elif resposta == 4:
            pyautogui.hotkey('win', 'd')
            time.sleep(1)
            recent()
            break
        elif resposta == 5:
            pyautogui.hotkey('win', 'd')
            time.sleep(1)
            apagar_lixeira()
            break
        elif resposta == 6:
            pyautogui.hotkey('win', 'd')
            time.sleep(1)
            apagar_tudo()
            break
        else:
            print("Escolha uma opçao válida entre 1 a 6")
    except ValueError: 
        print("Entrada inválida, por favor, insira apenas números de 1 a 6...")












