# API Test Automation Framework

A reusable API Test Automation Framework built using **Python**, **Pytest**, and **Requests** for automated testing of REST APIs. This framework validates authentication flows, CRUD operations, negative scenarios, and API response structures while generating detailed HTML reports for test execution.

The framework was developed to test a FastAPI-based Team Task Manager application and can be easily adapted for any REST API.

---

## Features

### Authentication Testing
- Valid Login
- Invalid Login
- Missing Credentials
- Unauthorized Access Validation

### CRUD Testing
- Create Resources
- Retrieve Resources
- Update Resources
- Delete Resources

### Negative Testing
- Invalid IDs
- Empty Request Bodies
- Invalid Data Types
- Missing Required Fields

### Data-Driven Testing
- JSON-based test data
- Pytest parameterization
- Multiple test scenarios with minimal code

### Reusable Framework Components
- Generic API Client
- Pytest Fixtures
- Environment-Based Configuration
- Fake Data Generation using Faker

### Reporting & Logging
- HTML Test Reports
- Request/Response Logging
- Execution Status Tracking

---

## Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Testing Framework | Pytest |
| API Library | Requests |
| Reporting | pytest-html |
| Test Data | JSON |
| Fake Data | Faker |
| Configuration | python-dotenv |
| Version Control | Git, GitHub |

---

## Project Structure

```text
api-test-automation-framework/

├── tests/
│   ├── test_auth.py
│   ├── test_users.py
│   ├── test_negative.py
│   └── test_login_parameterize.py
│
├── utils/
│   ├── api_client.py
│   ├── config.py
│   ├── logger.py
│   └── data_generator.py
│
├── test_data/
│   └── login_data.json
│
├── reports/
│
├── logs/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## Framework Architecture

```text
Pytest Test Cases
        │
        ▼
   API Client
        │
        ▼
 Requests Library
        │
        ▼
     REST API
        │
        ▼
    Database
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/<your-username>/api-test-automation-framework.git

cd api-test-automation-framework
```

### Create Virtual Environment

#### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Configuration

Create a `.env` file in the project root:

```env
BASE_URL=http://localhost:8000/api/v1

ADMIN_EMAIL=admin@example.com
ADMIN_PASSWORD=admin123
```

---

## Running Tests

### Execute Complete Test Suite

```bash
pytest
```

### Run with Verbose Output

```bash
pytest -v
```

### Execute Specific Test File

```bash
pytest tests/test_auth.py
```

```bash
pytest tests/test_users.py
```

---

## Generate HTML Report

```bash
pytest --html=reports/report.html --self-contained-html
```

Open the generated report:

```text
reports/report.html
```

---

## Sample Test Scenarios

### Authentication Testing

```python
def test_valid_login(client):

    response = client.post(
        "/auth/login",
        params={
            "username": ADMIN_EMAIL,
            "password": ADMIN_PASSWORD
        }
    )

    assert response.status_code == 200
```

### CRUD Validation

```python
def test_create_user(client, auth_token):

    response = client.post(
        "/users",
        user_data,
        headers=headers
    )

    assert response.status_code == 201
```

### Negative Testing

```python
def test_invalid_user_id(client, auth_token):

    response = client.get(
        "/users/999999",
        headers=headers
    )

    assert response.status_code == 404
```

---

## Test Coverage

The framework currently covers:

- Authentication APIs
- User Management APIs
- Positive Test Cases
- Negative Test Cases
- Data-Driven Test Cases
- Response Validation
- Authorization Validation

---

## Future Enhancements

- Schema Validation using JSON Schema
- Allure Reporting Integration
- Retry Mechanism
- Parallel Test Execution
- CI/CD Integration with GitHub Actions
- Docker Support
- API Performance Validation
- Test Execution Dashboard

---

## GitHub Actions (Planned)

```yaml
name: API Tests

on:
  push:

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5

      - run: pip install -r requirements.txt

      - run: pytest
```

---

## Key Learning Outcomes

- API Testing Fundamentals
- Test Automation Framework Design
- Pytest Fixtures and Parameterization
- Authentication and Authorization Testing
- REST API Validation
- Test Reporting and Logging
- Environment Management
- Reusable Test Architecture

---

## Author

**Ravi Teja**

Backend Developer | QA Automation Enthusiast

GitHub: https://github.com/TEJA3441

---

## License

This project is intended for educational, learning, and portfolio purposes.
