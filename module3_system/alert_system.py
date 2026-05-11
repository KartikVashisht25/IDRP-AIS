from playsound import playsound
import os

# Toggle system anytime
USE_CUSTOM_SOUND = True   # 👈 TURN OFF faaaah sound

# Absolute path (IMPORTANT)
CUSTOM_SOUND_PATH = r"C:\Users\kvash\OneDrive\Desktop\IDRP(AIS)\Assets\alert.wav"


def trigger_alert(decision):
    level = decision.get("alert_level", "")

    print("🚨 ALERT TRIGGERED:", level)

    if level == "HIGH RISK":
        try:
            if USE_CUSTOM_SOUND:
                playsound(CUSTOM_SOUND_PATH)
            else:
                print("🔊 Fallback beep (no custom sound)")
        except Exception as e:
            print("❌ SOUND ERROR:", e)








# import os

# # 🔄 Toggle system
# USE_CUSTOM_SOUND = True   # 👈 TURN OFF faaaah sound

# CUSTOM_SOUND_PATH = r"C:\Users\kvash\OneDrive\Desktop\IDRP(AIS)\Assets\alert.wav"


# def trigger_alert(decision):
#     level = decision.get("alert_level", "")

#     print("🚨 ALERT:", level)

#     if level == "HIGH RISK":

#         try:
#             if USE_CUSTOM_SOUND:
#                 from playsound import playsound
#                 playsound(CUSTOM_SOUND_PATH)
#             else:
#                 # ✅ Default Windows beep
#                 import winsound
#                 winsound.MessageBeep()
                
#         except Exception as e:
#             print("❌ SOUND ERROR:", e)