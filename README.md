# 🚀 Capstone Project — API Automation Framework

A complete API Automation Framework built with **Python Requests + Behave BDD + Allure Reporting**.

## 1. Module Name
Module 3 — Python BDD RESTful Automation

## 2. Experiment Title
API Automation Framework with Python Requests + Behave BDD + Allure Reporting

## 3. Problem Statement
Build a scalable API test automation framework that validates the User Management APIs of public REST services (JSONPlaceholder and reqres.in), with authentication, CRUD operations, BDD scenarios, and professional reports.

## 4. Objective
- Build a reusable API client using Python `requests`
- Write BDD-style feature files in Gherkin
- Implement step definitions using Behave
- Test CRUD operations (GET, POST, PUT, PATCH, DELETE)
- Validate authentication flows (register, login, error cases)
- Generate Behave HTML and Allure reports

## 5. Tools, Software & Concepts Used

| Category | Details |
|---|---|
| Language | Python 3 |
| HTTP Library | `requests` |
| BDD Framework | `behave` |
| Reporting | Behave HTML + Allure |
| Logging | Python `logging` |
| APIs Tested | `jsonplaceholder.typicode.com`, `reqres.in` |
| Concepts | REST, BDD, Gherkin, Session management, API Authentication |

## 6. Project Structure

```
capstone-project/
├── config/            → URLs, headers, timeouts
├── framework/         → Reusable API client + logger
├── features/          → BDD features + step definitions
├── test_data/         → JSON test data
├── logs/              → Runtime logs
├── Output/            → Reports + screenshots
├── allure-results/    → Raw Allure data
├── behave.ini         → Behave config
├── requirements.txt   → Dependencies
└── README.md
```

## 7. Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## 8. Execution

```bash
# Run all scenarios
behave

# Generate HTML report
behave -f behave_html_formatter:HTMLFormatter -o Output/behave-report.html

# Generate Allure results
behave -f allure_behave.formatter:AllureFormatter -o allure-results

# View Allure report
allure serve allure-results
```

## 9. Test Coverage

| Feature File | Scenarios |
|---|---|
| `users.feature` (JSONPlaceholder) | 6 — List, Get, Create, PUT, PATCH, Delete |
| `auth.feature` (reqres.in) | 5 — Register, Login, Login failure, Pagination, Create |

**Total:** 2 features · 11 scenarios · 32 steps · **All passing**

## 10. Output

### Terminal
![Terminal](Output/01-terminal.png)

### Behave HTML Report — Top
![HTML Report 1](Output/02-html-report1.png)

### Behave HTML Report — Bottom
![HTML Report 2](Output/02-html-report2.png)

### Allure Report
![Allure Report](Output/03-allure-report.png)

## 11. Result & Observation

All 11 scenarios passed (**11 passed, 0 failed, 0 error**, 100% pass rate). The framework:

- Validated CRUD operations against JSONPlaceholder
- Authenticated against reqres.in using email/password + API key header
- Correctly handled the missing-password error case (400)
- Reused `APIClient` across all tests — zero code duplication
- Logged every request to `logs/test_run.log`
- Generated readable Behave HTML and interactive Allure reports

## 12. Conclusion

This capstone demonstrates how a **layered API automation framework** can be built in Python with clean separation between feature files (business language), step definitions (glue), framework layer (reusable HTTP + logging), config, and test data — producing a maintainable, scalable, and easy-to-understand framework.