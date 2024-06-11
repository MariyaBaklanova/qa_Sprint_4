import allure
import pytest
from selenium import webdriver
from data.constants import Constant


@allure.title('Подготовка драйвера Firefox и его выключение')
#@pytest.fixture
#def driver():
    #driver = webdriver.Firefox()
    #driver.maximize_window()
    #yield driver
    #driver.quit()

@pytest.fixture
def driver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(Constant.MAIN_URL)
    yield driver
    driver.quit()