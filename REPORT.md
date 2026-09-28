<div align="center">

# 📄 Capstone Project Report

### API Automation Framework with Python Requests, Behave BDD & Allure Reporting

![Module](https://img.shields.io/badge/Module-3%20%E2%80%94%20BDD%20API%20Automation-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Tests-11%2F11%20Passed-brightgreen?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Behave](https://img.shields.io/badge/Behave-BDD-11AB00?style=for-the-badge)

**Submitted By:** Dibyajyoti Singha
**Program:** Wipro Python Automation Training
**Date:** September 2026

</div>

---

## Table of Contents

| # | Section |
|:-:|---------|
| 1 | [Abstract](#1-abstract) |
| 2 | [Introduction](#2-introduction) |
| 3 | [Problem Statement](#3-problem-statement) |
| 4 | [Objectives](#4-objectives) |
| 5 | [Tools & Technologies](#5-tools--technologies) |
| 6 | [System Architecture](#6-system-architecture) |
| 7 | [Project Structure](#7-project-structure) |
| 8 | [Implementation Details](#8-implementation-details) |
| 9 | [Test Cases & Results](#9-test-cases--results) |
| 10 | [Output & Screenshots](#10-output--screenshots) |
| 11 | [Conclusion](#11-conclusion) |
| 12 | [References](#12-references) |

---

## 1. Abstract

> This report presents a complete **API Automation Framework** built using Python's `requests` library and the **Behave BDD** framework.

The framework validates the User Management APIs of two public REST services — **JSONPlaceholder** and **reqres.in** — covering CRUD operations, authentication flows, error handling, and pagination.

**Result:** All **11 test scenarios pass** with a **100% pass rate**, and interactive reports are generated using Behave HTML and Allure reporting.

---

## 2. Introduction

API testing has become essential in modern software development. Unlike UI tests, API tests run faster, are more reliable, and can be integrated into CI/CD pipelines.

This capstone project demonstrates building a **production-quality API automation framework** in Python.

### APIs Tested

| API | Base URL | Purpose |
|-----|----------|---------|
| **JSONPlaceholder** | `https://jsonplaceholder.typicode.com` | Free REST API for CRUD operations |
| **reqres.in** | `https://reqres.in/api` | Practice API for authentication & pagination |

Behavior-Driven Development (BDD) is used to write test scenarios in **plain English** (Gherkin syntax), making them readable by both technical and non-technical stakeholders.

---

## 3. Problem Statement

Manual API testing is slow, error-prone, and doesn't scale. As the number of endpoints grows, verifying each request-response cycle manually becomes impractical.

**A structured automation framework is required to:**

- Reusably test REST endpoints (GET, POST, PUT, PATCH, DELETE)
- Handle authentication flows (register, login, error responses)
- Validate response status codes, headers, and body content
- Generate readable reports for test results
- Be maintainable so new tests can be added without rewriting existing code

---

## 4. Objectives

Design and build a **reusable, layered API automation framework** that:

- ✅ Uses Python's `requests` library for HTTP interactions
- ✅ Implements BDD-style feature files with Gherkin syntax
- ✅ Uses Behave to map Gherkin steps to Python step definitions
- ✅ Tests CRUD operations against a public REST API
- ✅ Validates authentication flows including error cases
- ✅ Stores test data externally in JSON files
- ✅ Logs every action for debugging
- ✅ Generates HTML and Allure reports
- ✅ Follows best practices for framework design

---

## 5. Tools & Technologies

| Category | Tool / Technology |
|----------|-------------------|
| **Programming Language** | Python 3.12 |
| **HTTP Library** | `requests` |
| **BDD Framework** | `behave` |
| **Reporting** | `allure-behave`, Behave HTML formatter |
| **Logging** | Python's built-in `logging` module |
| **Test Data Format** | JSON |
| **APIs Tested** | JSONPlaceholder, reqres.in |
| **Editor / IDE** | Visual Studio Code |
| **Version Control** | Git + GitHub |
| **Environment** | Windows 11, PowerShell |

---

## 6. System Architecture

The framework follows a **4-layer architecture**:

| Layer | Component | Responsibility |
|:-----:|-----------|----------------|
| 1 | **Feature Files** (`.feature`) | Business-readable Gherkin scenarios |
| 2 | **Step Definitions** (`steps/*.py`) | Python glue code for HTTP calls |
| 3 | **Framework Layer** (`framework/*.py`) | Reusable APIClient + Logger |
| 4 | **Config + Test Data** (`config/`, `test_data/`) | Externalized environment and inputs |

**Layer responsibilities:**

- **Feature Files** — contain only business logic in Gherkin syntax (`Given`, `When`, `Then`)
- **Step Definitions** — translate each Gherkin step into Python code; contain no HTTP logic
- **Framework Layer** — `APIClient` wraps Python `requests` and handles sessions, headers, and timeouts; `logger.py` provides structured logging
- **Config + Test Data** — externalize environment URLs, headers, and test inputs so nothing is hardcoded

---

## 7. Project Structure

```
capstone-project/
├── config/
│   └── config.py                   # URLs, headers, timeouts
│
├── framework/
│   ├── __init__.py
│   ├── api_client.py               # Reusable HTTP client
│   └── logger.py                   # Logging utility
│
├── features/
│   ├── users.feature               # User CRUD scenarios
│   ├── auth.feature                # Authentication scenarios
│   ├── environment.py              # Behave hooks
│   └── steps/
│       ├── __init__.py
│       ├── user_steps.py           # Step definitions for users.feature
│       └── auth_steps.py           # Step definitions for auth.feature
│
├── test_data/
│   ├── users.json                  # User test data
│   └── auth.json                   # Auth test data
│
├── logs/                           # Runtime logs
├── Output/                         # Reports + screenshots
├── allure-results/                 # Raw Allure data
│
├── .env.example
├── .gitignore
├── behave.ini
├── requirements.txt
└── README.md
```

---

## 8. Implementation Details

### 8.1 APIClient (`framework/api_client.py`)

The `APIClient` class wraps Python's `requests.Session()` and provides simplified methods for HTTP verbs:

```python
class APIClient:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        if headers:
            self.session.headers.update(headers)

    def get(self, endpoint, params=None): ...
    def post(self, endpoint, json=None): ...
    def put(self, endpoint, json=None): ...
    def patch(self, endpoint, json=None): ...
    def delete(self, endpoint): ...
```

> This is reused across all tests — **no code duplication**.

### 8.2 Logger (`framework/logger.py`)

A reusable logger writes to both `logs/test_run.log` and the console, using a standardized format:

```
2026-09-27 03:14:16 | INFO | POST /login - eve.holt@reqres.in
```

### 8.3 Feature Files

Feature files are written in Gherkin syntax. Example from `users.feature`:

```gherkin
Scenario: Create a new user
    When I create a user with name "Test User" and email "test@example.com"
    Then the response status should be 201
    And the response should contain the created user details
```

### 8.4 Step Definitions

Step definitions link Gherkin text to Python functions using decorators:

```python
@when('I create a user with name "{name}" and email "{email}"')
def step_create_user(context, name, email):
    client = APIClient(JSONPLACEHOLDER_URL)
    context.response = client.post("/users", json={"name": name, "email": email})
```

### 8.5 Behave Hooks (`features/environment.py`)

Hooks run before and after each scenario for logging:

```python
def before_scenario(context, scenario):
    logger.info(f"▶ Scenario: {scenario.name}")

def after_scenario(context, scenario):
    logger.info(f"  [{scenario.status.name.upper()}] {scenario.name}")
```

### 8.6 Test Data (`test_data/*.json`)

Test inputs are externalized:

```json
{
  "list_users_expected_count": 10,
  "create_user": { "name": "Test User", "email": "test@example.com" }
}
```

### 8.7 Execution

```bash
# Run tests
behave

# Generate HTML report
behave -f behave_html_formatter:HTMLFormatter -o Output/behave-report.html

# Generate Allure results and view the report
behave -f allure_behave.formatter:AllureFormatter -o allure-results
allure serve allure-results
```

---

## 9. Test Cases & Results

### 9.1 Test Coverage Summary

| Feature File | API | Scenarios |
|--------------|-----|:---------:|
| `users.feature` | JSONPlaceholder | 6 |
| `auth.feature` | reqres.in | 5 |
| **Total** | — | **11** |

### 9.2 Users Feature (JSONPlaceholder)

| # | Scenario | Method | Endpoint | Expected |
|:-:|----------|:------:|----------|----------|
| 1 | Get all users | `GET` | `/users` | 200, 10 users |
| 2 | Get user by ID | `GET` | `/users/1` | 200, user has name |
| 3 | Create a new user | `POST` | `/users` | 201, response has ID |
| 4 | Update user with PUT | `PUT` | `/users/1` | 200, name updated |
| 5 | Partial update with PATCH | `PATCH` | `/users/1` | 200, email updated |
| 6 | Delete a user | `DELETE` | `/users/1` | 200 |

### 9.3 Auth Feature (reqres.in)

| # | Scenario | Method | Endpoint | Expected |
|:-:|----------|:------:|----------|----------|
| 1 | Register new user | `POST` | `/register` | 200, response has token |
| 2 | Login successfully | `POST` | `/login` | 200, response has token |
| 3 | Login with missing password | `POST` | `/login` | 400, error mentions "password" |
| 4 | Get paginated users | `GET` | `/users?page=1` | 200, page number returned |
| 5 | Create a new user | `POST` | `/users` | 201, response has ID |

### 9.4 Overall Results

```
2 features passed, 0 failed, 0 skipped
11 scenarios passed, 0 failed, 0 skipped
32 steps passed, 0 failed, 0 skipped
Took 0min 11.002s

100% pass rate
```

---

## 10. Output & Screenshots

### 10.1 Terminal Output

![Terminal](capstone-project/Output/01-terminal.png)

### 10.2 Behave HTML Report — Top

![HTML Report Top](capstone-project/Output/02-html-report1.png)

### 10.3 Behave HTML Report — Bottom

![HTML Report Bottom](capstone-project/Output/02-html-report2.png)

### 10.4 Allure Report

![Allure Report](capstone-project/Output/03-allure-report.png)

---

## 11. Conclusion

This capstone project successfully demonstrates how a **layered, maintainable API automation framework** can be built in Python using modern BDD practices.

### Key Outcomes

- **11 test scenarios** covering CRUD, authentication, and error handling — all passing
- **100% pass rate** across both public APIs tested
- **Reusable architecture** — the `APIClient` utility is used across all tests, with zero code duplication
- **Externalized configuration** — URLs, headers, and test data live outside the test code
- **Structured logging** — every request is logged to a file for debugging
- **Professional reporting** — Behave HTML and interactive Allure reports

### Skills Demonstrated

| Skill | Applied In |
|-------|-----------|
| Python 3 | Framework, step definitions, utilities |
| REST API Testing | All scenarios |
| BDD with Behave | Feature files + step definitions |
| Test Framework Design | Layered architecture |
| Reporting | Allure + Behave HTML |
| Git & GitHub | Version control |

---

## 12. References

1. Python `requests` documentation — [requests.readthedocs.io](https://requests.readthedocs.io/)
2. Behave documentation — [behave.readthedocs.io](https://behave.readthedocs.io/)
3. Gherkin reference — [cucumber.io/docs/gherkin](https://cucumber.io/docs/gherkin/)
4. Allure Framework — [docs.qameta.io/allure](https://docs.qameta.io/allure/)
5. JSONPlaceholder — [jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com/)
6. reqres.in — [reqres.in](https://reqres.in/)

---

<div align="center">

**End of Report**

*Submitted as part of the Wipro Python Automation Training Program*

</div>
