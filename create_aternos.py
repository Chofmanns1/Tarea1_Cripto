from selenium import webdriver
import time

username = "chofmanntest1"
password = "hola123"

driver = webdriver.Chrome("C:\\Users\\crist\\Desktop\\Cripto\\WebDrivers\\chromedriver.exe")
driver.get("https://aternos.org/go/")
driver.set_window_size(1920, 1080)

time.sleep(2)

register_button = driver.find_element_by_link_text("Registrarse")
register_button.click()

time.sleep(2)

username_textbox = driver.find_element_by_id("user")
username_textbox.send_keys(username)

serviceTerms_checkbox = driver.find_element_by_xpath("//label[@for='accept-terms']")
serviceTerms_checkbox.click()

privacyTerms_checkbox = driver.find_element_by_xpath("//label[@for='prvcy-cnsnt']")
privacyTerms_checkbox.click()

next_button = driver.find_element_by_id("create-next")
next_button.click()

time.sleep(2)

password1_textbox = driver.find_element_by_id("password")
password1_textbox.send_keys(password)

password2_textbox = driver.find_element_by_id("password-retype")
password2_textbox.send_keys(password)

end_button = driver.find_element_by_id("signup")
end_button.click()