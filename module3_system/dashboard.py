def show_dashboard(features, prediction, decision):

    print("\n====== DRIVER STATUS ======")
    print(f"EAR: {features['ear']}")
    print(f"Blink Rate: {features['blink_rate']}")
    print(f"Closure Duration: {features['eye_closure_duration']}")
    print(f"Risk: {prediction['risk_label']}")
    print(f"Alert: {decision['alert_level']}")
    print("===========================\n")