from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os

from utils import fibonacci, primes, lcm, hcf
from ai import ask_ai

load_dotenv()

EMAIL = os.getenv("OFFICIAL_EMAIL")

app = FastAPI()

def success(data):
    return {
        "is_success": True,
        "official_email": EMAIL,
        "data": data
    }

def error(status=400):
    raise HTTPException(
        status_code=status,
        detail={"is_success": False}
    )

@app.post("/bfhl")
def bfhl(payload: dict):
    if len(payload) != 1:
        error()

    key, value = next(iter(payload.items()))

    try:
        if key == "fibonacci":
            if not isinstance(value, int):
                error()
            return success(fibonacci(value))

        if key == "prime":
            if not isinstance(value, list):
                error()
            return success(primes(value))

        if key == "lcm":
            if not isinstance(value, list) or not value:
                error()
            return success(lcm(value))

        if key == "hcf":
            if not isinstance(value, list) or not value:
                error()
            return success(hcf(value))

        if key == "AI":
            if not isinstance(value, str):
                error()
            return success(ask_ai(value))

        error()

    except:
        error(422)

@app.get("/health")
def health():
    return {
        "is_success": True,
        "official_email": EMAIL
    }
