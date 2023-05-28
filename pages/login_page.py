import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Login_page(Base):
    url = 'https://www.sima-land.ru/'


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    loggin_button = "//div[@data-testid='nav-item:cabinet']"
    enter_button = "//button[@data-testid='button']"
    user_name = "//div[@class='aLWWUx']//input"
    password = "//div[@class='cvONT1']//input"

    # Getters

    def get_loggin_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loggin_button)))

    def get_enter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    # Actions

    def click_loggin_button(self):
        self.get_loggin_button().click()
        print("Click loggin button")

    def click_enter_button(self):
        self.get_enter_button().click()
        print("Click enter_button")

    def input_user_name(self, username):
        self.get_user_name().send_keys(username)
        print("Input user name")

    def input_password(self, pass_word):
        self.get_password().send_keys(pass_word)
        print("Input password")

    # Methods


    """Authorization on web site"""

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_loggin_button()
        time.sleep(2)
        self.input_user_name("ansar2007@rambler.ru")
        self.input_password("Y3H9fRHV")
        self.click_enter_button()
        time.sleep(2)
