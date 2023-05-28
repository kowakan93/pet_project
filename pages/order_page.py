import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Order_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_broker = "//div[@id='option-block_delivery-4']//div"
    broker_num_3 = "//div[contains(@class,'w23Gx')][3]//div[@class='yDMpU']"
    select_pickup_point = "//button[@class='Ow5lS JkD3C G3wDd T3RwG ocjPO Z_qWa']"
    send_order_button = "//button[@id='send-order']"

    # Getters

    def get_select_broker(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_broker)))

    def get_broker_num_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.broker_num_3)))

    def get_select_pickup_point(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_pickup_point)))

    def get_send_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.send_order_button)))

    # Actions

    def click_select_broker(self):
        self.get_select_broker().click()
        print("Open many of brokers")

    def click_broker_num_3(self):
        self.get_broker_num_3().click()
        print("Select broker Антон Иванович")

    def click_select_pickup_point(self):
        self.get_select_pickup_point().click()
        print("Select pickup point")

    def click_send_order_button(self):
        self.get_send_order_button().click()
        print("Click send order button")

    # Methods

    def order_prod(self):
        time.sleep(13)
        self.click_select_broker()
        self.click_broker_num_3()
        self.click_select_pickup_point()
        self.click_send_order_button()
