from selenium import webdriver

username = "chofmanntest"

driver = webdriver.Chrome("C:\\Users\\crist\\Desktop\\Cripto\\WebDrivers\\chromedriver.exe")
driver.get("https://aternos.org/go/")
driver.set_window_size(1920, 1080)

forgotpass_button = driver.find_element_by_link_text("¿Olvidaste tu contraseña?")
forgotpass_button.click()

username_textbox = driver.find_element_by_id("user")
username_textbox.send_keys(username)

send_button = driver.find_element_by_id("reset-password")
send_button.click()