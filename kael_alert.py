import time
from emotion_detector import detectar_emocion
from telegram import enviar_alerta
from datetime import datetime, timedelta

ultima_alerta = datetime.min

def main():
    global ultima_alerta

    while True:
        emocion = detectar_emocion()

        if emocion:
            ahora = datetime.now()
            if ahora - ultima_alerta > timedelta(minutes=15):
                mensaje = f"[ALERTA EMOCIONAL] Se ha detectado una emoción: {emocion}"
                enviar_alerta(mensaje)
                ultima_alerta = ahora

        time.sleep(5)

if __name__ == "__main__":
    main()