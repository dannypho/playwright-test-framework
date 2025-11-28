# Test Automation Framework - Playwright

Modern test automation framework built with Python, Playwright, and Pytest using Page Object Model design pattern.

## Technologies

- Python 3.12
- Playwright 1.40
- Pytest 7.4.3
- Page Object Model (POM)
- Data-driven testing with CSV
- HTML reporting with screenshots/videos

## Features

- Page Object Model architecture
- Auto-waiting (no explicit waits needed)
- Screenshot on failure (automatic)
- Video recording on failure
- Trace viewer for debugging
- Multi-browser support (Chrome, Firefox, Safari)
- Data-driven testing with CSV
- Parallel execution support
- CI/CD ready (GitHub Actions)

### Prerequisites
- Python 3.12 or higher
- pip

### Setup

1. **Clone repository**
```bash
git clone https://github.com/dannypho/playwright-test-framework.git
cd playwright-test-framework
```

2. **Install dependencies**
```bash
python -m pip install -r requirements.txt
```

3. **Install Playwright browsers**
```bash
python -m playwright install
```

## Running Tests

### Basic Commands
```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_login.py

# Run specific test
pytest tests/test_login.py::TestLogin::test_successful_login_with_expect
```

### Reports
```bash
# Generate HTML report
pytest tests/ --html=reports/report.html

# View screenshots and videos (auto-captured on failure)
open test-results/
```

## Configuration

Edit `config/config.yaml` to customize:
```yaml
base_url: "https://the-internet.herokuapp.com"
browser: "chromium"  # chromium, firefox, or webkit
headless: false
timeout: 30000
```

## Data-Driven Testing

Add test data to `test_data/users.csv`:
```csv
username,password,expected_result
validuser,validpass,success
invaliduser,validpass,error
```

Tests automatically read and parameterize from CSV.

## CI/CD

Tests run automatically on GitHub Actions on every push.

View results in Actions tab on GitHub.
