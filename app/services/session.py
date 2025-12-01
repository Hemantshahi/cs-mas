class SessionService:
    def __init__(self):
        self.sessions = {}
        self.logs = []

    def append_message(self, user_id, message, gps=None):
        self.sessions.setdefault(user_id, []).append({
            "message": message,
            "gps": gps
        })

    def get_context(self, user_id):
        return self.sessions.get(user_id, [])[-5:]

    def log_incident(self, user_id, triage, notify):
        self.logs.append({
            "user": user_id,
            "triage": triage,
            "notify": notify
        })
