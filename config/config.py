"""Global configuration for the API Automation Framework."""

# ---- API Base URLs ----
JSONPLACEHOLDER_URL = "https://jsonplaceholder.typicode.com"
REQRES_URL = "https://reqres.in/api"

# ---- HTTP timeouts (seconds) ----
TIMEOUT = 15

# ---- Default headers ----
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

# ---- reqres.in requires this header on free tier ----
REQRES_HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "x-api-key": "reqres-free-v1",
}