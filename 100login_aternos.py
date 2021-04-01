from selenium import webdriver
import time

username = "chofmanntest"
password = "hola123123"

driver = webdriver.Chrome("C:\\Users\\crist\\Desktop\\Cripto\\WebDrivers\\chromedriver.exe")
driver.get("https://aternos.org/go/")
driver.set_window_size(1920, 1080)

for x in range (99):

    driver.get("https://aternos.org/go/")
    
    username_textbox = driver.find_element_by_id("user")
    username_textbox.send_keys(username)

    password_textbox = driver.find_element_by_id("password")
    password_textbox.send_keys(password)

    login_button = driver.find_element_by_id("login")
    login_button.click()

    time.sleep(1)
