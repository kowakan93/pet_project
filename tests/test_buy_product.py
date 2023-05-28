from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from pages.product_page import Product_page
from pages.cart_page import Cart_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.order_page import Order_page

def test_buy_product_1():
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities["pageLoadStrategy"] = "eager"
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument("--disable-notifications")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\C:\\Users\\kowak\\PycharmProjects\\resource')
    driver = webdriver.Chrome(options=options, service=g, desired_capabilities=capabilities)

    print("Start test")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_type_of_product()

    pp = Product_page(driver)
    pp.select_prod()

    cp = Cart_page(driver)
    cp.check_prod_in_cart()

    op = Order_page(driver)
    op.order_prod()

    driver.quit()