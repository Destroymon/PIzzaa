import pytest
from selenium import webdriver


@pytest.fixture(scope="session")    # Делаем так, чтобы браузер открывался в текущей сессиии
def browser():
    driver = webdriver.Chrome()  # Задаем браузер
    driver.maximize_window()  # Делаем полный экран
    yield driver  # Возвращаем генератор
    driver.quit()  # Выходим с браузера