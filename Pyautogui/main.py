import pyautogui as p
import os
import pandas as pd
import time
import io

p.hotkey("win", "r")
p.sleep(0.5)

p.write("Chrome")
p.sleep(0.5)
p.press('enter')
p.sleep(0.5)

p.write('https://rpachallenge.com/')
p.press('enter')
p.sleep(3)

janela = p.getActiveWindow()
janela.maximize()

data = pd.read_excel('challenge.xlsx')

regiao_inputs = (519,178,1043,796)

botao_iniciar = p.locateCenterOnScreen('StartBtn.png', confidence=0.9)
p.click(botao_iniciar)

def preencher_input(row, column):
    xPesquisa, yPesquisa = p.locateCenterOnScreen(f'{column.replace(" ", "")}.png', confidence=0.8, region=regiao_inputs)
    p.click(xPesquisa, yPesquisa+20)
    p.write(str(row[column]))

for index, row in data.iterrows():

    columns = data.columns.tolist()
    for column in columns:
        preencher_input(row, column)

    botao_submit = p.locateCenterOnScreen('SubmitBtn.png', confidence=0.9, region=regiao_inputs)
    p.click(botao_submit)

time.sleep(5)

p.screenshot().save("./score_pyautogui.png")
p.hotkey('ctrl', 'w')