
from BaseApp import BasePage
from selenium.webdriver.common.by import By



# Создаем класс ChromeLocators. Он будет только для хранения локаторов.
# В классе описываем локаторы:
class ChromeLocators:
    LOCATOR_CHOISE_MOSCOW = (By.CSS_SELECTOR, "a.locality-selector-popup__big-city")

    # find_elements_by_class_name = (
    #     By.XPATH, "//div[@class='sc-1tpn8pe-3 duQqqx']")
    #
    # LOCATOR_lENGTH_PIZZA = len(find_elements_by_class_name)

    LOCATOR_CHOISE_MOSCOW_Header = (By.CSS_SELECTOR,
                                    "header.sc-1of5u0p-0.hpZTJI "
                                    "div.left div.yrfxdq-0.jjxTjA.header__about h1.header__about-slogan:nth-child(1) > "
                                    "a.header__about-slogan-text.header__about-slogan-text_locality.header__about"
                                    "-slogan "
                                    "-text_link:nth-child(2))")

    # LOCATOR_lENGTH_PIZZA = (By.CLASS_NAME, "sc-1tpn8pe-3 duQqqx")
    LOCATOR_lENGTH_PIZZA = (By.CLASS_NAME, "sc-1tpn8pe-3 duQqqx")
    LOCATOR_WINDOW_PIZZA = (By.XPATH, "//body/div[@id='react-app']/main[1]/section[1]/article[1]")

class DODORegion(BasePage):
    # В click_on_region_button мы нажимаем на кнопку "Москва" в выборе региона доставки.
    def click_on_region_button(self):
        self.driverwait(ChromeLocators.LOCATOR_CHOISE_MOSCOW).click()

class LenghtPizza(BasePage):
    def click_on_region_button(self):
        self.driverwait(ChromeLocators.LOCATOR_CHOISE_MOSCOW).click()
    def look_for_element(self):
        self.driver.find_element(ChromeLocators.LOCATOR_lENGTH_PIZZA)
        return self.driver.find_element(ChromeLocators.LOCATOR_lENGTH_PIZZA)
        


class RandomPizza(BasePage):
    def click_on_region_button(self):
        self.driverwait(ChromeLocators.LOCATOR_CHOISE_MOSCOW).click()
    def click_random_pizza(self):
        self.driverwait(ChromeLocators.LOCATOR_WINDOW_PIZZA).click()
        # l = links[randint(0, len(links) - 1)]
        # l.click()
