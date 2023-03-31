"""
This module contains shared fixtures.

a fixture in pytest is a function that includes both setup and cleanup phases in one body.

"""

import json
import pytest
import selenium.webdriver



#Config fixture 
@pytest.fixture
def config(scope='session'):

  # Read the file
  with open('config.json') as config_file:
    config = json.load(config_file) #parses to python dictionary
  
  # Assert values are acceptable before running any tests
  assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']  #The test can now be chosen as chrome, firefox etc from the config file.
  assert isinstance(config['implicit_wait'], int)
  assert config['implicit_wait'] > 0

  # Return config so it can be used
  return config


@pytest.fixture
def browser(config):  #Now depends on config fixture, this will run for each test case.

  # Initialize the WebDriver instance
  if config['browser'] == 'Firefox':
    b = selenium.webdriver.Firefox()
  elif config['browser'] == 'Chrome':
    b = selenium.webdriver.Chrome()
  elif config['browser'] == 'Headless Chrome':
    opts = selenium.webdriver.ChromeOptions()
    opts.add_argument('headless')
    b = selenium.webdriver.Chrome(options=opts)
  else:
    raise Exception(f'Browser "{config["browser"]}" is not supported')

  # Make its calls wait for elements to appear
  b.implicitly_wait(config['implicit_wait'])

  #fixture still the same from here

  # Return the WebDriver instance for the setup
  yield b

  # Quit the WebDriver instance for the cleanup
  b.quit()
