import requests

BOT_TOKEN = "8854287711:AAFB-USbdvJkbCViHbFQAriM5iUI_iUKQMI"
CHAT_ID = "1063007171"


def send_telegram_alert(message):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": f"🚨 IDRP-AIS ALERT 🚨\n\n{message}"
    }

    try:

        response = requests.post(
            url,
            data=data
        )

        print("STATUS CODE:", response.status_code)
        print("RESPONSE:", response.text)

    except Exception as e:

        print("Telegram Error:", e)