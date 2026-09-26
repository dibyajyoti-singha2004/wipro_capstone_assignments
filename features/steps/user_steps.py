"""Step definitions for users.feature."""

from behave import when, then
from framework.api_client import APIClient
from framework.logger import get_logger
from config.config import JSONPLACEHOLDER_URL

logger = get_logger()


# ---------- WHEN ----------

@when("I request the list of users")
def step_get_users(context):
    logger.info("GET /users")
    client = APIClient(JSONPLACEHOLDER_URL)
    context.response = client.get("/users")


@when("I request user with ID {user_id:d}")
def step_get_user_by_id(context, user_id):
    logger.info(f"GET /users/{user_id}")
    client = APIClient(JSONPLACEHOLDER_URL)
    context.response = client.get(f"/users/{user_id}")


@when('I create a user with name "{name}" and email "{email}"')
def step_create_user(context, name, email):
    logger.info(f"POST /users - name={name}, email={email}")
    client = APIClient(JSONPLACEHOLDER_URL)
    context.response = client.post(
        "/users", json={"name": name, "email": email}
    )


@when('I update user {user_id:d} with name "{name}"')
def step_update_user(context, user_id, name):
    logger.info(f"PUT /users/{user_id}")
    client = APIClient(JSONPLACEHOLDER_URL)
    payload = {"id": user_id, "name": name, "email": "updated@example.com"}
    context.response = client.put(f"/users/{user_id}", json=payload)


@when('I partially update user {user_id:d} with email "{email}"')
def step_patch_user(context, user_id, email):
    logger.info(f"PATCH /users/{user_id}")
    client = APIClient(JSONPLACEHOLDER_URL)
    context.response = client.patch(f"/users/{user_id}", json={"email": email})


@when("I delete user {user_id:d}")
def step_delete_user(context, user_id):
    logger.info(f"DELETE /users/{user_id}")
    client = APIClient(JSONPLACEHOLDER_URL)
    context.response = client.delete(f"/users/{user_id}")


# ---------- THEN ----------

@then("the response status should be {status:d}")
def step_check_status(context, status):
    actual = context.response.status_code
    assert actual == status, (
        f"Expected status {status}, got {actual}. Body: {context.response.text[:200]}"
    )
    logger.info(f"Status check passed: {actual}")


@then("the response should contain {count:d} users")
def step_check_user_count(context, count):
    data = context.response.json()
    assert isinstance(data, list), f"Expected list, got {type(data)}"
    assert len(data) == count, f"Expected {count} users, got {len(data)}"
    logger.info(f"User count check passed: {len(data)}")


@then("the user name should not be empty")
def step_check_user_name(context):
    data = context.response.json()
    assert data.get("name"), f"No name in: {data}"
    logger.info(f"User name: {data['name']}")


@then("the response should contain the created user details")
def step_check_created(context):
    data = context.response.json()
    assert "id" in data, f"No id in: {data}"
    logger.info(f"Created user id: {data['id']}")


@then('the updated name should be "{name}"')
def step_check_updated_name(context, name):
    data = context.response.json()
    assert data.get("name") == name, f"Got {data.get('name')}, expected {name}"
    logger.info(f"Updated name: {name}")


@then('the updated email should be "{email}"')
def step_check_updated_email(context, email):
    data = context.response.json()
    assert data.get("email") == email, f"Got {data.get('email')}, expected {email}"
    logger.info(f"Updated email: {email}")