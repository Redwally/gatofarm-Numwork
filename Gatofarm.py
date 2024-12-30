from math import *
from time import *
from kandinsky import *
from ion import *

menu = 0
click = 1
click_interval = 0.2
auto_click = 0.1
activate_autoclik = True

def autoclick():
    global click
    global auto_click
    if activate_autoclik is True:

        click += auto_click  # Incrémente click avec auto_click
        click = round(click, 1)  # Arrondi à 1 chiffre après la virgule
        click = int(click * 10) / 10  # Forcer à garder seulement un chiffre après la virgule
        sleep(0.5)  # Délai d'une seconde


    




        

def sup():
    fill_rect(1, 1, 320, 240, "white")  # Efface l'écran

while True:
    if menu == 0:
        sleep(0.2)
        draw_string("[1]-clicker", 100, 50)
        draw_string("[2]-stats", 100, 70)
        draw_string("[3]-quit", 100, 90)

        if keydown(KEY_ONE):  # Pas besoin de "== True", `keydown` renvoie déjà un booléen
            menu = 1
            sup()
        elif keydown(KEY_TWO):
            menu = 2
            sup()
        elif keydown(KEY_THREE):
            break
    
    if menu == 1:
        autoclick()
        draw_string("click: "+str(click), 10, 10)
        draw_string("Auto_click:"+str(auto_click),10,30)
        draw_string("Auto_click:"+str(activate_autoclik),10,50)
        draw_string("[1]-Activer/desactiver autoclick",10,170)
        draw_string("[0]-Home menu",10,200)
        if keydown(KEY_ZERO):
            menu = 0
            sup()
        if keydown(KEY_EXE):
            click= click+1
            sleep(click_interval)
        
        if keydown(KEY_ONE):
            if activate_autoclik is False:
                activate_autoclik = bool(True)
                sleep(0.5)
            else:
                activate_autoclik = bool(False)
                sleep(0.5)