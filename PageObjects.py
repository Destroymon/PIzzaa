import random
import time
from selenium.webdriver import Keys, ActionChains
from BaseApp import BasePage
from selenium.webdriver.common.by import By



# Создаем класс ChromeLocators. Он будет только для хранения локаторов.
# В классе описываем локаторы:
class ChromeLocators:
    LOCATOR_CHOISE_MOSCOW = (By.CSS_SELECTOR, "a.locality-selector-popup__big-city")

    LOCATOR_CHOISE_MOSCOW_Header = (By.CSS_SELECTOR,
                                    "header.sc-1of5u0p-0.hpZTJI "
                                    "div.left div.yrfxdq-0.jjxTjA.header__about h1.header__about-slogan:nth-child(1) > "
                                    "a.header__about-slogan-text.header__about-slogan-text_locality.header__about"
                                    "-slogan "
                                    "-text_link:nth-child(2))")

    LOCATOR_lENGTH_PIZZA = (By.CLASS_NAME, "sc-1tpn8pe-3 duQqqx")
    LOCATOR_WINDOW_PIZZA = (By.XPATH, "//body/div[@id='react-app']/main[1]/section[1]/article[1]")
    LOCATOR_SIZE_SMALL_PIZZA = (By.XPATH, "//label[contains(text(),'Маленькая')]")
    LOCATOR_ADD_TO_CARD = (By.XPATH, "//body/div[4]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/button[1]")
    LOCATOR_CLICK_CARD = (By.XPATH, "///body/div[@id='react-app']/nav[1]/div[1]/div[2]/button[1]")

    LOCATOR_CLICK_IMG_PIZZA11 = (By.XPATH, "//body/div[@id='react-app']/main[1]/section[1]/article[8]/main[1]/div[1]")
    LOCATOR_CLICK_ADD_KEY = (By.XPATH, "//body/div[4]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/button[1]")
    LOCATOR_CLICK_IMG_PIZZA12 = (By.XPATH, "//body/div[@id='react-app']/main[1]/section[1]/article[10]/main[1]/div[1]")
    LOCATOR_CLICK_IMG_PIZZA13 = (By.XPATH, "//body/div[@id='react-app']/main[1]/section[1]/article[9]/main[1]/div[1]")
    LOCATOR_CLICK_IMG_PIZZA14 = (By.XPATH, "//body/div[@id='react-app']/main[1]/section[1]/article[11]/main[1]/div[1]")
    LOCATOR_CLICK_IMG_PIZZA15 = (By.XPATH, "//body/div[@id='react-app']/main[1]/section[1]/article[12]/main[1]/div[1]")
    LOCATOR_CARD_QANTITY = (By.XPATH, '//*[@id="react-app"]/nav/div/div[2]/button/div[2]')


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
    def click_small_pizza(self):
        self.driverwait(ChromeLocators.LOCATOR_SIZE_SMALL_PIZZA).click()
    def click_add_to_card(self):
        self.driverwait(ChromeLocators.LOCATOR_ADD_TO_CARD).click()
    def click_to_card(self):
        self.driverwait(ChromeLocators.LOCATOR_CLICK_CARD).click()
    def click_artikle_pizza(self):
        self.driverwait(ChromeLocators.LOCATOR_CLICK_IMG_PIZZA11).click()
        self.driverwait(ChromeLocators.LOCATOR_CLICK_ADD_KEY).click()
        self.driverwait(ChromeLocators.LOCATOR_CLICK_IMG_PIZZA12).click()
        self.driverwait(ChromeLocators.LOCATOR_CLICK_ADD_KEY).click()
        self.driverwait(ChromeLocators.LOCATOR_CLICK_IMG_PIZZA13).click()
        self.driverwait(ChromeLocators.LOCATOR_CLICK_ADD_KEY).click()
        self.driverwait(ChromeLocators.LOCATOR_CLICK_IMG_PIZZA14).click()
        self.driverwait(ChromeLocators.LOCATOR_CLICK_ADD_KEY).click()
        self.driverwait(ChromeLocators.LOCATOR_CLICK_IMG_PIZZA15).click()
        self.driverwait(ChromeLocators.LOCATOR_CLICK_ADD_KEY).click()
        # self.driverwait(ChromeLocators.LOCATOR_CARD_QANTITY).click()






