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
