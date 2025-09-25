# Emilo Social Media Automation

## Pre-requisites
- Python 3.10+
- Chrome browser installed
- ChromeDriver matching Chrome version

## Setup
1. Clone the repo:
   ```bash
   git clone <repo-url>
   cd emilo-automation
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Create a .env file in project root:

env
Copy code
EMAIL=your_email
PASSWORD=your_password
Running Tests
Run all tests:

bash
Copy code
pytest --html=reports/report.html
Run a specific test:

bash
Copy code
pytest tests/test_login.py --html=reports/login_report.html
Screenshots for failed tests will be saved in the screenshots/ folder.

Test Reports
After execution, open the HTML report generated in reports/ to see test results.

pgsql
Copy code

This version is clean, with proper code blocks for syntax highlighting, and ready to paste directly into your `README.md`.  

If you want, I can also **add a folder structure section** so anyone running the project knows where everything is located. Do you want me to do that?