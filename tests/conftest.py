import pytest
from utils.config_reader import ConfigReader

# Playwright automatically provides these fixtures:
# - browser
# - context  
# - page

# We just need to configure them

@pytest.fixture(scope="function", autouse=True)
def context(browser):
    """Create context with tracing enabled"""
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        record_video_dir="videos/"
    )
    
    # Start tracing
    context.tracing.start(screenshots=True, snapshots=True)
    
    yield context
    
    # Stop tracing and save
    context.tracing.stop(path="traces/trace.zip")
    context.close()

@pytest.fixture(scope="session")
def browser_type_launch_args():
    """Configure browser launch"""
    return {
        "headless": True,
        "slow_mo": ConfigReader.get('slow_mo')
    }

@pytest.fixture(scope="function")
def config():
    """Provide config to tests"""
    return ConfigReader.get_config()

# Optional: Custom screenshot on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """Hook to capture additional info on failure"""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        # Playwright already captures screenshots/videos
        # This is just for additional logging
        print(f"\nTest {item.name} failed")