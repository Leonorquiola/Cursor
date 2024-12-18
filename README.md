# Cursor
# Mouse Activity Script

Este proyecto es un script en Python diseñado para simular actividad del mouse en ventanas de Google Chrome con URLs permitidas. Cambia automáticamente entre pestañas si la URL activa no está en la lista permitida y detecta inactividad del usuario antes de mover el mouse.

## Características

- **Detección de inactividad**: Mueve el mouse solo cuando no hay actividad del usuario en un periodo de tiempo determinado (5 minutos por defecto).
- **Cambio de pestañas basado en URL**: Cambia a una pestaña permitida si la URL activa no está en la lista de URLs permitidas.
- **Lista de URLs permitidas y bloqueadas**: Mueve el mouse solo en las URLs especificadas y evita URLs bloqueadas.
- **Intervalo aleatorio y movimiento aleatorio del mouse**: Añade intervalos y movimientos aleatorios para simular actividad humana.

## Requisitos

- **macOS**: Este script usa `osascript` (AppleScript), que solo funciona en macOS, para cambiar entre pestañas en Google Chrome.
- **Google Chrome** en modo de depuración remota.

## Instalación

### 1. Clonar el repositorio

Clona este repositorio a tu máquina local:

```bash
git clone https://github.com/tu_usuario/mouse-activity-script.git
cd mouse-activity-script

2. Crear un entorno virtual (opcional, pero recomendado)
Es recomendable crear un entorno virtual para instalar las dependencias:
python3 -m venv venv
source venv/bin/activate

3. Instalar las dependencias
Este proyecto utiliza las siguientes bibliotecas:

pyautogui: Para mover el mouse.
requests: Para realizar solicitudes HTTP a la API de depuración de Chrome.
pynput: Para detectar la actividad del mouse y teclado.
Instala las dependencias usando pip:

pip3 install pyautogui requests pynput

4. Habilitar el modo de depuración remota en Chrome
Para que el script funcione, necesitas iniciar Google Chrome en modo de depuración remota. Cierra todas las ventanas de Chrome y luego abre una nueva ventana usando el siguiente comando en la terminal:

/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9223

/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9223 --profile-directory="Profile 13"

Este comando habilita un servidor de depuración en el puerto 9222, al cual el script se conectará para obtener las URLs de las pestañas abiertas.

5. Configurar permisos de accesibilidad en macOS
Para que el script controle el mouse y detecte la actividad del teclado, necesitas otorgar permisos de accesibilidad.

Ve a Preferencias del Sistema > Seguridad y Privacidad > Privacidad > Accesibilidad.
Agrega Python y tu editor de código (por ejemplo, Visual Studio Code) a la lista de aplicaciones permitidas.
Uso
Ejecuta el script desde la terminal:

python3 main.py

El script comenzará a monitorear la actividad del usuario y a mover el mouse en las URLs permitidas solo después de un periodo de inactividad.

