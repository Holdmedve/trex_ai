from selenium import webdriver
from contextlib import contextmanager


@contextmanager
def game_context():
    print("opening browser...")
    driver = webdriver.Chrome()
    print("browser opened")
    driver.set_page_load_timeout(10)

    _load_page(driver=driver, url=_get_game_url())

    yield

    close_game(webdriver=driver)


def _get_game_url():
    return "https://dinorunner.com"


def _load_page(driver, url):
    driver.get(url)


def close_game(webdriver):
    print("closing game...")
    webdriver.quit()
    print("game closed")
