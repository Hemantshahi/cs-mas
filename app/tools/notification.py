def send_notification(recipients, message):
    print(f"[SIM NOTIFY] -> {recipients}: {message}")
    return {"delivered": True, "recipients": recipients}
