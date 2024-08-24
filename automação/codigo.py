import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("microsoftedge")
pyautogui.press("enter")    

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=1743, y=435)

pyautogui.write("anerocha@gmail.com")
pyautogui.press("tab") 
pyautogui.write("sua senha")
pyautogui.click(x=1860, y=602) 
pyautogui.press("enter")
time.sleep(3)

tabela = pd.read_csv("produtos.csv")

print(tabela)

for linha in tabela.index:
    pyautogui.click(x=1755, y=317)
    
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    pyautogui.press("enter")
    
    pyautogui.scroll(5000)
