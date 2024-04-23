import time

import allure
from pages.order_page import OrderPage
from locators.locators_order_page import LocatorsOrderPage
from locators.locators_main_page import LocatorsMainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestOrder:
    @allure.title('Проверка заказа через верхнюю кнопку "Заказать"')
    @allure.description(
        'персональные данные клиента формируются рандомно, суть проверки, что заказ оформляется успешно и проходит весь флоу')
    def test_order_click_top_button(self, browser):
        order_page = OrderPage(browser)
        order_page.click_button(LocatorsMainPage.cookie_button)
        order_page.click_button(LocatorsMainPage.order_button_main)
        order_page.fill_form_one()
        order_page.click_button(LocatorsOrderPage.button_next)
        order_page.fill_form_two()
        assert 'Номер заказа' in order_page.get_element_text(LocatorsOrderPage.order_is_processed)

    @allure.title('Проверка заказа через нижнюю кнопку "Заказать"')
    @allure.description(
        'персональные данные клиента формируются рандомно, суть проверки, что заказ оформляется успешно и проходит '
        'весь флоу')
    def test_order_click_low_button(self, browser):
        order_page = OrderPage(browser)
        order_page.click_button(LocatorsMainPage.cookie_button)
        order_page.scroll_to_element(LocatorsOrderPage.zakaz_button_scroll)
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable(LocatorsOrderPage.zakaz))
        order_page.click_button(LocatorsOrderPage.zakaz)
        order_page.fill_form_one()
        order_page.click_button(LocatorsOrderPage.button_next)
        order_page.fill_form_two()
        assert 'Номер заказа' in order_page.get_element_text(LocatorsOrderPage.order_is_processed)
