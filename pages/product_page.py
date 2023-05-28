from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Product_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    pick_prod = "//div[@data-testid='catalog-item:list'][1]//div[@class='fivTV6 VYZNcy aO40fb']"
    add_to_cart_button = "//button[@data-testid='cart-control:add-to-cart-button']"
    cart_button = "//div[@data-testid='nav-item:cart']"
    name_of_prod = "//h1[@data-testid='product-name']"

    # Getters

    def get_pick_prod(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pick_prod)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_name_of_prod(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_of_prod)))

    # Actions

    def click_pick_prod(self):
        self.get_pick_prod().click()
        print("Select Пазл «Весёлый праздник», 15 х 11 см")

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print("Click add to cart button")

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Click cart button")

    # Methods

    def select_prod(self):
        self.click_pick_prod()
        self.get_screenshot()
        self.assert_word(self.get_name_of_prod(), "Пазл «Весёлый праздник», 15 х 11 см")
        self.click_add_to_cart_button()
        self.click_cart_button()

