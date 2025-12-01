from fastapi import FastAPI
from pydantic import BaseModel
from app.agents.llm_agent import LLM_Agent
from app.services.memory import MemoryBank
from app.services.session import SessionService
from app.agents.triage_agent import TriageAgent
from app.tools.notification import send_notification

app = FastAPI()
session_svc = SessionService()
triage = TriageAgent()
llm = LLM_Agent()
memory = MemoryBank()

class Report(BaseModel):
    user_id: str
    message: str
    gps: dict | None = None

@app.post("/report")
async def report_incident(r: Report):
    # Session me message add karo
    session_svc.append_message(r.user_id, r.message, r.gps)

    # LLM analyze
    llm_result = llm.analyze_message(r.message)

    # Existing triage
    triage_result = triage.classify(r.message)

    # Long-term memory me save
    memory.save_incident(r.user_id, r.message, triage_result["severity"])

    # Notify if high severity
    notify = {}
    if triage_result.get("severity") == "high":
        recipients = ["security@campus.example"]
        message = f"High severity incident by {r.user_id}: {r.message}. GPS: {r.gps}"
        notify = send_notification(recipients, message)

    # Log session
    session_svc.log_incident(r.user_id, triage_result, notify)

    return {
        "status": "ok",
        "triage": triage_result,
        "llm": llm_result,
        "notification": notify,
        "session_context": session_svc.get_context(r.user_id)
    }

