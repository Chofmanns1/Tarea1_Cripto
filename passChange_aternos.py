from selenium import webdriver
import time

username = "chofmanntest"
password = "hola12345"
newpass = "hola12"

driver = webdriver.Chrome("C:\\Users\\crist\\Desktop\\Cripto\\WebDrivers\\chromedriver.exe")
driver.get("https://aternos.org/go/")
driver.set_window_size(1920, 1080)

username_textbox = driver.find_element_by_id("user")
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_id("password")
password_textbox.send_keys(password)

login_button = driver.find_element_by_id("login")
login_button.click()

time.sleep(3)

account_button = driver.find_element_by_link_text("Cuenta")
account_button.click()

time.sleep(2)

oldpass_textbox = driver.find_element_by_id("old-password")
oldpass_textbox.send_keys(password)

newpass_textbox1 = driver.find_element_by_id("new-password")
newpass_textbox1.send_keys(newpass)

newpass_textbox2 = driver.find_element_by_id("new-password-retype")
newpass_textbox2.send_keys(newpass)

changepass_button = driver.find_element_by_xpath("(//*[@class='fas fa-lock'])[3]").click()