def func_five(browser):    #   Функция для выбора 5 пицц (не смог пока довести до ума, оставил, чтобы просто
                            # видели логику действий)
    actions = ActionChains(browser)
    test = 0
    elements = browser.find_elements(By.XPATH, "//section[@id='pizzas']//article")
    for i in range(5):
        actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(1)
        test = len(elements)
    add = []
    for i in elements:
        add.append(i)
    random_index = random.randrange(len(add))
    if random_index == 3:
        click = browser.find_element(By.XPATH,
                                     "//article[@data-yellow='true']//button[@type='button'][contains(text(),'589₽')]")
        click_order = browser.find_element(By.CSS_SELECTOR, 'div.sc-1dazsw3-3.dfOCuw.show div.sc-1dazsw3-2.pnLpo div.sc-1dazsw3-1.dHDRyZ div.gsrbdo-0.bFKozP div.gsrbdo-8.dQwDFJ div.gsrbdo-18.dlfBaI > button.sc-1rmt3mq-0.cpUbDl.gsrbdo-22.gaQAWN')
        return click, test, click_order
    elif random_index == 2:
        click = browser.find_element(By.XPATH,
                                     "//body[1]/div[3]/main[1]/section[1]/article[2]/div[1]/button[1]")
        click_order = browser.find_element(By.CSS_SELECTOR, 'div.sc-1dazsw3-3.dfOCuw.show div.sc-1dazsw3-2.pnLpo div.sc-1dazsw3-1.dHDRyZ div.gsrbdo-0.bFKozP div.gsrbdo-8.dQwDFJ div.gsrbdo-18.dlfBaI > button.sc-1rmt3mq-0.cpUbDl.gsrbdo-22.gaQAWN')
        return click, test, click_order
    elif random_index == 1:
        click = browser.find_element(By.XPATH,
                                     "//button[contains(text(),'Собрать')]")
        click_order = browser.find_element(By.CSS_SELECTOR, 'div.sc-1dazsw3-3.dfOCuw.show div.sc-1dazsw3-2.pnLpo div.sc-1dazsw3-1.dHDRyZ div.gsrbdo-0.bFKozP div.gsrbdo-8.dQwDFJ div.gsrbdo-18.dlfBaI > button.sc-1rmt3mq-0.cpUbDl.gsrbdo-22.gaQAWN')
        return click, test, click_order
    elif random_index > 3:
        click = browser.find_element(By.XPATH,
                                     f'//body[1]/div[3]/main[1]/section[1]/article[{random_index}]/footer[1]/button')
        click_order = browser.find_element(By.CSS_SELECTOR, 'div.sc-1dazsw3-3.dfOCuw.show div.sc-1dazsw3-2.pnLpo div.sc-1dazsw3-1.dHDRyZ div.gsrbdo-0.bFKozP div.gsrbdo-8.dQwDFJ div.gsrbdo-18.dlfBaI > button.sc-1rmt3mq-0.cpUbDl.gsrbdo-22.gaQAWN')
        print(random_index)
        return click, test, click_order

def func_one(browser):         # Функция для вызбора 1 пиццы
    actions = ActionChains(browser)
    test = 0
    elements = browser.find_elements(By.XPATH, "//section[@id='pizzas']//article")
    for i in range(5):
        actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(1)
        test = len(elements)
    add = []
    for i in elements:
        add.append(i)
    random_index = random.randrange(len(add))
    click = browser.find_element(By.XPATH,
                                 f'//body[1]/div[3]/main[1]/section[1]/article[{random_index}]/footer[1]/button')
    browser.execute_script("arguments[0].click();", click)
    return test