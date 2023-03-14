"""
These tests cover DuckDuckGo searches.
"""

from selenium import webdriver
import time

def test_basic_duckduckgo_search():

    # Given the DuckDuckGo home page is displayed
    # TODO

    # When the user searches for "panda"
    # TODO

    # Then the search result title contains "panda"
    # TODO
    
    # And the search result query is "panda"
    # TODO
    
    # And the search result links pertain to "panda"
    # TODO

  

    driver = webdriver.Chrome()

    driver.get('https://www.google.com')
    time.sleep(5)

    driver.quit()

    raise Exception("Incomplete Test")