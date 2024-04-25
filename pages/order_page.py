import random
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from conftest import browser
from helpers import *
import allure

from locators.locators_main_page import LocatorsMainPage
from locators.locators_order_page import LocatorsOrderPage
from pages.base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def click_cookie_button(self):
        self.click_button(LocatorsMainPage.cookie_button)

    def is_order_processed_text_visible(self):
        return 'Номер заказа' in self.get_element_text(LocatorsOrderPage.order_is_processed)

    def is_order_processed_text_visible(self):
        return 'Номер заказа' in self.get_element_text(LocatorsOrderPage.order_is_processed)

    def click_order_button(self):
        self.click_button(LocatorsMainPage.order_button_main)

    def click_next_button(self):
        self.click_button(LocatorsOrderPage.button_next)

    def zakaz_button_scroll(self):
        self.scroll_to_element(LocatorsOrderPage.zakaz_button_scroll)

    def zakaz_button(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(LocatorsOrderPage.zakaz))
        self.click_button(LocatorsOrderPage.zakaz)
    def button_next(self):
        self.click_button(LocatorsOrderPage.button_next)
    @allure.step('Заполняю форму оформления заказа персональные данные.')
    def fill_form_one(self):
        self.find(LocatorsOrderPage.metro).click()
        self.find(LocatorsOrderPage.contaner_metro)
        input_metro_option = self.find_elements(LocatorsOrderPage.meto_text)
        input_metro_random = random.choice(input_metro_option)
        selected_option_text = input_metro_random.text
        input_metro_random.click()

        input_name = self.find(LocatorsOrderPage.name)
        input_name.click()
        input_name.send_keys(name())

        input_second_name = self.find(LocatorsOrderPage.second_name)
        input_second_name.click()
        input_second_name.send_keys(second_name())

        input_address = self.find(LocatorsOrderPage.address)
        input_address.click()
        input_address.send_keys(address())

        input_phone = self.find(LocatorsOrderPage.phone_number)
        input_phone.click()
        input_phone.send_keys(phone_number())

    @allure.step('Заполняю форму c подробностями аренды')
    def fill_form_two(self):
        date = self.find(LocatorsOrderPage.date)
        date.click()
        input_date = self.find(LocatorsOrderPage.date_input)
        input_date.click()

        period = self.find(LocatorsOrderPage.period)
        period.click()

        period_choice = self.find(LocatorsOrderPage.period_input)
        period_choice.click()

        color = self.find(LocatorsOrderPage.color_grey)
        color.click

        commments = self.find(LocatorsOrderPage.comment_for_delivery)
        commments.click()
        commments.send_keys('Осторожно злая собака')

        self.click_button(LocatorsOrderPage.button_order)
        self.click_button(LocatorsOrderPage.button_yep_order)
