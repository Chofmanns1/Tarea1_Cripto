from selenium import webdriver

username = "chofmanntest"
password = "hola12"

driver = webdriver.Chrome("C:\\Users\\crist\\Desktop\\Cripto\\WebDrivers\\chromedriver.exe")
driver.get("https://aternos.org/go/")
driver.set_window_size(1920, 1080)

username_textbox = driver.find_element_by_id("user")
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_id("password")
password_textbox.send_keys(password)

login_button = driver.find_element_by_id("login")
login_button.click()