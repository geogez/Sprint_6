from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def wait_until_clickable(self, locator):
        WebDriverWait(self.browser, 3).until(EC.element_to_be_clickable(locator))

    def find(self, locator):
        return self.browser.find_element(*locator)

    def find_elements(self, locator):
        return self.browser.find_elements(*locator)

    def click_button(self, locator):
        self.wait_until_clickable(locator)
        self.find(locator).click()

    def get_element_text(self, locator):
        self.element_is_visible(locator)
        return self.find(locator).text

    def scroll_to_element(self, locator):
        element = self.find(locator)
        self.browser.execute_script("arguments[0].scrollIntoView();", element)

    def element_is_visible(self, locator):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator))

    def switch_to_window(self):
        return self.browser.switch_to.window(self.browser.window_handles[-1])

    def fill_field(self, locator, value):
        element = self.find(locator)
        element.clear()
        element.send_keys(value)

    def wait_for_site(self, url):
        WebDriverWait(self.browser, 10).until(EC.url_to_be(url))

    def current_get_url(self):
        return self.browser.current_url