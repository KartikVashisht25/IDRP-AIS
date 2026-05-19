import pygame
import threading
import time

from module3_system.telegram_alert import (
    send_telegram_alert
)

pygame.mixer.init()

ALERT_SOUND = "Assets/alert.mp3"

last_telegram_alert = 0
telegram_cooldown = 15

sound_playing = False


def play_alert():

    global sound_playing

    try:

        if not pygame.mixer.music.get_busy():

            pygame.mixer.music.load(ALERT_SOUND)

            pygame.mixer.music.play(-1)

            sound_playing = True

    except Exception as e:

        print("Alert Sound Error:", e)


def stop_alert():

    global sound_playing

    pygame.mixer.music.stop()

    sound_playing = False


def trigger_sound_alert():

    global sound_playing

    if not sound_playing:

        threading.Thread(
            target=play_alert,
            daemon=True
        ).start()


def trigger_telegram_alert(message):

    global last_telegram_alert

    current_time = time.time()

    if current_time - last_telegram_alert > telegram_cooldown:

        send_telegram_alert(message)

        last_telegram_alert = current_time


def trigger_alert(message="HIGH RISK ALERT"):

    trigger_sound_alert()

    trigger_telegram_alert(message)