from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Cart_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    name_prod_in_cart = "//div[@data-testid='item-name']"
    checkout_button = "//div[@data-testid='bottom-panel:checkout-button']"

    # Getters

    def get_name_prod_in_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_prod_in_cart)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    # Actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click check out button")


    # Methods

    def check_prod_in_cart(self):
        self.assert_word(self.get_name_prod_in_cart(), "Пазл «Весёлый праздник», 15 х 11 см")
        self.click_checkout_button()

