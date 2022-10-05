from selenium.webdriver.common.by import By

from PageObjects import DODORegion, LenghtPizza, RandomPizza


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

    def test_quantity_pizza_moscow_page(self, browser):
        quantity = LenghtPizza(browser)
        quantity.go_to_site()
        quantity.click_on_region_button()
        quantity.look_for_element()

        assert len(quantity.look_for_element()) == 1


class Test_Case_1:
    def test_dodo_click_pizza(self, browser):
        random = RandomPizza(browser)
        random.go_to_site()
        random.click_on_region_button()
        random.click_random_pizza()
        url = browser.current_url
        assert url == 'https://dodopizza.ru/moscow/pizza/halfs'     #Проверяем что открывается окно конструктора пицц

