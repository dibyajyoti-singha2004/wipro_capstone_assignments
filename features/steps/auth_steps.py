"""Step definitions for auth.feature."""

from behave import when, then
from framework.api_client import APIClient
from framework.logger import get_logger
from config.config import REQRES_URL, REQRES_HEADERS

logger = get_logger()


# ---------- WHEN ----------

@when('I register with email "{email}" and password "{password}"')
def step_register(context, email, password):
    logger.info(f"POST /register - {email}")
    client = APIClient(REQRES_URL, REQRES_HEADERS)
    context.response = client.post(
        "/register", json={"email": email, "password": password}
    )


@when('I login with email "{email}" and password "{password}"')
def step_login(context, email, password):
    logger.info(f"POST /login - {email}")
    client = APIClient(REQRES_URL, REQRES_HEADERS)
    context.response = client.post(
        "/login", json={"email": email, "password": password}
    )


@when('I login with email "{email}" and no password')
def step_login_no_password(context, email):
    logger.info(f"POST /login - {email} (no password)")
    client = APIClient(REQRES_URL, REQRES_HEADERS)
    context.response = client.post("/login", json={"email": email})


@when("I request reqres users page {page:d}")
def step_reqres_users(context, page):
    logger.info(f"GET /users?page={page}")
    client = APIClient(REQRES_URL, REQRES_HEADERS)
    context.response = client.get("/users", params={"page": page})


@when('I create a reqres user with name "{name}" and job "{job}"')
def step_reqres_create(context, name, job):
    logger.info(f"POST /users - {name}")
    client = APIClient(REQRES_URL, REQRES_HEADERS)
    context.response = client.post("/users", json={"name": name, "job": job})


# ---------- THEN ----------

@then("the response should contain a token")
def step_check_token(context):
    data = context.response.json()
    assert "token" in data and data["token"], f"No token: {data}"
    logger.info(f"Token received: {data['token'][:20]}...")


@then('the error message should mention "{keyword}"')
def step_check_error(context, keyword):
    data = context.response.json()
    text = str(data).lower()
    assert keyword.lower() in text, f"Expected '{keyword}' in: {data}"
    logger.info(f"Error mentions: {keyword}")


@then("the response should contain a page number")
def step_check_page(context):
    data = context.response.json()
    assert "page" in data, f"No page field: {data}"
    logger.info(f"Page: {data['page']} | Total: {data.get('total')}")