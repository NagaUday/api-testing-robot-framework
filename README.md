# api-testing-robot-framework

# Robot Framework – Customer Login Automation

This repository demonstrates how to use custom Robot Framework keywords in Python to authenticate a customer via the UCR Bypass API.

## Structure
- `tests/` contains Robot test cases
- `resources/` has Python keywords with logging
- `requirements.txt` contains dependencies

## Setup
```bash
pip install -r requirements.txt
robot tests/CustomerLogin.robot
