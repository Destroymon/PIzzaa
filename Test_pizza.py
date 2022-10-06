import random
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from PageObjects import DODORegion, LenghtPizza, RandomPizza, func_five


# Создаем класс для первого кейса проверок
class Test_Case_0:
    def test_DoDo_delivery_region(self, browser):  # Создаем первут проверку
        click = DODORegion(browser)  # Создаем экземпляр класса click
        click.go_to_site()  # Запускаем сайт
        click.click_on_region_button()       # Выбираем Москву
        url = browser.current_url
        assert url == 'https://dodopizza.ru/moscow' # Проверяем, что переход выполнен на нужный Url
        header_lolation = browser.find_element(By.CSS_SELECTOR, "header.sc-1of5u0p-0.hpZTJI "
                                                                "div.left div.yrfxdq-0.jjxTjA.header__about "
                                                                "h1.header__about-slogan:nth-child(1) > "
                                                                "a.header__about-slogan-text.header_"
                                                                "_about-slogan-text_locality.header_"
                                                                "_about-slogan-text_link:nth-child(2)")  #Считываем текст
        assert header_lolation.text == "Москва"     # Проверяем, что тест соответсвует ОР

    def test_quantity_pizza_moscow_page(self, browser):          #Кол-во Пицц на странице(спойлер, тест падает потому что не сходится с ОР = 34 :))
        quantity = LenghtPizza(browser)
        quantity.go_to_site()
        quantity.click_on_region_button()
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
        add[random_index].click()
        assert test == 34


class Test_Case_1:
    def test_dodo_click_pizza(self, browser):
        random = RandomPizza(browser)
        random.go_to_site()
        random.click_on_region_button()
        random.click_random_pizza()
        url = browser.current_url
        assert url == 'https://dodopizza.ru/moscow/pizza/halfs'     #Проверяем что открывается окно конструктора пицц

    def test_add_random_pizza_to_cart(self, browser):  # Проверить, что в шапке главной страницы, в кнопке "Корзина"
                                                       # появился счётчик добавленных товаров. Значение = 1.
        quantity = RandomPizza(browser)
        quantity.go_to_site()
        quantity.click_on_region_button()
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
                                     f'/html[1]/body[1]/div[3]/main[1]/section[1]/article[{random_index}]/main[1]/div[1]')

        # Переменную клик нужно изменить, выбрать элемент случайный с кодом f'//body[1]/div[3]/main[1]/section[1]/article[{random_index}]/footer[1]/button') это кнопка "Выбрать"
        # Однако, как сделать две проверки чтобы они работали, чтобы проверить и название и переход по щелчку на кнопку "выбрать" я не знаю, я пробовал разные методы, возможно нужно написать еще оджну функцию, чтобы выборать
        # Элемент который выбирается и при рандомном нажатии в функции сверху, но это займет долгое время для решения у меня, в сроки сдачи не уложусь

        browser.execute_script("arguments[0].click();", click)
        time.sleep(5)
        name_pizza_windows = browser.find_element(By.CSS_SELECTOR, "div.sc-1dazsw3-3.dfOCuw.show div.sc-1dazsw3-2.pnLpo" 
                                                                   " div.sc-1dazsw3-1.dHDRyZ div.gsrbdo-0.bFKozP div.gs"
                                                                   "rbdo-8.dQwDFJ div.gsrbdo-9.eDBIfW div.sc-11ezv7x-0.hA"
                                                                   "-DLvj div:nth-child(1) div:nth-child(1) div.gsrbdo-"
                                                                   "10.emwqeU div.gsrbdo-11.dtJPrk > span.gsrbdo-12.hshULL")
        # Проверка того
        assert name_pizza_windows.text == click.text
        quantity.click_add_to_card()
        time.sleep(5)
        card_qantity = browser.find_element(By.XPATH, '//*[@id="react-app"]/nav/div/div[2]/button/div[2]')
        assert card_qantity.text == "1"  # Проверка, что в корзине одна пицца
        time.sleep(10)
        return test

    def test_add_differets_cost(self, browser):  # Проверить, что в шапке главной страницы, в кнопке "Корзина"
        # появился счётчик добавленных товаров. Значение = 1.
        quantity = RandomPizza(browser)
        quantity.go_to_site()
        quantity.click_on_region_button()
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
        cost = browser.find_element(By.XPATH,
                                     f'/html[1]/body[1]/div[3]/main[1]/section[1]/article[{random_index}]/footer[1]/div[1]')

        #cost_prace = browser.find_element(By.XPATH, f'/html/body/div[3]/main/section[1]/article[{random_index}]/footer/div/text()[2]')
        browser.execute_script("arguments[0].click();", cost)
        time.sleep(5)
        name_pizza_windows = browser.find_element(By.CSS_SELECTOR, "div.sc-1dazsw3-3.dfOCuw.show div.sc-1dazsw3-2.pnLpo div.sc-1dazsw3-1.dHDRyZ div.gsrbdo-0.bFKozP div.gsrbdo-8.dQwDFJ div.gsrbdo-18.dlfBaI button.sc-1rmt3mq-0.cpUbDl.gsrbdo-22.gaQAWN span.money > span.money__value")

        # Проверка, что цены отличаются
        assert name_pizza_windows.text != cost.text     # Проверка, что значение цены на кнопке "Добавить в корзину за
        # {}Р" изменится. Сравнить со значением на главной странице (т.к. там указана цена за мелнькую пиццу)

class Test_Case_2:
    def test_quantity_pizza_moscow_page(self, browser):
        quantity = LenghtPizza(browser)
        quantity.go_to_site()
        quantity.click_on_region_button()
        arguments = func_five(browser)
        browser.execute_script("arguments[0].click();", arguments[0])
        assert arguments[1] == 34

