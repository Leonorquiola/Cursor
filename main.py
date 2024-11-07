import time
import pyautogui
import requests
import json
import random
import subprocess
from pynput import mouse, keyboard

# Configuración de URLs permitidas y bloqueadas
allowed_urls = [
    "https://dev.new.expensify.com:8082/",
    "https://app.slack.com/client/E03025Z7DT4/C07KY1LMXEF",
    "https://feather.openai.com/campaigns/a63becfe-faa1-4eb7-8439-12e5fc54f4e6?tab=tasks&tasks-tab=in_progress"
]
blocked_urls = ["https://www.youtube.com/"]

# Tiempo de inactividad (en segundos) antes de mover el mouse
inactivity_timeout = 20  # 20 segundos

# Variables globales para la detección de inactividad
last_activity_time = time.time()

# Función para obtener el último tiempo de actividad
def get_last_activity_time():
    global last_activity_time
    return last_activity_time

# Funciones para actualizar el tiempo de la última actividad
def on_mouse_move(x, y):
    """
    Actualiza el tiempo de la última actividad del mouse.
    """
    global last_activity_time
    last_activity_time = time.time()

def on_key_press(key):
    """
    Actualiza el tiempo de la última actividad del teclado.
    """
    global last_activity_time
    last_activity_time = time.time()

# Configura los escuchadores de eventos para mouse y teclado
mouse_listener = mouse.Listener(on_move=on_mouse_move)
keyboard_listener = keyboard.Listener(on_press=on_key_press)
mouse_listener.start()
keyboard_listener.start()

# Función para obtener la URL de la pestaña activa en Chrome
def get_active_tab_url():
    """
    Obtiene la URL de la pestaña activa de Google Chrome usando la API de depuración remota.
    """
    try:
        response = requests.get('http://localhost:9222/json')
        tabs = json.loads(response.text)
        for tab in tabs:
            if tab.get("type") == "page" and tab.get("url"):
                return tab.get("url")
    except Exception as e:
        print(f"Error al obtener la URL activa: {e}")
    return None

# Función para listar todas las URLs de las pestañas abiertas en Chrome
def get_all_tab_urls():
    """
    Devuelve una lista de URLs de todas las pestañas abiertas en Google Chrome.
    """
    try:
        response = requests.get('http://localhost:9222/json')
        tabs = json.loads(response.text)
        return [tab.get("url") for tab in tabs if tab.get("type") == "page" and tab.get("url")]
    except Exception as e:
        print(f"Error al listar las URLs de las pestañas: {e}")
    return []

# Cambia a una ventana con una URL permitida
def switch_to_allowed_url():
    """
    Cambia a una pestaña que contenga una URL permitida. Usa AppleScript para controlar Google Chrome.
    """
    tabs = get_all_tab_urls()
    for tab_url in tabs:
        if tab_url in allowed_urls:
            # Cambia a esta ventana usando AppleScript
            script = f'''
            osascript -e 'tell application "Google Chrome"
                repeat with w in windows
                    set i to 0
                    repeat with t in tabs of w
                        set i to i + 1
                        if URL of t is "{tab_url}" then
                            set active tab index of w to i
                            set index of w to 1
                            return
                        end if
                    end repeat
                end repeat
            end tell'
            '''
            subprocess.run(script, shell=True, check=True)
            print(f"Cambiando a la pestaña con URL permitida: {tab_url}")
            return True
    print("No se encontraron pestañas con URLs permitidas.")
    return False

# Función para mover el mouse en un rango aleatorio
def move_mouse_randomly():
    """
    Mueve el mouse de forma aleatoria en un pequeño rango para simular actividad.
    """
    x_offset = random.randint(-20, 20)
    y_offset = random.randint(-20, 20)
    pyautogui.moveRel(x_offset, y_offset)

# Función principal para verificar inactividad y mover el mouse
def move_mouse_in_url():
    """
    Verifica la inactividad y URL permitida. Cambia a una pestaña permitida si no estamos en una,
    y mueve el mouse si estamos en una pestaña permitida y ha habido inactividad suficiente.
    """
    while True:
        current_time = time.time()
        active_url = get_active_tab_url()

        # Verifica si ha habido inactividad suficiente
        if (current_time - get_last_activity_time() > inactivity_timeout):
            # Si la URL actual no es permitida, intenta cambiar a una permitida
            if active_url not in allowed_urls or active_url in blocked_urls:
                if not switch_to_allowed_url():
                    print("Esperando una pestaña permitida...")
            else:
                # Si estamos en una URL permitida, mueve el mouse
                move_mouse_randomly()
                print(f"Moviendo el mouse en la URL: {active_url}")
                last_activity_time = current_time  # Resetea el tiempo de inactividad después del movimiento
        else:
            print("La URL actual no está permitida o el usuario está activo. Esperando...")
        
        # Espera un intervalo aleatorio entre 5 y 10 segundos antes de la siguiente verificación
        time.sleep(random.uniform(5, 10))

if __name__ == "__main__":
    move_mouse_in_url()
