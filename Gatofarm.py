from time import monotonic, sleep
from kandinsky import fill_rect, draw_string
from ion import keydown, KEY_ONE, KEY_TWO, KEY_THREE, KEY_ZERO, KEY_EXE

menu = 0
click = 0.0
click_interval = 0.2
auto_click_rate = 0.1
autoclick_active = True

last_click_time = 0
last_autoclick_time = 0

def clear_screen():
    fill_rect(0, 0, 320, 240, "white")

clear_screen()

while True:
    now = monotonic()

    if menu == 0:
        clear_screen()
        draw_string("[1] Clicker", 100, 50)
        draw_string("[2] Stats", 100, 70)
        draw_string("[3] Quitter", 100, 90)
        sleep(0.2)

        if keydown(KEY_ONE):
            menu = 1
            clear_screen()
            sleep(0.2)
        elif keydown(KEY_TWO):
            menu = 2
            clear_screen()
            sleep(0.2)
        elif keydown(KEY_THREE):
            break

    elif menu == 1:
        # Autoclick toutes les 0.5 secondes
        if autoclick_active and now - last_autoclick_time > 0.5:
            click += auto_click_rate
            click = int(click * 10) / 10
            last_autoclick_time = now

        # Click manuel avec intervalle
        if keydown(KEY_EXE) and now - last_click_time > click_interval:
            click += 1
            last_click_time = now

        # Toggle autoclick
        if keydown(KEY_ONE):
            autoclick_active = not autoclick_active
            sleep(0.3)  # anti-rebond

        # Retour menu
        if keydown(KEY_ZERO):
            menu = 0
            clear_screen()
            sleep(0.3)

        clear_screen()
        draw_string("Clicks : " + str(click), 10, 10)
        draw_string("Auto_click : " + str(auto_click_rate), 10, 30)
        draw_string("Auto ON : " + str(autoclick_active), 10, 50)
        draw_string("[EXE] +1 Click", 10, 120)
        draw_string("[1] Toggle AutoClick", 10, 140)
        draw_string("[0] Retour menu", 10, 200)

        sleep(0.05)

    elif menu == 2:
        clear_screen()
        draw_string("Stats non implémentées.", 50, 100)
        draw_string("[0] Retour menu", 50, 130)
        sleep(0.2)
        if keydown(KEY_ZERO):
            menu = 0
            clear_screen()
            sleep(0.3)
