## Script para limpar arquivos temporarios do windows: 
# %temp%
# temp
# recent
# prefetch

import time
import pyautogui
import os
from tkinter import *

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

JanelaPrincipal = Tk()

JanelaPrincipal.title("Limpar Arquivos")
JanelaPrincipal.geometry("50x50")

TextoInicial = Label(JanelaPrincipal, text="Limpeza de Arquivos Temporarios\n Escolha um diretório para excluir.\n=========================")
TextoInicial.grid(column=0, row=0,padx=10,pady=10)


botao_temp = Button(JanelaPrincipal, text="Temp", command=temp)
botao_temp.grid(column=0, row=1)

botao_tempadm = Button(JanelaPrincipal, text="%Temp%", command=temp_directory)
botao_temp.grid(column=0, row=2)

botao_prefetch = Button(JanelaPrincipal, text="Prefetch", command=prefetch)
botao_prefetch.grid(column=0, row=3)

botao_recent = Button(JanelaPrincipal, text="Recent", command=recent)
botao_recent.grid(column=0, row=4)

botao_apagarlixeira = Button(JanelaPrincipal, text="Apagar Lixeira", command=apagar_lixeira)
botao_apagarlixeira.grid(column=0, row=5)

botao_apagartudo = Button(JanelaPrincipal, text="Apagar Todos", command=apagar_tudo)
botao_apagartudo.grid(column=0, row=6)

JanelaPrincipal.mainloop()








