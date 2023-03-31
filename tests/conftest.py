"""
This module contains shared fixtures.

a fixture in pytest is a function that includes both setup and cleanup phases in one body.

"""

import pytest
import selenium.webdriver


@pytest.fixture
def browser():

  # Initialize the ChromeDriver instance
  b = selenium.webdriver.Chrome()

  # Make its calls wait up to 10 seconds for elements to appear
  b.implicitly_wait(10)

  # Return the WebDriver instance for the setup
  yield b

  # Quit the WebDriver instance for the cleanup
  b.quit()
