from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver import ActionChains
import time

class Main_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = 'https://www.sima-land.ru/'

    # Locators

    section_word = "//h1[contains(text(), 'Игрушки')]"
    toys_menu_button = "//ul[contains(@class, 'GPqzD')]//li[7]"
    switch_raiting_button = "//div[contains(@class, 'cmaUGO')]//div[3]"
    price_regulation = "//div[@class='J1k9Dv GvT6bX']//button[2]"
    #Прогу прощения далее за локаторы. По другому их никак не написать.
    trade_marks = "//div[@class='feXcB7']//div[@class= 'X4iFet'][2]//div[2]"
    all_marks = "//div[@role='menuitem'][1]"
    select_age = "//div[@class='feXcB7']//div[@class= 'X4iFet'][3]//div[2]"
    pick_age = "//div[@role='menuitem'][2]"
    sex_select = "//div[@class='feXcB7']//div[@class= 'X4iFet'][4]//div[2]"
    pick_unisex = "//div[@role='menuitem'][1]"
    submit_button = "//button[@id='toy-widget-submit']"

    # Getters

    def get_section_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.section_word)))

    def get_toys_menu_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.toys_menu_button)))

    def get_switch_raiting_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.switch_raiting_button)))

    def get_trade_marks(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.trade_marks)))

    def get_all_marks(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.all_marks)))

    def get_select_age(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_age)))

    def get_pick_age(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pick_age)))

    def get_sex_select(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sex_select)))

    def get_pick_unisex(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pick_unisex)))

    def get_submit_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.submit_button)))

    # Actions

    def click_toys_menu_button(self):
        self.get_toys_menu_button().click()
        print("Click toys menu button")

    def click_switch_raiting_button(self):
        self.get_switch_raiting_button().click()
        print("Switch high raiting")

    def click_price_regulation(self):
        actions = ActionChains(self.driver)
        max_price = self.driver.find_element(By.XPATH, self.price_regulation)
        actions.click_and_hold(max_price).move_by_offset(-100, 0).release().perform()
        print("Regulate max price")

    def click_trade_marks(self):
        self.driver.execute_script("window.scrollTo(0, 200)")
        self.get_trade_marks().click()
        print("Choose trade mark")

    def click_all_marks(self):
        self.get_all_marks().click()
        self.get_trade_marks().click()
        print("Choose all marks")

    def click_select_age(self):
        self.get_select_age().click()
        print("Select age")

    def click_pick_age(self):
        self.get_pick_age().click()
        self.get_select_age().click()
        print("Pick 1-3 year")

    def click_sex_select(self):
        self.get_sex_select().click()
        print("Select sex of baby")

    def click_pick_unisex(self):
        self.get_pick_unisex().click()
        self.get_sex_select()
        print("Select unisex")

    def click_submit_button(self):
        self.driver.execute_script("window.scrollTo(0, 100)")
        self.get_submit_button().click()
        print("Click submit button")

    # Methods

    def select_type_of_product(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_toys_menu_button()
        self.assert_word(self.get_section_word(), "Игрушки")
        time.sleep(1)
        self.click_switch_raiting_button()
        time.sleep(1)
        self.click_trade_marks()
        self.click_all_marks()
        time.sleep(1)
        self.click_select_age()
        self.click_pick_age()
        time.sleep(1)
        self.click_sex_select()
        self.click_pick_unisex()
        time.sleep(1)
        self.click_price_regulation()
        time.sleep(1)
        self.click_submit_button()