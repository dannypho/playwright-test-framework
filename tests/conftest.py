import pytest
from utils.config_reader import ConfigReader

@pytest.fixture(scope="session")
def browser_type_launch_args():
    """Configure browser launch"""
    return {
        "headless": ConfigReader.is_headless(),
        "slow_mo": ConfigReader.get('slow_mo')
    }

@pytest.fixture(scope="function")
def config():
    """Provide config to tests"""
    return ConfigReader.get_config()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """Hook to capture additional info on failure"""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        print(f"\nTest {item.name} failed")