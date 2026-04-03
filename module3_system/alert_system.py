import winsound

def trigger_alert(decision):

    level = decision["alert_level"]

    if level == "HIGH RISK":
        print("🚨 HIGH RISK ALERT!")
        winsound.Beep(1500, 700)

    elif level == "DROWSY":
        print("⚠️ DROWSY ALERT")
        winsound.Beep(1000, 400)

    else:
        print("✅ SAFE")