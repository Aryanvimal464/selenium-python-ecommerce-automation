# Selenium Python E-Commerce Automation Framework

A complete web automation testing framework developed using *Python, Selenium WebDriver and Pytest* for testing an e-commerce web application.

This project follows the *Page Object Model (POM)* design pattern and automates important user workflows such as Login, Product Selection, Shopping Cart and Checkout.

---

## 📌 Project Overview

This project is created to demonstrate practical *QA Automation and Software Testing* skills.

The framework automates repetitive web application test scenarios and provides a structured, reusable and maintainable automation architecture.

### Main Objectives

- Automate e-commerce application workflows
- Create reusable Selenium page objects
- Execute test cases using Pytest
- Validate application functionality
- Use assertions for validation
- Implement explicit waits
- Generate HTML test reports
- Maintain test code using Page Object Model
- Manage the project using Git and GitHub

---

# 🛠️ Technologies & Tools

- *Python*
- *Selenium WebDriver*
- *Pytest*
- *HTML*
- *Page Object Model (POM)*
- *Git*
- *GitHub*
- *VS Code*

---

# 📂 Complete Project Structure

```text
selenium-python-ecommerce-automation/
│
├── pages/
│   │
│   ├── _init_.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   │
│   ├── _init_.py
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── utils/
│   │
│   ├── _init_.py
│   ├── config.py
│   └── driver_factory.py
│
├── reports/
│   │
│   └── report.html
│
├── screenshots/
│   │
│   └── Test failure screenshots
│
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
