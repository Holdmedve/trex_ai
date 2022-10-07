from selenium import webdriver
from selenium.common.exceptions import TimeoutException

def load_game():
    print('opening browser...')
    driver = webdriver.Firefox()
    print('browser opened')
    driver.set_page_load_timeout(10)

    retry_cnt = 0
    while True:
        try:
            print('loading page...')
            driver.get('https://dinorunner.com')
            print('page load finished')
            break
        except TimeoutException as e:
            # driver.delete_all_cookies()
            if retry_cnt < 3:
                print('page did not load, retrying...')
                retry_cnt += 1
            else:
                print('page did not load, retries threshold exceeded')
                raise e    

    assert driver.title == "Dinosaur T-Rex Game - Chrome Dino Runner Online"
    return driver

def close_game(webdriver):
    print('closing game...')
    webdriver.quit()
    print('game closed')
