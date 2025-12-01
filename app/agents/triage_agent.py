class TriageAgent:
    HIGH_KEYWORDS = {"bleeding", "unconscious", "stab", "attack", "hurt", "fire", "gun"}
    MEDIUM_KEYWORDS = {"fight", "harass", "theft", "robbed", "injury"}

    def classify(self, text: str):
        t = (text or "").lower()
        for k in self.HIGH_KEYWORDS:
            if k in t:
                return {"severity": "high", "actions": ["call_emergency"], "confidence": 0.95}
        for k in self.MEDIUM_KEYWORDS:
            if k in t:
                return {"severity": "medium", "actions": ["notify_security"], "confidence": 0.8}
        return {"severity": "low", "actions": ["log_only"], "confidence": 0.6}
