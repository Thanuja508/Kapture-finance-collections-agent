from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="Kapture Finance Mock Collections API")


# -----------------------------
# Mock customer database
# -----------------------------

CUSTOMER = {
    "customer_id": "CUS_1001",
    "name": "Rahul Sharma",
    "phone_last4": "4821",
    "loan_type": "Personal Loan",
    "overdue_amount": 8499,
    "days_past_due": 12
}


# -----------------------------
# Request models
# -----------------------------

class VerifyCustomerRequest(BaseModel):
    customer_name: str
    verification_value: str


class PromiseToPayRequest(BaseModel):
    customer_id: str
    amount: float
    payment_date: str


class PaymentLinkRequest(BaseModel):
    customer_id: str
    channel: str


class DispositionRequest(BaseModel):
    customer_id: str
    disposition: str
    notes: str = ""


# -----------------------------
# 1. Verify customer
# -----------------------------

@app.post("/verify_customer")
def verify_customer(data: VerifyCustomerRequest):

    verified = (
        data.customer_name.strip().lower() == CUSTOMER["name"].lower()
        and data.verification_value == CUSTOMER["phone_last4"]
    )

    if verified:
        return {
            "verified": True,
            "customer_id": CUSTOMER["customer_id"]
        }

    return {
        "verified": False,
        "customer_id": ""
    }


# -----------------------------
# 2. Log Promise To Pay
# -----------------------------

@app.post("/log_promise_to_pay")
def log_promise_to_pay(data: PromiseToPayRequest):

    return {
        "status": "recorded",
        "ptp_id": "PTP_5001",
        "customer_id": data.customer_id,
        "amount": data.amount,
        "payment_date": data.payment_date,
        "recorded_at": datetime.now().isoformat()
    }


# -----------------------------
# 3. Send payment link
# -----------------------------

@app.post("/send_payment_link")
def send_payment_link(data: PaymentLinkRequest):

    return {
        "status": "sent",
        "channel": data.channel,
        "customer_id": data.customer_id,
        "payment_link": "https://pay.kapture-finance.example/PTP_5001"
    }


# -----------------------------
# 4. Mark disposition
# -----------------------------

@app.post("/mark_disposition")
def mark_disposition(data: DispositionRequest):

    return {
        "status": "recorded",
        "customer_id": data.customer_id,
        "disposition": data.disposition,
        "notes": data.notes
    }


# -----------------------------
# Health check
# -----------------------------

@app.get("/")
def health_check():
    return {
        "status": "Kapture Finance API is running"
    }